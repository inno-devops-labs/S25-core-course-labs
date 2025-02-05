# Terraform Implementation Report

## Docker Infrastructure (Task 1)

### State Commands Output
The following commands were executed after successful infrastructure deployment at `terraform/docker` directory:

```bash
$ terraform state list
```

```
docker_container.nginx
docker_image.nginx
```

```bash
$ terraform state show docker_container.nginx
```

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
    hostname                                    = "9c0c31ee9af6"
    id                                          = "9c0c31ee9af6fad8ce21d45d880adb1e473f12785295619b673147e321b11b1f"
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

```bash
$ terraform state show docker_image.nginx 
```

```
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}
```

```bash
$ terraform output
```

```
container_id = "9c0c31ee9af6fad8ce21d45d880adb1e473f12785295619b673147e321b11b1f"
```

## Yandex Cloud Infrastructure (Task 1)

### State Commands Output
The following commands were executed after successful infrastructure deployment at `terraform/yandex` directory:

```bash
$ terraform state list
```

```
yandex_vpc_network.network
yandex_vpc_subnet.subnet
```

```bash
$ terraform state show yandex_vpc_network.network
```

```
# yandex_vpc_network.network:
resource "yandex_vpc_network" "network" {
    created_at                = "2025-02-05T16:54:48Z"
    default_security_group_id = "enplsb8ji25oc2t461q8"
    description              = null
    folder_id                = "b1g6b21ruf06jt32tulo"
    id                       = "enpmabv269l6hgsf84id"
    labels                   = {}
    name                     = "network-1"
    subnet_ids               = [
        "e9bgkn59veqpsss4fasg",
    ]
}
```

```bash
$ terraform state show yandex_vpc_subnet.subnet
```

```
# yandex_vpc_subnet.subnet:
resource "yandex_vpc_subnet" "subnet" {
    created_at     = "2025-02-05T16:54:50Z"
    description    = null
    folder_id      = "b1g6b21ruf06jt32tulo"
    id             = "e9bgkn59veqpsss4fasg"
    labels         = {}
    name           = "subnet-1"
    network_id     = "enpmabv269l6hgsf84id"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

```bash
$ terraform output
```

```
network_id = "enpmabv269l6hgsf84id"
subnet_cidr = "192.168.10.0/24"
subnet_id = "e9bgkn59veqpsss4fasg"
subnet_zone = "ru-central1-a"
```

### Challenges encountered
The main challenge was related to the documentation clarity, especially for Yandex Cloud configuration ::(((


## GitHub Infrastructure (Task 2)

### Best Practices Implemented

1. **Secure Token Management**
   I've done secure token handling by using environment variables for the GitHub token instead of hardcoding it in the configuration :)

2. **Resource Naming and Structure**
   Resource naming convention follows clear patterns that make the infrastructure code self-documenting

3. **State Management**
   Proper state management techniques: correctly importing existing resources into Terraform's state. This allows Terraform to track and manage pre-existing infrastructure components without trying to recreate them

4. **Security Configuration**
   The repository security was enhanced through several measures:
   - Branch protection rules for the master branch
   - Required code reviews for pull requests
   - Mandatory status checks before merging
   - Admin enforcement ensuring no bypassing of security rules

5. **Version Control**
   Version management was implemented through:
   - Pinned provider versions (~> 5.0) to ensure consistency
   - Inclusion of .terraform.lock.hcl in version control
   - Documented version constraints in the configuration

### Applied Configuration Example
```hcl
# GitHub repository configuration
resource "github_repository" "core-course-labs" {
  name        = "S25-core-course-labs"
  description = "Core course laboratories work"
  visibility  = "public"
  has_issues  = true
  has_wiki    = true
}

# Branch protection configuration
resource "github_branch_protection" "main" {
  pattern       = "master"
  enforce_admins = true
  required_status_checks {
    strict = true
    contexts = ["test", "build"]
  }
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
```

### Implementation Steps

The infrastructure was implemented using the following sequence of Terraform commands:

```bash
cd terraform/github

# Initialize Terraform working directory
terraform init

# Import existing GitHub repository
terraform import github_repository.core-course-labs S25-core-course-labs

# Review planned changes
terraform plan

# Apply the configuration
terraform apply
```

### Results and Benefits

The implemented configuration provides several advantages:

1. **Automated Management**: The entire GitHub repository configuration is now managed as code, making changes traceable and repeatable

2. **Enhanced Security**: Branch protection rules and required reviews ensure code quality and prevent accidental changes

3. **Maintainability**: Infrastructure changes can be reviewed, tested, and version controlled like regular code

4. **Consistency**: All repository settings are explicitly defined in code, preventing configuration drift and ensuring consistent settings across time