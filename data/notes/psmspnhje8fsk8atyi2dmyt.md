
- Areas: [[devlog.linux]]

---

**acpi** command is used to display the battery status and other ACPI information. It displays the information from the /[[devlog.proc]] or the /[[sys]] filesystem, such as battery status or thermal information.

## Examples

**-b | –battery** : It displays the battery information.

```
acpi -bi
```

**-V | –everything** : It is used to show every device, overrides above options.

```
acpi -V
```

**-p | –proc** : It uses the old /proc interface, default is the new /sys one.
