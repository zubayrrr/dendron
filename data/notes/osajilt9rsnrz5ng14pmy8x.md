
- Areas: [[devlog.linux]],[[areas.networking]]

---

`ifconfig` (interface configuration) command is used to configure the kernel-resident network interfaces. It is used at the boot time to set up the interfaces as necessary. After that, it is usually used when needed during debugging or when you need system tuning. Also, this command is used to assign the IP address and netmask to an interface or to enable or disable a given interface.

- `ifconfig` cannot display [[devlog.default gateway]] nor the [[devlog.dns]] but the [[devlog.route]] command from `net-tools` can do it.
- Newer alternative to `ifconfig` is [[devlog.ip]]

### Examples

- To display a list of network interfaces and the associated [[devlog.ip address]]:
  - `ifconfig -a` -a flag makes it display info about all interfaces but enabled and disabled. If you omit `-a` flag it'll display info only about enabled interfaces.
- Also displays how many packets and bytes were recieved and transmitted on each inteface.
- To get info about specific network inteface:
  - `ifconfig enp0s3`
- To turn an interface off/on:
  - `ifconfig enp0s3 down`
  - The interface will be down(disabled) and will not be previewed when ran `ifconfig`, use `ifconfig -a` to display it.
- To assign a new [[devlog.ip address]];
  - `ifconfig enp0s3 192.168.0.111/24 up` `/24` is the [[devlog.netmask]]
- To change the [[devlog.MAC]] Address:
  - Disable the interface: `ifconfig enp0s3 down`
  - `ifconfig enp0s3 hw ether 08:00:27:51:05:09`
  - Bring the interface back up: `ifconfig enp0s3 up`
