
- Areas: [[devlog.linux]]

---

- It displays the [[RUID and EUID]], the user that initially logged in(the current shell).
- `who` parses and displays the contents of the file `/var/run/utmp`, that logs the current users on the system.
- `/var/log/wtmp` - its kinda like history for the `/var/run/utmp` file, it maintains the logs for all the logged in users and logged out users (in the past)
- `who -H` -H Prints a line of column headings.
- `who -aH` a for –all
- `w` command provides list of users that are logged in, what current processes are they running
  - `load average` value should be below `1` or else theres a problem
  - [[uptime]] command also provides the same info
