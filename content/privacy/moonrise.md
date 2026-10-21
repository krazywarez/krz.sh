+++
title = "Moonrise Privacy Policy"
description = "Privacy policy for Moonrise, the night sky and space app for iPhone, iPad and Apple Watch."
weight = 5

[extra]
app = "apps/moonrise.md"
+++

_last updated: 21 october 2026_

Moonrise has no accounts, no analytics, no advertising, no in-app purchases,
and no third-party trackers or SDKs. your location is never sent to our
server. if you turn on aurora alerts or news alerts, the app sends our server
four things needed to deliver them, described below. if you turn on cloud
forecasts, it sends a rounded location to Apple's weather service. nothing
else is collected.

## location

if you allow it, Moonrise uses your location to work out where the Sun, Moon,
planets, stars and satellites are in your sky. this happens on your device.
your location is never sent to us. you can choose a city in Settings instead.

## cloud forecasts

cloud forecasts are off until you turn them on in Settings. when they are on,
the app asks Apple's weather service (WeatherKit) for an hourly forecast,
sending your location or chosen city rounded to 0.1° of latitude and
longitude, about 10 km. it asks at most once every three hours for each place,
and only while the app is open. the request goes from your device to Apple,
not through our server. Apple states that this location is used only to
provide the forecast, is not associated with personally identifiable
information and is not tracked between requests. the forecast is kept on your
device. turning cloud forecasts off deletes it.

## network connections

to show live data, the app requests:

- space weather, launch schedules and satellite orbits from our server,
  moonrise.krz.sh, which runs on Cloudflare Workers;
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
longer valid is deleted automatically, and so is any device that has not
checked in for 180 days.

## live activities

Live Activities on the Lock Screen (launch countdowns, satellite passes and
eclipse contact times) run on your device and send nothing to our server. when
you follow a launch, its countdown can be updated if the launch is held,
delayed or scrubbed. those updates are broadcast by our server through Apple to
every device following that launch; the broadcast does not identify your
device, and our server does not know who is following.

## data on your device

your settings, chosen city, the daily summary notification, the cloud forecast
and your observing log stay on the device. the observing log is saved as
plain-text files you can read in the Files app. they are included in your
device's iCloud or computer backups if you have those turned on. deleting the
app deletes them, apart from any log files you have moved elsewhere.

## changes

if this policy changes, the updated version will be posted here with a new date.

## contact

questions: [root@krz.sh](mailto:root@krz.sh).
