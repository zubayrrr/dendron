---
id: ungvanr0fogsuwsbfof5c4x
title: pkill
desc: ''
updated: 1653305490654
created: 20211028140114464
---

- Areas: [[devlog.linux]]

---

`pkill` is used to send [[devlog.signal]] to the [[devlog.process]]es of a running program based on given criteria. The processes can be specified by their full or partial names(unlike [[devlog.killall]]), a user running the process, or other attributes.

`pkill` is basically a wrapper around the [[devlog.pgrep]] program that only prints a list of matching processes.

### Example

- `pkill processName` or `pkill partialProcessNa`
