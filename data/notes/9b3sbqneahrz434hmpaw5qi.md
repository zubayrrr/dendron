
- Areas: [[devlog.linux]]

---

The SIGTERM [[devlog.signal]]is sent to a [[devlog.process]] to request its termination. Unlike the [[SIGKILL]] signal, it can be caught and interpreted or ignored by the process. This allows the process to perform nice termination releasing resources and saving state if appropriate. [[SIGINT]] is nearly identical to SIGTERM.

> —via [POSIX signals](https://dsa.cs.tsinghua.edu.cn/oj/static/unix_signal.html)

- The process may stop immediately, it can stop after some day (after cleaning up resources etc) or the process may run indefinitely (ignore), the process decides what it wants to do.
- It is also called as a `soft kill`
- Processes that ignore SIGTERM will have to be terminated using [[SIGKILL]]
