---
id: 43phw5fod5oq1gnkgfgplsf
title: Failed Authentications
desc: ''
updated: 1653305638881
created: '2021-10-22T00:00:00.000Z'
tags:
  - tidbits
---

- `cat -n /var/log/auth.log | grep -a "authentication failure"`
- `cat -n /var/log/auth.log | grep -a "authentication failure" | wc -1` using [[devlog.cat]], [[devlog.grep]] and [[devlog.wc]
