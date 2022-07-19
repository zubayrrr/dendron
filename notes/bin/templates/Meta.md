<%_ if (tp.file.title.charAt(0) == "{") { %>
<%-tp.file.include("[[bin/templates/inputs/book]]")%>
<%_ } else if (tp.file.title.charAt(0) == "@") { %>
<%-tp.file.include("[[people]]")%>
<%_ } else if (tp.file.title.charAt(0) == "!") { %>
<%-tp.file.include("[[Tweet]]")%>
<%_ } else if (tp.file.title.charAt(0) == "%") { %>
<%-tp.file.include("[[podcast]]")%>
<%_ } else if (tp.file.title.charAt(0) == "+") { %>
<%-tp.file.include("[[Youtube]]")%>
<%_ } else if (tp.file.title.charAt(0) == "(") { %>
<%-tp.file.include("[[article]]")%>
<%_ } else if (tp.file.title.charAt(0) == "&") { %>
<%-tp.file.include("[[paper]]")%>
<%_ } else if (tp.file.title.charAt(0) == "=") { %>
<%-tp.file.include("[[Thought]]")%>
<%_ } else { %>
<%-tp.file.include("[[New]]")%>
<%_ } \_%>
