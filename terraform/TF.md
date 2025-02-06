# Terraform

## Docker Infrastructure
### Output of "terraform show"

```
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
    hostname                                    = "194b3384c860"
    id                                          = "194b3384c8603e85c96a4bce69cd517d187e272327889134e6c3de170065cc53"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}   
```

### Output of "terraform state list"
```
docker_container.nginx
docker_image.nginx
```

### Applied changes
```
~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
```

### Output of "terraform output"
```
container_id = "f007b9a1db4ec816d03f48bfa19dacade801a7056d57a09526a87b09c493de85"
image_id = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx"
```


## Yandex Cloud Setup

### 1. Prerequisites Installation

#### Installing Yandex Cloud CLI
```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
echo 'source /home/fory/yandex-cloud/completion.zsh.inc' >>  ~/.zshrc
source "/home/fory/.bashrc"
```

#### Installing Terraform
Ensure Terraform is installed (version >= 0.13)

### 2. Authentication Setup

#### Service Account Creation
1. Create a service account in Yandex Cloud Console
2. Generate service account key:
```bash
yc iam key create \
  --service-account-id <service_account_id> \
  --folder-name <folder_name> \
  --output authorized_key.json
```

#### CLI Profile Configuration
```bash
# Create new profile
yc config profile create devops1

# Configure profile
yc config set service-account-key authorized_key.json
yc config set cloud-id <cloud-id>
yc config set folder-id <folder-id>
```

### 3. Terraform Provider Configuration

Create `~/.terraformrc`:
```hcl
provider_installation {
  network_mirror {
    url = "https://terraform-mirror.yandexcloud.net/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

### 4. Infrastructure Configuration

Our infrastructure consists of:
- VPC Network
- Subnet in ru-central1-a
- Boot disk with Ubuntu 20.04 LTS
- VM instance with 2 cores and 2GB RAM

#### Key Components:
```hcl
# Network configuration
- VPC Network: "network1"
- Subnet: "subnet1" (192.168.10.0/24)

# Compute Instance
- Platform: standard-v3
- Zone: ru-central1-a
- Resources: 2 cores, 2GB memory
- Disk: 15GB network-hdd
- OS: Ubuntu 20.04 LTS
```

### 5. Usage Instructions

#### Initialize Terraform
```bash
terraform init
```

#### Plan Changes
```bash
terraform plan
```

#### Apply Configuration
```bash
terraform apply
```

#### Access the VM
```bash
# Get the VM's public IP
terraform output external_ip_address_vm_1

# SSH into the VM
ssh ubuntu@<external_ip_address>
```

#### Destroy Infrastructure
```bash
terraform destroy
```



### 6. Challenges Encountered and Solutions

0. Yandex Cloud Documentation is complete peace of ...
    - Info about every required step I had to find by myself on Youtube, Terraform docs (which is not great also), ask Google and etc.
    - I've spent like 2 days to get everything working.

1. Platform Availability:
   - Initial issue with platform availability in ru-central1-d
   - Solution: Switched to ru-central1-a and standard-v3 platform

2. Authentication:
   - Required proper service account setup
   - Solution: Created dedicated service account with necessary roles

3. Network Configuration:
   - NAT configuration for internet access
   - Solution: Enabled NAT in network interface configuration


## GitHub Infrastructure

### 1. Prerequisites
- Terraform installed (version >= 0.13)
- GitHub account with personal access token
- Token with necessary permissions:
  - repo (full control)
  - admin:org
  - delete_repo

### 2. Authentication Setup
```bash
# Set GitHub token as environment variable
export GITHUB_TOKEN=my_access_token
```
### 3. Infrastructure Configuration

Our GitHub infrastructure consists of:
- Repository configuration
- Branch protection rules
- Security settings

### 4. Usage Instructions

#### Initialize Terraform
```bash
cd terraform/github
terraform init
```

#### Import Existing Repository
```bash
terraform import "github_repository.core-course-labs" "core-course-labs"
```

#### Plan Changes
```bash
terraform plan
```

#### Apply Configuration
```bash
terraform apply
```

### 5. Best Practices Implemented

1. **Security**:
   - Token stored as environment variable
   - Branch protection enabled
   - Required reviews configured
   - Vulnerability alerts enabled

2. **Version Control**:
   - Provider version pinning
   - Clean branch management
   - Protected main branch

3. **Code Quality**:
   - Required status checks
   - Code owner reviews
   - Pull request reviews

4. **Infrastructure as Code**:
   - Declarative configuration
   - Version controlled infrastructure
   - Documented setup and changes

5. **State Management**:
   - Local state for personal projects
   - Import of existing resources
   - Careful state handling