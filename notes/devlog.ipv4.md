---
id: d6dakasx29em4cil8uhjy62
title: Ipv4
desc: ""
updated: 1656595275716
created: 1656585263009
---

# IPv4 Addressing

The IPv4 address is a 32-bit number that uniquely identifies a network interface on a system. An IPv4 address is written in decimal digits, divided into four 8-bit fields that are separated by periods. Each 8-bit field represents a byte of the IPv4 address. This form of representing the bytes of an IPv4 address is often referred to as the dotted-decimal format.

![](https://res.cloudinary.com/zubayr/image/upload/v1656592001/wiki/uraeawlkks6yqmy5ci3n.png)

The following figure shows the component parts of an IPv4 address, `172.16.50.56`.

#### Parts of IPv4

- **Network part:**   
  The network part indicates the distinctive variety that’s appointed to the network. The network part conjointly identifies the category of the network that’s assigned.
- **Host Part:**   
  The host part uniquely identifies the machine on your network. This part of the IPv4 address is assigned to every host.   
  For each host on the network, the network part is the same, however, the host half must vary.
- **Subnet number:**   
  This is the nonobligatory part of IPv4. Local networks that have massive numbers of hosts are divided into subnets and subnet numbers are appointed to that.

![](https://res.cloudinary.com/zubayr/image/upload/v1656585458/wiki/yavrzufmne9yunyfearq.png)

- Subnet mask defines the network portion
  - Network portion if binary 1
  - Host portion if binary 0

![](https://res.cloudinary.com/zubayr/image/upload/v1656592063/wiki/gapcxwmkfgyk1pocnobt.png)

![[devlog.subnet# Classes-of-IP-Address]]

## Routable IPs

- Publically routable IP addresses are globally managed by ICANN.
	- Internet Corporation for Assigned Names and Numbers
		- ARIN, LACNIC, AFNIC, APNIC and RIPE NCC
	- Public IPs must be purchased before use through your ISP.


## Private IPs

- Private IP’s can be used by anyone.
- Not routable outside your local area network.
- [[devlog.NAT]] allows for routing of private IPs through a public IP.

![](https://res.cloudinary.com/zubayr/image/upload/v1656595632/wiki/dqv5dipadhxwg6buduxl.png)

## Specialized IPs

- Loopback address (`127.x.x.x` range) Home
	- Refers to the device itself and is used for testing 
	- Most commonly used at `127.0.0.1`

- Automatic Private IP Addresses (APIPA)
	- Dynamically assigned by OS when DHCP server is unavailable and an address has not been assigned.
	- Range of `169.254.x.x`

![](https://res.cloudinary.com/zubayr/image/upload/v1656595864/wiki/ialin5xihhskcrxzkger.png)


Special address ranges are never assigned by an administrator or DHCP server.