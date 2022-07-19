---
id: kw0o7kw0m2y89681r3nv66d
title: Connection Testing
desc: ''
updated: 1653136419204
created: 1653136097978
tags:
  - tidbits
---

- Areas: [[devlog.linux]]

---

A bash script to constantly check the network connection to the default gateway or a machine on the LAN or a remote machine on the internet.

```bash
#!/bin/bash
output="$(ping -c 3 $1)"
# echo "$output"

if [[ "$output" == *"100% packet loss"*]];then
  echo "network connection to $1 is not working!"
else
  echo "network connection to $1 is working!"
```
