
- Areas: [[devlog.linux]]

---

- It is an association between an [[devlog.inode]] structure and a file name in a directory.
- You cannot create a hard link to a directory.
- All hard links have some [[devlog.inode]] structure and [[devlog.inode]] number

### Example

- `ps aux > processes.txt`
  - To create a [[hard link]]: `ln processes.txt p.txt`
  - If we were to change the location of `processes.txt`, `p.txt` will not be effected.
