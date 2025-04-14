# Lab 4: Infrastructure as Code

## Task 1: Docker Infrastructure Using Terraform

### Steps
1. Installed Terraform and set up the workspace.
2. Created a Docker container using Terraform.
3. Used input variables to rename the Docker container.
4. Applied the configuration and captured the outputs.

### Terraform Commands
```bash
terraform init
terraform apply -var "container_name=myapp"
```

#### Output of `terraform apply`
<details>
<summary>Click to expand</summary>

```
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
      + name = "tutorial"
      + restart = "no"
      + ports {
          + external = 8080
          + internal = 80
          + ip = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + name = "nginx:latest"
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:
container_id = "46477bd3f0e05058dfd0b07a36f6f0d00d3f0e47791a14bac66928e9e56b13ef"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
```
</details>

---

## Task 2: AWS Infrastructure Using Terraform

### Steps
1. Set up AWS credentials using environment variables.
2. Created an EC2 instance using Terraform.
3. Applied the configuration and captured the outputs.

### Terraform Commands
```bash
terraform init
terraform apply
```

#### Output of `terraform apply`
<details>
<summary>Click to expand</summary>

```
Terraform will perform the following actions:

 terraform apply 

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.app_server will be created
  + resource "aws_instance" "app_server" {
      + ami                                  = "ami-0058f736afded77b3"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + iam_instance_profile                 = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + source_dest_check                    = true
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "ExampleAppServerInstance"
        }
      + tags_all                             = {
          + "Name" = "ExampleAppServerInstance"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification (known after apply)

      + cpu_options (known after apply)

      + ebs_block_device (known after apply)

      + enclave_options (known after apply)

      + ephemeral_block_device (known after apply)

      + maintenance_options (known after apply)

      + metadata_options (known after apply)

      + network_interface (known after apply)

      + private_dns_name_options (known after apply)

      + root_block_device (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_instance.app_server: Creating...
aws_instance.app_server: Still creating... [10s elapsed]
aws_instance.app_server: Creation complete after 16s [id=i-0aef8aba8b3efdc1c]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```
</details>

### Debugging AWS Issues
#### Steps to Resolve AWS Credential Errors
1. **Verify AWS CLI Configuration**
   ```bash
   aws sts get-caller-identity
   ```
2. **Set AWS Credentials as Environment Variables**
   ```bash
   export AWS_ACCESS_KEY_ID="your_access_key_id"
   export AWS_SECRET_ACCESS_KEY="your_secret_access_key"
   ```
3. **Update AWS CLI Credentials File**
   ```bash
   nano ~/.aws/credentials
   ```
   Add the following:
   ```ini
   [default]
   aws_access_key_id = your_access_key_id
   aws_secret_access_key = your_secret_access_key
   ```
4. **Find AMI ID for EC2 Instance**
   ```bash
   aws ec2 describe-images --owners amazon --filters "Name=name,Values=*ubuntu*" --region us-west-2
   ```

---

## Task 3: GitHub Repository Management Using Terraform

### Steps
1. Created a GitHub repository using Terraform.
2. Configured repository settings (name, description, visibility, etc.).
3. Applied the configuration and captured the outputs.

### Terraform Commands
```bash
terraform init
terraform apply
```

#### Output of `terraform apply`
<details>
<summary>Click to expand</summary>

```
 terraform apply 
var.github_token
  GitHub Personal Access Token


github_repository.core-course-labs: Refreshing state... [id=core-course-labs]
github_branch_protection.main: Refreshing state... [id=BPR_kwDON1OQxs4DikJb]

Changes to Outputs:
  + branch_protection_id = "BPR_kwDON1OQxs4DikJb"
  + repository_id        = "core-course-labs"
  + repository_url       = "https://github.com/YehiaSobeh/core-course-labs"

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes


Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

branch_protection_id = "BPR_kwDON1OQxs4DikJb"
repository_id = "core-course-labs"
repository_url = "https://github.com/YehiaSobeh/core-course-labs"
```
</details>

---

## Bonus Task: GitHub Teams Using Terraform

### Steps
1. Created a GitHub organization.
2. Defined teams (admins, maintainers, contributors) with varying permissions.
3. Assigned teams to the repository:
   - **Admins**: Admin (full access)
   - **Maintainers**: Push (write access)
   - **Contributors**: Pull (read-only access)
4. Applied the configuration and captured the outputs.

### Terraform Commands
```bash
terraform init
terraform apply
```

#### Output of `terraform apply`
<details>
<summary>Click to expand</summary>

```
 terraform apply 
github_team.contributors: Refreshing state... [id=12130965]
github_team.maintainers: Refreshing state... [id=12130964]
github_team.admins: Refreshing state... [id=12130963]
github_repository.core-course-labs: Refreshing state... [id=core-course-labs]
github_team_repository.contributors_access: Refreshing state... [id=12130965:core-course-labs]
github_team_repository.maintainers_access: Refreshing state... [id=12130964:core-course-labs]
github_team_repository.admins_access: Refreshing state... [id=12130963:core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # github_repository.core-course-labs will be updated in-place
  ~ resource "github_repository" "core-course-labs" {
        id                          = "core-course-labs"
        name                        = "core-course-labs"
      - vulnerability_alerts        = true -> null
        # (32 unchanged attributes hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  + admins_team_id       = "12130963"
  + contributors_team_id = "12130965"
  + maintainers_team_id  = "12130964"
  + repository_id        = "core-course-labs"
  + repository_url       = "https://github.com/DevOps-2025-lab4/core-course-labs"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.core-course-labs: Modifying... [id=core-course-labs]
github_repository.core-course-labs: Modifications complete after 3s [id=core-course-labs]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

admins_team_id = "12130963"
contributors_team_id = "12130965"
maintainers_team_id = "12130964"
repository_id = "core-course-labs"
repository_url = "https://github.com/DevOps-2025-lab4/core-course-labs"
```
</details>

---

## Best Practices Applied
- **Version Control**: Pinned provider versions using `required_providers`.
- **Secrets Management**: Stored sensitive data (e.g., tokens) in environment variables.
- **Modularity**: Organized configurations into separate folders for Docker, AWS, and GitHub.
- **State Management**: Used remote state storage (e.g., S3 + DynamoDB) for team collaboration.
- **Documentation**: Documented all steps and outputs in `TF.md`.

## Challenges Faced
- **Docker**: Ensuring the container name was dynamically configurable using input variables.
- **AWS**: Finding the correct AMI ID for the desired region.
- **GitHub**: Importing an existing repository into Terraform state.
- **GitHub Teams**: Ensuring the repository was under an organization to use team resources.

