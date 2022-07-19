
<%*
  
  function getUnique(value, index, self) {
    return self.indexOf(value) === index;
  }
  var out = '';
  var exclude_tags = [
    '#double_click_me'
  ];
  // find the window
  let cmEditor =this.app.workspace.activeLeaf.view.editor
  /* I don't exactly how to find line direct, so I search around code mirror and 
	 found this which give offset from the begging of the file later I convert it to line, 
	 character position and increment it by 1 to
  */
  let tagspos = this.app.workspace.activeLeaf.view.data.search("tags:")
  let posLine = this.app.workspace.activeLeaf.view.editor.offsetToPos(tagspos)
  posLine.ch += (tagspos + 1)
  cmEditor.focus()
  cmEditor.setCursor(posLine)
  var tUnique = tp.file.tags.filter(getUnique);
  var tArr = tUnique.filter(t => exclude_tags.includes(t) === false);
  if (tArr.length) {
    tArr.sort();
    var tStr = tArr.join(', ').replace(/#/g,'');
    out = '[' + tStr + ']';
  }
%>
<%* tR += out %>
