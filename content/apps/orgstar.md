+++
title = "orgstar"
description = "An Org mode editor and agenda for Mac, iPhone and iPad."
weight = 4

[extra]
link = "https://gitbay.org/krz/orgstar"
link_label = "Source"
appstore = "https://apps.apple.com/us/app/orgstar-org-mode-agenda/id6821552018"
privacy = "/privacy/orgstar/"
tagline = "Your org files, wherever you are."
tint = "#5b7a2e"
platforms = ["Mac", "iPhone", "iPad"]
icon = "https://i.krz.sh/apps/orgstar/icon.png"
header = "https://i.krz.sh/apps/orgstar/hero.jpg?v=0.7.0"

[[extra.highlights]]
title = "Plain text"
text = "Reads and writes the same files Emacs does, byte for byte."

[[extra.highlights]]
title = "Agenda"
text = "Scheduled items, deadlines, habits and calendar events."

[[extra.highlights]]
title = "Capture anywhere"
text = "Templates from the app, share sheet, Shortcuts and widgets."

[[extra.screenshots]]
src = "https://i.krz.sh/apps/orgstar/screenshots/web/01-agenda.jpg"
alt = "Agenda"
caption = "the agenda across your files"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/orgstar/screenshots/web/02-reader.jpg"
alt = "Reader"
caption = "read with folding"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/orgstar/screenshots/web/03-editor.jpg"
alt = "Editor"
caption = "edit with Org's commands"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/orgstar/screenshots/web/04-tables.jpg"
alt = "Tables"
caption = "tables and formulas"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/orgstar/screenshots/web/05-capture.jpg"
alt = "Capture"
caption = "capture with templates"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/orgstar/screenshots/web/06-search.jpg"
alt = "Search"
caption = "search everything"
+++

orgstar is a native editor for [Org mode](https://orgmode.org) files on the Mac,
with an app for iPhone and iPad. it reads and writes the same plain-text files
Emacs does, behaves the way Org does where the two overlap, and leaves every
byte you didn't change as it was, so Emacs and your sync tool can work on the
same folder.

## why it exists

Org mode is a plain-text system for notes, tasks and planning, and it
lives inside Emacs. orgstar is for the times Emacs isn't there: on a phone, on
an iPad, or on a Mac where you want a native app. the files stay the source of
truth. there is no database of your notes, only an index for search and the
agenda, rebuilt from the files whenever they change.

## what it does

- edit headings, TODO keywords, priorities, tags, timestamps, lists, tables and
  source blocks, styled as you type
- see scheduled items, deadlines, habits and calendar events in the agenda
- capture with Org's templates, from the app, the share sheet, Shortcuts or
  org-protocol links
- clock in and out of entries and read clock reports
- compute table formulas and tangle source blocks into files
- export to HTML and Markdown
- search across file names, headings and text

## on the Mac

the Mac app adds Emacs, Mac and Doom (Vim) keys, a board view, Babel for more
languages, and export through Emacs when it is installed. install it with
Homebrew:

```sh
brew tap krz/tap https://gitbay.org/krz/homebrew-tap.git
brew install --cask orgstar
```

## on iPhone and iPad

the iOS app has the editor, agenda, capture, search, clocking, reminders,
export and tangling, plus Home Screen and Lock Screen widgets and a Live
Activity for the running clock. it works on folders you choose in iCloud Drive
or another app's storage, such as a Syncthing folder.

## the manual

every feature is documented in the
[orgstar manual](https://krz.gitbay.site/orgstar/).

## no analytics, no ads, no SDKs

no accounts, no tracking, no third-party SDKs. your notes stay in your folders.
