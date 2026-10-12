+++
title = "Domain Dig"
description = "DNS and SSL analysis, in your pocket."
weight = 2

[extra]
link = "https://gitbay.org/krz/domain-dig"
link_label = "Source"
appstore = "https://apps.apple.com/us/app/domaindig/id6760368004"
privacy = "/privacy/domain-dig/"
tagline = "See how any domain is really configured and served."
tint = "#0f766e"
platforms = ["iPhone"]
# icon = "https://i.krz.sh/apps/domain-dig/icon.png"
# header = "https://i.krz.sh/apps/domain-dig/header.jpg"

[[extra.highlights]]
title = "Every record"
text = "A to PTR, DNSSEC, reachability and the redirect chain."

[[extra.highlights]]
title = "Email security"
text = "SPF, DMARC, DKIM, MTA-STS and BIMI in one check."

[[extra.highlights]]
title = "TLS, end to end"
text = "Certificate, SANs, cipher and the full chain."

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/01.jpg"
alt = "Lookup and DNS records"
caption = "run a lookup, see everything"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/02.jpg"
alt = "Record types and email security"
caption = "every record type and email check"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/03.jpg"
alt = "SSL certificate and chain"
caption = "full TLS certificate and chain"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/04.jpg"
alt = "IP location and open ports"
caption = "IP geolocation and open ports"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/05.jpg"
alt = "Saved domains"
caption = "save the domains you watch"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/06.jpg"
alt = "Lookup history"
caption = "history, kept on device"

[[extra.screenshots]]
src = "https://i.krz.sh/apps/domaindig/screenshots/web/07.jpg"
alt = "Resolver settings"
caption = "choose your DNS resolver"
+++

Domain Dig is a fast, native iOS app for inspecting a domain end to end. enter a
name and get a full report: DNS records, email-security posture, the live TLS
certificate and chain, HTTP headers, IP geolocation, and reachable ports. no
account, no tracking, everything rendered in plain monospace.

## why it exists

the answers you need about a domain are scattered across a dozen web tools. Domain
Dig pulls them into one screen you can run from your phone: reachability, records,
certificates, and headers in a single scrollable report.

## what it does

- run a full lookup on any domain from one screen
- read every DNS record type: A, AAAA, MX, TXT, NS, SOA, CNAME, SRV, CAA, DS, PTR
- confirm DNSSEC and check reachability and the redirect chain
- audit email security: SPF, DMARC, DKIM, MTA-STS, and BIMI
- inspect the SSL/TLS certificate, SANs, validity, cipher, and full chain
- review HTTP response headers with a security grade
- geolocate the resolved IP and scan common ports
- look up registration and ownership via RDAP
- monitor domains and get alerts via webhook or Slack

## details that matter

- DNSSEC validation and a live TLS version and cipher-suite readout
- certificate chain depth, expiry countdown, and a jump to crt.sh
- email-security checks that flag missing SPF, DMARC, DKIM, MTA-STS, or BIMI
- a port scan that knows when a host sits behind Cloudflare's proxy
- pick your resolver: Cloudflare, Google, Quad9, or a custom server

## on your device

- save domains you watch and revisit past lookups from history
- everything is stored locally; nothing syncs to us
- optional iCloud sync (off by default) carries settings and history across your devices via your own iCloud account
