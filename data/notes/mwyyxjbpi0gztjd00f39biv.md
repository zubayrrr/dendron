
- Areas: [[areas.devops]]
- Related: [[devlog.puppet]], [[devlog.chef]]

---

- Ansible is a configuration management system used to configure, automate,monitor, and troubleshoot devices in large networks.
- It is written in [[devlog.python]] and is open source under GPL License.
- There is a control node and many managed nodes (network devices we manage with Ansible). Windows OS is not supported as a control node at this moment (only [[devlog.WSL]]);
- Ansible uses an agentless architecture. No application is installed on the managed nodes and no daemon, process or agent is running;
- Ansible uses for device configuration. Any system that can be configured using [[devlog.SSH]] can also be configured using Ansible;
- When managing Windows it users native PowerShell remote support instead of SSH;
- It is also known as an orchestration engine, used in large networks with many devices that need to be configured, maintained and troubleshooted in an automated way.
- Ansible uses Modules which are scripts or units of work that do the actual job.
- Theres no process that runs continuously on neither the controlling machine or the managed machine(s)
- The controlling node doesn't have be a privileged user, it can simply ssh into the managed node.

## Ansible Components

- Inventory is a list of managed nodes. An inventory file is also sometimes called a "host file". The inventory can specify information such as IP address, hostname or domain-name for each managed node. Default location: `/etc/ansible/hosts` (or use the `-i` flag to use a custom file). An inventory file can be formatted as an INI or YAML file.
- Modules are the units of code ansible executes. Each module has a particular use, from administering users on a specific type of database to managing VLAN interfaces on a specific type of network device or to installing, configuring and starting a specific server like for example Apache2 on a Linux distribution.
- Tasks are units of action in Ansible. You can execute a single task once with an Ad-Hoc command or multiple tasks in a playbook.
- Playbooks are ordered lists of tasks. We can run those tasks in that order repeatedly.
- Playbooks are written in YAML and are easy to read, write, share and understand.

## Inventory File

Within the inventory file, we can organize our server into different groups, this will help us keep the host in order and permit us to use group variables. A host can be part of multiple groups.

```ini
[servers]

vps1 ansible_host=207.154.254.221
vps2 ansible_host=167.122.186.63
vps3 ansible_host=139.59.155.232
```

- `ansible_host` is a predefined variable that holds the value of the managed hosts.
- To parse the inventory file and list all the hosts defined in the inventory file:
  - `ansible -i ./hosts --list-hosts all`
- To check if ansible is able to communicate with the hosts
  - `ansible -i ./hosts vps1 -m ping -u userName -k` (to test for the whole group, use the group name such as: `servers` instead of `vps1`)
  - `-m` is for "module" in this case we're using the `ping` module - it checks the ssh authentication for the each node.
  - `-u` defines the username that will connect to the remote hosts.
  - `-k` to prompt for password.
    - `sshpass` module must be installed on the controlling machine
    - Edit `/etc/ansible/ansible.cfg` to uncomment `host_key_checking = False`
    - If you want to test ssh communication for all the hosts in the inventory file, use option "all" instead of a group or a specific host
- To get setup info
  - `ansible -i ./hosts servers -m setup -u student -k`
- To setup ssh authentication
- You can omit the `-u` and `-k` option you can declare them in the inventory file.

```ini
[servers]

vps1 ansible_host=207.154.254.221
vps2 ansible_host=167.122.186.63
vps3 ansible_host=139.59.155.232

[servers:vars]
ansible_user=student
ansible_ssh_pass=clearPW123
ansible_become_pass=sudoPWroot
ansible_port=22
```

- You should use a vault to securely pass your credentials instead of hardcoding it.
- To overwrite variables for a specific host, such as using a different user to authenticate

```ini
[servers]

vps1 ansible_host=207.154.254.221 ansible_user=student2
vps2 ansible_host=167.122.186.63
vps3 ansible_host=139.59.155.232

[servers:vars]
ansible_user=student
ansible_ssh_pass=clearPW123
ansible_port=22
```

## Ad-Hoc Commands VS Playbooks

- Ad-Hoc commands can be used to do quick and simple things like checking the logs, checking if a process is running, or installing a package on a list of servers.
- Playbooks are used for big deployments, orchestration or system configuration. We use the `ansible` command to run an Ad-Hoc command and the `ansible-playbook` command to run a playbook.
- `ansible` is used to run Ad-Hoc commands. These commands are quick and easy but are not reusable. You don't save them for later, they demonstrate the simplicity and power of ansible.
  - Some examples are rebooting servers, updating servers, copy files, manage package, users.
- Playbooks are scripts written in [[devlog.YAML]] and are composed of one or more play in an ordered list and each play executes one or more tasks using ansible modules.
- Both Ad-Hoc commands and Playbooks use modules to perform different tasks. Modules are units of code that do the actual work in Ansible.

## Ad-Hoc Commands

### The Shell Module

The general syntax of running an Ad-Hoc command is:

`ansible -i [path-to-invetory-file] [group-to-connect-to] -m [module] -a [module-arguments] -u [user] -k`
`ansible -i ./hosts servers -m shell -a "df -h" -u user1 -k`

By default ansible uses multi-threading, with 5 threads as the default. If you've more than 5 hosts, you can increase the threads using the `-f` option.

Example:

`ansible -i ./hosts servers -m shell -a "ip address show dev eth0 | grep ether | cut -d ' ' -f6 | grep -v ">>"`

### The Script Module

- This module can be used to run a local shell script on a remote system.
- The classical method of doing something like this would be to first copy the script to the remote machines using [[devlog.scp]], connect to it and run the script.
- Using the script module, the controlling machine's script is run on each host(in fact the local script is transferred to remote node and then executed).
- This module is also supported for Windows targets.

Example:

`ansible -i ./hosts servers -m scripts -a "./backsup.sh" --become -K`

`--become` to run the script as [[devlog.root]] on the host machines
`-K` to prompt for [[devlog.sudo]] password (you can omit this if you've already declared it inside the inventory file)

### The APT Module

- This module automates software installation, removal and update.
- It allows you to manage packages on Ubuntu(Debian) Distributions.
- If you use other distros, use the corresponding package managers.

Example:

Install a specific software on all the hosts.

The `state` option indicates the desired state of a package.

`ansible -i ./hosts severs -m apt -a "name=nmap state=present update_cache=true" -u [user] -k --become -K`

- Remove a specific software on all the hosts.

`ansible -i ./hosts severs -m apt -a "name=nmap state=absent purge=yes update_cache=true" --become`

- To perform a full system update on all the hosts.

`ansible -i ./hosts servers -m apt "upgrade=full" --become`

- To remove dependencies that are no longer required.

`ansible -i ./hosts servers -m apt "autoremove=yes autoclean=yes" --become`

### The Service Module

This module is used to control the services running on the host nodes.

Examples:

- To start a service on all the hosts.

`ansible -i ./hosts servers -m service -a "name=ngnix state=started" --become`

- To reload a service on all the hosts.

`ansible -i ./hosts servers -m service -a "name=ngnix state=restarted" --become`

- To stop a service on all the hosts.

`ansible -i ./hosts servers -m service -a "name=ngnix state=stopped" --become`

- Set a service to start on boot on all the hosts.

`ansible -i ./hosts servers -m service -a "name=ngnix enabled=yes" --become`

### The User & Group Module

- This module is used to manage groups, user accounts and user attributes.

Examples:

- Creating a new group on all remote hosts

`ansible -i ./hosts servers -m group -a "name=developers state=present" --become`

- Removing an existing group from all remote hosts

`ansible -i ./hosts servers -m group -a "name=developers state=absent" --become`

- Adding a new user to all remote hosts
  - You can give comma separated values if you want to add the user to multiple groups
  - The last three options are optional
    `ansible -i ./hosts servers -m user -a "name=johndoe state=present groups=developers create_home=yes comment=\"new user\" shell=/bin/bash generate_ssh_key=yes ssh_key_bits=2048" --become`

## Resources

- [geerlingguy/ansible-for-devops: Ansible for DevOps examples.](https://github.com/geerlingguy/ansible-for-devops)
