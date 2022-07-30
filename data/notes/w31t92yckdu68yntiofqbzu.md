
- Areas: [[devlog.linux]]

---

`pstree` displays hierarchical tree structure of all running [[devlog.process]]es, similar to [[devlog.ps]] and [[psgrep]]

Use `pstree | less`

It merges identitcal branches by putting them between square brackets and prefixing them with an integer that represents the number of branches. To disbale merging of identical branches use `-c` option.

The threads of a process are found under the parent process and are shown in curly braces.
