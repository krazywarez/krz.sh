+++
title = "Moonrise Privacy Policy"
description = "Privacy policy for Moonrise, the night sky and space app for iPhone, iPad and Apple Watch."
weight = 5

[extra]
app = "apps/moonrise.md"
+++

_last updated: 19 october 2026_

Moonrise shows the night sky, the solar system, the Sun and space launches. it
has no accounts, no analytics, no advertising, no in-app purchases, and no
third-party trackers or SDKs.

## what we collect

nothing, unless you turn on aurora alerts or news alerts. those are described
below.

## location

if you allow it, Moonrise uses your location to work out where the Sun, Moon,
planets, stars and satellites are in your sky. this happens on your device.
your location is not sent to us or to anyone else. you can choose a city in
Settings instead.

## network connections

to show live data, the app requests:

- space weather, launch schedules and satellite orbits from our server,
  moonrise-server.audit-labs.workers.dev, which runs on Cloudflare Workers;
- space weather and aurora data from NOAA's Space Weather Prediction Center;
- images of the Sun from NASA's Solar Dynamics Observatory;
- images in the Library from NASA, ESA, ESO, NOIRLab and the Library of
  Congress;
- Deep Space Network status and Mars rover raw images from NASA/JPL;
- space news headlines from the Spaceflight News API, run by The Space Devs.

these requests contain no identifiers. as with any internet request, the
servers receive your IP address. Cloudflare may keep short-lived logs; see
Cloudflare's privacy policy.

## aurora and news alerts

both are off until you turn them on in Settings. when either is on, the app
sends our server:

- this device's push notification token, which Apple issues so a server can
  send it notifications;
- a 5° band of geomagnetic latitude worked out on the device (for example
  "50° to 55° north"), not your location;
- your time zone's offset from UTC, so aurora alerts arrive at night and the
  news digest at 9 a.m.;
- which of the two alerts are on.

these are stored with the time the device last checked in and used only to
send those alerts. they are not linked to your identity or shared. turning
both alerts off deletes them from the server. a token that Apple reports as no
longer valid is deleted automatically.

## data on your device

your settings, chosen city, the daily summary notification and your observing
log stay on the device. the observing log is saved as plain-text files you can
read in the Files app. they are included in your device's iCloud or computer
backups if you have those turned on. deleting the app deletes them, apart from
any log files you have moved elsewhere.

## live activities

a launch countdown on the Lock Screen runs on your device and sends nothing to
our server.

## changes

if this policy changes, the updated version will be posted here with a new date.

## contact

questions: [root@krz.sh](mailto:root@krz.sh).
