
- Use public key authentication for SSHing into servers.
- Always create a new user (Do not use root user) on new machines. Add the user to the `sudo` group.
- Create dedicated users for software like [[devlog.jenkins]], [[devlog.nexus]] etc. Never run these services/software with root user permissions.
- Never keep active access keys, generate them when you need it and simply delete them after use.
- It is a good practice to run [[devlog.Docker]] containers with their own service user.
- You should version your projects like using [[devlog.git]] tags. A tag is like a branch that doesn't change.
- What makes a good/senior DevOps engineer (among other things) is their ability to compare different tools and use the most efficient one to get the task done.

## Resources

- [DevOps Best Practices | Atlassian](https://www.atlassian.com/devops/what-is-devops/devops-best-practices)
