+++
title = "gitbay — Privacy Policy"
description = "Privacy policy for gitbay, the gitbay client for iOS."
weight = 5
+++

_last updated: 31 august 2026_

gitbay is a native iOS client for [gitbay](https://gitbay.org), a self-hosted
git forge. it talks to the instance you point it at, directly from your device.
we run no servers of our own for this app, and we receive none of your data.

## what we collect

nothing. no krz account, no analytics, no ads, no third-party trackers
or SDKs. the app has two dependencies, both for rendering text, and neither
makes a network request.

## what stays on your device

your access token and the list of accounts you have added are stored in the iOS
Keychain, marked as available on this device only — they are not synced to
iCloud or to any other device you own. the only other thing kept is which
account is currently selected.

the app uses an ephemeral network session, so responses, cookies, and
credentials are not written to disk. nothing you browse is cached between
launches. deleting the app removes everything.

## network connections

gitbay connects only to the instance you configure at sign-in. those requests
carry your access token, go straight to that server, and are governed by its
own terms and privacy policy. we are not a party to that traffic and never see
it. if you run your own instance, that traffic reaches only you.

## changes

if this policy changes, the updated version will be posted here with a new date.

## contact

questions: [root@krz.sh](mailto:root@krz.sh).
