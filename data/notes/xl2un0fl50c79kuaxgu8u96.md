
- Source: https://www.metaswitch.com/knowledge-center/reference/what-is-open-shortest-path-first-ospf
- Author: Iwan Price-Evans
- Areas: [[areas.networking]]

***

# What is Open Shortest Path First (OSPF)?

> ## Excerpt
> The OSPF (Open Shortest Path First) protocol is used to distribute IP routing information throughout a single Autonomous System (AS) in an IP network.

---
The OSPF (Open Shortest Path First) protocol is one of a family of IP Routing protocols, and is an Interior Gateway Protocol (IGP) for the Internet, used to distribute IP routing information throughout a single Autonomous System (AS) in an IP network.

The OSPF protocol is a link-state routing protocol, which means that the routers exchange topology information with their nearest neighbors. The topology information is flooded throughout the AS, so that every router within the AS has a complete picture of the topology of the AS. This picture is then used to calculate end-to-end paths through the AS, normally using a variant of the Dijkstra algorithm. Therefore, in a link-state routing protocol, the next hop address to which data is forwarded is determined by choosing the best end-to-end path to the eventual destination.
