---
id: i5wu7j4cvg8tzfyzkawbsjt
title: Ec2 Server Status Check using Boto3
desc: ""
updated: 1658319831089
created: 1658181553134
---

- Related: [[devlog.boto]], [[devlog.AWS EC2]]

---

**Premise**

We have a lot of [[devlog.AWS Ec2]] instances created with [[devlog.Terraform]] with Autoscaling configured. Instances get created and deleted all the time. Since, EC2 instances need some time to initialize, we want to know what is the status of our EC2 instances.

Instances are grouped as "Reservations"

```py
import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")


def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True # by default only returns status for instances in "running" state
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")
    print("#############################\n")


schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()
```
