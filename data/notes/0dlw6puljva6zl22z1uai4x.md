
- `topics:` [[devlog.linux]]
- `resources:` [[The Grymoire's tutorial on SED]]

---

`sed` command is used for string replacement

### Example

If we want to eliminate the "," in "Kutuzov," and redirect the output to a new-file

`sed 's/Kutuzov,/Kutuzov/' war-and-peace.txt > new-file`
