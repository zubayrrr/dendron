
- Areas: [[devlog.linux]]

---

## The below examples are to display ports open on the current or host system(localhost).

Display all open ports using [[devlog.netstat]]

```
sudo netstat -tupan
```

- `-t` for TCP ports
- `-u` for UDP ports
- `-p` for process ID and the name of the program thats listening
- `-a` all ports both listening and not listening
- `-n` shows numerical address instead of determining symbolic hosts and port names

Under the “Local Address” if it shows `0.0.0.0` as an IP Address, it means the process is listening on all IP Addresses of the host.

## Filtering with [[devlog.grep]]

```
sudo netstat -tupan | grep :22

#or

sudo netstat -tupan | grep sshd
```

## Using [[devlog.ss]]

Display all listening ports

```
ss -tupan
```

## Using [[devlog.lsof]]

Display listening ports using [[devlog.lsof]],

```
sudo lsof -iTCP -sTCP:LISTEN
```

`-iTCP` `-sTCP:LISTEN` shows only the files that opened TCP ports that are listening.

Add `-nP` to display both port and host names in numeric format

```
sudo lsof -iTCP -sTCP:LISTEN -nP
```

Filter by specific port number

```
sudo lsof -iTCP:22 -sTCP:LISTEN -nP
```

---

## To check for ports open on other machines

Scan for open ports on that machine using [[devlog.telnet]] or [[devlog.nmap]]

```
telnet ip_address port
```

You’ll need an active network connection with that machine on which you’re trying to scan for ports.

```
sudo nmap ip_address

# scan for specific port

nmap -p 80 linux.com

# scan version

nmap -p 80 linux.com -sV
```
