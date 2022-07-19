<%\*
const title*prefix = await tp.system.suggester(
["🎥 Video",
"🐦 Tweet",
"💭 Thought",
"🎧 Podcast",
"👤 Person",
"📜 Paper",
"🌱 Seedling",
"📚 Book",
"📰 article"],
["+ ",
"! ",
"= ",
"% ",
"@ ",
"& ",
"",
"{ ",
"( "],
false,
"Type of Note"
)
let title = await tp.system.prompt("What is the name of your new note?")
await tp.file.rename(title_prefix + title)
*%>
