
- Areas: [[devlog.linux]], [[areas.networking]]

---

- Getting Information about the Network Interfaces
  - [[ifconfig]], [[devlog.ip]]
  - `lo` stands for loopback (inteface)
  - [[enp0s3]] for the [[devlog.Ethernet]] interface
  - There are other names for interfaces such as [[wlo1]] , [[wlan0]] for wireless interface.
- When configuring network intefaces using [[devlog.ip]], [[ipconfig]], [[devlog.route]] you must run them as root([[devlog.sudo]])
- Network inteface configuration set by [[ifconfig]] or [[devlog.ip]] are not persistent, after a system restart all the changes are lost. To make them persist, we need to edit distro specifc configuration file. For example on Ubuntu you have to use [[devlog.netplan]], [[systemd-networkd]] for static configuration of the network.
- Network Troubleshooting/Tesing
  - [[devlog.ping]]
