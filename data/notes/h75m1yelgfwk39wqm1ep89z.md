
![[devlog.subnet# Drawbacks-of-Classful-Addressing]]

## Classless Interdomain Routing (CIDR)

CIDR is a notation for describing blocks of IP addresses and is used heavily in various networking configurations. IP addresses contain 4 octets, each consisting of 8 bits giving values between 0 and 255. The decimal value that comes after the slash is the number of bits consisting of the routing prefix. This in turn can be translated into a netmask, and also designates how many available addresses are in the block.

Sometimes we want to vary the length of our subnet masks and we don’t want to stick to the standard classes so we use CIDR. It helps optimize the IP space. It uses variable length subnet mask(VLSM).

CIDR (Classless Inter-Domain Routing) -- also known as supernetting -- is a method of assigning Internet Protocol (IP) addresses that improves the efficiency of address distribution and replaces the previous system based on Class A, Class B and Class C networks.

## Resources

- [CIDR.xyz](https://cidr.xyz/)
- [IPv4, CIDR, and VPC Subnets Made Simple! - YouTube](https://www.youtube.com/watch?v=z07HTSzzp3o&t=216s)
