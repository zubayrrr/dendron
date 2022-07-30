
- Comprised of all devices on shared [[devlog.Ethernet]] segment (everything on same cable or [[devlog.Hub]])
- Devices operate at half-duplex when connected to a [[devlog.Hub]] (Layer 1 Device)
- Devices must listen before they transmit to avoid collisions when operating as `CSMA/CD`
- The larger the Collision Domain, the more chaos in the network.
- Collision Domains need to broken down into smaller chunks for more efficiency

---

### Collision Domains on [[devlog.Switch]]es

- [[devlog.Ethernet]] [[devlog.Switch]]es increase scalability of the network by creating multiple collision domains
- Each port on a switch is a Collision Domain, no chance of collisions and increases speed
- Switches can operate in full-duplex mode

---

### Collision Domains on [[devlog.Hub]]s

- [[devlog.Hub]]s were used to connect multiple network segments together
- Each [[devlog.LAN]] segment becomes a separate [[devlog.Collision Domains]]
- As the network gets larger in which a [[devlog.Hub]] is being utilized to connect all the machines, the network will get more chaotic as [[devlog.Hub]] don't break up [[devlog.Collision Domains]], it'll be treated as one large collision domain.
- To deal with this issue a [[devlog.Bridge]] needs to be introduced to the network.

![](https://raw.githubusercontent.com/zubayrrr/twiki/main/bin/image.cqfqt7rooe6.png)
