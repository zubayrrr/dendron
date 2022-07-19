---
id: qfc3k99hj61yzdpez1zbfg4
title: File Attributes
desc: ''
updated: 1653683833093
created: 20211027181819556
---

- Areas: [[devlog.linux]]

---

### File Attributes

- A part from permissions Linux also has advance access control features such as [[devlog.ACL]]s and attributes.
- The attributes define the properties of the files, they depend on the underlying file system such as [[devlog.ext4]] where the attribute data must be stored along with other control structures.
- Each file attribute can have one of the two states: `set` or `clear`
- Attributes is separate from other metadata such as file system permissions, owners, groups, timestamps and so on.
- [[devlog.ls]] doesn't display the file attributes, use [[devlog.lsattr]] for that and to change attributes use [[devlog.chattr]]
