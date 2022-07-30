
- Areas: [[devlog.linux]]

---

When you’re typing a command in the Linux terminal, you’re generally calling a program to do a certain job, for example, [[devlog.ls]], [[devlog.cp]], [[devlog.mv]], [[devlog.rm]], [[devlog.cd]], [[devlog.rm]], [[devlog.mkdir]], etc. All these programs are located somewhere in the file system, right? How does [[devlog.bash]] know where these programs are?

Here come the environment variables into play, especially the PATH variable. This variable is responsible for telling bash where to look for those programs.

PATH is an [[devlog.environment variable]] that keeps track of certain directories. By default, the PATH variable contains the following locations.

- `/usr/bin`
- `/usr/sbin`
- `/usr/local/bin`
- `/usr/local/sbin`
- `/bin`
- `/sbin`
- `/snap/bin` (if Snap is installed)

To see what directories are currently registered under PATH, run the following command.

`echo $PATH`

Here, the $ sign is to denote a variable. The echo command prints the value of the PATH variable.

The PATH variable stores where executables may be found. Whenever any command is run, the shell looks up the PATH directories for the target executable file and runs it.

> — via [How Does PATH Work in Bash](https://linuxhint.com/path_in_bash/)

## Add a new path to the $PATH [[env|devlog.environment variable]] variable

- Open your `~/.zshrc` or `~/.bashrc`
- export PATH=$PATH:/path-to-dir
- Save and reload shell or (`source ~/.zshrc`)
