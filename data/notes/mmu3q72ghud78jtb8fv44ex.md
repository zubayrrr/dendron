
OSI stands for Open Systems Interconnection, developed in 1977 by the International Organization for Standardization(ISO).

- ISO 7498 is for the standard, OSI model.
- OSI Model can also be referred to as OSI Stack.

---

OSI model doesn't always accurately describe how networks actually operate (some things can operate at multiple layers of the OSI model), our networks today operate on the [[devlog.tcp⁄ip model]] model but OSI model was the standard to describe how all and any network can possibly operate.

OSI model serves as a reference model:

- To categorize functions of the network into particular layer(s).
- To compare technologies across different manufacturers.
- To understand how to best communicate with that device, how to troubleshoot it etc.

The OSI model has 7 layers:
| Group | # | Layer Name | Key Responsibilities | Data Type Handled | Scope | Common Protocols and Technologies |
|--------------|---|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Lower Layers | 1 | Physical | Encoding and Signaling; Physical Data Transmission; Hardware Specifications; Topology and Design | Bits | Electrical or light signals sent between local devices | (Physical layers of most of the technologies listed for the data link layer) |
| Lower Layers | 2 | Data Link | Logical Link Control; Media Access Control; Data Framing; Addressing; Error Detection and Handling; Defining Requirements of Physical Layer | Frames | Low-level data messages between local devices | IEEE 802.2 LLC, Ethernet Family; Token Ring; FDDI and CDDI; IEEE 802.11 (WLAN, Wi-Fi); HomePNA; HomeRF; ATM; SLIP and PPP |
| Lower Layers | 3 | Network | Logical Addressing; Routing; Datagram Encapsulation; Fragmentation and Reassembly; Error Handling and Diagnostics | Datagrams / Packets | Messages between local or remote devices | IP; IPv6; IP NAT; IPsec; Mobile IP; ICMP; IPX; DLC; PLP; Routing protocols such as RIP and BGP |
| Lower Layers | 4 | Transport | Process-Level Addressing; Multiplexing/Demultiplexing; Connections; Segmentation and Reassembly; Acknowledgments and Retransmissions; Flow Control | Datagrams / Segments / Packets | Communication between software processes | TCP and UDP; SPX; NetBEUI/NBF |
| Upper Layers | 5 | Session | Session Establishment, Management and Termination | Sessions | Sessions between local or remote devices | NetBIOS, Sockets, Named Pipes, RPC |
| Upper Layers | 6 | Presentation | Data Translation; Compression and Encryption | Encoded User **D**ata | Application data representations | SSL; Shells and Redirectors; MIME |
| Upper Layers | 7 | Application | User Application Services | User **D**ata | Application data | DNS; NFS; BOOTP; DHCP; SNMP; RMON; FTP; TFTP; SMTP; POP3; IMAP; NNTP; HTTP; Telnet |

Table via - [The TCP/IP Guide - OSI Reference Model Layer Summary](http://www.tcpipguide.com/free/t_OSIReferenceModelLayerSummary.htm)

The mnemonic we can use to remember is: "**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way\!"

At different layers, data/information is called by different names.

The mnemonic to remember the data types in the OSI model is: "**D**on't **S**ome **P**eople **F**orget **B**irthdays?"

---

![[devlog.physical layer - osi]]
![[devlog.data link layer - osi]]
![[devlog.network layer - osi]]
![[devlog.transport layer - osi]]
![[devlog.session layer - osi]]
![[devlog.presentation layer - osi]]
![[devlog.application layer - osi]]

---

## Lab

Using [[devlog.wireshark]] packet analyzer to pull apart network traffic and see the different layers of the OSI model.

![[devlog.wireshark# Lab]]

## Resources

- [7 Layers of The OSI Model (A Complete Guide)](https://www.softwaretestinghelp.com/osi-model-layers/#1_Layer_1_8211_Physical_layer)
