---
id: ervusa6qabwyx7sbb1a4vcg
title: AWS EKS
desc: ""
updated: 1656319791634
created: 1655885960862
---

Elastic Kubernetes Service

It is an alternative to [[devlog.AWS ECS]].

EKS is a service that provides and manages a [[devlog.Kubernetes]] control plane on its own. You have no access to the master nodes on EKS since they’re under a special AWS account.

To run a Kubernetes workload, EKS establishes the control plane and Kubernetes API in your managed AWS infrastructure and you’re good to go.

At this point, you can deploy workloads using native K8s tools like kubectl, Kubernetes Dashboard, Helm, and Terraform.

- You **don’t have to install, operate, and maintain** your Kubernetes control plane.
- EKS allows you to **easily run tooling and plugins** developed by the Kubernetes open-source community.
- EKS **automates load distribution and parallel processing** better than any DevOps engineer could.
- Your Kubernetes assets integrate seamlessly with AWS services if you use EKS.
- EKS uses VPC networking.
- Any application running on EKS is compatible with one running in your existing Kubernetes environment. You can migrate to EKS without applying any changes to the code.
- Supports **EC2 spot instances** using managed node groups that follow spot best practices and allow some pretty great cost savings.

## Managing a Kubernetes cluster

Setting up a cluster in EKS is relatively complicated and comes with some prerequisites. You need to set up and use the AWS CLI and aws-iam-authenticator, and set up IAM permissions and users which adds to your workload.

EKS doesn’t create worker nodes automatically, so you’re also in charge of managing that process. You also need to make extra effort to set up EKS with CloudFormation or Terraform.

- EKS comes with a **well-defined way of upgrading the control plane with minimized disruption**. You can then update worker nodes using the newer Kubernetes AMI, create a new worker group, and finally migrate your workload to the new nodes.
- **Scaling up the cluster is simple** and based on adding more worker nodes. The control plane is fully managed, so there’s no need to worry about adding or upgrading master node sizes when your cluster grows.
- **Carrying out the most common maintenance tasks** is easy in EKS – you can add worker nodes, replace them, terminate instances, and upgrade your setup with minimal disruption to your cluster.

Via - [AWS EKS vs. ECS vs. Fargate vs. Kops: Where to Manage Your Kubernetes in 2022? - CAST AI – Kubernetes Automation Platform](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes/)

## How does EKS work?

You create a EKS cluster which represents a control plane. These will be master nodes.

When you create an EKS service/cluster AWS will provision Kubernetes master nodes that already have Kubernetes master services installed on them.

Since they're managed by AWS EKS, it'll automatically replicate the master nodes across multiple Availability Zones.

Etcd is part of the master nodes which store the whole configuration/the current state of Kubernetes cluster. This storage is also replicated/backed up by AWS.

For Worker Nodes:

You'll create [[devlog.AWS EC2]] instances, so called "Compute Fleet" of multiple virtual servers and connect them to EKS.

Worker nodes have Kubernetes process running on it so the Kubernetes master node can communicate with them.

In this case also, you need to manage the EC2 instance for your worker nodes, yourself.

You have the option of "semi-managed" EC2 instances for your cluster. EKS with Nodegroup. The Nodegroup will handle some of the heavy lifting for you. Basically make it easier for you to configure new worker nodes for your cluster.
For example: Worker nodes managed by nodegroup will get all the processes necessary installed on them(like container runtime, K8s processes) transform them into Worker Nodes.

It is a good practice to use Nodegroups.

You still need to configure things like [[devlog.AWS ASG]]. Even this can be delegated to AWS you can again combine [[devlog.AWS Fargate]] for your EKS cluster.

Fully managed worker nodes with Fargate and Fully managed control plane(master nodes) with EKS.

You can also use EC2 and Fargate in the same EKS cluster.

## Setting up EKS Cluster

- Master nodes
  - Provision an EKS cluster
- Worker nodes
  - Create Nodegroup of EC2 instances(compute fleet)
  - OR you can use Fargate
- Connect Nodegroup with EKS cluster
- Connect to cluster using `kubectl`
  - Deploy your containerized applications

## Creating EKS Cluster via Management Console

**Overview/steps**

1. Create [[devlog.AWS IAM]] Role for EKS service

Role is created so the EKS service(attached) has the permissions/policies to create things in AWS account. To allow AWS to create and manage components on our behalf/on our account.

2. Create a VPC

This is where our worker nodes will run. 

A new VPC is created because EKS cluster needs specific networking configuration for it to work properly. It needs [[devlog.kubernetes]] and AWS specific networking rules, worker node specific firewall configuration. It is necessary for master nodes to communicate with them and manage them.

Default VPC is not optimized for EKS cluster(not the best practice).

Examples of rules:

Firewall rules (of subnets) that are configured by Network ACLs, inside the subnet you’ve EC2 instances. EC2 instances have their own firewall rules that are defined by security groups.

It is a best practice to create/configure subnets in worker node VPC, i.e creating **public** subnets and **private** subnets(creating external load balancer). 

Through IAM Role you give Kubernetes permissions  to change VPC configuration(Nodeport service; to open ports on our behalf in our VPC etc).

You can use templates provided by AWS instead of creating the VPC by ourselves.

3. Create EKS Cluster (Control Plane)

These will be a set of master nodes that are managed by AWS.

4. Connect to the cluster using `kubectl`

To connect to this cluster from our local machine.

5. Create IAM Role for EC2 service

To give EC2 service the permissions to call AWS API and configure, create stuff in our AWS account. Essentially to create worker nodes for the EKS cluster.

6. Create Node Group, attach it to EKS cluster

Node Group is a group of EC2 instances that are gonna run as worker nodes in the EKS cluster(master nodes).

7. Configure Auto Scaling

This is created so that the number of EC2 instances are intelligently scaled up/down to match resource requirement.

8. Deploy an application to EKS cluster

---

**Lab**

1. Create IAM Role

![](https://res.cloudinary.com/zubayr/image/upload/v1656319924/wiki/y1xcw9jn85hmsnyy6ckw.png)

![](https://res.cloudinary.com/zubayr/image/upload/v1656319963/wiki/uier1mhwdqxdkzrkugc3.png)

![](https://res.cloudinary.com/zubayr/image/upload/v1656320002/wiki/vrof1roeuovsnm9xbzef.png)

Policy is automatically selected.

![](https://res.cloudinary.com/zubayr/image/upload/v1656320059/wiki/otyhdlqylbuzgrry5jj8.png)

2. Create a [[devlog.AWS VPC]]

Using [[devlog.AWS CloudFormation]] template for creating VPC. You’ll create the entire stack(whatever components your VPC needs) from the CF template.

Docs - [Creating a VPC for your Amazon EKS cluster - Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/creating-a-vpc.html)