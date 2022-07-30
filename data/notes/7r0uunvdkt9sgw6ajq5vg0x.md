
- Areas: [[areas.networking]]

---

A device that connects two different networks together and intelligently forwards traffic to and from a network based on its logical address([[devlog.ip address]])

Modern routers use [[devlog.ip address]]es to determine the routing of network traffic, although there are other routing protocols as well.

---

- Layer 3 device used to connect multiple networks together
- Making forwarding decisions based on logical network address information
  - Such as using [[devlog.ip address]]es ([[devlog.IPv4]] or [[devlog.IPv6]])
- Routers are typically more feature rich and support a broader range of interface types than multilayer [[devlog.Switch]]es

---

- Each port is a separate [[devlog.collision domains]]
- Each port is a separate [[devlog.broadcast domain]]

**How a router routes a packet:**

When a router receives a packet, it makes a routing decision based on the destination address portion of the packet. It then looks up the destination address in its routing table. If the destination address is within a known network/subnetwork, the router forwards the packet to the next hop gateway for that destination network/subnetwork. Once the packet leaves the router, it is the responsibility of the next hop gateway to forward the packet to its final destination. If the router does not have the destination network in its routing table, it may forward the packet to a predetermined default gateway if configured and let the default gateway handle getting the packet to the destination network or it will drop the packet and inform the sending host that the network is not reachable.

The routing table is a list of networks that router knows about. It can learn these routes by 3 means: a routing protocol such as; [[devlog.RIP]], [[devlog.IGRP]], and [[devlog.OSPF]], a static route that has been manually been set by a network administrator, or by being directly connected to that network on one of its interfaces.

The routing table will contain many pieces of information about the learned network, but the main information is the network address and the next hop gateway.

The network address can be either a full class network address or a subnetwork address, depending on the netmask being used. The next hop gateway is the ip address of the gateway to hand off the outbound packet to.

Keep in mind that all of the routers must know of a way to reach each other. The receiving host must have a path to get back to the sending host in order for data to pass.

Via — [Basic IP Addressing and Troubleshooting Guide](http://penta2.ufrgs.br/trouble/ts_ip.htm)
