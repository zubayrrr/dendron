---
id: z1szfep23mzeolyvhmcpb2u
title: Wget Hacks
desc: ""
updated: 1655889609594
created: 1655889024932
tags:
  - tidbits
---

- Areas: [[devlog.linux]]

---

**Change user-agent**

Me: [[devlog.wget]] [URL]
Server: 403 FORBIDDEN
Me: wget -U Mozilla/5.0 [URL]
Server: 200 OK

Via - [(Ryan Castellucci on Twitter](https://twitter.com/ryancdotorg/status/1539168895059349504)

[`wget -U Googlebot` is like multipass for rate limiting](https://twitter.com/ryancdotorg/status/1539168895059349504)
