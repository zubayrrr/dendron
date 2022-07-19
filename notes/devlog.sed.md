---
id: 0dlw6puljva6zl22z1uai4x
title: sed
desc: ''
updated: 1652815757462
created: 20211123201031068
---

- `topics:` [[devlog.linux]]
- `resources:` [[The Grymoire's tutorial on SED]]

---

`sed` command is used for string replacement

### Example

If we want to eliminate the "," in "Kutuzov," and redirect the output to a new-file

`sed 's/Kutuzov,/Kutuzov/' war-and-peace.txt > new-file`
