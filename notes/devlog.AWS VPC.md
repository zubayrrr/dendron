---
id: 3ozxwzvy9lv8t60yjvx45e9
title: AWS VPC
desc: ""
updated: 1656335026421
created: 1656159335261
---

A VPC is a logically isolated portion of the AWS cloud within a region where you can deploy your resources inside it.

[[devlog.AWS S3]] is an example of service that sits outside of a VPC.

Within a region there are availability zones, you can use those availability zone by creating subnets and assigning subnets to those availability zones. A subnet is always assigned to one availability zone. It cannot span over multiple AZs. You can multiple subnets within same AZs.

We can deploy resources such as [[devlog.AWS EC2]] in a subnet. There is such a thing called **VPC Router**. We can interact with it by configuring **route tables**. The VPC Router takes care of routing within the VPC and outside of VPC.

To be able to access the internet, you also need an **Internet Gateway**. It is attached to your VPC. You only get one per VPC. It is used to send data out to the internet and in from the internet.

We configure the route table with the Internet Gateway ID that tells it to send all the traffic that doesn't fit for one the networks in the route table to the internet gateway.

You’ve a default VPC that AWS automatically creates for you in every region.

You can create multiple VPCs within a region(5 by default, soft limit).

Each VPC has a [[devlog.CIDR]] block, overall block of address from which you then create the addresses you assign to the subnets.
