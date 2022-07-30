
Prometheus is a monitoring tool. It collects metrics and stores it with which we can make dashboards and alerts.

It was created to monitor highly dynamic container environments like [[devlog.kubernetes]], [[devlog.docker swarm]] etc. It can also be used in traditional non-container infrastructure.

Typically you've many servers that run containerized applications, hundreds of different processes running on that infrastructure which are all interconnected. To get insights on this infrastructure such as errors, latency etc.

To make it easier for us to debug these system and fix them without much downtime, we'll use something like Prometheus, that will constantly monitor all the services/resources, alerts the maintainers as soon as anything goes wrong. **In fact it can identify problems before they even occur** and notify the maintainers so the failures can be prevented.

# Prometheus Architecture

## Prometheus Server

This is what does the actual monitoring.

It constitutes of three components:

- Time Series DB - stores metrics data, no. of exceptions.
- Data Retrieval Worker - responsible for pulling metrics from applications/services/servers - target resources and pushing them to the Time series DB.
- HTTP Server - Accepts PromQL queries for that stored data. Web server API is used to display data in a dashboard or UI - either Prometheus UI or Grafana etc.

## Targets and Metrics

What does Prometheus monitor?

It can be an entire [[devlog.Linux]] server, Windows server, a standalone [[devlog.apache]] server, single application or service. These are called as **Targets**.

Each target has unit of monitoring:

- For a Linux server it could be current CPU usage, memory usage, disk space usage.
- For an application - No. of exceptions, requests, request duration.

A unit that you'd want to monitor for a target is called a **Metric**.
They're what gets stored in Prometheus DB component. Prometheus defines human readable, text based format for the metrics. Metric entries or data has `TYPE` and `HELP` attributes to increase it's readability.

`HELP` is basically description of the metric.
`TYPE` is one of three metric types:

- `Counter`
  - For how many times x happened
- `Gauge`
  - For a metric that can go up and down. Eg: Current value of x now?
- `Histogram`
  - For tracking how long something took or how big something was(like the size of a request).

## Getting metrics

How does Prometheus collect metrics from the targets?

**Pulling**

Your application(regardless of technology) will have to expose a metrics HTTP endpoint and Prometheus will scrape from the endpoint. By default is is: `hostaddress/metrics`.

Data available in the `/metrics` endpoint should be in the correct format that Prometheus understands.

Some servers expose Prometheus endpoints by default so you don't really have to do extra work for it. But many services don't have native Prometheus endpoints in which case you'd need an **Exporter**

**Exporter**

It basically a script/service that fetches metrics from your target and converts them in format Prometheus understands and exposes it's converted data at it's own `/metrics` endpoint where Prometheus can scrape them.

Prometheus has a list of exporters for different services like [[devlog.MySQL]], [[devlog.Elasticsearch]], [[devlog.Linux]] servers, [[Build Tools|devlog.build automation]], Cloud Platforms and so on.

If you want to monitor a Linux server, see: [Monitoring Linux host metrics with the Node Exporter | Prometheus](https://prometheus.io/docs/guides/node-exporter/)

![](https://res.cloudinary.com/zubayr/image/upload/v1656150261/wiki/xfe8c37gmzogdoin3wtx.png)

Exporters are also available as Docker images. SO

If you want to monitor [[devlog.mysql]] container in a [[devlog.kubernetes]] cluster, you can deploy  a sidecar container of MySQL exporter that will run inside the pod with MySQL container, connect to it and start sending MySQL metrics for Prometheus and making them available at it’s own `/metrics` endpoint.

**Monitoring  your own applications?**

- How many requests your applications are receiving.
- How many exceptions are occurring.
- How many server resources your application is using.

 For this you can use Client Libraries for different languages using which you can expose `/metrics` endpoint for metrics that are relevant to you.
[Client libraries | Prometheus](https://prometheus.io/docs/instrumenting/clientlibs/)


## Push based VS Pull based

Most monitoring systems like [[devlog.AWS CloudWatch]] or [[devlog.New Relic]] etc use a Push system. Applications and servers are responsible for pushing their metric data to a centralized collection platform of that monitoring tool.

In large microservices based system this approach can create a bottleneck for your infrastructure as all of these microservices constantly make push request to your monitoring tool thus flooding your system.

Plus, you’ll also need to install additional software(daemons) on each of your targets to push the metrics to the monitoring server. In contrast with Prometheus which only requires a scraping endpoint.

Multiple Prometheus instances can collect/pull metrics. Using pull, Prometheus can easily detect whether a service is up and running or not.

Pushing can be ambiguous when checking if the service is up or not when compared to pull mechanism. Because there can be many reasons for a push request to fail. 

**Pushing**

Pushgateway can be utilized when a target only runs for a short time.
Eg: A batch job, scheduled job etc. For such jobs, Prometheus offers Pushgateway component. So these services can push metrics directly to Prometheus DB.

![](https://res.cloudinary.com/zubayr/image/upload/v1655885235/wiki/yguspabejdgcr4qbzegm.png)

## Configuring Prometheus 

`prometheus.yaml` file contains all the info needed for Prometheus to know what(targets) to scrape and when(intervals). 

Prometheus then uses **Service Discovery**  mechanism to find those target endpoints.

You can find the sample config files with default values which comes with your first Prometheus installation.

![](https://res.cloudinary.com/zubayr/image/upload/v1656153062/wiki/p2l9ubydx8h1viv4pafn.png)

Under `global:` you define how often Prometheus will scrape it’s targets.

Rules are for aggregating metric values or creating alerts when conditions 
are met.

`scrape_configs:` define what resources Prometheus monitors; essentially targets. You can define your own jobs and default values for each job(overwrite global interval values).

Since Prometheus has it’s own `/metrics` endpoint, it can monitor it’s own health.

## AlertManager

How does Prometheus trigger alerts that are defined by rules in `prometheus.yaml` and who receives these alerts?

Prometheus has a component called AlertManger that is responsible for firing alerts via different channels (Emails, Slack channel or other notification clients).

Prometheus server will read alert rules and if the conditions under rules is met an alert is fired. 

## Prometheus Data Storage 

Where does Prometheus store all the data that it collects/aggregates? How can other systems use this data?

Prometheus stores metric data on disks, includes Local on disk **Time Series DB** but also optionally integrates with remote storage system. It is stored in custom Time Series format. Because of this you cannot directly write this data on a relational DB or something else.

Once collected, Prometheus lets you query the data through it’s server API using it’s query language called **PromQL**.

## PromQL

You can use Prometheus dashboard UI to ask Prometheus server via PromQL to for example show the status of a target right now.

Or use more powerful data visualization tools like **Grafana** to display the data which uses PromQL under the hood to get data out of Prometheus .

Example PromQL query to:

Query all HTTP status codes except `4xx` ones

```sql
http_requests_total{status!~"4.."}
```

This query does some subquery:

Returns the 5 minute rate of the _http_requests_total_ metric for the past 30 minutes.

```sql
rate(http_requests_total[5m]) [30m:]
```

![](https://res.cloudinary.com/zubayr/image/upload/v1656153983/wiki/qu5c4x2hrwuozqeqebxy.png)

## Sailent Characteristics of Prometheus 

It is designed to be reliable even when other systems have an outage so you can diagnose the problems and fix them.

Each Prometheus server is standalone and self-contained. It doesn’t depend on network storage or other remote services. It is meant to be still working when other parts of the infrastructure are broken.

It doesn’t require extensive setup needed.

**Drawbacks:**

It can be difficult to scale, when you have hundreds of servers that you want to use multiple Prometheus instances for aggregation of metrics setting them up can get complicated.

A workaround this would be to increase the capacity of your Prometheus server, limit the number of metrics Prometheus collects from applications.

## Prometheus Federation

To scale monitoring with scalable cloud apps.

Prometheus Federation allows one Prometheus server to scrape data from another Prometheus server. This will allow you to scale your Prometheus setup with your multi-node applications.

## Prometheus with Docker & Kubernetes 

It is fully compatible with both.

Prometheus components are available as Docker images and therefore can be deployed on Kubernetes or other container environments.

It provides monitoring of K8s Cluster Node Resource out of the box! Once deployed on K8s, it starts gather metrics data on each Kubernetes node server without any extra configuration.
