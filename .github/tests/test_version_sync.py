"""Exercise the exact workflow update-script with real bash, jq and yq.

Run: python3 .github/tests/test_version_sync.py
Only gh is stubbed: no network, GitHub writes, or working-tree manifest writes.
"""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/sync-version-with-upstream.yml"
SCRIPT = subprocess.check_output(
    ["yq", "-r", '.jobs.sync.steps[0].with."update-script"', str(WORKFLOW)],
    text=True,
)
MANIFEST = "name: mumble\nversion: '1.5.613'\nparts:\n  mumble:\n    source-tag: v$SNAPCRAFT_PROJECT_VERSION\n"


class VersionSyncTests(unittest.TestCase):
    def run_sync(self, release, manifest=MANIFEST, status=0, success=False, changed=False):
        # Respect the caller's TMPDIR; never touch the repository's real manifest.
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "snap").mkdir()
            target = root / "snap/snapcraft.yaml"
            target.write_text(manifest)
            target.chmod(0o640)
            before = target.read_bytes()
            (root / "release.json").write_text(release)
            binary = root / "bin"
            binary.mkdir()
            gh = binary / "gh"
            gh.write_text(
                '#!/bin/bash\nset -eu\n'
                '[[ "$*" == "api repos/mumble-voip/mumble/releases/latest" ]]\n'
                '[[ -n "${GH_TOKEN:-}" ]]\n'
                'cat release.json\nexit "${MOCK_STATUS}"\n'
            )
            gh.chmod(0o755)
            result = subprocess.run(
                ["bash", "-c", SCRIPT], cwd=root,
                env={**os.environ, "PATH": f"{binary}:{os.environ['PATH']}",
                     "GH_TOKEN": "fixture-not-a-secret", "MOCK_STATUS": str(status)},
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode == 0, success, result.stderr)
            expected = manifest.replace("version: '1.5.613'", "version: '1.5.939'").encode() if changed else before
            self.assertEqual(target.read_bytes(), expected)
            self.assertEqual(target.stat().st_mode & 0o777, 0o640)
            self.assertEqual(list((root / "snap").glob("*.sync-version.*")), [])

    def test_valid_update(self):
        self.run_sync(self.release(), success=True, changed=True)

    def test_no_change(self):
        self.run_sync(self.release(), MANIFEST.replace("1.5.613", "1.5.939"), success=True)

    def test_invalid_release(self):
        fixtures = ["", "not json", "{}", "null", "[]", '{"tag_name":null}',
                    self.release(tag=""), self.release(tag="v1.5.939/unsafe"),
                    self.release(tag="v1.5.939\nversion: 9"), self.release(tag="v1.5.939; touch PWNED"),
                    self.release(tag="v1.5.939-rc1"), self.release(tag="v" + "1" * 40 + ".5.939"),
                    self.release(tag=123), self.release(draft=True), self.release(prerelease=True)]
        for fixture in fixtures:
            with self.subTest(release=fixture):
                self.run_sync(fixture)

    def test_api_failure(self):
        self.run_sync(self.release(), status=1)

    def test_invalid_manifest(self):
        fixtures = ["", "name: mumble\n", MANIFEST + "version: '1.5.939'\n",
                    MANIFEST.replace("1.5.613", ""), MANIFEST.replace("1.5.613", "../unsafe"),
                    MANIFEST + "broken: [\n", MANIFEST + "---\nversion: '1.5.613'\n",
                    MANIFEST.replace("version: '1.5.613'", "version: &anchor '1.5.613'"),
                    MANIFEST.replace("version: '1.5.613'", "version: null")]
        for fixture in fixtures:
            with self.subTest(manifest=fixture):
                self.run_sync(self.release(), fixture)

    def test_duplicate_keys(self):
        fixtures = [
            '"version": \'9.9.9\'\n' + MANIFEST,
            MANIFEST + '"version": \'9.9.9\'\n',
            MANIFEST + "extra:\n  key: one\n  key: two\n",
        ]
        for fixture in fixtures:
            with self.subTest(manifest=fixture):
                self.run_sync(self.release(), fixture)

    @staticmethod
    def release(tag: object = "v1.5.939", draft=False, prerelease=False):
        return json.dumps({"tag_name": tag, "draft": draft, "prerelease": prerelease})


if __name__ == "__main__":
    unittest.main(verbosity=2)
