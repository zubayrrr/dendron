---
id: pdd1ljoj7m3l5k35ixyh4ax
title: lsattr
desc: ''
updated: 1653437835252
created: 20211027181214604
---

- Areas: [[devlog.linux]]

---

`lsattr` is used to display the file attributes for the subdirectories of the current directory.

`-` indicates attribute is cleared and alphabets represent different attributes such as:

- The `e` attribute indicates that the file is using extents for mapping the blocks on disk. It may not be removed using [[devlog.chattr]].
- The `I` attribute is used by the htree code to indicate that a directory is being indexed using hashed trees. It may not be set or reset using [[devlog.chattr]], although it can be displayed by `lsattr`.

`lsattr -R dirName` to list attributes recursively(of the subdirectories)

For more: man [[devlog.chattr]]
