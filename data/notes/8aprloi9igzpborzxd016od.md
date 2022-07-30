
- Areas: [[devlog.linux]]
- Related: [[devlog.APT]

---

dpkg is software at the package management base within the free OS Debian and its several derivatives. This software is used for installing, removing, and providing details of **.deb packages**.

Debian comes from Debra Lynn, [[Ian Murdock]]’s spouse; deb+ian = debian

dpkg is a low-level mechanism. A higher level mechanism, i.e., **[[devlog.APT]** is more widely used as compared to the dpkg tool because it can retrieve packages by remote locations and negotiate with typical package relations like dependency resolution.

The database of dpkg is located in the **/var/lib/dpkg** file. This **"status"** file includes the installed software list on our current system. Also, there are no details about repositories within this database.

## Examples

Install a package

`dpkg -i zip_2.31-3_i386.deb`

Install all packages recursively from directory
`dpkg -R /tmp/downloads`

Remove/Delete everything including configuration files
`dpkg -P apache-perl`

List all installed packages, along with package version and short description

```
dpkg -l
dokg -l | less
```

> via — https://www.cyberciti.biz/howto/question/linux/dpkg-cheat-sheet.php

Check all the programs from a package

```
dpkg -L coreutils
```

Find to which package a program belongs

```
which -a ls
dpkg -S /bin/ls
```

List all installed packages

```
sudo dpkg --get-selections
```
