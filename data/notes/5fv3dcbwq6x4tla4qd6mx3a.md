
## Networking Basics

- **Host** are any devices which send or receive traffic.
- [[devlog.IP Address]] the identity of each host.

**Networks**

- A logical group of hosts which require similar connectivity.
- A network is what transports traffic between hosts.
- Networks can contain other networks([[devlog.subnet]]s).
- Networks connect to other networks([[devlog.internet]]).

**Switches**

- Switches facilitate communication within a network.
- A switch forwards data packets between hosts. A switch sends packets directly to hosts.
- A switch only sends data to the single device it is intended for (unlike a [[devlog.hub]], which is very dumb).
- Network: A Grouping of hosts which require similar connectivity.
- Hosts on a Network share the same IP address space.

**Modem**

- [[devlog.Modem]] is short for modulator/demodulator.
- There are two kinds of signals:
  - A computer **only** reads Digital Signal.
  - Analog Signal that is used on the internet.
- To deal with this a modem is introduced - whose responsibility is a to convert the signals from Digital to Analog and vice versa.

![](https://res.cloudinary.com/zubayr/image/upload/v1656493565/wiki/g8gzj19fawcjw7v4xr06.png)

**Router**

A [[devlog.router]] comes into the picture after a modem.

There are generally two kinds of Routers - large routers for business and small routers for homes/small offices.

Let's talk about small office/home routers:

A router is what routes or passes internet connection to all your devices(after modem has done it's thing).

![](https://res.cloudinary.com/zubayr/image/upload/v1656493698/wiki/vl4jvm2mj37ysepiueqd.png)

These small office/home routers typically come with a builtin switch with multiple ports(so you can connect multiple devices using ethernet cable connection), it also functions as a wireless access point so that Wi-Fi enabled devices can also have internet access.

If you only need one device to access the internet you don't need a router - you can simply use a modem.

---

Routers select paths for data packets to cross networks and reach their destinations. This is done by connecting with different networks and forwarding data from network to network.

Router facilitates communication between networks. As we said before that a switch looks after communication within a network a router allows us to join these networks together or at least give them access to each other if permitted.

A router can provide a traffic control point (security, filtering, redirecting) More and more switches also provide some of these functions now.

Routers learn which networks they are attached to. These are known as routes, a routing table is all the networks a router knows about.

A router has an IP address in the networks they are attached to. This IP is also going to be each host's way out of their local network also known as a gateway.

---

![[devlog.osi model]]
![[devlog.tcp⁄ip model]]
![[devlog.ipv4]]
![[devlog.cidr]]