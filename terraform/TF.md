
# Terraform

## Table of Contents

- [Terraform](#terraform)
  - [Table of Contents](#table-of-contents)
  - [Docker](#docker)
    - [Building the infrastructure](#building-the-infrastructure)
    - [List of states](#list-of-states)
    - [Outputs](#outputs)
  - [AWS](#aws)
  - [Github](#github)
  - [Github Team](#github-team)
  - [Best Practices](#best-practices)

## Docker

### Building the infrastructure

```bash
terraform init
terraform fmt
terraform validate
terraform apply
```

`terraform apply`
<details>
<summary>output</summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-docker-container % terraform apply
docker_image.app_python: Refreshing state... [id=sha256:d8a0b68df6bb582874c17b2e62fdbb907d8a46d8b4bc86122c831ce5cfc2d73balihamdan/app_python:latest]
docker_container.app_python: Refreshing state... [id=56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python must be replaced
-/+ resource "docker_container" "app_python" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "gunicorn",
          - "app_python.app:app",
          - "--workers",
          - "4",
          - "--worker-class",
          - "uvicorn.workers.UvicornWorker",
          - "--bind",
          - "0.0.0.0:8000",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "56f585e2bf4a" -> (known after apply)
      ~ id                                          = "56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "python-app"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                                = "bridge" -> null # forces replacement
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "app_user" -> null
      - working_dir                                 = "/app" -> null
        # (18 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ python-container-id    = "56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_python: Destroying... [id=56f585e2bf4a9df7ee88a2cc4fd6870dd260c08417a7d56fe124e048f195dbf7]
docker_container.app_python: Destruction complete after 0s
docker_container.app_python: Creating...
docker_container.app_python: Creation complete after 1s [id=17e08d444351a21d75a33c22d22f15b321f6d2dc127ee56f0ab23b0cb15eb522]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

python-container-id = "17e08d444351a21d75a33c22d22f15b321f6d2dc127ee56f0ab23b0cb15eb522"
python-container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])

```
</details>

### List of states

`terraform state list`

<details>
<summary>output<code></code></summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-docker-container % terraform state list

docker_container.nginx
docker_image.nginx
```

</details>

`terraform state show`

<details>
<summary>output</summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-docker-container % terraform state show docker_container.nginx
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "2898c4f389ae"
    id                                          = "2898c4f389ae0a2db5f1f8e30be500873e755e044e3614ef11f4ae923bf76763"
    image                                       = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

</details>

## AWS

- Before I could use AWS resources, I needed to have my IAM credentials set up. So I modified the ~/.aws/credentials and wrote the following in it

```
[default]
aws_access_key_id =
aws_secret_access_key = 
aws_session_token = <your-session-token>
```

`terraform apply`

<details>
<summary>output</summary>

```cmd
`
alihamdan@Alis-MacBook-Air-2 learn-terraform-aws % terraform apply       

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.my-terraform-server will be created
  + resource "aws_instance" "my-terraform-server" {
      + ami                                  = "ami-08d70e59c07c61a3a"
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
          + "Name" = "my-terraform-server"
        }
      + tags_all                             = {
          + "Name" = "my-terraform-server"
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

Changes to Outputs:
  + aws-public-ip = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes
aws_instance.my-terraform-server: Creating...
aws_instance.my-terraform-server: Still creating... [10s elapsed]
aws_instance.my-terraform-server: Creation complete after 17s [id=i-05bdca30f4803342f]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

aws-public-ip = "34.213.60.57"

```
</details>


### Outputs

`terraform output`
<details>
<summary>output</summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-aws % terraform output
python-container-id = "17e08d444351a21d75a33c22d22f15b321f6d2dc127ee56f0ab23b0cb15eb522"
python-container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

---
## Github

`terraform import`

<details>
<summary>output</summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-github % terraform import "github_repository.repo" "S25-core-course-labs"            
var.github_token
  GitHub personal access token

  Enter a value: 

github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

```

</details>

`terraform apply`

<details>
<summary>output</summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-github % terraform apply                                                             
var.github_token
  GitHub personal access token

  Enter a value: 

github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "master"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
      + description                 = "My-test-repo"
      + gitignore_template          = "Python"
      - has_downloads               = true -> null
      - has_projects                = true -> null
      ~ has_wiki                    = true -> false
        id                          = "S25-core-course-labs"
      + license_template            = "mit"
        name                        = "S25-core-course-labs"
        # (28 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 1s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDONx8ruM4Dimz4]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

Outputs:

repo_url = "https://github.com/Ali12hamdan/S25-core-course-labs"
alihamdan@Alis-MacBook-Air-2 learn-terraform-github %
```

</details>

`terraform output`
<details>
<summary>output</summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-github % terraform output
repo_url = "https://github.com/Ali12hamdan/S25-core-course-labs"
```

</details>

## Github Team

`terraform apply`

<details>
<summary>output</summary>

```cmd
alihamdan@Alis-MacBook-Air-2 learn-terraform-github-teams % terraform apply
var.github_token
  GitHub personal access token

  Enter a value: 


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_repository.test will be created
  + resource "github_repository" "test" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + branches                    = (known after apply)
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "This is testing"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "test-repo"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

  # github_team.QA will be created
  + resource "github_team" "QA" {
      + create_default_maintainer = false
      + description               = "This team is responsible for QA"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "QA"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_members.QA will be created
  + resource "github_team_members" "QA" {
      + etag    = (known after apply)
      + id      = (known after apply)
      + team_id = (known after apply)

      + members {
          + role     = "member"
          + username = "Ali12hamdan"
        }
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.QA: Creating...
github_repository.test: Creating...
github_team.QA: Creation complete after 10s [id=12130990]
github_team_members.QA: Creating...
github_repository.test: Still creating... [10s elapsed]
github_repository.test: Creation complete after 12s [id=test-repo]
github_team_members.QA: Creation complete after 2s [id=12130990]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
alihamdan@Alis-MacBook-Air-2 learn-terraform-github-teams %
```

</details>

## Best Practices

- The files were named based on the resources or their tasks. `main.tf` contained version and providers. `variable.tf` and `outputs.tf` contained the variables and outputs respectively. The other files were named based on the resources they were creating or managing.
- Naming convention followed [terraform-best-practices](https://www.terraform-best-practices.com/naming).
- The secrets are not hardcoded and used as environment variables.
- `terraform fmt` and `terraform validate` were used to format and validate the code.
- `terraform plan` was always used to verify the changes before applying them. Also, `terraform state list` and `terraform state show` were used before destroying any resource.
- For existing resources, `terraform import` was used to import the resources to the state file.
- Specifying Terraform and provider versions to avoid unexpected updates.