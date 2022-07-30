
- Areas: [[devlog.linux]]

---

`ps` stands for [[devlog.process]] status, displays processes running in the current terminal.

Basic information displayed consists of 4 columns PID, TTY, TIME, CMD

- [[devlog.PID]]
- [[devlog.tty]] represents the name of the controlling terminal for the [[devlog.process]]
  - If you see `?` in the TTY column, it indicates the process has no terminal attached to it, probably a system service, or a [[devlog.daemon]].
- TIME represents the cumulative CPU time of the process shown in minutes and second
- CMD is the name of the command that was used to start the process
- PPID - ID of the parent process
- STIME time whe the process was started

### Options

- `ps -e` for all processes running
- `ps -f` full status information
- `ps -ef` all process with full status information
- `ps -ef | wc -l`
- `ps aux` or `ps -aux`
- `ps aux --sort=%mem | less` sort by MEM usage, in ascending order, add `-` before `%mem%` for descending order
- `ps -f -u userName` for user specific processes
- `ps -ef | grep sshd` filter with [[devlog.grep]]
  - You might get 2 results even though only one processes is truly running, but `grep` selects itself since a process was created when you tried to filter using `grep`
- See also: [[devlog.pgrep]], [[devlog.pstree]]

---

- %CPU - CPU utilization in percentage
- %MEM - Memory utilization of a process, ratio of the processes resident set size to the physical memory of the machine
- VSZ - virtual memory size, includes all the memory the process can access including the memory that is swapped out, memory that is allocated but not used, memory from the shared library
- RSS - physical memory the process is using indicates how much memory is allocated to the process, doesn't include the memory swapped out, includes memory from shared library as long they're actually in memory, it does include stack and heap memory.
- STAT - state of the process using code
  - S for sleeping
  - R for running
  - T for stopped
  - Z for zombie
  - I for idle kernel thread
  - \< means high priority
  - N means low priority
- A CPU core can run a single process at a specific moment, if there are 4 cores on a CPU, then no more than 4 processes can run simultaneously, it appears that the OS is performing jobs simultaneously but in reality it is performing one process per core at a time and just switches between all of its ongoing processes, the Linux kernel will execute some instructions from process A and then will set aside process A and executes instructions from process B. This process is called [[devlog.process scheduler]].
