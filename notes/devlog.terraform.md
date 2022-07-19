---
id: mkwoo3ek4y6bnddpy1iteb9
title: Terraform
desc: ""
updated: 1658154000010
created: 1653430082985
---

Terraform is an open source infrastructure as code ([[devlog.IaC]]) software tool that allows DevOps engineers to programmatically provision the physical resources an application requires to run. To create and configure infrastructure . NOT for installing stuff on the server, just for provisioning.

It is a universal [[devlog.IaC]] tool, works with different cloud providers and technologies.

![[devlog.IaC]]

It uses declarative syntax(as opposed to imperative syntax) to define what the end result looks like and it will figure out how to provision the infrastructure.

- It is also helps in automating the infrastructure as it changes over time.
- To replicate the same infrastructure in different environments(Dev, Staging, Production)

Using Terraform, your infrastructure is idempotent. You don't need to remember the current state, you only define your desired state. Since, you use declarative syntax, you don't define the steps like you would if you were using imperative syntax.

## [[devlog.ansible]] VS Terraform

- Terraform is mainly an infrastructure provisioning tool.
- Ansible is mainly used for configuring infrastructure.
- Its a common practice to combine both to get the best of both.

## Terraform Architecture

It has 2 components:

### Core

- Takes 2 input sources
  - Terraform Config
  - State(current state of the infrastructure)
- Core takes the input from the config and state and compares what needs to be changed and what is already there as per the config and state.
- It essentially **creates the execution plan** that the providers use.

### Providers

- This can be providers for the specifc technology(AWS, GCP, Azure, OpenStack, other [[devlog.IaaS]])
- It can also has providers for higher level technologies([[devlog.kubernetes]], other [[devlog.PaaS]] or even [[devlog.SaaS]])
- It has over 100 providers and over 1000 resources.

## Example config files

![](https://res.cloudinary.com/zubayr/image/upload/v1655346903/wiki/lazrvzt8omhhkplp3xwt.png)

![](https://res.cloudinary.com/zubayr/image/upload/v1655346973/wiki/tcxkbpv4dyrx9yjtnufu.png)

We only define a few attributes in the configuration file, the rest or defaults are handled by terraform. Auto-generated.

## Terraform commands for different stages

- `refresh` - query infra provider to get current state.
- `plan` - create an execution plan, just preview no real changes.
- `apply` - executes the plan(it does all the above steps, like refresh and plan and then apply).
- `destroy` - destroys the resources/infrastructure in the right order, does cleaning up of the resources. Reverting. It works similar to `apply`, it checks the state and makes a plan for what needs to be done.

## Providers

- They're basically a piece of code that knows how to talk to a specific technology. To connect to it and start using. Interact.
- Expose resources for specific technology(AWS, GCP, Azure, OpenStack, other [[devlog.IaaS]])
- Responsible for understanding API of that platform.
- [Browse Providers | Terraform Registry](https://registry.terraform.io/browse/providers)
- Providers don't come with installation of terraform, they need to be installed separately.
- Once provider is installed using the `terraform init` command, the complete API of that provider is available.
- You get 2 components from the Providers
  - Resources
  - Data Sources

## Resources

- You can use the `resource` keyword in your `.tf` file using the resource's name.
- The name of a resource follows the convention of `<provider>_<resource>`.
- You can assign the resource to a variable by providing a variable name right after the resource name.
- Each resource block describes one or more infrastructure objects. As referred to as "attributes" or "parameters".
- When you're creating a resource for another resource that doesn't yet exist, you can reference the object.

## Data Sources

- Allows data to be fetched for use in the `.tf` files.
- Query existing resources/components.
- It follows the same convention as the resource names.

## Terraform Commands

- `terraform init` - initialize the working directory. Installs the providers defined in the config file.
- `terraform apply` - apply the changes using the configuration file in the working directory.
- `terraform apply -auto-approve` - to skip the approve prompt.
- `terraform destroy` - if `-target` is not specified, it'll destroy all of the resources defined in the configuration file.

## Examples

### Creating an EC2 instance with Terraform

```json
provider "aws" {
  region = "us-east-1"
  access_key = "AKIAJX7X7X7X7X7X7X7X"
  secret_key = "secret"
  // don't hard code the above values use Environment variables
}

resource "aws_vpc" "test_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "test-subnet-1" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = "10.0.10.0/24"
  availability_zone = "us-east-1a"
}

// if you wanted to create a subnet for an existing vpc, you could hard code the ID of your vpc OR use data sources

data "aws_vpc" "existing_vpc" {
  //  use filter or attributes to filter through of your existing vpc/resource
  default = true
}

resource "aws_subnet" "test-subnet-2" {
  vpc_id = data.existing_vpc.id
  cidr_block = "172.31.48.0/20"
  availability_zone = "us-east-1a"
```

### Changing resources

Adding names using `tags:` keyword and using the reserved `Name` attribute for defining a name.
To remove something, you'd simply remove it from the config file.

```json
provider "aws" {
  region = "us-east-1"
  access_key = "AKIAJX7X7X7X7X7X7X7X"
  secret_key = "secret"
  // don't hard code the above values
}

resource "aws_vpc" "test_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name: "development-vpc",
    vpc_env: "dev"
  }
}

resource "aws_subnet" "test-subnet-1" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = "10.0.10.0/24"
  availability_zone = "us-east-1a"
    tags = {
    Name: "development-subnet"
  }
}

// if you wanted to create a subnet for an existing vpc, you could hard code the ID of your vpc OR use data sources

data "aws_vpc" "existing_vpc" {
  //  use filter or attributes to filter through of your existing vpc/resource
  default = true
}

resource "aws_subnet" "test-subnet-2" {
  vpc_id = data.existing_vpc.id
  cidr_block = "172.31.48.0/20"
  availability_zone = "us-east-1a"
```

### Removing/Destroying resources

1. Remove the resource from Terraform config file and `terraform apply`. (Recommended)
2. `terraform destroy -target resource_type.resource_name`

## State

`terraform.tfstate` - it is a `json` file where Terraform stores the state of your managed infrastructure. It generates this file on your first `terraform apply`.

`terraform.tfstate.backup` is the file that is created to store the backup of the previous state.

Neither of these files should be updated manually and must be updated as a result of executing `terraform` commands.

Terraform has commands to access the information in the state file.

- `terraform state` - list all subcommands of `state`.
- `terraform state list` - list all resources in the state.
- `terraform state mv` - move an item in the state.
- `terraform state show` - show a resource in the state. Useful for checking the values of the attributes that were autogenerated by Terraform.

## Output

We can define what value we want Terraform to spit at the end of applying of the configuration from the resources. Output values are like function's return values.

```json
output "dev-vpc-id" {
  value = aws_vpc.development_vpc.id
}

output "dev-subnet-id" {
  value = aws_subnet.dev-subnet-1.id
}
```

## Variables

You use variables inside of the configuration file. variables = input variables. If you don't want to hard code values you can pass them as parameters. Define and reference it. Input variables are like function arguments. They're defined using `variable` keyword. Makes it easier to replicate, parameterize, and reuse the same configuration over different environments. You'd have different `.tfvars` files for different environments.

```json
variable "subnet_cidr_block" {
  description = "CIDR block for the subnet"
  default = "10.0.30.0/24"
  type = string
}

resource "aws_vpc" "development_vpc" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = var.subnet_cidr_block
  availability_zone = "us-east-1a"
  tags: {
    Name: "subnet-1-dev"
  }
}
```

There are three ways to pass values to input variables.

1. Prompt when `terraform apply` is run.
2. Define the value when running apply command
   - `terraform apply -var "subnet_cidr_block=10.0.30.0/24`
3. Use a `.tfvars` to pass the values from a file. (Recommended)
   - `terraform.tfvars` - this is a file that contains the (keys)values for the variables. (If you don't pass a file name, it'll look for this file)
   - Use the `-var-file` flag to pass the file name.
     - `terraform apply -var-file terraform-dev.tfvars`

### Default values

Default value will kick in if terraform cannot find the value in the `.tfvars` file or as a command line argument. A default value makes the variable optional.

### Type constraints

`type` specifies what value types the variable can accept.

Using `list`:

```json
variable "cidr_blocks" {
  description = "CIDR blocks list"
  type = list(string)
}

resource "aws_subnut" "dev-subnet-1" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = var.cidr_blocks[1]
  availability_zone = "us-east-1a"
  tags: {
    Name: "subnet-1-dev"
  }
}
```

You can also use objects or lists of objects. You can also validate the type of the value for the objects as well.

```json
// terraform-dev.tfvars

cidr_blocks = [
  {cidr_block = "10.0.10.0/16", name = "dev_vpc"},
  {cidr_block = "10.0.20.0/24, name = "dev_subnet"}
]
```

```json
variable "cidr_blocks" {
  description = "CIDR blocks list and Name tag"
  type = list(object({
    cidr_block: string
    name: string
  }))
}

resource "aws_vpc" "test_vpc" {
  cidr_block = var.cidr_blocks[0].cidr_block
  tags = {
    Name: var.cidr_blocks[0].name
  }
}
```

## Environment Variables

Environment variables are defined by the providers for you to use.

1. Use `export` to set the environment variable, it will be available only for the current shell session.

   `export AWS_SECRET_ACCESS_KEY=<secret_access_key>`
   `export AWS_ACCESS_KEY_ID=<access_key_id>`

2. Set the environment variable in the `~/.aws/credentials` to be available globally, you may also use `aws configure` to set the credentials.

### TF Environment Variable

Define your own custom variables and use `.tf_var` to pass them to the Terraform configuration as global environment variables.

- Define the variable - `export TF_VAR_my_custom_variable="my_custom_value"`
- To use it, reference it without the `TF_VAR_` prefix.

```json
variable "my_custom_variable" {}

resource "aws_subnut" "dev-subnet-1" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = var.cidr_blocks[1]
  availability_zone = var.my_custom_variable
  tags: {
    Name: "subnet-1-dev"
  }
}
```

![[devlog.terraform aws]]

## Provisioners

Provisioners can be used to model specific actions on the local machine running the Terraform Core or on a remote machine to prepare servers or other infrastructure objects. But HashiCorp states in its documentation that they should be used as the last solution!

### Null resource

From the Terraform docs:

The null provider is a rather-unusual provider that has constructs that intentionally do nothing. This may sound strange, and indeed these constructs do not need to be used in most cases, but they can be useful in various situations to help orchestrate tricky behavior or work around limitations.

The documentation of each feature of this provider, accessible via the navigation, gives examples of situations where these constructs may prove useful.

Usage of the null provider can make a Terraform configuration harder to understand. While it can be useful in certain cases, it should be applied with care and other solutions preferred when available.

The Terraform null_resourceis commonly used to run scripts on a specified trigger.

### Connection attribute

`remote-exec` provisioners require connection credentials to function, even though `remote-exec` might be defined in a resource block that is a server, it doesn't connect to it unless explicity defined.

### `remote-exec` provisioner

This provisioner invokes a script on the newly created resource. it’s similar to connecting to the resource and running a bash or a command in the terminal.

It can be used inside the Terraform resource object and in that case it will be invoked once the resource is created, or it can be used inside a null resource which is my prefered approche as it separates this non terraform behavior from the real terraform behavior.

- Invokes script on a remote resource after it is created
  - `inline` - list of commands
  - `script` - path to script

```terraform
resource "null_resource" "configure-vm" {

  connection {
      type = "ssh"
      user = var.username
      host = var.ip_address
      private_key = var.tls_private_key
    }

  ## Copy files to VM :
  provisioner "file" {
    source = "/Users/zakariaelbazi/Documents/GitHub/zackk8s/kubernetes" #TODO move to variables.
    destination = "/home/${var.username}"
  }

  ## install & start minikube
  provisioner "remote-exec" {
    inline = [
      "sudo chmod +x /home/${var.username}/kubernetes/install_minikube.sh",
      "sh /home/${var.username}/kubernetes/install_minikube.sh",
      "./minikube start --driver=docker"
    ]
  }
}
```

> Note that you can not pass any arguments to the script or command, so the best way is to use file provisioner to copy the files to the resources and then invoke them with the remote-exec provisioner like I did above for my script that installs minikube on the azure-vm.

> An other thing to pay attention to is that by default, provisioners that fail will also cause the Terraform apply to fail. To avoid that, the on_failure can be used.

```terraform
resource "null_resource" "configure-vm" {
    .........
    ..........

  provisioner "remote-exec" {
    inline = [
      "sudo chmod +x /home/${var.username}/kubernetes/install_minikube.sh",
      "sh /home/${var.username}/kubernetes/install_minikube.sh",
      "./minikube start --driver=docker"
    ]
    on_failure = continue #or fail

  }
}
```

In this example, I am using inline which is a series of command, the on_failure will apply only to the final command in the list !

### `local-exec` provisioner

Technically, this one is very similar to the one before in terms of behavior or use but it works in the local machine ruining Terraform. It invokes a script or a command on local once the resource it’s declared in is created.

It’s the only provisioner that doesn’t need any ssh or winrm connection details as it runs locally.

## Resources

- [What is terraform provisioner? | Jhooq](https://jhooq.com/terraform-provisioner/)
- [All you need to know about Terraform provisioners and why you should avoid them. | AWS Tip](https://awstip.com/all-you-need-to-know-about-terraform-provisioners-and-why-you-should-avoid-them-22b5ef8d2db2)
- [Terraform Tutorial: Drift Detection Strategies](https://www.trendmicro.com/ru_ru/devops/22/c/terraform-tutorial-drift-detection-strategies.html)
