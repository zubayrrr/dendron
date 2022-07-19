---
videos: <% tp.file.cursor(0) %>
---

# Weekly Review:

%% This template Requires the Templatr plugin and should be run on fridays, if not on friday, the value offsets should be adjusted %%

[[2022-W19]] <== This Week ==> [[2022-W21]]

## Notes Created This Week

```dataview
TABLE tags
FROM ""
WHERE file.ctime.year = [[README]].file.ctime.year 
	AND file.ctime.month = [[README]].file.ctime.month
	AND file.ctime.day >= [[2022-W19]].file.ctime.day
	AND file.ctime.day <= [[2022-W20]].file.ctime.day
SORT file.name
```

[[2022-05-10]] ==> [[2022-05-16]] 

- [[2022-05-10]] 
	- <% tp.file.cursor(1) %>
- [[2022-05-11]] 
	- <% tp.file.cursor(2) %>
- [[2022-05-12]] 
	- <% tp.file.cursor(3) %>
- [[2022-05-13]] 
	- <% tp.file.cursor(4) %>
- [[2022-05-14]] 
	- <% tp.file.cursor(5) %>
- [[2022-05-15]] 
	- <% tp.file.cursor(6) %>
- [[2022-05-16]] 
	- <% tp.file.cursor(7) %>
