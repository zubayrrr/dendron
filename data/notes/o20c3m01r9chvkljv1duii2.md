
- Areas: [[devlog.linux]]

---

`groupdel` command is used to delete an existing [[devlog.group]]

Syntax:

`sudo groupdel groupName`

- On successful deletion it doesn't print any output
- It is not possible to delete the primary group of an existing user without first removing the user with [[userdel]]
