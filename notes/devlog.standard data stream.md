---
id: a0fbh28d1rhy2pb0i9hlylg
title: Standard Data Stream
desc: ''
updated: 1653437393526
created: 20211011131704576
---

- `topic`: [[devlog.linux]]

---

- Each command is a computer program that takes [[devlog.Redirecting stdin & stderr]], process it and gives [[Redirecting standard output|devlog.stdout]].
- Every Linux command or program we run has three data streams connected to it:
  - [[devlog.Redirecting stdin & stderr]] - Standard Input, denoted with `0`
  - [[devlog.stdout]] - Standard Output, denoted with `1`
  - [[devlog.stderr]] - Standard Error, denoted with `2`
- Standard Data Stream

![](https://raw.githubusercontent.com/zubayrrr/twiki/main/bin/image.1upbcz4kmqj.png)

- By default the [[devlog.stdout]] of a command comes out to the terminal via the Output Data Stream, but we can redirect this [[devlog.stdout]].
- Stderr is one of the Outputs of the command Inputted that is not part of the Stdout and is logged separately.
- Stdin is connected to the keyboard to take in a command from the user. Stdin is also a Data Stream, hence it can also be redirected.
- We can pass Stdout of one command to Stdin of another command. This is called Piping. Chaining of this process is called Pipeline.
- Command line argument are the options passed following the command.  
  Example: `cal 12 2021`, where `12` and `2021` are the arguments. Command line argument only associate with the command or the option they're dealing with.
- The difference between command line arguments and Data Streams is that Data Streams flow, they can be redirected and piped together but command line arguments are mostly static.
- Not all commands accept Stdin, e.g: `echo`.
