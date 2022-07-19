---
id: r08bzdg34axuhyu8ljpt4r8
title: Format the boot partition to FAT32
desc: ''
updated: 1652815757263
created: 20211101191427820
tags:
  - tidbits
---

- Areas: [[devlog.linux]]

---

`sudo mkfs.vfat -F32 /dev/sdb1` make sure to change `/dev/sdb1` to the appropriate disk name
