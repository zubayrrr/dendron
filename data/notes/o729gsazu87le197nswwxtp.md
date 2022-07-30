
- Areas: [[devlog.linux]]

---

- They're defined for the current shell and are inherited by any child shells or processes.
- They're used to pass information to process that are spawned from the current shell.
- Displayed using `env` or `printenv`
- [[$PATH|devlog.path]] is such an example
- When assigning multiple values to a variable, its common to separate them using a colon `:`
- By convention - env variables are written in uppercase letters.
- Usually they're not used directly; instead they're referenced by individual applications/services.
  - `$HOME` is such an example
- Run `env | less` to list all env variable set on your machine.
- You can also use `printenv` to print variables
  - `printenv SHELL PWD LC_TIME`

## Create a new env variable

- Add a line: `export VARNAME=VARVAL` in your `~/.zshrc`
- To create a system wide variable available for all users; declare the variable in `/etc/profile` or `/etc/bash.bashrc`
- There is also `/etc/environment` in which you can set env variables each on a new line
