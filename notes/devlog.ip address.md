---
id: mj7tlpbhhzfpg8pbegkkasb
title: IP Address
desc: ""
updated: 1656492696567
created: "2021-10-09T00:00:00.000Z"
caption: Internet Protocol Address
---

Related: [[devlog.subnet]]

---

IP Address is basically how computers(servers) talk to each other on the internet. IP Address is provided by a Network Interface of a computer, these are public IP Addresses. IP Address are made user friendly by using a [[devlog.dns]]that converts a domain name to an IP Address.

**IP Address Components:**

Like other network layer protocols, the IP addressing scheme is integral to the process of routing IP data through an internetwork.

Each host on a TCP/IP network is assigned a unique 32-bit logical address. The IP address is divided into two main parts; the Network Number and the Host Number.

The network number identifies the network and must be assigned by the Internet Network Information Center (InterNIC) if the network is to be part of the Internet.

The host number identifies a host in the network and is assigned by the local network administrator.

**IP Address Format:**

The 32-bit IP address is grouped 8 bits at a time, each group of 8 bits is an octet. Each of the four octets are separated by a dot, and represented in decimal format, this is known as dotted decimal notation. Each bit in an octet has a binary weight (128, 64, 32, 16, 8, 4, 2, 1). The minimum value for an octet is 0 (all bits set to 0), and the maximum value for an octet is 255 (all bits set to 1).

![](https://res.cloudinary.com/zubayr/image/upload/v1655735910/wiki/wtzdd2lbx2pixujmqqx0.png)

**IP Address Classes:**

IP addressing supports three different commercial address classes; Class A, Class B, and Class C.

In a class A address, the first octet is the network portion, so the class A address of, 10.1.25.1, has a major network address of 10. Octets 2, 3, and 4 (the next 24 bits) are for the hosts. Class A addresses are used for networks that have more than 65,536 hosts (actually, up to 16,581,375 hosts!).

In a class B address, the first two octets are the network portion, so the class B address of, 172.16.122.204, has a major network address of 172.16. Octets 3 and 4 (the next 16 bits) are for the hosts. Class B addresses are used for networks that have between 256 and 65,536 hosts.

In a class C address, the first three octets are the network portion. The class C address of, 193.18.9.45, has a major network address of 193.18.9. Octet 4 (the last 8 bits) is for hosts. Class C addresses are used for networks with less than 254 hosts.

Via — [Basic IP Addressing and Troubleshooting Guide](http://penta2.ufrgs.br/trouble/ts_ip.htm)

---

## Structure of an IP Address

IP Addresses are written in decimal dotted notation.

`192.168.0.1`

Each part of the IP address is a binary octet.

![](https://res.cloudinary.com/zubayr/image/upload/v1656322930/wiki/gruxal4tsobjfhxdkw00.png)

This is important for [[devlog.subnet]]ting.

## Networks and Hosts

Every IP address has a Network ID and a Host ID

Network ID will remain same for every computer on this network.

Host ID will be unique for every computer on this network.

Subnet masks tells us which part is the Network ID and which is Host ID.

![](https://res.cloudinary.com/zubayr/image/upload/v1656323194/wiki/glrh3blvpzga1d4itquu.png)

When we have `255` (all the 8 bits are 1) is where we essentially have a bit that is a `1`. It represents a Network ID.

Last octet in the orange box is the Host ID, every bit in a subnet mask that is a `0` means there are values that can be assigned to host.

![](https://res.cloudinary.com/zubayr/image/upload/v1656323419/wiki/vsvc0stwao9rrbyuib2e.png)

Lets say you’ve a network with several computers, they each will have different host IDs but same network ID.

## Classes of IPv4 Address

![](https://res.cloudinary.com/zubayr/image/upload/v1656323639/wiki/gnfsubay6bnavdg3spkv.png)

**Private IP address range**

Reserved for private/internal use in an organization according to IETF RFC-1918.

![](https://res.cloudinary.com/zubayr/image/upload/v1656323694/wiki/piorhozhal6mgghcyo24.png)

![[devlog.cidr]]

---

## How is an [[devlog.ip address]] assigned?

Apparently using some [[devlog.dhcp]] magic, [[devlog.router]] assigns an [[devlog.IP address]] to any computer/thing that connects to it.

Why is that most of the IP address start from `192.168.1.204` when they each of the octet can be anywhere between 0.255?

It is because of subnet mask. If your subnet mask is `255.255.255.0` it'll match one on one with `192.168.1.204` the first three of the IP address will always remain the same IN YOUR NETWORK.

The last octet or the number in subnet if it is 0 - it basically tells us that the last octet can be whatever you want (as long as it is between 0-255)

The first three octets are NETWORK ID - the last octet is HOST ID

HOST ID will change based on the device connected.

When a networks wants to talk to something that is not on the same network - it takes the help of Default Gateway aka Router.

You cannot use `192.168.1.0` it is the NETWORK ADDRESS.

OR

You cannot use `192.168.1.255` it is the BROADCAST ADDRESS. When you send something to last IP Address in a network, it tells it to everyone in the network.

OR

You cannot use `192.168.1.1` because it's the Router's address(Default Gateway)

In total you can `253` addresses.

---

Your IP Address is the size of 32 bits, 4 bytes(8 bits = 1 byte). Hence four binary octets.

Powers of 2 chart is utilized to convert binary to decimal.

8 Bit Octet Chart

![](https://res.cloudinary.com/zubayr/image/upload/v1656331702/wiki/npacf0svnom9sisa86sd.png)

## Resources

- [what is an IP Address? // You SUCK at Subnetting // EP 1 - YouTube](https://www.youtube.com/watch?v=5WfiTHiU4x8)
