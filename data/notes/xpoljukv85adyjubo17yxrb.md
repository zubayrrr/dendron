
# [Programmable Notes](https://maggieappleton.com/programmatic-notes)

## The Context

Most "note-taking" or "knowledge management" software acts as a passive storage container. You create notes, shuffle them around into folders, add a few tags, and then they sit there. Waiting. Until you consciously remember go looking for them.

This warehouse approach to notes requires us – the human agent in the system – to do a **lot** of cognitive labour if we want to *use* our notes. And *using* our notes is the entire point of any note-taking enterprise.

Most of us have an ulterior motive beyond writing notes – we want to remember, understand, synthesise ideas, come to confident conclusions, generate new ideas informed by historical and social events, write coherent essays, or work through difficult problems.

Getting to any of these outcomes requires far more work than typing words into a storage container and retrieving them again. Most note-taking software doesn't guide us towards any particular workflows or ways of thinking with our notes. We have to develop them ourselves.

We have to remember what kind of information we saved in the first place. We have to know what keywords or search methods will allow us to find it again. We have develop ways to integrate old ideas with new ones. We have to prompt ourselves to expand on our notes, combine them, synthesise them into new realisations, and critique our own conclusions.

Thankfully, there's a long history of people finding ways to makes these cognitive tasks easier. We can draw on well-established cultural practices and techniques; we can write and build . We can practice and . We can use to regularly resurface old ideas. We can write for an engaged and discerning public audience. We can even sign up for expensive masters degrees that will force us to ask hard questions and conjure up defensible answers.

These practices are what turns notes into understandings, conclusions, informed opinions, new ideas, and original creations. But we've yet to see note-taking software that **actively facilitates and encourages** these kind of workflows. They are, for the most part, still behaving like storage boxes.

What if we started to think about note-taking systems as active agents, rather than receptacles?

Agents can prompt you to do specific activities in a sequence. They can ask you questions. They can suggest relevant material based on what you've already written. They can periodically resurface old ideas to ask if they still ring true. They can prompt you to connect two disparate ideas together. They can mimic conversational partners who debate the strengths and weaknesses of a point – naive partners perhaps, but still better than no partner at all.

"Agents" here are simply programmes; pre-written sequences of instructions that facilitate standardised cultural practices and repeatable ways of relating to the world.

We could, in essence, run automated programmes and algorithms over our notes. Programmes that we have the agency to write as users.

## The Pattern

Programmable notes are note-taking systems that allow you to write programmatic rules that facilitate particular ways of working with your notes.

Based on triggers (specific conditions are met, input from the user, time of day), they kick off a sequence of actions. Actions might be prompts for the user to answer, transformations on the notes themselves, or requests to external websites and data sources for information.

We're floating into the land of computational abstraction so let's make this tangible with some examples:

I could go on, but I'll spare you from my other 99 mediocre programmatic note ideas. It's hopefully clear that the goal of these is to encourage practices like reflection, synthesis, connection, and serendipity. The goal is not to simply amass notes.

None of the automations I've suggested above are impractically complex or technologically impossible. They all follow a reasonably simple *if this, then that* structure that most of us will find familiar. Many are perfectly possible and currently used in existing platforms.

The plug-in for is the system I personally use to build these types of workflows. It offers a set of triggers, variables, and commands you can chain together into fairly readable statements like: `<%SET:topOfMindToday,<%INPUT:What's on your mind today?%>%>` or `<%RANDOMBLOCKFROM:Writing Ideas%>`.

Even with limited programming knowledge, many people in the community have been able to fashion their own Smartblock flows. Plenty of them have their workflows to the community Github for others to use. These include over a selection of text, pulling data into your notes, and a flow walking you through the benefits, risks, and costs of all your options.

The UX of both Smartblocks and Roam is still pretty rough. But they're pointing towards something promising. They're also not alone in enabling users to write their own programmable notes. There are a wide range of user-created plug-ins for similar platforms like and that enable some of these same workflows.

is another app that allows users to build fairly complex programmatic systems within documents. You can create buttons that trigger actions and write automation scripts with conditional logic.

Another project I'm watching closely is 's app (currently in alpha) that promises to feature *"geists"* – "little scripts that find connections between notes, and use procedural generators to construct algorithmic provocations."

These trends all bode well for programmable notes. They prove that – given enough agency – users will enthusiastically write their own programmes that facilitate the particular note-taking practices and techniques they find valuable.

This is in action. The developers and designers of note-taking apps will never be able to create systems that suit the needs of everyone's particular knowledge management workflows. Enabling users to design and share their own is the only way to give people agency over their knowledge bases.

#### But what about AI???

It is impossible to propose agentive computational systems designed to help us think better without bringing up **THE AI**. Let's first point out the term "AI" is a nebulous and finicky cultural narrative. People use it in all sorts of ways depending on the political agenda of the speaker.

In this context, I'm using *AI* to refer to systems that use natural language processing, neural networks, and machine learning to respond to people in seemingly 'intelligent' ways. These will play an enourmous role in the future of programmable notes.

We've yet to see note-taking platforms meaningfully add *AI* affordances into their systems, but there are hints at how they could in other platforms.

The most impressive and promising I've seen is , a research tool that helps academics and students find relevant papers and data based on natural language inputs. You can ask it a question like "What's the point of note-taking?" and recieve a list of research papers that are likely to hold the answer. Even better, Elicit creates a one sentence summary of the paper's main finding and presents it in the results.

Finding relevant research papers is critical for academics and researchers, but isn't a large part of everyone's writing and sense-making process.

Elicit has an alternative suite of tools that I find much more intriguing for our use case. Using the same NLP technology you can run requests like:

-   Clarify a concept
-   Suggest similar search terms
-   Brainstorm possible counter arguments
-   Rephrase a sentence
-   Help me be more specific.

These simple linguistic transformations and generative prompts don't require a high level of intellectual sophistication to be useful. Sometimes you just need a wall to bounce ideas off. And modern NLP systems are a great wall. They can give us just a touch of reflection, perspective, and serendipity when we get stuck in our own heads.

To address the slippery-slope argument, I think it's pointless to worry about these systems doing too much of our thinking for us. Rephrasing a sentence is a far cry from writing an informed and insightful social criticism essay.

They certainly might prompt us to think in novel and unfamiliar ways though. is still the end goal here. Let's hope we see more of it.
