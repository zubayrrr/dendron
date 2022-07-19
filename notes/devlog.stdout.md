---
id: do68y261xeu98bpq3vl5cn9
title: stdout
desc: ''
updated: 1652947243111
created: 20211011140104292
---

- It is part of [[devlog.Standard Data Stream]]
- [[devlog.stdout]] is denoted by the number 1 in the [[devlog.Standard Data Stream]]
- Example of changing destination of [[devlog.stdout]]: `cat 1> output.txt`
- Where `1` is the number of data stream `>` is direction and `output.txt` is destination. (note that we cannot add a space after `1` or before the `>` sign)
- Alternatively you can skip the `1` because Linux by default is expecting [[devlog.stdout]] so just do: `cat > output.txt`
- To avoid truncation (overwriting), you can use `>>` example:  
  `cat >> output.txt` and now whenever you try to redirect [[devlog.stdout]], it'll append instead of truncating.
- Example: `date >> date.md`
