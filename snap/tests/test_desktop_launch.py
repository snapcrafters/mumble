"""Host-side launcher contract tests; these do not replace confined runtime tests."""
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import unittest


LAUNCHER = Path(__file__).resolve().parents[1] / "local" / "desktop-launch"


class DesktopLaunchTests(unittest.TestCase):
    def launch(self, extra=None, args=(), code=0, triplet="x86_64-linux-gnu"):
        env = {
            "PATH": os.defpath,
            "SNAP": "/snap/mumble/test revision",
            "SNAP_USER_DATA": "/home/test/snap/mumble/123",
            "SNAP_USER_COMMON": "/home/test/snap/mumble/common",
            "ARCH_TRIPLET": triplet,
            "UNRELATED": "preserve me",
        }
        env.update(extra or {})
        script = (
            "import json, os, sys; "
            "print(json.dumps({'env': dict(os.environ), 'args': sys.argv[1:]})); "
            f"sys.exit({code})"
        )
        result = subprocess.run(
            [str(LAUNCHER), sys.executable, "-c", script, *args],
            env=env, text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, code, result.stderr)
        return json.loads(result.stdout)

    def test_default_paths_for_both_architectures(self):
        for triplet in ("x86_64-linux-gnu", "aarch64-linux-gnu"):
            with self.subTest(triplet=triplet):
                env = self.launch(triplet=triplet)["env"]
                lib = f"{env['SNAP']}/usr/lib/{triplet}"
                self.assertEqual(env["LD_LIBRARY_PATH"], f"{lib}:{lib}/pulseaudio")
                self.assertEqual(env["XDG_CONFIG_HOME"], env["SNAP_USER_DATA"] + "/.config")
                self.assertEqual(env["XDG_CACHE_HOME"], env["SNAP_USER_COMMON"] + "/.cache")
                self.assertEqual(env["XDG_CONFIG_DIRS"], "/etc/xdg:" + env["SNAP"] + "/etc/xdg")
                self.assertEqual(env["XDG_DATA_DIRS"], env["SNAP"] + "/usr/local/share:" + env["SNAP"] + "/usr/share:/usr/local/share:/usr/share")
                self.assertNotIn("PULSE_SERVER", env)

    def test_preserves_gpu_and_inherited_environment(self):
        inherited = {
            "LD_LIBRARY_PATH": "/snap/mumble/current/gpu-2404/lib",
            "XDG_DATA_DIRS": "/custom/data:/other/data",
            "XDG_CONFIG_DIRS": "/custom/config",
            "QT_PLUGIN_PATH": "/packaged/qt5/plugins",
        }
        env = self.launch(inherited)["env"]
        self.assertTrue(env["LD_LIBRARY_PATH"].startswith(inherited["LD_LIBRARY_PATH"] + ":"))
        self.assertTrue(env["XDG_DATA_DIRS"].endswith(":" + inherited["XDG_DATA_DIRS"]))
        self.assertTrue(env["XDG_CONFIG_DIRS"].startswith(inherited["XDG_CONFIG_DIRS"] + ":"))
        self.assertEqual(env["QT_PLUGIN_PATH"], inherited["QT_PLUGIN_PATH"])
        self.assertEqual(env["UNRELATED"], "preserve me")

    def test_default_pulse_socket(self):
        env = self.launch({"XDG_RUNTIME_DIR": "/run/user/1000/snap.mumble"})["env"]
        self.assertEqual(env["PULSE_SERVER"], "unix:/run/user/1000/snap.mumble/../pulse/native")

    def test_explicit_pulse_server_is_preserved(self):
        env = self.launch({"XDG_RUNTIME_DIR": "/run/user/1000/snap.mumble", "PULSE_SERVER": "unix:/custom/pulse"})["env"]
        self.assertEqual(env["PULSE_SERVER"], "unix:/custom/pulse")

    def test_empty_runtime_does_not_invent_pulse_server(self):
        self.assertNotIn("PULSE_SERVER", self.launch({"XDG_RUNTIME_DIR": ""})["env"])

    def test_arguments_and_child_exit_status(self):
        args = ["with spaces", "*", "$HOME", "", "--option=value"]
        self.assertEqual(self.launch(args=args, code=37)["args"], args)

    def test_mode(self):
        self.assertEqual(stat.S_IMODE(LAUNCHER.stat().st_mode), 0o755)


if __name__ == "__main__":
    unittest.main()
