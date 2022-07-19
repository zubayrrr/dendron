---
id: odobz2lkl658ukcl7h241iu
title: SIGKILL
desc: ''
updated: 1653305505908
created: 20211028135238396
---

- Areas: [[devlog.linux]]

---

The SIGKILL [[devlog.signal]]is sent to a [[devlog.process]] to cause it to terminate immediately ([[devlog.kill]]). In contrast to [[SIGTERM]] and [[SIGINT]], this signal cannot be caught or ignored, and the receiving process cannot perform any clean-up upon receiving this signal.

> —via [POSIX signals](https://dsa.cs.tsinghua.edu.cn/oj/static/unix_signal.html)

- Also known as `hard kill`
