<h1 align="center">
  <img src="https://raw.githubusercontent.com/snapcrafters/mumble/master/img/mumble-logo.png" alt="Mumble">
</h1>

<p align="center"><b>This is the snap for Mumble.</b> It is a community-maintained package to easily install the app on Ubuntu, Fedora, Debian and other major Linux distributions. It is available in the Snap Store, Ubuntu Software, and a number of other applications.</p>

<p align="center"><i>"Mumble is Open Source, Low Latency, High Quality Voice Chat"</i></p>

<p align="center">
<a href="https://snapcraft.io/mumble"><img src="https://snapcraft.io/mumble/badge.svg" alt="Snap Status"></a>
</p>

## Install

```shell
snap install mumble
```

([Don't have snapd installed?](https://snapcraft.io/docs/core/install))

<p align="center">Published for <img src="https://raw.githubusercontent.com/anythingcodes/slack-emoji-for-techies/gh-pages/emoji/tux.png" align="top" width="24" /> with :gift_heart: by Snapcrafters</p>

## How to contribute to this snap

Thanks for your interest! Below you find instructions to help you contribute to this snap.

The general workflow is to submit pull requests that merges your changes into the `master` branch here on GitHub. Once the pull request has been merged, we will automatically build the snap and publish it to the `edge` channel in the Snap Store. Once the snap has been tested thoroughly, we promote it to the `stable` channel so all our users get it!

### Initial setup

If this is your first time contributing to this snap, you first need to set up your own fork of this repository.

1. [Fork the repository](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) into your own GitHub namespace.
2. [Clone your fork](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository), so that you have it on your local computer.
3. Configure your local repo. To make things a bit more intuitive, we will rename your fork's remote to `myfork`, and add the snapcrafters repo as `snapcrafters`.

   ```shell
   git remote rename origin myfork
   git remote add snapcrafters https://github.com/snapcrafters/mumble.git
   git fetch --all
   ```

### Submitting changes in a pull request

Once you're all setup for contributing, keep in mind that you want the git information to be all up-to-date. So if you haven't "fetched" all changes in a while, start with that:

```shell
git fetch --all -p
```

Now that your git metadata has been updated you are ready to create a bugfix branch, make your changes, and open a pull request.

1. All pull requests should go to the stable branch so create your branch as a copy of the stable branch:

   ```shell
   git checkout -b my-bugfix-branch snapcrafters/master
   ```

2. Make your desired changes and build a snap locally for testing:

   ```shell
   snapcraft --use-lxd
   ```

3. After you are happy with your changes, commit them and push them to your fork so they are available on GitHub:

   ```shell
   git commit -a
   git push -u myfork my-bugfix-branch
   ```

4. Then, [open up a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) from your `my-bugfix-branch` to the `snapcrafters/master` branch.
5. Once you've opened the pull request, it will automatically trigger the build-test action that will launch a build of the snap. You can watch the progress of the snap build from your pull request (Show all checks -> Details). Once the snap build has completed, you can find the built snap (to test with) under "Artifacts".
6. Someone from the team will review the open pull request and either merge it or start a discussion with you with additional changes or clarification needed.
7. Once the pull request has been merged into the stable branch, we will rebuild the snap using your changes and publish it to the [Snap Store](https://snapcraft.io/mumble) into the `edge` channel. After sufficient testing of the snap from the `edge` channel, one of the maintainers or administrators will promote the snap to the stable branch in the Snap Store.

## Maintainers

* [@merlijn-sebrechts](https://github.com/merlijn-sebrechts/)

## License

* The license of both the build files in this repository is the MIT license.
* The license of Mumble itself is [the 3-clause BSD license](https://github.com/mumble-voip/mumble/blob/master/LICENSE)
