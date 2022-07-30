
## Creating Admin Users

- A user has to be added to the [[devlog.sudo]] [[devlog.group]] or the `sudoer file` inorder for them to use `sudo` privileges, [[usermod]] can be used to achieve this.
  - `sudo usermod -aG sudo james`
