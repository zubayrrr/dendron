---
id: l6mm6spmjonb3zpaca8nldg
title: Application Layer - OSI
desc: ""
updated: 1656562041903
created: 20211010131443024
---

# Layer 7 – Application Layer

- Provides application level services (Not MS Word or Notepad)
- Layer where the users communicate with the computer
- Functions:
  - Application services
  - Services advertisement

This layer grants a direct interface and access to the users with the network. The users can directly access the network at this layer. Few Examples of services provided by this layer include e-mail, sharing data files, FTP GUI based software like Netnumen, Filezilla (used for file sharing), telnet network devices etc.

There is vagueness in this layer as is not all user-based information and the software can be planted into this layer.

For Example, any designing software can’t be put directly at this layer while on the other hand when we access any application through a web browser, it can be planted at this layer as a web browser is using HTTP (hypertext transfer protocol) which is an application layer protocol.

### Application Services

Application level services in the [[devlog.OSI Model]] context mean stuff like file transfer, the user communicates with the computer and the computer passes on the user request to the network.

- Application services unite communicating components from more than one network application.
- E.g:
  - File transfers and file sharing
  - E-mail
  - Remote access
  - Network management activities
  - [[devlog.Client]]/[[devlog.Server]] Processes

---

### Service Advertisement

- Some applications send out announcements
- States the services they offer on the network
- Some centrally register with the Active Directory server instead
- E.g:
  - Printer
  - File Servers

---

### Layer 7 Examples

- E-mail ([[devlog.POP3]], [[devlog.IMAP]], [[devlog.smtp]])
- Web Browsing ([[devlog.HTTP]], [[devlog.HTTPS]])
- Domain Name Service ([[devlog.DNS]])
- File Transfer Protocols ([[devlog.FTP]], [[devlog.FTPS]])
- Remote Access ([[devlog.telnet (protocol)]]), [[devlog.ssh]])
- Simple Network Management Protocol ([[devlog.SNMP]])
