---
id: maq3lm0jfcnd30vhbxkdz6e
title: Give execution permissions
desc: ''
updated: 1652815757392
created: 20211124212945336
tags:
  - tidbits
---

- Areas: [[devlog.linux]]

---

To give yourself execute permission for the file containing the script use the command:

`chmod u+rwx filename.py`

To give other users permission to read and execute but not alter the shell script use:

`chmod go+rx filename.py`
