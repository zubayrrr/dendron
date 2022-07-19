---
id: bq0gblqc282v024og4l0v5c
title: Data Mart
desc: ''
updated: 1653318643707
created: 20211130161918584
---

- Areas: [[devlog.Data Engineering]]

---

Dependent and Independent(of [[devlog.data warehouse]]) data marts.

### Dependent

- Sources from Data Warehouse
- (Mostly) uniform data across marts
- Architecturally straightforward
- Many sources
- ETL from sources
- Probably large data volumes
- Dimensionally organized data

### Independent

- Sourced directly from applications and systems
- Little or no uniformity across marts
- "Spaghetti" architecture
- One or more sources
- ETL from sources
- Possibly large data volumes
- Dimensionally organized data
