
- Areas: [[devlog.linux]]

---

`gawk` or `awk` is a very powerful text processing tool.

### Example

gawk can parse the results of the "uptime" command (uptime provides length of time a Linux server has been running and some other system load data).

Getting the eigth field from the [[devlog.stdout]] of [[uptime]]

`uptime|sed 's/min,\ //' |sed 's/,//g'|awk '{print $8}'`
