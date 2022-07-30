
- Areas: [[devlog.linux]]

---

`kill` is used to terminate a process.

It sends a [[devlog.signal]]to a [[devlog.process]] or a group of processes causing them to act according to the signal.

When the signal is not specified its default is: 15 or [[SIGTERM]]

`kill -l` to list all available signals: [[devlog.SIGHUP],[[SIGKILL]] etc

Besides `kill`, [[devlog.killall]] and [[devlog.pkill]] can also be used to send signals to processes.
