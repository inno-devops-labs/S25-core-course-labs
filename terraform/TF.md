# Terraform infrastructure as code documentation

## Table of contents

1. [Docker infrastructure](#docker-infrastructure)
2. [Yandex Cloud infrastructure](#yandex-cloud-infrastructure)
3. [GitHub infrastructure](#github-infrastructure)
4. [Best practices](#best-practices)

## Docker infrastructure

### Setup and installation

1. Install Terraform
2. Configure Docker provider
3. Build infrastructure

### Implementation details

#### Provider configuration

```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.1"
    }
  }
}

provider "docker" {
  host = "unix:///Users/nikitadrozdov/.orbstack/run/docker.sock"
}
```

#### Resources

1. Docker Image

```hcl
resource "docker_image" "moscow_time" {
  name = var.image_name
  build {
    context = "../../app_python"
    tag     = [var.image_tag]
  }
  keep_locally = false
}
```

2. Docker Container

```hcl
resource "docker_container" "moscow_time" {
  image = docker_image.moscow_time.image_id
  name  = var.container_name
  ports {
    internal = 8000
    external = var.external_port
  }
}
```

#### Variables

```hcl
variable "container_name" {
  description = "The name of the container"
  type        = string
  default     = "moscow-time-app"
}

variable "image_name" {
  description = "The name of the Docker image"
  type        = string
  default     = "moscow-time"
}

variable "image_tag" {
  description = "The tag for the Docker image"
  type        = string
  default     = "moscow-time:latest"
}

variable "external_port" {
  description = "The external port for the container"
  type        = number
  default     = 8000
}
```

### Commands output

#### Terraform init

```bash
Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "3.0.1"...
- Installing kreuzwerker/docker v3.0.1...
- Installed kreuzwerker/docker v3.0.1 (unauthenticated)

Terraform has been successfully initialized!
```

#### Terraform state list

```bash
docker_container.moscow_time
docker_image.moscow_time
```

#### Terraform state show (container)

```hcl
# docker_container.moscow_time:
resource "docker_container" "moscow_time" {
    attach                                      = false
    command                                     = [
        "uvicorn",
        "app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    hostname                                    = "16f25b8c397c"
    id                                          = "16f25b8c397c26dd9d2d14557abbbdc00d9f65ce7f25ecc6b73b4182e0a4889a"
    image                                       = "sha256:bbce1f53c2ede3e58fc2b69abec905ec752ae032f51460087698ea9f9dd757e2"
    name                                        = "moscow-time-app"
    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

#### Terraform output

```bash
container_id = "16f25b8c397c26dd9d2d14557abbbdc00d9f65ce7f25ecc6b73b4182e0a4889a"
image_id = "sha256:bbce1f53c2ede3e58fc2b69abec905ec752ae032f51460087698ea9f9dd757e2moscow-time"
```

### Applied changes log

```bash
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Changes made:
1. Created Docker image 'moscow-time' from app_python context
2. Created Docker container 'moscow-time-app' with port mapping 8000:8000
```

### Verification

```bash
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
16f25b8c397c   bbce1f53c2ed   "uvicorn app:app --h…"   15 seconds ago   Up 14 seconds   0.0.0.0:8000->8000/tcp   moscow-time-app
```

### Variable usage example

#### Renaming container using variables

```bash
$ terraform apply -var="container_name=moscow-time-app-v2"

Terraform will perform the following actions:
  # docker_container.moscow_time will be created
  + resource "docker_container" "moscow_time" {
      + name = "moscow-time-app-v2"
      ...
    }

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:
container_id = "de65874f996ecd43e71230d531dfc4e4b0b5cc64ce74e05217f5633067eb7291"
image_id = "sha256:bbce1f53c2ede3e58fc2b69abec905ec752ae032f51460087698ea9f9dd757e2moscow-time"
```

This demonstrates how to use input variables to modify resource attributes during apply. The container was successfully renamed from 'moscow-time-app' to 'moscow-time-app-v2' using the container_name variable.

## Yandex Cloud infrastructure

### Setup process

1. **SSH key generation**

   ```bash
   ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
   ```

   - Generated 4096-bit RSA key pair
   - Public key saved to `~/.ssh/id_rsa.pub`
   - Private key saved to `~/.ssh/id_rsa`

2. **Terraform configuration**
   - Created directory structure for Yandex Cloud configuration
   - Initialized Terraform with Yandex provider:

     ```bash
     terraform init
     ```

   - Provider version: yandex-cloud/yandex v0.136.0

### Infrastructure components

1. **Network resources**

   ```hcl
   resource "yandex_vpc_network" "network-1" {
     name = "network-1"
   }

   resource "yandex_vpc_subnet" "subnet-1" {
     name           = "subnet-1"
     zone           = "ru-central1-d"
     network_id     = yandex_vpc_network.network-1.id
     v4_cidr_blocks = ["192.168.10.0/24"]
   }
   ```

2. **Compute instances**
   - **VM-1 (terraform1)**:
     - 2 cores
     - 2 GB RAM
     - Ubuntu 20.04 (image_id: fd800c7s2p483i648ifv)
     - Network: Connected to subnet-1 with NAT enabled

   - **VM-2 (terraform2)**:
     - 4 cores
     - 4 GB RAM
     - Ubuntu 20.04 (image_id: fd800c7s2p483i648ifv)
     - Network: Connected to subnet-1 with NAT enabled

3. **User configuration**
   - Created custom user 'nikas' with sudo privileges
   - Configured SSH access using cloud-init

   ```yaml
   #cloud-config
   users:
     - name: nikas
       groups: sudo
       shell: /bin/bash
       sudo: 'ALL=(ALL) NOPASSWD:ALL'
       ssh_authorized_keys:
         - ssh-rsa [YOUR_PUBLIC_KEY]
   ```

### Applied configuration

```bash
# Infrastructure creation
terraform apply
```

**Results**:

- Resources created: 4 (2 VMs, 1 network, 1 subnet)
- Creation time: ~51 seconds
- Network creation: 2 seconds
- Subnet creation: 1 second
- VM creation: 31-51 seconds

### Network configuration

**IP addresses**:

- VM-1:
  - External IP: 84.201.171.46
  - Internal IP: 192.168.10.27
- VM-2:
  - External IP: 84.201.169.31
  - Internal IP: 192.168.10.3

### Validation and formatting

1. **Configuration validation**

   ```bash
   terraform validate
   ```

   - Result: Success! The configuration is valid.

2. **Code formatting**

   ```bash
   terraform fmt
   ```

   - Applied consistent formatting to all Terraform files

### Challenges and Solutions

1. **SSH access configuration**
   - Initial setup used direct SSH key injection
   - Migrated to cloud-init for better user management
   - Solution: Implemented user-data configuration with cloud-init

2. **Provider configuration**
   - Required specific provider version
   - Handled provider lock file generation
   - Note: Lock file includes checksums for darwin_arm64 platform

3. **Resource creation time**
   - Network resources created quickly (2-3 seconds)
   - VM creation took longer (30-50 seconds)
   - Solution: Implemented parallel resource creation where possible

### Best practices implemented

1. **Security**
   - Used SSH key authentication
   - Created custom user with sudo privileges
   - Implemented secure network configuration with NAT

2. **Network design**
   - Isolated network with dedicated subnet
   - NAT enabled for internet access
   - Internal network range: 192.168.10.0/24

3. **Resource management**
   - Consistent naming convention
   - Resource tagging
   - Proper state management

### Terraform state

Current state includes:

- 1 VPC network
- 1 subnet
- 2 compute instances
- All associated networking configurations

### Maintenance and updates

To update the infrastructure:

1. Modify configuration files as needed
2. Run `terraform validate` to check syntax
3. Run `terraform plan` to preview changes
4. Run `terraform apply` to apply changes

To destroy the infrastructure:

```bash
terraform destroy
```

## GitHub infrastructure

### Setup and configuration

1. **Provider setup**

   ```hcl
   terraform {
     required_providers {
       github = {
         source  = "integrations/github"
         version = "~> 5.0"
       }
     }
   }

   provider "github" {
     token = var.github_token
   }
   ```

2. **Authentication**
   - Created GitHub Personal Access Token (PAT)
   - Required scopes: "repo", "read:repo_hook", "read:org", "read:discussion"
   - Token stored as environment variable: `export GITHUB_TOKEN="your-token"`

### Repository configuration

```hcl
resource "github_repository" "core_course_labs" {
  name        = "S25-core-course-labs"
  description = "Core course labs for DevOps training"
  visibility  = "public"

  has_issues    = true
  has_wiki      = true
  has_projects  = true
  has_downloads = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true
}
```

### Branch protection rules

```hcl
resource "github_branch_protection" "master" {
  repository_id = github_repository.core_course_labs.node_id
  pattern       = "master"

  required_status_checks {
    strict = true
    contexts = ["Python CI"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    required_approving_review_count = 1
  }
}
```

### Import process

1. **Import command**

   ```bash
   terraform import "github_repository.core_course_labs" "S25-core-course-labs"
   ```

2. **State verification**

   ```bash
   terraform state show github_repository.core_course_labs
   ```

### Applied best practices

1. **Security**
   - Token stored as environment variable
   - Sensitive variables marked with `sensitive = true`
   - `.gitignore` configured to exclude sensitive files
   - Branch protection rules implemented

2. **Code organization**
   - Separate directory for GitHub configuration
   - Clear resource naming
   - Modular configuration files

3. **Version control**
   - Provider version pinning
   - State file exclusion
   - Documentation maintained

4. **Compliance**
   - Branch protection rules
   - Required status checks
   - Pull request reviews required

### Maintenance

1. **Repository updates**

   ```bash
   terraform plan    # Review changes
   terraform apply   # Apply changes
   ```

2. **State management**
   - Regular state backups
   - State file security
   - Clean state removal when needed

### Challenges and solutions

1. **Token management**
   - Challenge: Secure token storage
   - Solution: Environment variables and sensitive marking

2. **Branch protection**
   - Challenge: Existing branch protection
   - Solution: Import existing rules before modification

3. **State handling**
   - Challenge: Sensitive data in state
   - Solution: Proper .gitignore and state backup procedures

## Best practices

1. **State management**
   - Use remote state storage
   - Implement state locking
   - Keep state files secure

2. **Code organization**
   - Modular structure
   - Clear naming conventions
   - Proper documentation

3. **Security**
   - Use variables for sensitive data
   - Implement least privilege access
   - Regular security audits
