+++
title = "Hutch"
description = "A native iOS client for SourceHut."
weight = 1

[extra]
link = "https://github.com/krazywarez/hutch"
link_label = "Source"
appstore = "https://apps.apple.com/us/app/hutch-for-sourcehut/id6760742299"
privacy = "/privacy/hutch/"
+++

SourceHut workflows, built for mobile.

Hutch is a fast, native iOS app for working with [SourceHut](https://sr.ht) when
you're away from your desk. it focuses on what matters on mobile: triaging work,
reviewing patches, monitoring builds, following discussions, and managing
repositories and tickets — without a browser. available now on the App Store for
iPhone.

## why it exists

SourceHut is intentionally simple, efficient, and workflow-focused. Hutch brings
that same philosophy to iOS: an interface designed for quick decisions and real
work on the go, not a stripped-down viewer. it's built to read, respond, create,
and manage work across the SourceHut ecosystem.

## what it does

- review patch threads and browse mailing lists
- manage trackers, tickets, assignees, labels, and comments
- browse Git and Mercurial repositories, files, refs, commits, and diffs
- submit, monitor, retry, and inspect builds and logs
- follow projects linking repositories, trackers, and lists
- manage profile settings, SSH keys, PGP keys, and access tokens

## interface

from patch review to trackers, builds, and repositories, Hutch is built to make
SourceHut feel at home on iOS.

<div class="shots">
<figure><img loading="lazy" src="https://img.cleberg.net/apps/hutch/screenshots/iphone/01_patch.jpg" alt="Patch review"><figcaption>review patches anywhere</figcaption></figure>
<figure><img loading="lazy" src="https://img.cleberg.net/apps/hutch/screenshots/iphone/02_thread.jpg" alt="Threaded inbox"><figcaption>stay on top of discussions</figcaption></figure>
<figure><img loading="lazy" src="https://img.cleberg.net/apps/hutch/screenshots/iphone/03_builds.jpg" alt="Builds"><figcaption>monitor builds in real time</figcaption></figure>
<figure><img loading="lazy" src="https://img.cleberg.net/apps/hutch/screenshots/iphone/04_tickets.jpg" alt="Tickets"><figcaption>manage issues on the go</figcaption></figure>
<figure><img loading="lazy" src="https://img.cleberg.net/apps/hutch/screenshots/iphone/05_repo.jpg" alt="Repository diff"><figcaption>explore your code</figcaption></figure>
<figure><img loading="lazy" src="https://img.cleberg.net/apps/hutch/screenshots/iphone/06_projects.jpg" alt="Projects"><figcaption>everything in one place</figcaption></figure>
<figure><img loading="lazy" src="https://img.cleberg.net/apps/hutch/screenshots/iphone/07_actions.jpg" alt="Build submission"><figcaption>take action instantly</figcaption></figure>
</div>

## major features

- home dashboard with projects, assigned tickets, recent builds, and inbox shortcuts
- unread-first inbox with thread detail, patch rendering, and reply via Apple Mail
- Git and Mercurial repository browsing, settings, ACLs, and creation flows
- tracker and ticket workflows: comments, assignees, resolutions, and labels
- build submission, history, log viewing, cancellation, and rebuild flows
- project views linking repositories, trackers, and mailing lists into one hub

## built for sourcehut users

- native Swift interface with no analytics, ads, or tracking SDKs
- deep links for repositories, tickets, and builds via `hutch://`
- share actions across repositories, files, commits, tickets, builds, and profiles
- pull-to-refresh, loading, empty, and error states across major screens
- Keychain-backed auth with secure SourceHut personal access tokens

## resources

- [project homepage](https://sr.ht/~ccleberg/Hutch/)
- [issue tracker](https://todo.sr.ht/~ccleberg/Hutch/)
- [hutch-devel mailing list](https://lists.sr.ht/~ccleberg/hutch-devel)
- [hutch-announce mailing list](https://lists.sr.ht/~ccleberg/hutch-announce)
