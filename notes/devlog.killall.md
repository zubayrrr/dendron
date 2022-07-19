---
id: 1ml1vdkyp8rhohc14leduv0
title: killall
desc: ''
updated: 1653318304099
created: 20211028135602440
---

- Areas: [[devlog.linux]]

---

`killall` is used for killing any or all running process on the system based on a given name. This command will terminate the processes forcibly when a specified name matches. If no [[devlog.signal]]name is specified, [[SIGTERM]] is sent.

It takes name of the process, instead of the [[devlog.PID]].

`killall` doesn't accept partial names, to [[devlog.kill]] using partial names, use [[devlog.pkill]]

### Example

- `killall -15 processName`
