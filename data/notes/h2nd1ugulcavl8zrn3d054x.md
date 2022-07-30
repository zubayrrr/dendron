
- Areas: [[devlog.linux]]

---

Dropping packets from a list of IPs

```bash
#!/bin/bash

DROPPED_IPS="8.8.8.8 1.1.1.1 10.10.10.1"
for ip in $DROPPED_IPS
do
  echo "Dropping packets from $ip"
  iptables -I INPUT -s $ip -j DROP
done
```

Supply list of IPs from a txt file

```bash
#!/bin/bash

for ip in $(cat ips.txt)
do
  echo "Dropping packets from $ip"
  iptables -I INPUT -s $ip -j DROP
done
```
