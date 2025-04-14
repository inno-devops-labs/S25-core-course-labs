# Infrastructure Docker

## Terraform State Commands

### List Resources
```bash
$ terraform state list
docker_container.nginx
docker_image.nginx
```

### Container Details
```bash
$ terraform state show docker_container.nginx
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
    hostname                                    = "a976bbe76cba"
    id                                          = "a976bbe76cbad7961d5f2a60cc4a90006012c88f46efac678b795cd2ef99e67b"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
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

### Image Details
```bash
$ terraform state show docker_image.nginx
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}
```

### Output Values
```bash
$ terraform output
container_id = "a976bbe76cbad7961d5f2a60cc4a90006012c88f46efac678b795cd2ef99e67b"
image_id = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx"
```


# Terraform Implementation with Yandex Cloud

This guide documents the process of implementing infrastructure in Yandex Cloud using Terraform, including step-by-step commands and their outputs.

## Initial Configuration

### Provider Setup
```hcl
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
      version = "0.136.0"
    }
  }
}

locals {
    folder_id = "<folder-id>"
    cloud_id = "<cloud-id>"
}

provider "yandex" {
  cloud_id = local.cloud_id
  folder_id = local.folder_id
  service_account_key_file = "authorized_key.json"
}
```

### Network Configuration
```hcl
resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet-1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}
```

### VM Configuration
```hcl
resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"
  zone = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd85u0rct32prepgjlv0"  # Ubuntu 22.04 LTS
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:<your-ssh-public-key>"
  }
}
```

## Implementation Steps

### 1. Initialize Terraform

Run the initialization command:
```bash
terraform init
```

Output:
```
Initializing provider plugins...
- Finding yandex-cloud/yandex versions matching "0.136.0"...
- Installing yandex-cloud/yandex v0.136.0...
- Installed yandex-cloud/yandex v0.136.0 (self-signed, key ID E40F590B50BB8E40)
```

### 2. Validate Configuration

Check configuration validity:
```bash
terraform validate
```

Success output:
```
Success! The configuration is valid.
```

### 3. Plan Infrastructure

Review planned changes:
```bash
terraform plan
```

Sample output:
```
Terraform will perform the following actions:

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  ...
```

### 4. Apply Configuration

Create the infrastructure:
```bash
terraform apply
```

Success output:
```
yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Creation complete after 1s [id=enp72d7huclt6nrkrfgr]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bf407b2t49mosq3bqq]
```

### 5. Verify Resources

Check created resources:
```bash
terraform show
```

Resource details:
```
# Network Configuration
Network ID: enp72d7huclt6nrkrfgr
Subnet ID: e9bf407b2t49mosq3bqq

# VM Configuration
Instance ID: fhm7f5sv2oirvrdvjl5i
Public IP: 51.250.12.215
Status: running
Zone: ru-central1-a
```

## Resource Specifications

### Network Details
- VPC network name: network-1
- Subnet CIDR: 192.168.10.0/24
- Zone: ru-central1-a

### VM Details
- Name: terraform1
- Image: Ubuntu 22.04 LTS
- Resources: 2 vCPUs, 2GB RAM
- Network: NAT enabled for internet access
- Access: SSH key authentication

## Testing Access

Verify the setup using SSH:
```bash
ssh ubuntu@51.250.12.215
```

## Clean Up

To remove all created resources:
```bash
terraform destroy
```

This will remove all resources managed by Terraform in your Yandex Cloud environment.




# Terraform GitHub Infrastructure Documentation

## 1. Security Best Practices

### Secrets Management
- GitHub token is managed via environment variables instead of being hardcoded
- No sensitive data is stored in the Terraform configuration
- Used `GITHUB_TOKEN` environment variable for authentication

### Access Control
- Implemented branch protection rules for the main branch
- Required pull request reviews before merging
- Enforced status checks for all branches

## 2. Code Organization

### File Structure
```
terraform/
├── main.tf        # Main resource definitions
```

### Modular Design
- Used variables for reusable values
- Implemented outputs for important information
- Consolidated configuration in a single file for simplicity

## 3. Version Control

### Provider Versioning
- Explicitly specified provider versions using version constraints
- Used `~>` operator for minor version flexibility while ensuring compatibility

### State Management
- State files should be stored remotely (e.g., in S3, Azure Storage, or GCS)
- State locking should be enabled to prevent concurrent modifications

## 4. Implementation Steps and Results

### Initial Setup
First, we initialized Terraform and installed the GitHub provider:

```bash
m7@m7-computer:~/Рабочий стол/Study/S25-core-course-labs/app_python/terraform/github$ terraform init
Initializing the backend...
Initializing provider plugins...
- Finding integrations/github versions matching "~> 5.0"...
- Installing integrations/github v5.45.0...
- Installed integrations/github v5.45.0 (signed by a HashiCorp partner, key ID 38027F80D7FD5FB2)
```

### Token Configuration
We set up the GitHub token as an environment variable:

```bash
export GITHUB_TOKEN="..."
```

### Repository Import
After setting up the token, we imported the existing repository:

```bash
m7@m7-computer:~/Рабочий стол/Study/S25-core-course-labs/app_python/terraform/github$ terraform import "github_repository.core-course-labs" "S25-core-course-labs"
github_repository.core-course-labs: Importing from ID "S25-core-course-labs"...
github_repository.core-course-labs: Import prepared!
  Prepared github_repository for import
github_repository.core-course-labs: Refreshing state... [id=S25-core-course-labs]

Import successful!
```

### Configuration Application
Applied the Terraform configuration:

```bash
m7@m7-computer:~/Рабочий стол/Study/S25-core-course-labs/app_python/terraform/github$ terraform apply
github_repository.core-course-labs: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_protection.main will be created
  + resource "github_branch_protection" "main" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "R_kgDONx-J3Q"
      + require_conversation_resolution = false
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }

      + required_status_checks {
          + contexts = [
              + "tests",
            ]
          + strict   = true
        }
    }

  # github_repository.core-course-labs will be updated in-place
  ~ resource "github_repository" "core-course-labs" {
      ~ auto_init                   = false -> true
      + description                 = "Core course labs repository containing Moscow Time web application"
      ~ has_issues                  = false -> true
      ~ has_wiki                    = true -> false
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (32 unchanged attributes hidden)
    }

Plan: 1 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  + repository_git_url = "git://github.com/MarketerKA/S25-core-course-labs.git"
  + repository_url     = "https://github.com/MarketerKA/S25-core-course-labs"

Enter a value: yes

github_repository.core-course-labs: Modifying... [id=S25-core-course-labs]
github_repository.core-course-labs: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_protection.main: Creating...
github_branch_protection.main: Creation complete after 3s [id=BPR_kwDONx-J3c4Dih6A]

Apply complete! Resources: 1 added, 1 changed, 0 destroyed.

Outputs:
repository_git_url = "git://github.com/MarketerKA/S25-core-course-labs.git"
repository_url = "https://github.com/MarketerKA/S25-core-course-labs"
```


## 5. Best Practices for Maintenance

1. Regular Updates:
   - Keep provider versions updated
   - Review and update branch protection rules as needed
   - Regularly validate repository settings

2. Documentation:
   - Maintain updated README
   - Document any custom configurations
   - Keep track of changes in CHANGELOG

3. State Management:
   - Regularly backup Terraform state
   - Use state locking for collaborative environments
   - Implement remote state storage

4. Testing:
   - Test configuration changes in a development environment
   - Validate changes with `terraform plan` before applying
   - Review output changes carefully