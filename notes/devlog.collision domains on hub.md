---
id: e0ug7ilzwuclmjrey8psnvv
title: Collision Domains on Hub
desc: ''
updated: 1653318485179
created: 20211013094627410
---

- [[devlog.Hub]]s were used to connect multiple network segments together
- Each [[devlog.LAN]] segment becomes a separate [[devlog.Collision Domains]]
- As the network gets larger in which a [[devlog.Hub]] is being utilized to connect all the machines, the network will get more chaotic as [[devlog.Hub]] don't break up [[devlog.Collision Domains]], it'll be treated as one large collision domain.
- To deal with this issue a [[devlog.Bridge]] needs to be introduced to the network.

![](https://raw.githubusercontent.com/zubayrrr/twiki/main/bin/image.cqfqt7rooe6.png)
