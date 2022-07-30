
- Areas: [[devlog.linux]]

---

`ip` command in Linux is present in the net-tools which is used for performing several network administration tasks. IP stands for Internet Protocol. This command is used to show or manipulate routing, devices, and tunnels. It is similar to [[ifconfig]] command but it is much more powerful with more functions and facilities attached to it. ifconfig is one of the deprecated commands in the net-tools of Linux that has not been maintained for many years. `ip` command is used to perform several tasks like assigning an address to a network interface or configuring network interface parameters.

It can perform several other tasks like configuring and modifying the default and static routing, setting up tunnel over IP, listing IP addresses and property information, modifying the status of the interface, assigning, deleting and setting up IP addresses and routes.

### Examples

- To display a list of network interfaces and the associated [[devlog.ip address]]:
  - `ip address show` "address" is the object and "show" is the command executed on the object, `ip addr show` `ip a show` are same. You can also omit the `show` command as it is the default.
- If you want to display only [[devlog.IPv4]] or [[devlog.IPv6]] addresses:
  - `ip -4 address` and `ip -6 address`
- To get info about specific network inteface:
  - `ip addr show dev enp0s3` or `ip a s dev enp0s3`
- To get [[devlog.default gateway]]:
  - `ip route show`
- To turn an interface off/on:
  - `ip link set enp0s3 down`
  - The interface will be down(disabled) and to display it:
    - `ip link dev enp0s3`
  - `ip link set enp0s3 up` to enable it
- To assign a new [[devlog.ip address]]:
  - Remove existing IP Address from the interface: `ip address del 192.168.0.111/24 dev enp0s3`
  - Add the needed IP Address: `ip address add 192.168.0.222/24 dev enp0s3`
- To change default gateway;
  - Removing existing default gateway: `ip route del default`
  - Add a new default gateway: `ip route add default via 192.168.0.2`
- To change the [[devlog.MAC]] Address:
  - `ip link set dev enp0s3 address 08:00:27:51:05:01`
