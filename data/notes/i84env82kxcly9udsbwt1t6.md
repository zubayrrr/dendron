
- Areas: [[devlog.linux]]

---

`fdisk` is a menu-driven command-line utility that allows you to create and manipulate partition tables on a hard disk.

## Examples

To list the `/dev/sda` partition table and partitions you would run:

```
fdisk -l /dev/sda
```

When no device is given as an argument, `fdisk` will print partition tables of all devices listed in the `/proc/partitions` file:

```
fdisk -l
```

> via — [Fdisk Command in Linux (Create Disk Partitions) | Linuxize](https://linuxize.com/post/fdisk-command-in-linux/)
