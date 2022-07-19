---
id: i5wu7j4cvg8tzfyzkawbsjt
title: Ec2 Server Status Check using Boto3
desc: ""
updated: 1658187834349
created: 1658181553134
---

- Related: [[devlog.boto]]

---

**Premise**

We have a lot of [[devlog.AWS Ec2]] instances created with [[devlog.Terraform]] with Autoscaling configured. Instances get created and deleted all the time. Since, EC2 instances need some time to initialize, we want to know what is the status of our EC2 instances.
