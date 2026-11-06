<h1 align="center">
  <img src="img/mumble-logo.png" alt="Mumble">
  <br />
  Mumble
  <br />
</h1>

<p align="center"><b>This is the snap for Mumble</b>, <em>"Open Source, Low Latency, High Quality Voice Chat"</em>. It works on Ubuntu, Fedora, Debian, and other major Linux distributions.</p>

<p align="center">
  <a href="https://snapcraft.io/mumble"><img alt="Get it from the Snap Store" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg" /></a>
</p>

<p align="center">
  <a href="https://snapcraft.io/mumble"><img src="https://snapcraft.io/mumble/badge.svg" alt="Snap Store version"></a>
  <a href="https://github.com/snapcrafters/mumble/actions/workflows/pull-request.yml"><img src="https://github.com/snapcrafters/mumble/actions/workflows/pull-request.yml/badge.svg" alt="Pull request builds"></a>
  <a href="https://github.com/snapcrafters/mumble/actions/workflows/release-to-candidate.yml"><img src="https://github.com/snapcrafters/mumble/actions/workflows/release-to-candidate.yml/badge.svg?branch=candidate" alt="Candidate releases"></a>
  <a href="https://github.com/snapcrafters/mumble/actions/workflows/sync-version-with-upstream.yml"><img src="https://github.com/snapcrafters/mumble/actions/workflows/sync-version-with-upstream.yml/badge.svg?branch=candidate" alt="Upstream version sync"></a>
</p>

This community-maintained package contains the desktop client, not the Mumble server. It is not officially maintained by the upstream developers.

## Install

```shell
sudo snap install mumble
```

([Don't have snapd installed?](https://snapcraft.io/docs/core/install))

## Configuration

### Microphone access

If microphone access is not connected automatically, connect it explicitly:

```shell
sudo snap connect mumble:audio-record
```

Use Mumble's Audio Wizard to select and test your input and output devices. PulseAudio works with both PulseAudio desktops and PipeWire's PulseAudio compatibility service.

## How to contribute

### Reporting issues

Please [open an issue](https://github.com/snapcrafters/mumble/issues/new) if you find a bug, have a feature request, or if the snap is out of date. Include the snap revision, your desktop environment and steps to reproduce.

### Updating the snap

Snap versions are [automatically kept in sync](https://github.com/snapcrafters/mumble/actions/workflows/sync-version-with-upstream.yml) with upstream releases. To update it manually, [open a pull request](https://github.com/snapcrafters/mumble/compare) against `candidate`.

When the pull request is merged, the release workflow builds the declared architectures remotely and publishes to `latest/candidate`. It then creates a call-for-testing issue and gathers screenshots. After testing, a maintainer can promote the snap to stable.

To build locally with Snapcraft and LXD:

```shell
snapcraft pack --use-lxd
```

### Testing

Subscribe to the [candidate channel](https://snapcraft.io/mumble) and [leave a comment](https://github.com/snapcrafters/mumble/issues?q=is%3Aissue+is%3Aopen+label%3Atesting) with your results.

```shell
sudo snap install mumble --channel=candidate
```

For an existing installation, use `sudo snap refresh mumble --channel=candidate`. Test audio setup, a server connection and normal voice chat. Return to stable with `sudo snap refresh mumble --channel=stable`.

### Maintainers

- [@merlijn-sebrechts](https://github.com/merlijn-sebrechts)

## License

The scripts and documentation in this project are released under the [MIT License](LICENSE). Mumble itself is released under the [3-clause BSD license](https://github.com/mumble-voip/mumble/blob/master/LICENSE).
