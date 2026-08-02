+++
title = "Domain Dig — Privacy Policy"
description = "Privacy policy for Domain Dig, the DNS and SSL inspector for iOS."
weight = 2
+++

_last updated: 2 august 2026_

Domain Dig inspects DNS records, SSL/TLS certificates, ownership, and related
signals for domains you enter. every lookup runs from your device. we operate no
servers, and we receive none of your data.

## what we collect

nothing. no account, no analytics, no ads, no third-party trackers or SDKs.

## what stays on your device

recent lookups and their results are stored locally on your device so you can
revisit them. deleting the app removes the local copy. if you turn on iCloud
sync (off by default), your settings, monitoring configuration, domain notes,
and history metadata are stored in your own private iCloud account so they carry
across your devices — that data goes to Apple's iCloud, never to us, and you can
turn it off in Settings.

## network connections

to answer a lookup, Domain Dig queries public DNS resolvers and connects to the
hosts you inspect in order to read their certificates. it also contacts a few
third-party lookup services to enrich the results — an IP-geolocation provider
(ipapi.co), RDAP registries (via rdap.org), Certificate Transparency logs
(crt.sh), and the HSTS preload list (hstspreload.org). the domains and IP
addresses you look up are therefore visible to these resolvers and services, and
may be logged by them under their own policies. we do not see or record any of
it.

if you configure a Webhook or Slack integration, Domain Dig sends alerts to the
URL you provide; that destination is chosen and controlled by you.

## changes

if this policy changes, the updated version will be posted here with a new date.

## contact

questions: [root@krz.sh](mailto:root@krz.sh).
