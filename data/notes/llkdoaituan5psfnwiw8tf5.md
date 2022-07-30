
- Related: [[devlog.boto]], [[devlog.AWS EKS]]

---

**Premise**

We want to get our EKS Cluster info like:

- Cluster Status
- Which [[devlog.Kubernetes]] version?
- Cluster Endpoint

```py
import boto3

client = boto3.client('eks', region_name="eu-west-3")
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']

    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster endpoint: {cluster_endpoint}")
    print(f"Cluster version: {cluster_version}")
```
