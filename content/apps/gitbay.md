+++
title = "gitbay"
description = "A native iOS client for gitbay, a CLI-first git forge."
weight = 3

[extra]
link = "https://gitbay.org/krz/gitbay-ios"
link_label = "Source"
privacy = "https://gitbay.org/privacy"
appstore = "https://apps.apple.com/us/app/gitbay/id6806399095"
tagline = "Your forge, from the couch."
tint = "#4338ca"
platforms = ["iPhone", "iPad"]
icon = "https://i.krz.sh/apps/gitbay/icon.png"
header = "https://i.krz.sh/apps/gitbay/hero.jpg"

[[extra.highlights]]
title = "Review and merge"
text = "Unified diffs, inline comments and approvals."

[[extra.highlights]]
title = "Watch builds"
text = "Pick a job and read the logs when a build goes red."

[[extra.highlights]]
title = "No passwords"
text = "A scoped token minted over SSH, kept in the keychain."

[[extra.screenshots]]
src = "https://i.krz.sh/apps/gitbay/screenshots/web/01_dashboard.jpg"
alt = "Dashboard"
caption = "what is waiting on you"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/gitbay/screenshots/web/02_repo.jpg"
alt = "Repository"
caption = "every repository surface in one list"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/gitbay/screenshots/web/03_mr_list.jpg"
alt = "Merge requests"
caption = "merge requests, open through merged"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/gitbay/screenshots/web/04_mr_detail.jpg"
alt = "Merge request detail"
caption = "description, checks, reviews, commits"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/gitbay/screenshots/web/05_diff.jpg"
alt = "Unified diff"
caption = "read the diff, then decide"
+++

gitbay is a native iOS app for [gitbay](https://gitbay.org), a CLI-first git
forge where SSH is the API and the command line is the product. the app is the
other half of that: a reading, reviewing and responding surface for the times
you are not at a keyboard. universal, for iPhone and iPad.

## why it exists

gitbay is built so the terminal is the primary interface, and nothing about it
needs a browser. but review does not always happen at a desk. this app is for
the parts of the work that are decisions rather than typing: reading a diff,
answering a question, approving a merge, checking why a build went red. it does
that without pretending a phone is a workstation.

## what it does

- read and review merge requests, with a unified diff and inline comments
- triage issues: labels, assignees, milestones, comments
- browse repositories: file tree, blobs with syntax highlighting, history at a
  ref or per file, blame, branches and tags
- edit a file on a branch, when the fix is one line
- watch builds, pick a job, read the logs
- read releases and the wiki
- explore repositories, follow activity, and read profiles

## READMEs that render properly

Markdown and Org both render. Org is not converted to HTML and shown in a web
view; it renders as native views through
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
advertising, and no third-party analytics: two dependencies in total, both for
rendering. what you read and what you write stays between your device and your
forge.
