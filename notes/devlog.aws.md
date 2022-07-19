---
id: gvpkbgglehtr9ej5e0uj44j
title: AWS
desc: ''
updated: 1655034100357
created: 1653569035047
---

AWS is an [[devlog.IaaS]]. AWS stands for Amazon Web Services, A cloud services platform. Collection of different computer programs/services Amazon offers to build applications and websites.

AWS also refers to the IT company(subsidiary of Amazon) that created these services.

## Overview

![[devlog.cloud]]

### A brief history of AWS

- It all started with the idea of "[[Infrastructure as a service|devlog.IaaS]]".
- AWS was first released in 2006.
- S3 was first first service that was released.

### 10,000 Foot overview (of important AWS services)

- Compute relates to running applications or processing things with computer power, including, virtual servers and serverless computing.
- Storage relates to services like [[devlog.AWS S3]] that is used to store and retrieve data.
- Databases relates to [[devlog.AWS RDS]], [[devlog.AWS DynamoDB]] etc.
- Migration & Transfer relates to services that help you migrate your databases from non-AWS platforms(traditional servers) to AWS and also help you sync your data.
- Networking & Content Delivery refers to VPC. virtual private cloud, where all the services exist, there are also content delivery services such as CloudFront and DNS services like Route 53.
- Developer Tools relates to all the tools that were made to make developer's life easier in writing software and host it on AWS, from writing code, to building and deploying to servers.
- Robotics relates to the AWS RoboMaker service that helps with robotics application development.
- Customer Enablement services include Support from AWS themselves.
- Blockchain services for all your cryptocurrency and blockchain needs.
- Satellite services include Ground Station.
- Quantum Technologies relates to Amazon Braket that provides development environment for quantum applications and algorithms.
- Management & Governance services helps you manage AWS, on premises infrastructure.
- Media Services relates to all the services related to media, trans-coding audio, video etc.
- Machine Learning services offers a wide range of applications from automatic code quality check to image recognition, automatic language translation and automatic car-driving.
- Analytics relates to processing of large data, petabytes of data.
- Security, Identity & Compliance offers services that help with authentication, storing passwords, automatic detection of network breaches, noncompliance with predefined security policies and firewalls.
- Front-end Web & Mobile services which help in making websites and mobile applications.
- AR & VR relates to Amazon Sumerian, a service for creating, running 3D AR and VR applications.
- Applications Integrations which helps AWS services work together such as SQS.
- Cost Management, services that help you manage your budgets and costs in AWS.
- Customer Engagement helps you manage and engage with your customers.
- Business Applications has services such as Chime, Amazon's video conferencing software, Alexa for business etc.
- End User Computing offers services for users such as WorkSpaces which provides a virtual desktop that can be accessed from anywhere in the world.
- IOT services to help you build and manage IOT devices.
- Game Development relates to Amazon GameLift for hosting games.
- Container services that help you package code and all its dependencies in one unit that can be run reliably any computing environment.

### Regions & Availability zones

- AWS has regions, physical locations around the world where they put their data centers which have the servers that host their services.
- Currently AWS has regions in North America, South America, Europe, the Middle East, Africa and the Asia Pacific.
- Inside regions we've availability zones, each region has isolated and multiple availability zones in geographic area, they all have their own power, security and they're all connected to each other via redundant, ultra high speed, and low latency networks.
- Availability zone names are randomly generated for each AWS user, example: what could be ap-southeast-2a for you will be something else for another user, like ap-southeast-2c, this is done to ensure people utilize all of their availability zones.
- This is also done for redundancy, so that if a problem occurs at one data center, you will not be effected by it. To avoid a single point of failure. Its unlikely all of their availability zones will be hit by power cut or other such infrastructure issues.

## Security and Identity

- One of the most important things to keep in mind when building cloud applications is that your data and infrastructure is protected all times and any threats against them are being protected.
- Coming to Identity, you've to make sure that those who do have access to your infrastructure can only access what they need to access.
- AWS has various ways to implement Security & Identity, which can be used in different ways to do different things.

### Data protection:

- A service to discover and protect your sensitive data is Amazon Macie.
- A service to store and manage encryption keys is AWS Key Management.
- A service for hardware-based key storage and regulatory compliance is AWS CloudHSM.
- A service to provision, manage and deploy SSL and TLS security certificates, is AWS Certificate Manager.
- A service to store and retrieve secrets like passwords is [[devlog.AWS Secrets Manager]].

### Infrastructure protection:

- [[devlog.AWS IAM]] - Identity and Access Management is a way to manage who can access what throughout your AWS resources and services in your account.
- A service for denial of service protection is AWS Shield.

- A service to filter malicious website traffic is AWS Web Application Firewall or WAF.

- A service to centrally manage firewall rules is AWS Firewall Manager.

### Threat Detection:

- A service that automatically detects threats is Amazon Guard Duty.
- A service to analyze application security is Amazon Inspector.
- A service to record and evaluate configurations of AWS resources is AWS Config.
- A service to track user activity and API usage in your AWS account is AWS Cloudtrail.

### Identity Management:

- A service to securely manage access to your AWS account services and resources is AWS Identity and Access Management or [[devlog.AWS IAM]].
- A service to implement cloud single sign-on is AWS Single Sign-on.
- A service to manage identity inside your applications that you've made such as users logging in is Amazon Cognito.
- A service to implement and manage Microsoft Active Directory is AWS Directory Service.
- A service to centrally govern and manage multiple AWS accounts in one place is AWS Organizations.

---

- [[devlog.Amazon VPC]] - Virtual Private Cloud is a way to organize your AWS resources into virtual private networks.
  - Subnets, Network ACL.
  - [Control traffic to subnets using Network ACLs - Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [[devlog.CIDR Blocks]] - CIDR blocks are used to define the (a range) IP addresses that are allowed to access your AWS resources.
  - [Subnet Calculator - CIDR - IP ADDRESS CALCULATOR - MxToolbox](https://mxtoolbox.com/subnetcalculator.aspx)
- Security group
- Firewall rules
- Subnets

---

## Compute

- AWS describe their own compute capability as compute for any workload, instances, containers and serverless computing.
- Compute refers to using a computer to processing something, from adding numbers to hosting multi availability zone multi-region fault tolerant version of any kind of applications.
- This is where the processing happens.

### Computing services AWS offers:

- Instances
  - [[devlog.AWS EC2]] or Elastic Compute Cloud refers to instances or virtual machines, a service that provides secure and resizeable virtual machines in the cloud.
  - A service that helps you run fault tolerant workloads for up to 90% of the time for the normal price of EC2 is Amazon EC2 Spot.
  - A service which can automatically add or remove computing capacity to meet your changes in computing demand is called Amazon EC2 Auto Scaling.
  - A service that provides an easy to use cloud platform to build an application or website is called Amazon LightSail.
- [[devlog.containers & images]]
  - A service to run reliable, secure and scalable containers is Amazon Elastic Container or [[devlog.AWS ECS]].
  - A service to store manage and deploy container images is Amazon Elastic Registry or [[devlog.AWS ECR]].
  - A full managed [[devlog.Kubernetes]] service is Amazon Elastic Kubernetes Service or [[devlog.AWS EKS]].
- Serverless
  - A service that lets you run code without servers is AWS Lambda.
- Edge
  - A service called AWS Outposts lets you run your AWS services on your own servers instead of Amazon's.
  * A service that lets you bring a lot of data into AWS is called the AWS Snow Family. Devices that you can order to put files into that will be shipped back to Amazon and loaded into your AWS account.
  * A service which lets you access AWS services from 5G devices without having to go via the internet is AWS Wavelength.
  * A service that assists in migrating your VMware workloads to AWS is called VMware Cloud on AWS.
  * A service that lets you run latency sensitive applications closer to end users is called AWS Local Zones.
