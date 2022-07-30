
- Areas: [[devlog.linux]]

---

A signal is an asychnronous notification sent to a process, that determines how the process should behave when the signal is delivered.

A [[devlog.process]] can decide to ignore some of the signals, like [[SIGTERM]] is an 'invitation' for termination.

Nonpriviledged users can send signals only to their own processes, while root can send signals to users.

There are two types of signals:

- Maskable: signals which can be changed or ignored by the user (e.g., Ctrl+C or [[SIGINT]]).
- Non-Maskable: signals which cannot be changed or ignored by the user. These typically occur when the user is signaled for non-recoverable hardware errors.

### Example

- `pgrep -l gedit` gedit is a process used in this example
  - `14804 gedit` 14804 is the [[devlog.PID]] for gedit
- `kill -2 14804` `-2` from the list of signals that you can get by `kill -l`
- `pidof firefox` [[devlog.pidof]] is another command that you can use to the [[devlog.PID]] of a process (since a process can have subprocesses, firefox can have multiple PIDs)
  - `kill -INT all-processes-IDs` another way to send the interrupt signal is using `-INT`
- `kill -SIGINT $(pidof firefox)` to substitute [[devlog.stdout]] of [[devlog.pidof]]

See also: [[devlog.SIGHUP]
