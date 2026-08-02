+++
title = "Hutch — Privacy Policy"
description = "Privacy policy for Hutch, the Sourcehut client for iOS."
weight = 1
+++

_last updated: 2 august 2026_

Hutch is a native iOS client for [Sourcehut](https://sr.ht). it talks to
Sourcehut directly from your device. we have no user accounts, and we never
receive your Sourcehut credentials. the one exception — a small first-party
service used to draw contribution graphs — is described below.

## what we collect

we have no krz account system, no analytics, no ads, and no
third-party trackers or SDKs. the only data that ever reaches a server we
operate is described under "the Hutch Stats service" below, and it is limited
to the public Sourcehut usernames you ask to see contribution graphs for.

## what stays on your device

your Sourcehut personal access token is stored in the iOS Keychain on your
device. cached repositories, tickets, and activity are stored locally so the
app stays fast and works offline. deleting the app removes all of it.

## network connections

most of Hutch connects only to the Sourcehut instance you point it at — sr.ht
by default, or a self-hosted instance you configure. those requests carry your
access token, go straight to that server, and are governed by its own terms and
privacy policy. we are not a party to that traffic and never see it.

## the Hutch Stats service

to render contribution graphs (the calendar-style activity charts on user
profiles), Hutch asks a small first-party service, `hutch-stats.krz.sh`, for a
person's public Sourcehut activity. this happens when you open a profile,
including your own.

each request sends the public Sourcehut **username** you are viewing and a date
range. it does **not** send your access token or any Sourcehut credentials; the
only header is a generic `Hutch/<version>` user-agent that contains no device or
account identifiers. as with any web request, the service also sees the network
(IP) address it came from. we use this data only to answer the request and do
not build profiles from it or share it.

if you would rather not use this service, contribution graphs are the only
feature that depends on it. advanced users and self-hosters can point Hutch at a
different stats endpoint via the `HUTCH_STATS_BASE_URL` setting.

## changes

if this policy changes, the updated version will be posted here with a new date.

## contact

questions: [root@krz.sh](mailto:root@krz.sh).
