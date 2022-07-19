---
id: qnmnin2mvf4qs4rmyxpmeeo
title: '4 Essential Linux Productivity Tools Ulauncher, Espanso, Planner, and Obsidian'
desc: ''
updated: 1652786932977
created: 1652786932977
tags:
  - articles
---

# [4 Essential Linux productivity tools: Ulauncher, Espanso, Planner, and Obsidian](https://input.sh/linux-productivity-tools/)

As a user of a Linux-based operating system, I always envied macOS users for the choice of productivity tools available on their disposal, with tools like [Alfred](https://www.alfredapp.com/) , [TextExpander](https://textexpander.com/) , [Bear](https://bear.app/) , [Keyboard Maestro](https://www.keyboardmaestro.com/main/) , [OmniFocus](https://www.omnigroup.com/omnifocus/) and so forth. I believe I've achieved comparable results on my [elementary OS](https://elementary.io/) install, and I want to share the tools I'm relying on on a daily basis.

## A better launcher

I have a lot of respect for Slingshot, a default launcher for **elementary OS**. It has some features that I really miss when I'm not behind my favourite desktop environment, most notable of which are:

1.  **Fuzzy search:** Instead of having to type "firefox" precisely, I can (mis)type something that resembles the word Firefox and it will still show it as a result. For example: "ffx", "frf", "ffox". Any combination of letters contained in the word "Firefox" will return it as a result.
2.  **Quick calculations:** When I want to quickly calculate something basic, I don't have to start a dedicated calculator app. I just press the ~start~ meta key and do them straight from my app launcher.

[Ulauncher](https://ulauncher.io/) takes it a step further, similarly to how Alfred does it on a macOS. Sure, I can launch applications using it, but I can also install plugins for it that allow me to quickly reach many, *many* functions. Some examples include:

-   [Starting a timer](https://ext.ulauncher.io/-/github-ulauncher-ulauncher-timer) with something like `ti 10m Message goes here`, which will show me a desktop notification with a defined message after the specified amount of time.
-   [Control Spotify](https://ext.ulauncher.io/-/github-pywkm-ulauncher-spotify) . Typing `sp` gives me the ability to pause/play current track, as well as to skip to the next or previous track.
-   [SSH connection manager](https://ext.ulauncher.io/-/github-jetbug123-ulauncher-ssh) allows me to quickly reach SSH connections saved in my `~/.ssh/config`.
-   [Clipboard manager](https://ext.ulauncher.io/-/github-friday-ulauncher-clipboard) saves anything that's in my clipboard, allowing me to quickly access things I've copied over.

Depending on your needs, it can do a lot more, like [launch VSCode projects](https://ext.ulauncher.io/-/github-brpaz-ulauncher-vscode-projects) , [manage Docker containers](https://ext.ulauncher.io/-/github-brpaz-ulauncher-docker) , [calculate hashes](https://ext.ulauncher.io/-/github-friday-ulauncher-hash2) , [search through Jira](https://ext.ulauncher.io/-/github-safaariman-ulauncher-jira) , [do an IP lookup](https://ext.ulauncher.io/-/github-munim-ulauncher-ip-lookup) , [convert units](https://ext.ulauncher.io/-/github-noam09-ulauncher-units) , look for a password in [Bitwarden](https://ext.ulauncher.io/-/github-kbialek-ulauncher-bitwarden) or [LastPass](https://ext.ulauncher.io/-/github-brpaz-ulauncher-lastpass) and on and on and on.

I use a combination of the two. I use the default launcher for launching apps and doing some calculations, and I use Ulauncher to do so much more.

Unfortunately, none of these solutions have something similar to [Alfred's Workflows](https://www.alfredapp.com/workflows/) , but you can create your own Ulauncher extensiosn or launch scripts written in your preferred scripting language.

## Glorified to-do list manager

I don't think *any* to-do app available on Linux comes even close to being as beautiful and feature-packed as Planner. Just look at how pretty it is!

![Planner's main interface](inbox/assets/Planner's%20main%20interface.png)

Your projects can be organised into folders, and your tasks can have labels, deadlines, reminders, and so on. Tasks can be organized into projects, sections, and have sub-tasks. You can sync them with Todoist to have them available on more devices, but you don't have to.

Similarly to Todoist, you can see all the tasks that have a deadline set to today + any overdue tasks, you can see the tasks that are due soon, and you have an inbox as a place where you can store the tasks quickly without having to figure out which project they should go to.

One killer feature for me is that I can have a keyboard shortcut that toggles the quick add window, allowing me to add a new task pretty effortlessly regardless of which app I'm using.

## Expanding text

For text expansion, I use a cross-platform tool written in Rust called [Espanso](https://espanso.org/) . Regardless of what I'm typing, I can define shortcuts that convert something easy to write in something that takes more effort. For example, I can type `:date` in any text field and it will be swapped by today's date when I press the space bar.

I can define custom text replacements by simply adding two lines inside a YAML file (`~/.config/espanso/default.yml`):

```
matches:
  - trigger: ":hw"
    replace: "Hello world"
```

It can also use a trigger to return an output from a script or a shell command, though I have yet to find a use case for that. You can also configure a shortcut to trigger a [passive mode](https://espanso.org/docs/passive-mode/) , which will select everything in the current text field and expand it if it finds any triggers you've defined.

On the downside, it currently doesn't come with a graphical interface, though a graphical interface is at the top of its [roadmap](https://github.com/federico-terzi/espanso/issues/255) .

## A note-taking system

I've tried many solutions for note taking over the years, like keeping my notes in Markdown files, [Notion](https://www.notion.so/) , and [Inkdrop](https://www.inkdrop.app/) . That all ended when I found out about [Obsidian](https://obsidian.md/) . It's my go-to note taking system ever since it launched in public beta and I can't see myself using anything else for the foreseeable future.

A few months ago I wrote about [why I do(n't) keep my notes in Markdown](https://input.sh/why-i-dont-write-my-notes-in-markdown/). In it, I emphasized a certain set of problems I've experienced whenever I wanted to keep my notes inside of a folder full of Markdown files:

1.  Linking between notes is hard.
2.  Dealing with images is hard.
3.  Editing notes on a phone.
4.  Clipping articles into my notes.

The first two are instantly solved by Obsidian out-of-the-box. [GitJournal](https://gitjournal.io/) solved my third one, and I've solved the last one by [adjusting the script](https://gitjournal.io/) I've outlined in the previous article.

Now I can truly keep all of my notes in one place and sync them between devices however I want to. I can also generate a handy graph showing various links I've created between my notes:

![Screenshot-from-2020-08-03-14-44-40](inbox/assets/Screenshot-from-2020-08-03-14-44-40.png)

## In conclusion

I was able to transform my Linux experience to another level using a combination of awesome productivity tools that work natively on my Linux-based system. Overall, I'm pretty happy with my setup, as I was able to find an alternative to the majority of macOS-specific productivity tools I always wished to have access to.

If you know of a similarly useful Linux-based productivity tool or are building one, please let me know on Mastodon / Twitter, as I'd love to be one of your first users. I'm not an open source purist and I'm more than willing to pay money for something that will truly improve my daily workflow.
