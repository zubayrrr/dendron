
- [[devlog.stderr]] is denoted by number 2.
- This is commonly used to keep log of errors from various servers and services.
- Make sure to use `>>` to append the error to the log file instead of overwriting or truncating it.
- Example of redirecting [[devlog.Redirecting stdin & stderr]]:
  - `cat -k blah 2> error.txt`
    - Since `-k blah` is an invalid command argument, it'll throw an error that will be caught inside the `error.txt` file.
  - `tail -n 3 /etc/shadow 2>> error.txt`
- You can also pass multiple arguments to save [[devlog.stdout]] as well as [stderr], such as:  
  `cat >> output.txt 2>> error.txt` or  
  `tail -n 2 /etc/passwd /etc/shadow > output.txt 2> error.txt`
- Passing both [[devlog.stdout]] and [[devlog.stderr]] to same file:
  - `tail -n 2 /etc/passwd /etc/shadow > output.txt 2>&1` where `1` is the ID of the stdout, `&` is the operator that redirects the error to the output

---

- We can serve [[devlog.Redirecting stdin & stderr]] from somewhere other than our keyboard.
- We can put our input in a file, suppose `input.txt` and then by doing  
  `car 0< input.txt` we can ask `cat` to get the input from the `input.txt` file instead of getting it from the keyboard(which is the default). You can omit the `0` since Stdin is the only default thing it is expecting and just make it `cat < input.txt`.

---

- We can now push the input to an output without using the keyboard by doing:  
  `cat < input.txt > output.txt`

---

- We can also push the input to a different file, even to another terminal instance.
- Step 1: Open a new terminal instance using the shortcut Ctrl + Alt + T.
- Step 2: Get the location of the terminal using the [[devlog.tty]] command.
- Step 3: From the previously opened terminal, `cat < input.txt > /dev/pts/2`. where `/dev/pts/2` is the output we got from the [[devlog.tty]] command.
