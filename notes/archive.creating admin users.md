---
id: qh05nhekoydzi8s33m16o05
title: Creating Admin users
desc: ''
updated: 1653683844830
created: '2021-10-26T00:00:00.000Z'
tags:
  - tidbits
---

## Creating Admin Users

- A user has to be added to the [[devlog.sudo]] [[devlog.group]] or the `sudoer file` inorder for them to use `sudo` privileges, [[usermod]] can be used to achieve this.
  - `sudo usermod -aG sudo james`
