---
id: q92tfbbhyglmyk3jdtx5vm5
title: TCP⁄IP Model
desc: ''
updated: 1656581236010
created: 20210926141245140
---

- Areas: [[areas.networking]]

---

The [[devlog.OSI Model]] is just a reference/logical model. It was designed to describe the functions of the communication system by dividing the communication procedure into smaller and simpler components. But when we talk about the TCP/IP model, it was designed and developed by Department of Defense (DoD) in 1960s and is based on standard protocols. It stands for Transmission Control Protocol/Internet Protocol. The TCP/IP model is a concise version of the OSI model. It contains four layers, unlike seven layers in the OSI model.

The layers are:

- Process/Application Layer
- Host-to-Host/Transport Layer
- Internet Layer
- Network Access/Link Layer

## Difference between TCP/IP and OSI Model:

| TCP/IP                                                                           | OSI                                                                                                    |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| TCP refers to Transmission Control Protocol.                                     | OSI refers to Open Systems Interconnection.                                                            |
| TCP/IP has 4 layers.                                                             | OSI has 7 layers.                                                                                      |
| TCP/IP is more reliable                                                          | OSI is less reliable                                                                                   |
| TCP/IP does not have very strict boundaries.                                     | OSI has strict boundaries                                                                              |
| TCP/IP follow a horizontal approach.                                             | OSI follows a vertical approach.                                                                       |
| TCP/IP uses both session and presentation layer in the application layer itself. | OSI uses different session and presentation layers.                                                    |
| TCP/IP developed protocols then model.                                           | OSI developed model then protocol.                                                                     |
| Transport layer in TCP/IP does not provide assurance delivery of packets.        | In OSI model, transport layer provides assurance delivery of packets.                                  |
| TCP/IP model network layer only provides connection less services.               | Connection less and connection oriented both services are provided by network layer in OSI model.      |
| Protocols cannot be replaced easily in TCP/IP model.                             | While in OSI model, Protocols are better covered and is easy to replace with the change in technology. |

## Layers

![[devlog.network interface layer - tcpip]]
![[devlog.internet layer - tcpip]]
![[devlog.transport layer - tcpip]]
![[devlog.application layer - tcpip]]

## Data Transfer Over Network

When we're trying to transfer data over network, we've to tell it where its going to go. We use [[devlog.ip address]]es to get to the system but how does the data know which applications are listening on that system? Thats where Ports come into the picture.

- Port numbers can range from 0 to 65,536, you can run services on all of these ports.
- Ports are categorized into "Well-known" & "Reserved Ports".
  - Well-known ports range from 0 to 1024.
    - Examples: [[devlog.FTP]] on Port 21, [[devlog.HTTP]] on Port 80 and so on
- Ephemeral Ports:
  - Short-lived transport port that is automatically selected from predefined range
  - Ports 1025 to 65,536
  - Examples: Running a Web Application locally, such as TiddlyWiki on NodeJs on Port 4000.

### Data Transfer in the real world

![](https://res.cloudinary.com/zubayr/image/upload/v1656578336/wiki/ouwxuee31fco6wjridoh.png)

### IPv4 Packets

IPv4 Packets (Packet Header) contain the following information:

- Source Address
  - IP of sender
- Destination Address
  - IP of receiver
- IP Flags
  - Allows packet fragmentation
- Protocol
  - [[devlog.TCP]] or [[devlog.UDP]]

## Ports and Protocols

![[devlog.ports & protocols]]

## Look-into

- IPv4/IPv6 Packet Header
- TCP/UDP Packet Header

See also: [[devlog.Using nmap to look for open ports]]
