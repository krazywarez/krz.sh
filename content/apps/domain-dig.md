+++
title = "Domain Dig"
description = "DNS, TLS, email security and ownership for any domain, with monitoring, audits and exports."
weight = 2

[extra]
link = "https://gitbay.org/krz/domain-dig"
link_label = "Source"
appstore = "https://apps.apple.com/us/app/domaindig/id6760368004"
privacy = "/privacy/domain-dig/"
tagline = "See how any domain is really configured and served."
tint = "#1c57bd"
platforms = ["iPhone", "iPad"]
icon = "https://i.krz.sh/apps/domaindig/icon.png?v=5.5.3"
header = "https://i.krz.sh/apps/domaindig/hero.jpg?v=5.5.3"

[[extra.highlights]]
title = "Every record"
text = "A to PTR, DNSSEC, the redirect chain and what answers on the wire."

[[extra.highlights]]
title = "Email and TLS"
text = "SPF, DMARC, DKIM, MTA-STS and BIMI; the certificate, chain and cipher."

[[extra.highlights]]
title = "A portfolio, not a lookup"
text = "Track domains, monitor them on a schedule, keep the snapshots and audit them."

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/01.jpg?v=5.5.3"
alt = "Lookup, summary and risk score"
caption = "run a lookup, see everything"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/02.jpg?v=5.5.3"
alt = "DNS records and DNSSEC"
caption = "every record, with DNSSEC"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/03.jpg?v=5.5.3"
alt = "Email security checks"
caption = "SPF, DMARC, DKIM, MTA-STS, BIMI"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/04.jpg?v=5.5.3"
alt = "TLS certificate details"
caption = "the certificate, chain and cipher"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/05.jpg?v=5.5.3"
alt = "IP location and port scan"
caption = "where it resolves, and what answers"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/06.jpg?v=5.5.3"
alt = "Portfolio dashboard"
caption = "the whole portfolio at a glance"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/07.jpg?v=5.5.3"
alt = "Watchlist"
caption = "watch the domains that matter"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/08.jpg?v=5.5.3"
alt = "Resolver and network settings"
caption = "your resolver, your enrichment"
+++

Domain Dig is a fast, native app for inspecting a domain end to end. enter a
name and get a full report: DNS records, email-security posture, the live TLS
certificate and chain, HTTP headers, IP geolocation, reachable ports, and
registration. no account, no tracking, everything rendered in plain monospace.

## why it exists

the answers you need about a domain are scattered across a dozen web tools.
Domain Dig pulls them into one screen you can run from your phone, then keeps
what it found: reachability, records, certificates, and headers in a single
scrollable report, with a snapshot history behind it.

## what it does

- run a full lookup on any domain, one at a time or a pasted list
- read every DNS record type: A, AAAA, MX, TXT, NS, SOA, CNAME, SRV, CAA, DS, PTR
- confirm DNSSEC and check reachability and the redirect chain
- audit email security: SPF, DMARC, DKIM, MTA-STS, and BIMI
- inspect the SSL/TLS certificate, SANs, validity, cipher, and full chain
- review HTTP response headers with a security grade
- geolocate the resolved IP and scan common ports
- look up registration and ownership via RDAP, and discover subdomains
- roll every check into a risk score with plain-language insights
- track domains on a dashboard, monitor them on a schedule, and get alerts
- group domains into workflows and run them as a batch
- compare two domains side by side, or one domain against its own history
- run structured audit sessions with checklists, findings, and evidence
- export as text, CSV, JSON, Markdown, or PDF, single report or whole portfolio

## details that matter

- DNSSEC validation and a live TLS version and cipher-suite readout
- certificate chain depth, expiry countdown, and a jump to crt.sh
- email-security checks that flag missing SPF, DMARC, DKIM, MTA-STS, or BIMI
- a port scan that knows when a host sits behind Cloudflare's proxy
- pick your resolver: Cloudflare, Google, Quad9, or a custom server
- a Quick lookup profile when you do not need every check
- third-party enrichment is a switch: turn it off and nothing goes to rdap.org,
  crt.sh, or ipapi.co
- alerts over webhook, Slack, or SMTP, and finished reports uploaded to your own
  S3-compatible bucket
- a local API, Home Screen widgets, Shortcuts, and a share extension

## on your device

- everything is stored locally; nothing syncs to us, and there is no backend
- optional iCloud sync (off by default) carries settings, domains, and history
  across your devices via your own iCloud account
- back up and restore the whole store, or import and export what you choose
