+++
title = "gitbay"
description = "A native iOS client for gitbay, a CLI-first git forge."
weight = 3

[extra]
link = "https://gitbay.org/krz/gitbay-ios"
link_label = "Source"
privacy = "https://gitbay.org/privacy"
appstore = "https://apps.apple.com/us/app/gitbay/id6806399095"
+++

your forge, from the couch.

gitbay is a native iOS app for [gitbay](https://gitbay.org), a CLI-first git
forge where SSH is the API and the command line is the product. the app is the
other half of that: a reading, reviewing and responding surface for the times
you are not at a keyboard. universal, for iPhone and iPad.

## why it exists

gitbay is built so the terminal is the primary interface, and nothing about it
needs a browser. but review does not always happen at a desk. this app is for
the parts of the work that are decisions rather than typing — reading a diff,
answering a question, approving a merge, checking why a build went red — without
pretending a phone is a workstation.

## what it does

- read and review merge requests, with a unified diff and inline comments
- triage issues: labels, assignees, milestones, comments
- browse repositories: file tree, blobs with syntax highlighting, history at a
  ref or per file, blame, branches and tags
- edit a file on a branch, when the fix is one line
- watch builds, pick a job, read the logs
- read releases and the wiki
- explore repositories, follow activity, and read profiles

## interface

<div class="shots">
<figure><img loading="lazy" src="https://i.krz.sh/apps/gitbay/screenshots/iphone/01_dashboard.jpg" alt="Dashboard"><figcaption>what is waiting on you</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/gitbay/screenshots/iphone/02_repo.jpg" alt="Repository"><figcaption>every repository surface in one list</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/gitbay/screenshots/iphone/03_mr_list.jpg" alt="Merge requests"><figcaption>merge requests, open through merged</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/gitbay/screenshots/iphone/04_mr_detail.jpg" alt="Merge request detail"><figcaption>description, checks, reviews, commits</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/gitbay/screenshots/iphone/05_diff.jpg" alt="Unified diff"><figcaption>read the diff, then decide</figcaption></figure>
</div>

## READMEs that render properly

Markdown and Org both render. Org is not converted to HTML and shown in a web
view — it renders as native views through
[OrgSwiftUI](https://gitbay.org/krz/org-swift), so the text is selectable, it
scales with Dynamic Type, and VoiceOver reads it. syntax highlighting inside
source blocks follows the system light and dark appearance.

## your key is your identity

there are no passwords and no krz account. auth is a bearer token you mint over
SSH on a machine that already has your key:

```sh
gitbay auth token create --name iphone --scope full --ttl 90d
```

the token lives in the iOS keychain. a read-only token works too, it just
cannot comment or merge.

## any instance

gitbay.org is not special. the host is entered at sign-in, so the app works
against whatever instance you run.

## no analytics, no ads, no SDKs

the app talks to your instance and to nothing else. there are no trackers, no
advertising, and no third-party analytics — two dependencies in total, both for
rendering. what you read and what you write stays between your device and your
forge.
