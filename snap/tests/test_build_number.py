"""Exercise the recipe's actual shell parameter without Snapcraft legacy variables."""
import os
from pathlib import Path
import subprocess
import unittest


class BuildNumberTests(unittest.TestCase):
    def test_version_comes_from_craftctl(self):
        recipe = (Path(__file__).resolve().parents[1] / "snapcraft.yaml").read_text()
        parameter = next(line.strip()[2:] for line in recipe.splitlines()
                         if line.strip().startswith("- -DBUILD_NUMBER="))
        for version in ("1.5.939", "1.5.1000"):
            with self.subTest(version=version):
                env = {"PATH": os.defpath, "TEST_VERSION": version}
                result = subprocess.run(
                    ["bash", "-c", 'set -eu; craftctl() { test "$*" = "get version"; printf "%s\\n" "$TEST_VERSION"; }; '
                     + "set -- " + parameter + '; printf "%s\\n" "$1"'],
                    env=env, text=True, capture_output=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), "-DBUILD_NUMBER=" + version.rsplit(".", 1)[1])


if __name__ == "__main__":
    unittest.main()
