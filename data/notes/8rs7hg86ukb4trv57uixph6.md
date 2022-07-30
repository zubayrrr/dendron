
- Areas: [[devlog.linux]]

---

> if /etc/resolv.conf is a symbolic link, you won't be able to write it. If you want to overwrite the content in the file, remove the file and then create a new fi

1. Remove symbolic link
   `sudo rm /etc/resolv.conf`
2. Write to new file. E.g.
   `sudo echo "nameserver 8.8.8.8" > /etc/resolv.conf`

— via [resolvconf - /etc/resolv.conf" E166: Can't open linked file for writing - Ask Ubuntu](https://askubuntu.com/questions/1071656/etc-resolv-conf-e166-cant-open-linked-file-for-writing)
