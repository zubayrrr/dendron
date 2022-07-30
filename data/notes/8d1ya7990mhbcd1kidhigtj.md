
- Areas: [[devlog.linux]]

---

Show / manipulate wireless devices and their configuration

`iw` is a newer command which is more powerful than `iwconfig`, but different syntax that [[ifconfig]]/[[iwconfig]]. (In fact there is an analogous command called [[devlog.ip]] which is meant to replace ifconfig for wired interfaces

## Examples

```
iw list | less
```

To view the available WiFi hardware/interfaces:

```
$ iw dev
```

You can check the link details:

```
$ iw dev wlan0 link
```

To disconnect from an AP run:

```
$ sudo iw dev wlan0 disconnect
```

> — via [Using iw to Manage Wireless LAN in Linux](http://ict.siit.tu.ac.th/help/iw)
