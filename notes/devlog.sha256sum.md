---
id: 6pfeic1cz5vt0wgm5ctmmsw
title: sha256sum
desc: ''
updated: 1652818329137
created: 20211023105342824
---

- Areas: [[devlog.linux]]

---

The `sha256sum` command displays or checks [[sha256sum]] (256-bit) checksums. With no FILE, or when FILE is - (a dash), it reads the digest from standard input.

- \-b, –binary Read in binary mode.
- \-c, –check Read SHA256 sums from the FILEs and check them.
- –tag Create a BSD-style checksum.
- \-t, –text Read in text mode (default).
- –quiet Don't print OK for each successfully verified file.
- –status Don't output anything, status code shows success.
- –strict Exit non-zero for improperly formatted checksum lines.
- \-w, –warn Warn about improperly formatted checksum lines.

Example:

- `cp /usr/bin/ls .` - copying the [[devlog.ls]] binary to current working dir
  - `sha256sum /usr/bin/ls ./ls` - if the hashes are same, it means both the files are identical
- Modifying the [[devlog.ls]] binary that was previously copied: `echo "a" > ls`
  - check again `sha256sum /usr/bin/ls ./ls` and the hashes return will be different

See also: [[cmp]], [[devlog.diff]]
