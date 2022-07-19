---
id: gbeh61d6hvbmxxy63chp81b
title: Kubernetes
desc: ""
updated: 1657954267111
created: 1653409437988
---

Kubernetes is an open-source system for automating deployment, scaling, and management of [[containerized applications|devlog.containers & images]] in different environments; [[devlog.cloud]], [[devlog.VM]]s or physical environments. It is a container orchestration tool. Developed by Google.

To understand what Kubernetes is good for, let's look at some examples:

- You would like to run a certain application in a container on multiple different locations. Sure, if it's 2-3 servers/locations, you can do it by yourself but it can be challenging to scale it up to additional multiple location.
- Performing updates and changes across hundreds of containers
- Handle cases where the current load requires to scale up (or down)
- If you are big team of engineers (e.g. 200) deploying applications using containers and you need to manage scaling, rolling out updates, etc. You probably want to use Kubernetes
- The rise of [[devlog.microservices]] caused increased usage of container technologies.
- Application nowadays comprise of multiple; hundreds to thousands of containers. Managing them using custom scripts can be a pain.
- Container orchestration offers:
  - High availability or no downtime.
  - Scalability or high performance.
  - Disaster recovery - backup, restore, etc.

## What Kubernetes objects/components are there?

- Pod(s)
- Service
- ReplicationController
- ReplicaSet
- DaemonSet
- Namespace
- ConfigMap

can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

### Pods

> A pod is a collection of containers sharing a network, acting as the basic unit of deployment in [[devlog.Kubernetes]]. All containers in a pod are scheduled on the same node.

An abstraction over a container - a pod creates a layer on top of a container. Usually, only one application is running per pod. You don't directly create pods. You create deployments.

Kubernetes offers a virtual network out of the box. Each pod gets its own IP Address. Which they can use to communicate with each other. It is an internal [[devlog.IP Address]].

They're ephemeral, meaning they are not persistent, they can die if the application crashes or if you run out of resources. A new one will automatically be created with new IP Address. To help with this, Kubernetes Service is used.

### Service and Ingress

- Static IP Address that can be attached to each pod. Life cycle of a service and a pod are not connected. Even if the pod dies, the service will still be there.
- To make the application accessible through a browser, an external service needs to be created that opens communication from external sources. For a database, you'd have an internal service.
- It also acts as a load balancer. It will catch a request and forward it to the node that is least busy.
- **Ingress** is another component of Kubernetes that forwards request to the service. It makes URL more suitable for the end user.

### ConfigMap and Secret

- **ConfigMap** acts as an external configuration file. It is a way to store configuration data that is not in the code. Like a database URL that a pod utilizes.
- To store username and password, **Secret** is used. It is not stored in plain text, it is base64 encoded. (This does not mean encryption)

### Volumes

- Volumes are used to persistently store data(logs, databases, etc.).
- It basically attaches a physical storage - a hard drive or a network drive(local or remote) - to a pod.
- K8s explicitly doesn't manage persistent data.

### Deployment and StatefulSet

- To reduce down time - to make it fault tolerance - you can replicate everything(a node). That is connected to the same service.
- This replication of the pod isn't done manually. Instead you'd define a blueprint and tell it how many replicas you want it to run. This is called **Deployment**.
- It is a abstraction over pods.
- Deployment is used to create StateLess applications.
- In practice, you'd be working with deployments not with pods.
- You cannot replicate databases with Deployment, since databases have states and it can be prone to inconsistencies if deployments are used to replicate them.
- **StatefulSet** are used to replicate databases or to create stateful applications. It also take care of scaling them up or down. It makes sure database reads and writes are synchronized.
- Deploying StatefulSet applications can be tedious on K8s. It is a common practice to host database applications outside K8s and only have StateLess applications inside K8s cluster.

## Kubernetes Architecture

### Worker Machines/Nodes

- Each node has multiple pods running on it.
- There are 3 process that must be installed on each node that used to schedule and manage the pods.
- Nodes are the cluster service that actually do that work.

1. Container runtime
   - [[devlog.Docker]]
   - [[devlog.cri-o]]
   - [[devlog.conatinerd]] (Most popular)
2. Kubelet - is the process that actually schedules the pods and the containers underneath. It is the process of Kubernetes that has interfaces with both container runtime and the node(machine) itself. It assigns the resources etc.
3. Kube Proxy - is the process that forwards the traffic from services to the pods. It has intelligent forwarding logic inside that makes sure the communication works in a performant way with low network overhead.

### Master Node

All the managing processes are taken care by the Master node inside the K8s cluster. There are 4 processes that are installed on the master node. Completely different process from Worker Nodes that control the cluster state and the Worker Nodes.

1. API Server - if you want to deploy a new application on a K8s cluster, you will interact with this using a client such as Kubernetes dashboard, a CLI tool like Kubelet. It is like a cluster gateway. It receives the initial request(changes) needed to made on the cluster or queries from the cluster and also takes care of authorization.
2. Scheduler - intelligently decides which Worker Node the next component will run on. It estimates the resources required for your request and schedules a new pod is to be scheduled.
3. Controller manager - when pods die on a node, it detects state changes and tries to recover the cluster state. It makes the request to the scheduler to restore those dead pods. Scheduler does its thing.
4. etcd - Key value store that stores the cluster state. It is the brain of the cluster. Every change inside the cluster is saved in this key value store. etcd is how the scheduler gets its info from. The actual application's data is NOT stored on etcd.

A K8s cluster is made up of multiple master nodes. Each master node runs its own processes. API Server is load balanced and etcd store does a distributed storage across all master nodes. They don't take a lot of resources compared to the worker nodes as their job is just delegating work.

## Minikube

Minikube is a tool that lets you run Kubernetes locally. Minikube runs a single-node Kubernetes cluster on your personal computer so that you can try out Kubernetes, or for daily development work.

It is a one node cluster, master and worker process run on one node. It comes with docker preinstalled. It runs via VM or a hypervisor.

## kubectl

Kubectl is the Kubernetes command line tool that allows you to run commands against Kubernetes clusters. For example, you can use it to create, delete, list, and inspect Kubernetes objects. It is basically a client for the Kubernetes API Server.

- Get all components

`kubectl get all`
`kubectl get all | grep`

- Get status of nodes

`kubectl get nodes`

- Get status of pods

`kubectl get pods`

- Get status of services

`kubectl get services`

- Create components

`kubectl create`

- Create deployment

`kubectl create deployment nginx-depl --image=nginx` (most basic blueprint, rest are defaults)

- Get deployments

`kubectl get deployment`

- Replicaset - managing replicas of a pod

`kubectl get replicaset`

- Edit deployment

`kubectl edit deployment nginx-depl` (will get auto-generated config file with default values)

### Debugging pods

`kubectl logs pod-name`

- Get additional information about a pod

`kubectl describe pod pod-name`

- Get the terminal of the application(pod)

`kubectl exec -it pod-name -- bin/bash`

- Delete deployment

`kubectl delete deployment deployment-name`

### Kubernetes deployment configuration file

If a deployment does not exist, it will be created. If it exists, it will be updated.

`kubectl apply -f deployment.yaml`
`kubectl apply -f config-file-nginx.yaml`

It is used for creating and configuring K8s clusters. There are 3 parts to it:

1. Metadata
2. Specification
   - Attributes are specific to the `kind`
3. Status (auto-generated and added by kubernetes)
   - Kubernetes will compare the desired with the actual state and if the desired state ≠ actual state, K8 will try to fix it.

![](https://res.cloudinary.com/zubayr/image/upload/v1655117494/wiki/ipq3mbgswsrb0ufg7hrt.png)

![](https://res.cloudinary.com/zubayr/image/upload/v1655117667/wiki/fakkxkxbdvspydlfnd4f.png)

- The status is constantly updated, it gets it’s data from `etcd`.
- The format of the configuration file is [[devlog.YAML]].
- The code is stored along with the source code of your application or it can have it's own repository.
- The configuration file is structured in a "template" or a "blueprint" way.
- The connection is made using "selectors" and "labels".
- Pods get the label through the template blueprint.
- This label is matched by the selector.
- To get the configuration of a running deployment, use `kubectl get deployment deployment-name -o yaml`
  - You'll find a lot of information will be auto-generated by Kubernetes.
- To copy a deployment you already have, you'll have to remove auto-generated stuff and clean the configuration file before creating a deployment from it.
- You can use the configuration file to delete a deployment. `kubectl delete -f deployment.yaml`

### Creating a Secret

![](https://res.cloudinary.com/zubayr/image/upload/v1655127535/wiki/ag8cc3fib3l5qtkvwasf.png)

When you store values, don’t use plain text, encode them in base64. For example: `echo -n "somevalue" | base64`

`kubectl apply -f secrets.yaml`

Secret once created can be referenced in your deployment configuration files.

Example of secret being referenced:

![](https://res.cloudinary.com/zubayr/image/upload/v1655127895/wiki/lmddjxbristzwqipuuy3.png)

### Creating a Service

Deployment and Service can be put in a single file. You don’t define a type unlike an External Service where type is defined because Internal Service or ClusterIP(it gives an internal IP Address) is the default.

Example of a Service configuration

![](https://res.cloudinary.com/zubayr/image/upload/v1655128136/wiki/vepvw9yubv8izozijvjo.png)

Reapply the `deployment.yaml` and the newly added Service will also be created.

![](https://res.cloudinary.com/zubayr/image/upload/v1655128207/wiki/ljbcr1cfavkzz0lsbjd1.png)

To validate if the Service is attached to the correct Pod, you can run `kubectl describe service service-name` and cross check `endpoints` IP Address with the Pod’s `kubectl get pod -o wide`.

### Creating ConfigMap

![](https://res.cloudinary.com/zubayr/image/upload/v1655128682/wiki/mow4k1vejxaungybxje8.png)

ConfigMap must already be created in the K8s cluster before referencing it.

`kubectl apply -f configmap.yaml`

Referencing ConfigMap

![](https://res.cloudinary.com/zubayr/image/upload/v1655128847/wiki/odygjn3izkrd8gotfhlq.png)

### Creating an External Service

It is very similar to a typical Service. Internal service also acts like a load balancer but an External Service acts like loan balancer by accepting external request by assigning the service an external [[devlog.IP Address]].

![](https://res.cloudinary.com/zubayr/image/upload/v1655129162/wiki/gpts0wcs1wrdij7txbfc.png)

## Namespaces

Namespaces are a way to organize clusters into virtual sub-clusters — they can be helpful when different teams or projects share a Kubernetes cluster. Any number of namespaces are supported within a cluster, each logically separated from others but with the ability to communicate with each other. Namespaces cannot be nested within each other.

Any resource that exists within Kubernetes exists either in the default namespace or a namespace that is created by the cluster operator. Only nodes and persistent storage volumes exist outside of the namespace; these low-level resources are always visible to every namespace in the cluster.

When you create a cluster by default K8s gives you 4 namespaces out of the box.

To list namepsaces - `kubectl get namepsace`

The Kubernetes-dashboard namespace is shipped automatically in minikube(it is specific to minikube installation).

1. `kube-system`

It is not meant for your use, you shouldn't modify it. The components that are deployed on `kube-system` are system processes. They're from master and managing processes or kubectl.

2. `kube-public`

It has publicly accessible data. A configmap which contains cluster information(accessible even without authentication).

Run `kubectl cluster-info` to get this information.

3. `kube-node-lease`

It holds information about the heartbeats of nodes. Each node has associated lease object in namespace which contains information about that node's availability.

4 `default`

This is the namespace that is referenced by default for every Kubernetes command, and where every Kubernetes resource is located by default. Until new namespaces are created, the entire cluster resides in ‘default’.

### Create your own namespace

Run `kubectl create namespace <name-of-namespace>`

OR

Use namespace configuration file to create a namespace(recommended because you can integrate version control).

![](https://res.cloudinary.com/zubayr/image/upload/v1656236351/wiki/vahcacuyv9fjezvza8e4.png)

### When yo use namespace

To avoid your default namespace to get filled with different components that you might use. It can get difficult to manage as you’d have no overview of your resources.

Resources can be ground using namespaces. A way of logically grouping your resources inside the cluster.

For example:

- A namespace for your DBses and required resources.
- A namespace for monitoring, where you can deploy [[devlog.Prometheus]] and all the stuff it needs.
- A namespace for [[devlog.elastic stack]], where the [[devlog.ElasticSearch]], [[devlog.kibana]] resources go.
- A namespace for ngnix-ingress resources.

They should be avoided if the project is not that large or doesn’t have that many users(as per official guide) but you can do it anyway instead of throwing everything in the default namespace.

**Conflicts**

Namespaces are also useful if you’ve multiple teams.
To avoid conflicts such as deploying of the same application in a single namespace and having it overwritten by the other teams. You can use namespaces for different projects inside your cluster.

**Resource sharing**

Lets say you’ve one cluster and you want to host both staging and development environment in the same cluster(to utilize common resources without having to redeploy them for different environments).

**Blue/Green deployment**

You can have two different versions of production application that share common resources.

**Limit Access and Resources**

You can limit access and resources to namespaces when working with multiple teams. Minimizing the risk of one team accidentally interfering with the other. Each team will have their own secure, isolated environment.

You can limit the resources each namespace consumes. You can allot each team a share of resources for their applications.

### Characteristics of Namespace

You can’t access most resources from another namespace.

**Each NS must define it’s own configmap**. Eg: You’ll need to create a configmap for your namespace that is referencing a DB, you cannot use other namespace’s configmap. The same applies for secrets(credentials of a shared service).

What you can access from another NS is a **service**.

![](https://res.cloudinary.com/zubayr/image/upload/v1656237672/wiki/ijk9q4etvplakbc2gfc0.png)

Where yellow is namespace and white is the service being referred in a configmap.

**Components that cannot be namespaced**

These components live globally in a cluster, you cannot isolate them in a NS.
Eg: Persistent Volumes, Nodes.

List resources that are not bound to namespace

`kubectl api-resources --namespaced=false`

List resources that are bound to namespace

`kubectl api-resources --namespaced=true`

### Create resource in a namespace

Run `kubectl apply -f mysql-configmap.yaml --namespace=my-namespace`

OR include the destination namespace in the configmap itself

![](https://res.cloudinary.com/zubayr/image/upload/v1656238019/wiki/jwpagppds4pc1qjvsa2p.png)

### Get component created in a specific NS

`kubectl get configmap -n my-namespace`

Because by default **it’ll only the default namespace** if you don’t specify.

### Change active NS

Switch the default NS to your choice of NS

`kubectl` doesn’t have an solution for this but `kubens` does!

Install `kubectx` which will install `kubens` as well.

`kubens` ran without options will return all the NSes and highlights active NS.

`kubens my-namespace` will switch the active NS to `my-namespace`

## etcd

## Taints

## Sidecar containers

- https://www.magalix.com/blog/the-sidecar-pattern

## Resources

- [Kube by Example Homepage](https://kubebyexample.com/)
- [Concepts | Kubernetes](https://kubernetes.io/docs/concepts/_print/)
- [An Ultimate Kubernetes Hands-on Labs and Tutorials | kubelabs](https://collabnix.github.io/kubelabs/)
