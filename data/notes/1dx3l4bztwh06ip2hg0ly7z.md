
- Areas: [[devlog.linux]]

---

- `less` is a command line utility that displays the contents of a file or a command output, one page at a time. It is similar to [[more]], but has more advanced features and allows you to navigate both forward and backward through the file.
- When starting less doesn’t read the entire file it reads the contents of a file one page(one screen) at a time which results in much faster load times compared to text editors like [[devlog.vim] or [[nano]] .
- The less command is mostly used for opening large files .
- Syntax:
  - `less path-to-file`
- Notes:
  - [[Man Pages]] launch the `less` command by default
  - `Ctrl + F` or `space` to move forwards one window
  - `Ctrl + B` to move backwards one window
  - `g` to go to the very beginning of the file
  - `G` to go to the very end of the file
  - To search a string from the very top of the file, press `/` and type the string
    - Use `n` or `N` to navigate between the search results
  - To search from the bottom of the file, press `?` and type the string
