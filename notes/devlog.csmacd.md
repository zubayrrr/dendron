---
id: z130icy9h0z0gwz9szs6ngb
title: CSMA/CD
desc: ''
updated: 1653318515616
created: 20211013080634676
caption: Carrier Sense Multiple Access/Collision Detect
---

- Areas: [[areas.networking]]

---

- [[devlog.Ethernet]] devices transmit based on a principle called Carrier Sense Multiple Access/Collision Detect or CSMA/CD
- Carrier Sense
  - Listen to the wire, verify it is not busy
- Multiple Access
  - All devices have access at any time
- Collision Detect
  - If two deviecs transmit at the same time, a collision occurs
  - Back off, wait a random time and try again
