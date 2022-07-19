---
id: s4ptsgijppmceg9hcdsot7i
title: xargs
desc: ''
updated: 1652947198755
created: 20211012134449204
---

- Areas: [[devlog.linux]]

---

- Picking up here from [[Piping]] and [[tee]]
- The xargs come into play for commands that don't accept any [[devlog.Redirecting stdin & stderr]] to be piped, commands that only accept commad arguments.
- Example: `echo` command doesn't accept any [[devlog.Redirecting stdin & stderr]], it only accepts command args
- To work around this we first need to convert the [[devlog.Redirecting stdin & stderr]] into command args and then pipe it.
- Demonstration:

`date | echo` will not work nor will `date | echo "hello"` work

What will work is:

`date | xargs echo`

you can also pass `echo`'s own command args such as:

`date | xargs echo "hello"` but here it will run its own arg first

To see this in action:

`date | cut -d " " -f 1 | xargs echo`

---

- Using `cat` to get file names to delete from a file, passing(piping) it as args to `rm` command.
- Making a file and writing file names to be deleted.
- `FilesToDelete.txt` contains: date.txt day.txt
- Now:

`cat FilesToDelete.txt | xargs rm`
