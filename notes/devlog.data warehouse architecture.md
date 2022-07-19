---
id: oppcapyr6oew027thjm2z91
title: Data Warehouse Architecture
desc: ''
updated: 1653318643711
created: 20211130161032384
---

- Areas: [[devlog.Data Engineering]]

---

### Centralized [[devlog.data warehouse]]

- A single data warehousing environment, rather than one made up of multiple components.
- Ideally, it should be your default or "go to" architecture
- Single Database
- Obvious advantage: One stop shopping(of data)
- High cross-org cooperation
- High data governance
- Ripple effects
- Emphasis on "enterprise" (EDW)
  - Relational
  - Specialized Database (DWing appliances)

### Component Based

- Decomposition
- Mix and match technology
- "Bolt together" components
- Overcome org. challenges
- Often inconsistent data
- Difficult to cross-integrate
  - Architected would contain
  - DW + DMs
- Or simply DMs only
- DW Bus all DMs follow "Conformed Dimensions"
- Non-Architected
  - Federated EDW

See also: [Data Mart]([[devlog.data mart]])
