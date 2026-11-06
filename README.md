<h1 align="center">
  <img src="img/mumble-logo.png" alt="Mumble">
  <br />
  Mumble
</h1>

<p align="center"><b>This is the snap for Mumble</b>, a free, open-source, low-latency, high-quality voice chat application. It works on Ubuntu, Fedora, Debian and other major Linux distributions.</p>

<p align="center">
  <a href="https://snapcraft.io/mumble"><img src="https://snapcraft.io/mumble/badge.svg" alt="Snap Store version"></a>
  <a href="https://github.com/snapcrafters/mumble/actions/workflows/pull-request.yml"><img src="https://github.com/snapcrafters/mumble/actions/workflows/pull-request.yml/badge.svg" alt="Pull request builds"></a>
  <a href="https://github.com/snapcrafters/mumble/actions/workflows/release-to-candidate.yml"><img src="https://github.com/snapcrafters/mumble/actions/workflows/release-to-candidate.yml/badge.svg?branch=candidate" alt="Candidate releases"></a>
  <a href="https://github.com/snapcrafters/mumble/actions/workflows/sync-version-with-upstream.yml"><img src="https://github.com/snapcrafters/mumble/actions/workflows/sync-version-with-upstream.yml/badge.svg?branch=candidate" alt="Upstream version sync"></a>
</p>

This package is maintained by the Snapcrafters community. It is not an official upstream Mumble package and contains the desktop client, not the Mumble server.

## Install

```shell
sudo snap install mumble
```

[Install snapd first](https://snapcraft.io/docs/core/install) if it is not already available on your distribution.

### Microphone access

If microphone access is not connected automatically, connect it explicitly:

```shell
sudo snap connect mumble:audio-record
```

Use Mumble's Audio Wizard to select and test your input and output devices. PulseAudio is supported, including the PulseAudio compatibility server on PipeWire desktops; the native PipeWire backend is disabled because the audio interfaces do not expose its socket. Network voice chat and desktop integration are subject to the snap's strict confinement; the upstream feature list is not a guarantee that every game overlay or positional-audio integration is available in this package.

## Contribute

### Report an issue

[Open an issue](https://github.com/snapcrafters/mumble/issues/new) for packaging bugs, missing functionality or outdated releases. Include the output of `snap info mumble`, your distribution, desktop session and steps to reproduce. Report application bugs that also occur outside the snap to [Mumble upstream](https://github.com/mumble-voip/mumble/issues).

### Update the snap

Open pull requests against **`candidate`**. The [upstream sync workflow](https://github.com/snapcrafters/mumble/actions/workflows/sync-version-with-upstream.yml) checks for new stable upstream releases daily.

To build locally, fork this repository, clone your fork and create a branch from `candidate`. With Snapcraft and LXD installed and configured, run:

```shell
snapcraft pack --use-lxd
```

Install your locally built artifact for testing:

```shell
sudo snap install --dangerous ./mumble_<version>_<architecture>.snap
```

Replace the filename with the artifact produced by your build. Pull requests use the [shared Snapcrafters CI](https://github.com/snapcrafters/ci) to build and review the amd64 snap.

After a change is merged to `candidate`, the release workflow builds the declared architectures remotely and publishes them to `latest/candidate`. It then opens a call-for-testing issue and gathers desktop screenshots. Publication requires the repository's release credentials and `Candidate Branch` environment to be configured. Stable promotion is a separate maintainer action after testing, not an automatic consequence of merging a pull request.

### Test candidate releases

For a new installation:

```shell
sudo snap install mumble --channel=latest/candidate
```

For an existing installation:

```shell
sudo snap refresh mumble --channel=latest/candidate
```

Test the audio setup, connection to a server and normal voice-chat workflow. Leave your results on the relevant [call-for-testing issue](https://github.com/snapcrafters/mumble/issues?q=is%3Aissue+is%3Aopen+label%3Atesting), including the snap revision and your desktop environment.

Return to stable with:

```shell
sudo snap refresh mumble --channel=latest/stable
```

## Maintainers

- [@merlijn-sebrechts](https://github.com/merlijn-sebrechts/)

## License

The build scripts and documentation in this repository are released under the [MIT License](LICENSE). Mumble itself is released under the [3-clause BSD license](https://github.com/mumble-voip/mumble/blob/master/LICENSE).
