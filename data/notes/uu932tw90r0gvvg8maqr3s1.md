
- AWS Identity and Access Management (IAM), is a service that allows AWS customers to manage user access and permissions for their accounts, and available APIs/services within AWS. IAM can manage users, security credentials (such as API access keys), and allow users to access AWS resources.
- You can create users and groups and set permissions on both of them to either allow or deny access to AWS resources via use of policies.
- IAM is free and included in every AWS account.
- 2 main features of IAM are Users and Roles.

IAM components are **Global**, they are not created in a particular region but are specified for a whole account.

### IAM Users

- Once you create an AWS account you're given Root user access, this is the main account you log into your AWS resources with. It has unlimited privileges.
- With Root user you can create an IAM user, another name for a username and password that can log into your AWS account, but you decide who gets access to what.
- With IAM you can create specific policies to define what a user can access, you can also add users to a group, to which policies can be applied making it easier.
- You can create a group that has access to your development servers and then add all the developers to that group.
- In addition to human users, you can also have system users on AWS. For example, you can have [[devlog.jenkins]] that deploys [[devlog.Docker]] container on [[devlog.AWS EC2]] instance or [[devlog.Jenkins]] that pushes Docker images to AWS Docker Repo called [[devlog.AWS ECR]].
- It is a good practice to assign permissions/policies to a group and then add the user to the group.

### IAM Policy Example: Admin User

IAM has both, a visual editor and a JSON editor.

Example of Admin policy in JSON editor:

```json
{
  "Version": "2012-01-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

### IAM Roles

- They allow you to delegate access to a user or a service, roles differ from users in a way that not only users can assume a role but also services can assume a role as well.
- Basically delegating AWS Services to other AWS Services.
- Its an extra layer of security above just the usual username, password and firewalls.
- Example of a role: a website can assume a role that has access to your Database.
- Roles can also allow other users from different AWS accounts to use a resource in your AWS account.

### IAM Users VS IAM Roles

- Users are assigned to human users or system users.
- Policies cannot be assigned to AWS Services directly. Instead, you can assign a role to a service and then assign a policy to that role.
- There are roles for each service. Roles have permissions/policy attached to it.
- Whenever you create a role:
  - Assign that role to an AWS Service.
  - Attach policies to that role.
