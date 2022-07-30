
- Areas: [[devlog.linux]]

---

`netplan` is used to statically configured a network interface. Typically Laptops and Desktops have their [[devlog.ip address]] assigned dynamically by a [[DHCP]] server(in most cases, the [[devlog.router]]), however a server requires a static configuration to avoid single point of failure problem using a [[DHCP]] server.

`netplan` is default network configuration tool in Ubuntu. It uses [[YAML]] files located in ``/etc/netplan`, it currently supports two renderers or backend services to control network interfaces on Ubuntu based systems, they're [[NetworkManager]] and [[systemd-networkd]].

[[NetworkManager]] is commonly used Desktop machines while [[systemd-networkd]] is used on servers without a [[GUI]].
