---
id: b22uf82a31xkdp1cnlx713v
title: Nmap
desc: ''
updated: 1653437672473
created: 20211011081705090
caption: Network Mapper
---

- Network Mapper is a command line tool that maps the network.
- Do [[devlog.ping]] sweeps to check what is up and available.
- Look at individual ports and what OS that remote [[devlog.Server]] is running.

---

Scanning from a machine connected to the [[devlog.LAN]], scanning for open ports on a web server also on [[devlog.LAN]] using [[devlog.Nmap]]

    nmap -sS -O 10.0.2.6 |more

- `-sS` tells `nmap` to do a SYN Scan using only SYN packets from the [Three-Way Handshake] (SYN-SYN/ACK-ACK).
- `-O` tells `nmap` to also scan what OS the web server is using.
- `10.0.2.0` should be replaced with the target [[devlog.ip address]].
- `|more` tells `nmap` to give result one after another.
- Example Output: ![](https://raw.githubusercontent.com/zubayrrr/twiki/main/bin/image.pbozqpwksbr.png)
- All of the unused service/port should be closed to make the server secure.
- [[zenmap]] is GUI for [[devlog.Nmap]]
