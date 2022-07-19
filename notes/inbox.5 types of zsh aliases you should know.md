---
id: q9n3dfkllbc97galu8ipkcm
title: 5 Types of Zsh Aliases You Should Know
desc: ''
updated: 1652786933044
created: 1652786933044
tags:
  - articles
---

# [5 Types Of ZSH Aliases You Should Know](https://www.thorsten-hans.com/5-types-of-zsh-aliases)

My shell means everything to me. It is the first program I start in the morning and the last one I close in the evening. It is the program that I regularly tweak to boost my overall productivity. From my perspective, Microsoft’s release of Windows Terminal 1.0 and WSL 2.0 will boost overall Shell adoption. Over the past decade, I have seen numerous users installing and using different shells. However, the number of people that invest time in configuring their shell to be more productive is just a small percentage. And that is a shame!

You can also stick with tools like Finder or Windows Explorer if you install and use a shell without customizing it. Shells like ZSH shine once they have individual configurations: configurations that make you - the user - super productive. I wrote this article for inspiration. It should demonstrate how you can increase your overall productivity with simple things like adopting the 5 types of aliases in ZSH. Aliases are the first step towards a tailored shell experience. Aliases are a super individual thing.

I use Docker, Kubernetes, and Microsoft Azure every day. That said, it makes sense for me to have aliases supporting me with these tools and environments. However, maybe you are using different clouds and command-line tools so that you will end up with different aliases. The key takeaway should be that you create and use aliases to help you get your job done.

All your aliases are defined in `~/.zshrc`. ZSH loads the configuration file during startup. However, you can always force to reload your configuration file use `source ~/.zshrc`.

This article will teach you how to create and use these five types of aliases:

-   [Simple Aliases](https://www.thorsten-hans.com/#simple-aliases)
-   [Suffix Aliases](https://www.thorsten-hans.com/#suffix-aliases)
-   [Functions for Aliases With Parameters](https://www.thorsten-hans.com/#functions-for-aliases-with-parameters)
-   [Global Aliases](https://www.thorsten-hans.com/#global-aliases)
-   [Operating system specific aliases](https://www.thorsten-hans.com/#operating-system-specific-aliases)

## Simple Aliases

Simple Aliases are a good starting point. I use them to reduce the number of keystrokes to fire up a command. The definition of a simple alias uses the `alias my-alias="command"` pattern.

```
# navigation aliases
alias dev="cd ~/dev/"
alias personal="cd ~/dev/thorstenhans"
alias business="cd ~/dev/thinktecture"

# kubectl aliases
alias k="kubectl"
alias kgx="kubectl config get-contexts"

# docker aliases
alias d="docker"
alias dps="docker ps"
```

Having those aliases registered in my `~/.zshrc`, I can navigate quickly to commonly used directories and to fire-up commands that I use frequently using just a few keystrokes.

## Suffix Aliases

Suffix Aliases are defined using the `-s` flag. With suffix aliases, you can launch files with a specific extension (or suffix) in your favorite tool. To register a suffix alias, we use the `alias -s extension=name-of-the-tool` pattern. The following samples assume that VisualStudio Code is installed and can be launched using the `code` command from the terminal.

```
# Azure CLI files
alias -s azcli=code

# Markdown files
alias -s md=code

# JSON files
alias -s json=code

# bulk association
alias -s {cs,ts,html}=code
```

Load the modified `~/.zshrc` and execute the following:

```
echo "#Hello World" > sample.md

# now type the name of the file and commit via ENTER
sample.md
```

The suffix alias translates `sample.md` into `code sample.md`, and you should see VisualStudio Code launching and showing the content of `sample.md`.

## Functions for Aliases With Parameters

Sometimes you want to create aliases that require some contextual information. Parameters are used to describe this contextual information for shell commands. The registration of aliases with parameters looks pretty similar to a function definition in regular programming languages. We use the following pattern to define aliases with parameters:

```
aliasname() {
  command $firstParam $secondParam
}
```

For example, consider you want to optimize the process of listing Azure Kubernetes Service (AKS) instances in your Azure Subscription. To achieve this, Azure CLI provides the `az aks list` command. The command allows further configuration by adding several parameters.

The following alias accepts two parameters—first, the Resource Group Name (Resource Groups are logical containers in Azure). The second parameter specifies the desired output format.

```
getaks() {
  az aks list -g $1 -o $2
}
```

We can now use the `getaks` alias with parameters to look for AKS instances in `resource-group-1` and print results in colored JSON (`jsonc`) using `getaks resource-group-1 jsonc`.

## Global Aliases

Global aliases are defined using the `-g` flag. A global alias is aggressive. Once registered, it replaces all occurrences of the alias name with the specified command. The definition follows the pattern `alias -g aliasName="command"`.

```
# I have to ask for Azure Resource Ids frequently
alias -g qId="--query id -o tsv"
```

Having `qId` registered as a global alias, I can optimize my performance when asking for unique resource identifiers using Azure CLI. See the following snippet comparing the regular command, to the optimized one using my global alias:

```
# proper command to query the identifier of an AKS instance
az aks show -n myaks2020 -g rg-demo --query id -o tsv

# command to query the identifier of an AKS instance with global alias
az aks show -n myaks2020 -g rg-demo qId
```

## Operating system specific aliases

An operating system specific alias is not a real type. However, I think platform-specific aliases are important—especially when using multiple platforms. I use macOS as a daily driver, so I also have some aliases tied to my rig.

However, I love VisualStudio Codespaces that are using Linux as an operating system. In both situations, I want to use my dotfiles. To achieve this, I use simple `if`\-statements.

```
# macOS aliasses
if [[ $OSTYPE == darwin* ]]; then
alias flush='dscacheutil -flushcache'
# Apps
alias browse="open -a /Applications/Google\ Chrome.app"
# * Browse Azure Portal
alias azure="browse https://preview.portal.azure.com"
fi
```

See the following image showing all my platform related aliases for macOS:

![Platform specific aliases in ZSH](https://www.thorsten-hans.com/images/zsh-aliases-1.png "5 alias types in zsh - platform specific aliases")

## Use Aliases To Edit and Reload .zshrc <!– omit in toc –>

I have two aliases in my `~/.zshrc`, which are super-efficient. I open my `~/.zshrc` in my favorite editor with `ec` and source it (apply the current state of `~/.zshrc` to your ZSH session) with `sc`. The alias definition for both looks like this:

```
# open ~/.zshrc in using the default editor specified in $EDITOR
alias ec="$EDITOR $HOME/.zshrc"

# source ~/.zshrc
alias sc="source $HOME/.zshrc"
```

## Conclusion <!– omit in toc –>

You have seen five different types of ZSH aliases (counting os-specific aliases as dedicated type) that will boost your productivity.

Take your time. Do some research. Identify the command-line tools you are using daily or regularly, find patterns, and create corresponding aliases that increase your productivity by reducing keystrokes.

Having powerful shells on all operating systems (finally including windows using WSL 2.0), you should care about your shell performance. Make ZSH your own.

I do a lot of conference speaking; if you are presenting at conferences or meetups too, you should start your presentation by quickly explaining the aliases you will use throughout the talk to onboard your audience. Maybe they are using `kc` instead of `k` for `kubectl`. 😂

Special thanks to [Sundeep Agarwal](https://github.com/learnbyexample) for pointing me to some typos and to [simohamed](https://github.com/smhmd) for the tip regarding bulk association for suffix aliases.
