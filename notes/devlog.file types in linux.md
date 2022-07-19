---
id: n4mbtl0ty1ak7bjr1vwwtva
title: File Types in Linux
desc: ''
updated: 1653437909465
created: 20211022064408744
caption: 'File Types in Linux (ls -F, file)'
---

- Areas: [[devlog.linux]]

---

- The file type is not given by the filename extension
- File extensions don't really matter in Linux, they're only useful for the GUIs to recognize what type of file it is.
- The terminal looks at the file's header to determine what kind of file we're dealing with.
- You can use: `file path-to-file`
- `ls -F` will list out contents, sorted by file type
- You can also use: `ls -l path-to-file` to check what kind of file it is, whether it is a regular file or a directory to [[devlog.symlink]] etc.
- `file path/*` is another way
