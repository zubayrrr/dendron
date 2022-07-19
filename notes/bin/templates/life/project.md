---
created: {{DATE}}
title: README
tags: 
  - project
status: 
subtitle: {{VALUE:Project Subtitle}}
draft: true
---
%%
```js quickadd
const goalNotes = DataviewAPI.pages("#goal").where(p => !p.file.path.contains("template")).values;
const targetGoal = await this.quickAddApi.suggester(goalNotes.map(p => p.file.name), goalNotes);
const targetGoalFile = app.vault.getAbstractFileByPath(targetGoal.file.path);
let markdownLink = this.app.fileManager.generateMarkdownLink(targetGoalFile, '');
markdownLink = `${markdownLink.slice(0, markdownLink.length - 2)}${markdownLink.slice(markdownLink.length - 2)}`
return `Goal:: ${markdownLink}`;
```
%%
***

## Project Info

## Thoughts 

## Resources

## Review questions

## Tasks
- [ ] 