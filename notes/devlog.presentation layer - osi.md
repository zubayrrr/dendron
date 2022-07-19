---
id: 2nnii3yd2gbdvevk0zxu9m1
title: Presentation Layer - OSI
desc: ""
updated: 1656561830210
created: 20211010130635116
---

# Layer 6 – Presentation Layer

- Responsible for formatting the data exchanged and securing the data with proper encryption.
- Functions:
  - Data formatting
  - Encryption

As suggested by the name itself, the presentation layer will present the data to its end users in the form in which it can easily be understood. Hence, this layer takes care of the syntax, as the mode of communication used by the sender and receiver may be different.

### Data Formatting

- Formats data for proper compatibility between devices.
  - ASCII
  - GIF
  - JPG
- Ensures data is readable by receiving system
- Provides proper data structures
- Negotiates data transfer syntax for the [[devlog.Application Layer - OSI]]

---

### Encryption

- Used to scramble the data in transit to keep it secure for prying eyes.
- Provides confidentiality of data.
- E.g.
  - [[devlog.TLS]] to secure data between your PC and website.

---

### Layer 6 Examples

**Presentation styles** - taking ones and zeros and present them in the human readable format?

- [[devlog.HTML]], [[devlog.XML]], [[devlog.PHP]], [[devlog.JavaScript]]
- [[devlog.ASCII]], [[devlog.EBCDIC]], [[devlog.UNICODE]]
- GIF, JPG, TIF, SVG, PNG
- MPG, MOV

**Encryption styles** - how do we secure data in a jumbled format?

- [[devlog.TLS]], [[devlog.SSL]]
