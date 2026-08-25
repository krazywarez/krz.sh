+++
title = "Domain Dig"
description = "DNS and SSL analysis, in your pocket."
weight = 2

[extra]
link = "https://gitbay.org/krz/domain-dig"
link_label = "Source"
appstore = "https://apps.apple.com/us/app/domaindig/id6760368004"
privacy = "/privacy/domain-dig/"
+++

See how any domain is really configured and served.

Domain Dig is a fast, native iOS app for inspecting a domain end to end. enter a
name and get a full report: DNS records, email-security posture, the live TLS
certificate and chain, HTTP headers, IP geolocation, and reachable ports — no
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

## interface

everything about a domain on one report — tap through the certificate chain,
email checks, and open ports.

<div class="shots">
<figure><img loading="lazy" src="https://i.krz.sh/apps/domaindig/screenshots/iPhone/01.png" alt="Lookup and DNS records"><figcaption>run a lookup, see everything</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/domaindig/screenshots/iPhone/02.png" alt="Record types and email security"><figcaption>every record type and email check</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/domaindig/screenshots/iPhone/03.png" alt="SSL certificate and chain"><figcaption>full TLS certificate and chain</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/domaindig/screenshots/iPhone/04.png" alt="IP location and open ports"><figcaption>IP geolocation and open ports</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/domaindig/screenshots/iPhone/05.png" alt="Saved domains"><figcaption>save the domains you watch</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/domaindig/screenshots/iPhone/06.png" alt="Lookup history"><figcaption>history, kept on device</figcaption></figure>
<figure><img loading="lazy" src="https://i.krz.sh/apps/domaindig/screenshots/iPhone/07.png" alt="Resolver settings"><figcaption>choose your DNS resolver</figcaption></figure>
</div>

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
