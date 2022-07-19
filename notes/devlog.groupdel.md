---
id: o20c3m01r9chvkljv1duii2
title: groupdel
desc: ''
updated: 1653683844839
created: 20211026114228340
---

- Areas: [[devlog.linux]]

---

`groupdel` command is used to delete an existing [[devlog.group]]

Syntax:

`sudo groupdel groupName`

- On successful deletion it doesn't print any output
- It is not possible to delete the primary group of an existing user without first removing the user with [[userdel]]
