
1. **EC2 instance is running out of disk space. What actions will you take to mitigate the issue?**

- [[devlog.AWS EC2]] disk space typically refers to [[devlog.AWS EBS]] volume.
- We'll first check if its a root volume or any other volume
  - /root - OS
  - /application - for all our applications
- If its root volume then we'll first try to check logs(`/var/logs`) and clear some space if not the instance might shut down.
- If its the application volume(learn the reason of high disk usage), then we'll use EBS feature to take the snapshot and increase disk space for the EC2 instance.

2. **Explain different ways in which** [[devlog.prometheus]] **can get metrics?**

![[devlog.prometheus# Getting-metrics]]

3. **What is Kubernetes kOps?**

[[devlog.kubernetes]] [[devlog.kOps]] is an automation tool used to setup Kubernetes cluster. It is an alternative to `kubeadmin`.

kOps can help you spin a test cluster or a small dev cluster quickly. It is not something that will help you setup managed Kubernetes cluster([[devlog.AWS EKS]]). It can create, destroy, upgrade, maintain production-grade, high availability clusters and also provision necessary cloud infrastructure(only recommended if you cannot afford managed service).

It supports many cloud providers.

4. **What is instance fleet in AWS?**

Instance fleet in [[devlog.AWS]] refers to a configuration - information to launch a fleet or a group of [[devlog.AWS EC2]] instances, in a single API call. A fleet can launch multiple instance(mixed set) types across multiple Availability Zones using On-Demand Instance, Reserved Instance and Spot Instance purchasing options together.

In the configuration you can define:

- Separate capacity targets and maximum amount you're willing to pay per hour for On-Demand, Spot instances.
- Specify the instance types that work best for your applications.
- Specify how EC2 should distribute your fleet capacity within each purchasing options.

The instance fleet configuration for [[devlog.AWS EMR]] lets you select wide variety of provisioning options for Amazon EC2 instances and helps you develop a flexible and elastic resourcing strategy for each node type in your cluster.

5. **How do you pass “message” for your git commit**

Use the flag `-m [message]` for your [[devlog.git]] commit. Although you can commit without passing a message.

`git commit -m "🔥 commit message"`

6. **What application server are you familiar with?**

[[devlog.web server & application server]]

For Java applications, we have [[devlog.tomcat]] but there are different application servers for applications based on different technologies.

7. **How to check logs of a Docker container/filter last 200 lines from the logs.**

`docker container logs <container_name>`
`docker container logs --tail 200 <container_name>`

8. **What happens to container logs if it is restarted?**

You won’t lose any logs for restarting a container but since containers are stateless, you will lose the logs if a container is **deleted**. If you want to persist logs you can use external persistent storage. You can also push the container logs to something like [[devlog.AWS CloudTrail]] or [[devlog.splunk]]

9. **Horizontal Scaling VS Vertical Scaling**

**Horizontal scaling** means scaling by adding more machines to your pool of resources (also described as “scaling out”); something like [[devlog.AWS Auto Scaling Group]], creating replicas(think [[devlog.kubernetes]]). If you are hosting an application on a server and find that it no longer has the capacity or capabilities to handle traffic, adding a server may be your solution.

Whereas **vertical scaling** refers to scaling by adding more power (e.g. CPU, RAM) to an existing machine (also described as “scaling up”). For instance, if your server requires more processing power, vertical scaling would mean upgrading the CPUs. You can also vertically scale the memory, storage, or network speed.

See: [Horizontal Vs. Vertical Scaling: How Do They Compare?](https://www.cloudzero.com/blog/horizontal-vs-vertical-scaling)

10. **ReplicationController in Kubernetes**

A ReplicationController is responsible for running the specified number of pod copies(replicas) across the cluster.

ReplicationController is not auto scale.

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
```

11. **What is helm?**

![[devlog.helm]]

12. **Which Python module would you use to write a simple program to test API code?**

The code should just check if the API endpoint is working or not.

**Answer:**

I would use the **request** module in [[devlog.python]]. It has the `get()` function wherein you'd pass pass the API endpoint and fetch status/http code `.status_code`.

If it returns `200` - API endpoint is working fine.

13. **Which HTTP responses would you monitor and for which would you trigger alerts?**

Example of API endpoints:

```
/this-is-an-endpoint
/another/endpoint
/some/other/endpoint
/login
/accounts
/cart/items
```

HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

- Informational responses (100–199)
- Successful responses (200–299)
- Redirection messages (300–399)
- Client error responses (400–499)
- Server error responses (500–599)

- If HTTP response is in the 400 or 500 range we'll trigger an alert by writing a script of setting up a monitoring service.

14. **Can we run a Jenkins agent inside a docker container along with our test?**

- Running Jenkins agent inside a [[devlog.Docker]] container is (one of) the standard way of implementing pipelines.
- This question is focusing on isolation of pipeline steps.
- Here the code is expected to run inside a docker container which can use a custom test image if required.
- This is the best way to perform testing without having every [[devlog.Jenkins]] agent needing to have packages installed.
- To use any kind of Docker containers, I'd add it as a part of the agent. We can call any kind of images(from DockerHub or Custom), whatever stages and test steps we mention as part of our pipeline will run inside that docker container. Multi node Jenkins setup.

![](https://res.cloudinary.com/zubayr/image/upload/v1655971387/wiki/m9mcgppau59fyaewl0uw.png)

15. **What are some of the ways of setting up alerts?**

It is not feasible to have multiple alerting methods in one org. Alerts notifications can be Emails, Phone calls, Slack messages, etc. This ties into the [[devlog.on-call]] management.

Some of the open source methods:

- [[devlog.prometheus]] -> Alertmanager
- [[devlog.AWS CloudWatch]] -> SNS
- Nagios -> Alerting

16. **Help repository to store/access helm charts**

Helm repositories are a common practice to store helm charts, which can be access by our [[devlog.kubernetes]] cluster as part of a deployment. This helps with versioning our helm charts, rollbacks, upgrade etc.

- Cloudsmith
- Jfrog Artifactory
- [[devlog.AWS S3]]
- Google Cloud Storage
- Artifact Hub(Open Source)

17. **Jenkins multi-node setup, how to add new slave/follower to master?**

Having only one node is usually not enough(availability) for any organization so a multi-node setup is required for scaling. You can add a slave/follower for a master on "Manage [[devlog.Jekins]]" page and the option "Manage Nodes and Clouds". You will provide node info such as the IP Address, username, password etc and get it registered. We can also add slaves dynamically, you'd need an auto scaling group by your Cloud Provider.

18. **How do you block an IAM user from accessing a specific S3 bucket?**

It is difficult to manage bucket level policies using IAM policy. We can achieve this using [[devlog.AWS S3]] bucket policy, you'd use the IAM user's ARN and “deny” the user.

19. **Is a large docker image a cause of concern? How would you tackle it?**

Applications can be large if they're complex and do a lot of things but if it is a simple application...large size is not warranted and can be mitigated.

- Bigger docker image would result in longer build time.
- Docker image downloaded(from DockerHub) may throw errors or cause API rate limit issues.
- Application will be bulkier and harder to debug and scale.

To resolve this:

- Smaller Base Image(Alpine images).
- Introduce Multi-stage build - from the Base image you build up your image and discard your previous image builds.
- Remove package binaries after installing and don't install packages that are not necessary.
- Lock your package/dependencies versions.

20. **Are you aware of AWS IAM policies/can you read them?**

Policy evaluation logic

Example

```json
{
  "Version": "2012-10-17", // version is fixed
  "Statement": [
    {
      "Sid": "AllowS3ListRead", // high level ALLOW action
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation", // explicitly defining what actions are allowed
        "s3:GetAccountPublicAccessBlock",
        "s3:ListAccessPoints",
        "s3:ListAllMyBuckets"
      ],
      "Resource": "arn:aws:s3:::*"
    },
    {
      "Sid": "AllowS3Self", // high level ALLOW action
      "Effect": "Allow",
      "Action": "s3:*", // everything is allowed but only limited to the below two buckets
      "Resource": ["arn:aws:s3:::carlossalazar/*", "arn:aws:s3:::carlossalazar"]
    },
    {
      "Sid": "DenyS3Logs", // high level DENY action
      "Effect": "Deny",
      "Action": "s3:*", // everything is denied for any bucket with the suffix "logs"
      "Resource": "arn:aws:s3:::*log*"
    }
  ]
}
```

Example via - [Policy evaluation logic - AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

21. **What role does `pv` and `pvc` play in Kubernetes?**

PV stands for PersistentVolume
PVC stands for PersistentVolumeClaim

Pod gets it's storage using PVC which would in turn get hold of PV which will utilize an NFS or [[devlog.AWS EBS]] volume.

PVC will define what kind of volume and the storage amount it needs and it will search of PVs(which you'd have provisioned) and choose from those.

PV can exist independently from a Pod, you don't need to have a Pod for a PV to be created.

22. **When creating RDS using Terraform, how do you save DB username and password securely?**

Since DB username and password are considered secrets, they cannot be saved in plaintext on a repository along with the Terraform code.

You can use Hashicorp's Vault, store your secrets on your Vault.

Integrate it with Terraform. In your `main.tf` you can reference it as a Data Block. Mention Vault provider in the Provider section.

You can also use other secret stores/managers like [[devlog.AWS Secrets Manager]] etc. Or you can also use environment variables.

23. **Have you support any DBs?**

You don't need to be a DB expert but you have to have clear understanding of different kinds of DBs used, their use cases and pick one based on your experience and profile.

- Key-value DB
  - [[devlog.Redis]], etcd
- Column DB
  - Cassandra
- NoSQL/Document/Schemaless DB
  - [[devlog.mongoDB]]
  - [[devlog.AWS DynamoDB]]
- Relational DB
  - [[devlog.mysql]]
  - [[devlog.AWS Aurora]]
  - [[devlog.PostgreSQL]]

24. **How do you ensure certain packages are installed on all your EC2 instances and are persisted?**

HashiCorp's [[devlog.Packer]] is the solution. Packer is an open source tool that enables you to create identical machine images for multiple platforms from a single source template which can be written in JSON. You can use it in your multi-cloud setup or On-prem infra too.

A common use case is creating "Golden Images" that teams across an organization can use in cloud infrastructure.

We could also use custom [[devlog.AWS AMI]] images too but is limited to Cloud.

25. **Differentiate Managed, Customer Managed and Inline IAM policies.**

- Managed: Created and maintained by AWS.
- Customer Managed: Created and maintained by customer. Custom policies created by an organization using [[devlog.terraform]]. It can be attached to multiple users or groups.
- Inline: Created and attached directly to IAM User, Group or Role. It is created for that specific Role, User, Group ...if the Role, User or Group is destroyed, the policy is also deleted.

26. **What build tools are you familiar with?**

![[devlog.build automation# Building-Java-Applications:# Publishing-build-artifacts]]

26. **Ingress and Egress**

[[archive.ingress]] and [[archive.egress]]

In IT they refer to:

Ingress: Incoming/Inbound traffic
Egress: Outgoing/Outbound traffic

They're mostly associated with security groups([[devlog.firewall]]). They're also associated with VPCs and subnets where we control the incoming traffic from the internet and routing the traffic between subnets.

Eg: Allowing or denying ports for certain traffic([[devlog.ssh]], [[devlog.http]]). In prod, you'd usually lock it in the VPC IP Range.

27. **Differentiate Docker Image and Docker Layer.**

- Docker Layers are not separate components, you cannot have a single Docker Layer and use it. They're a subcomponent of a Docker Image.
- But an Image can consist of a single Layer(that's often the case when running `squash` command)
- Each Layer is an Image by itself.
- They're generated when you run `docker container` commands.
- Each Layer stores the changes compared to the image it's based on `docker history` can fetch you info on it's Layers.
- Each instruction in a Dockerfile results in a layer.

28. **What is bastion host or gateway server and what roles do they play?**

![[devlog.bastion host]]

29. **How do you troubleshoot an Auto Scaling Group that is facing issues provisioning new nodes(it is using spot instances)?**

Having an [[devlog.AWS Auto Scaling Group]] full of only spot instances is not a good idea unless the application can bear a little bit of downtime or have a back up ASG.

There could be two of many causes for this:

- Increase in spot price
- EC2 quota limit

Spot instances an be taken away from you if there is a change in bid price. Bidding high doesn't guarantee yous spot instances.

There is a soft limit set of every account on how many EC2 instances you can spin up. It can be mitigated by going to AWS Support and raise a ticket for increasing quota limit.

30. **Troubleshoot a Pod that is unable to access a volume due to access error.**

Volumes are handled/provisioned in Kubernetes as a part of PVs.

AccessMode of volume - see that your PVC or your volume supports `ReadWriteMany` permission for multi-pod access.

The access modes are:

- `ReadWriteOnce` the volume can be mounted as read-write by a single node. ReadWriteOnce access mode can still allow multiple pods to access the volume when the pods are running on the same node.
- `ReadOnlyMany` the volume can be mounted as read-only by many nodes.
- `ReadWriteMany` the volume can be mounted as read-write by many nodes.
- `ReadWriteOncePod` the volume can be mounted as read-write by a single Pod. Use ReadWriteOncePod access mode if you want to ensure that only one pod across whole cluster can read that PVC or write to it. This is only supported for CSI volumes and Kubernetes version 1.22+.

- [[devlog.NFS]] allows `ReadWriteMany`.
- [[devlog.AWS EBS]] only allows `ReadWriteOnce`.

31. **How to setup K8s in AWS?**

You can set them up directly on [[devlog.AWS EC2]]. Using either `kops` commands or `kubeadmin`. Or you can go with [[devlog.AWS EKS]].

If you want to set it up locally you'd go for `minicube`.

In prod we look for stability of our environment, hence the safest bet would be to go with a managed service such as EKS. For development you can go with [kOps](https://github.com/kubernetes/kops) clusters.

Code deployment should be taken care by [[devlog.helm]].

32. **Explain Load Balancers in AWS.**

![[devlog.load balancer]]

![[devlog.AWS ELB]]

33. **Have you used sonarqube?**

![[devlog.sonarqube]]

34. **Best practices for Incident Management.**

Applications expose metrics, metrics are collected using monitoring system, we have alert rules to trigger a phone call, Slack notification or email to the [[devlog.on-call]] engineer.

The organization should have a proper:

- Monitoring system
  - [[devlog.AWS CloudWatch]]
  - [[devlog.prometheus]]
- Alerting system
  - SNS
  - AlertManager

Postmortem: Understand what went wrong and how to mitigate in the future.

35. **How to validate variables during terraform plan time, for example format of the variable?**

In [[devlog.terraform]] you can define a `validation` block and specify a condition for the variable.

![](https://res.cloudinary.com/zubayr/image/upload/v1656067537/wiki/heqtzp8ccvxdlfsaqsbx.png)

Scenario: String may not contain a /.

```json
variable "string_may_not_contain" {
  type = string
  default = "test"

  validation {
    error_message = "Value cannot contain a \"/\"."
    condition = !can(regex("/", var.string_may_not_contain))
  }
}
```

Example via - [Terraform: Variable validation with samples](https://dev.to/drewmullen/terraform-variable-validation-with-samples-1ank)

36. **Explain/Differentiate `CMD` and `ENTRYPOINT` in Docker.**

The CMD command​ specifies the instruction that is to be executed when a Docker container starts. This CMD command is not really necessary for the container to work, as the echo command can be called in a RUN statement as well. The main purpose of the CMD command is to launch the software required in a container.

CMD commands are ignored by Daemon when there are parameters stated within the docker run command.

CMD. Sets default parameters that can be overridden from the Docker Command Line Interface (CLI) when a container is running.

You can pass input from CMD to ENTRYPOINT.

```bash
# CMD
FROM ubuntu:latest
CMD["echo", "Hello World!"]
```

ENTRYPOINT

It is a directive or instruction that is used to specify the executable which should run when a container is started from a Docker image. It has two forms, the first one is the ‘exec’ form and the second one is the ‘shell’ form. If there is no entrypoint or CMD specified in the Docker image, it starts and exits at the same time that means container stops automatically so, we must have to specify entrypoint or CMD so that when we will start the container it should execute or it'll stop.

We can override the ENTRYPOINT instruction while starting the container using the ‘–entrypoint’ flag. Also if we have multiple ENTRYPOINT instructions mentioned in Dockerfile then the last ENTRYPOINT will have an effect.

You can run shell scripts using ENTRYPOINT and pass it's output to CMD

```bash
FROM ubuntu
RUN apt-get update && apt-get install -y nginx
ENTRYPOINT ["nginx", "-g", "daemon off;"]
```

Both run during docker container runtime. Using either one of them is best practice but they can be combined too.

37. **Troubleshoot EC2 instance in an ASG that are getting terminated.**

If EC2 quota and pricing is not the issue:

EC2 instances get terminated if they're unhealthy.EC2 instances can become unhealthy if:

- Disk space being full.
- High CPU usage.
- No memory left.

To debug

- Run [[devlog.top]] command to see CPU utilization, check what process/application is using up the resources. Take this up with your developer.
- Disk space EBS volume could be full and and OS might be running out of all disk space.
- Run [[devlog.free]] command to check if any swap memory is left or not, you might want to increase it.

See: [[devlog.create and use swap file on linux]]

38. **How to control of deployment of pods on nodes that are going to be used explicitly for those pods?**

- We can achieve this by using **Taints and Tolerance** in K8's.
- A taint when attached to a node, will ripple pods from getting provisioned or getting accepted.
- We can add a taint to a pod `kubectl taint nodes nodex key=value:Effect`
- Taints are properties of nodes that push pods away if they don't tolerate this taint.
- Like labels, one or more Taints can be applied to a node. The node must not accept any pod that doesn't tolerate all of these taints.

40. **You've 2 different servers with different ports and usernames, how do you use ansible runbook/playbook on both of the servers?**

In our `ansible.conf` we can define different `ansible_user` and `ansible_port` in the hostfile.

```conf
[webservers]
10.4.20.90 ansible_port=4000 ansible_user=roger
39.12.3.23 ansible_port=8001 ansible_user=liam
```

41. **What is Terraform state lock?**

If supported by your backend, [[devlog.Terraform]] will lock your state for all operations that could write state. This prevents others from acquiring the lock and potentially corrupting your state. State locking happens automatically on all operations that could write state.

You won't see any logs of when/as this happens. If state locking fails, Terraform will continue.

You can disable state locking for most commands with the `-lock` flag but it is not recommended. If acquiring the lock is taking longer than expected, Terraform will output a status message. If Terraform doesn't output a message, state locking is still occurring if your backend supports it.

42. **How do you setup slack notifications on Jekins?**

You can leverage Jenkins plugins, you can use the Jenkins - Slack plugin and use Slack webhook URL.
Whenever a pipeline job fails:
`slackSend color: "failure", message: "Pipeline failed, critical."

43. **How do you see your trajectory as a DevOps Engineer?**

There is always something to learn. You could mention some of the tools/technologies that you want to learn - some you want to better understand. Show them that you are someone who is looking to constantly improve himself/herself(themselves).

You'd want to collaborate with your senior engineers to learn from them directly. Maybe you want to take up more responsibility in the organization etc.

44. **How to ignore a certain part of our ansible playbook that might fail and cause our playbook to exit?**

We can achieve this using `ignore_errors` sub arguments.

```yaml
- name: Do not count this as a failure
  ansible.builtin.command: /bin/false
    ignore_errors: yes
```

45. **When making a change to existing code what is a `git` best practice?**

Git clone the repo, checkout the respective branch. Make your change and commit your changes. To understand the motivation behind the change and the history, you can use `git blame`.

The git blame command is used to examine the contents of a file line by line and see when each line was last modified and who the author of the modifications was. Basically gives you the history and the author of the file.

46. **At a high level, create an shell script to automatically push certain logs to S3 at a particular time.**

This is a Whiteboard design question.

- Firstly, we'd make sure what we're using, IAM role or access keys.

```bash
#!/bin/bash

# assign path-to-logs to a variable

# use aws CLI commands to copy files to S3

# aws s3 cp <path-to-logs> <s3-bucket>

# use cron job to execute the script at a particular time
```

47. **What is a package in Python?**

The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file. It is an executable file.To organize modules we have **Packages** in Python.

Modules can have other modules inside them.

Package(1) -> Modules(x) -> Fns(x)

Example module:

```py
#the os module provides an operating system interface from Python
import os
#prints the name of the operating system
print(os.name)
#prints the absolute path for the module
print(os.getcwd())
```

48. **What are your day to day responsibilities as a DevOps engineer?**

Paint a brief picture of what your day to day work looks like.

- A DevOps engineer works in collaboration other engineers(devs, testers, SRE, sales).
- 9:00 AM -> 10:00 AM check Slack, update [[devlog.Jira]] with your tasks.
- 10:00 AM -> 10:30 AM daily standup, share progress with your team on the work you've done previous day and what you'll do today.
- 10:30 AM -> 1:00 PM work on your Jira ticket.
- 1:00 PM -> 2:00 PM lunch.
- 2:00 PM -> 4:00 PM pair program with other engineers or meetings, design discussions.
- 4:00 PM -> 5:00 PM learning new stuff that can benefit the org, share knowledge with other team members.

## Credits

- [50 DevOps Interview Questions & Answers - 2022 | Udemy](https://www.udemy.com/course/50-devops-interview-questions-answers/)
