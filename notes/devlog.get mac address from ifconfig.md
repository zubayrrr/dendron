---
id: en7wdmf7rc8a7l3s8940klv
title: Get MAC Address from ifconfig
desc: ''
updated: 1652818339102
created: 20211022180919380
tags:
  - tidbits
---

- Areas: [[areas.networking]]

---

`ifconfig | grep ether | cut -d" " -f10`  
using [[cut]], [[ifconfig]], [[devlog.grep]]
