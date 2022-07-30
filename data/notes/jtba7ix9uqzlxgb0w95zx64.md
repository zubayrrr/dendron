
- Areas: [[devlog.linux]]
- Related: [[devlog.lsusb]]

---

**lspci** command is a utility on linux systems used to find out information about the PCI busses and devices connected to the PCI subsystem. You can understand the meaning of the command by considering the word **lspci** in two parts.  The first part ls, is the standard utility used on linux for listing information about the files in the filesystem.  Pci is the second part of the command, so you can see naturally the command **lspci** will list information about PCI subsystem the same way that **ls** will list information about the file system.

## Examples

```
lspci -vmm
```

```
lspci | grep -i wireless
lspci | grep -i vga
```