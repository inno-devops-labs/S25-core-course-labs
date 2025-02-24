# Terraform in practice

## Best Practices Applied

### 1. Code Quality & Validation

Ensuring code consistency and correctness:

```bash
# Enforce formatting across all configurations
terraform fmt -recursive

# Validate syntax and logical correctness
terraform validate
```

### 2. Sensitive Data Handling

Secure storage and management of credentials:

```hcl
# Local Configuration Files (Git ignored)
# .gitignore entry
*.auto.tfvars
*.tfvars
```

### 3. Version Control Safety

Managing Terraform state and ignored files:

```gitignore
.terraform/
*.tfstate
*.tfstate.backup
*.auto.tfvars
```

Committed files:

- `main.tf` - Core configuration
- `variables.tf` - Variable declarations
- `TF.md` - Documentation

### 4. Provider Management

Maintaining provider versions for stability:

```hcl
provider "..." {
  version = "~> N.0" # Strict version constraint
}
```

## Docker Infrastructure Using Terraform

`terraform state show`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform state show docker_container.nginx
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
    hostname                                    = "98da2c706b95"
    id                                          = "98da2c706b95be14867bc7296e50d09794ccd599944753850373e8c37999f98d"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "AnotherEfimsContainerName"
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
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

`terraform state list`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform state list
docker_container.nginx
docker_image.nginx
```

Changes applied:

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform apply
docker_image.nginx: Refreshing state... [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx]
docker_container.nginx: Refreshing state... [id=3846435eac0e8e9ff88c27351a961a16e13da52a61c625a0293fcf0a69730998]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "3846435eac0e" -> (known after apply)
      ~ id                                          = "3846435eac0e8e9ff88c27351a961a16e13da52a61c625a0293fcf0a69730998" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
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
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=3846435eac0e8e9ff88c27351a961a16e13da52a61c625a0293fcf0a69730998]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=712bc613797381e4570dac0e83a9328eb98780850a2c22cf10adda2730cdc6d9]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

Input var utilization:

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform apply -var "container_name=AnotherEfimsContainerName"
docker_image.nginx: Refreshing state... [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx]
docker_container.nginx: Refreshing state... [id=723ac69f90051cdec1d558b03492c3231b72c24f8e95b96eb013b2adb809e46d]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "723ac69f9005" -> (known after apply)
      ~ id                                          = "723ac69f90051cdec1d558b03492c3231b72c24f8e95b96eb013b2adb809e46d" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "EfimsNginxContainer" -> "AnotherEfimsContainerName" # forces replacement
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
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=723ac69f90051cdec1d558b03492c3231b72c24f8e95b96eb013b2adb809e46d]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=98da2c706b95be14867bc7296e50d09794ccd599944753850373e8c37999f98d]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

`terraform output`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform> terraform output
container_id = "755946cae6aa15e743284c44e9de39343e9256752a3e3642436639a3b5f98f0d"
image_id = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx"
```

## Yandex Using Terraform

### Challenges

The most challenge for me was to find free plan cloud as I have already played with Yandex one and exhausted all the limits.
After the years of research I decided to share the VM of my kind friend =)

### Set up

Yandex has a well formatted official documentation, so the process of the cloud set up was pretty straightforward.

```bash
yc init
```

```bash
yc config profile create devops  
```

Export envs

```bash
export YC_TOKEN=$(yc iam create-token)                               
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)
```

`terraform plan`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\yandex> terraform plan
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd86cpunl4kkspv0u25a"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_disk.boot-disk-2 will be created
  + resource "yandex_compute_disk" "boot-disk-2" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd86cpunl4kkspv0u25a"
      + name        = "boot-disk-2"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDGBCnkRvJrkmHNQWy+ZLMB+BWWlrgqd2Xf8bnLW8OAV s.lekhtin
            EOT
        }
      + name                      = "terraform1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_compute_instance.vm-2 will be created
  + resource "yandex_compute_instance" "vm-2" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDGBCnkRvJrkmHNQWy+ZLMB+BWWlrgqd2Xf8bnLW8OAV s.lekhtin
            EOT
        }
      + name                      = "terraform2"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 4
          + memory        = 4
        }
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 6 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + external_ip_address_vm_2 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_2 = (known after apply)
```

`terraform apply`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\yandex> terraform apply

...
yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_compute_disk.boot-disk-2: Creating...
yandex_vpc_network.network-1: Creation complete after 3s [id=enpl111c4fqjeaa6lcku]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bmg59rnir1rh0il0ii]
yandex_compute_disk.boot-disk-2: Creation complete after 7s [id=fhmt9lfoa30368s63ghg]
yandex_compute_instance.vm-2: Creating...
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 12s [id=fhmt1tufbq1tv73rju6s]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-2: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-2: Still creating... [21s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-2: Creation complete after 26s [id=fhm8jpcqltt2sj5i7oqr]
yandex_compute_instance.vm-1: Creation complete after 25s [id=fhm31bbe78akca0tlvev]

Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "158.160.49.176"
external_ip_address_vm_2 = "158.160.34.120"
internal_ip_address_vm_1 = "192.168.10.27"
internal_ip_address_vm_2 = "192.168.10.12"
```

## Terraform for GitHub

I have configured setup and applied it:

### Import Existing Repository

`terraform import github_repository.repo S25-core-course-labs`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\github> terraform import github_repository.repo S25-core-course-labs
github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Look at plan changes

`terraform plan`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\github> terraform plan
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
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
          + required_approving_review_count = 0
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "Efim devops labs"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.
```

### Apply Terraform Changes

`terraform apply`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\github> terraform apply
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
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
          + required_approving_review_count = 0
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "Efim devops labs"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDONvZp7M4DiVeY]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

## GitHub Teams Using Terraform

[Resulted Repo](https://github.com/devops-efim/devops-efim)

`terraform apply`

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\terraform\gihub-teams> terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main_branch will be created
  + resource "github_branch_default" "main_branch" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "devops-efim"
    }

  # github_branch_protection.repo_protection will be created
  + resource "github_branch_protection" "repo_protection" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 0
        }
    }

  # github_repository.repository will be created
  + resource "github_repository" "repository" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + branches                    = (known after apply)
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Repository for devops-efim"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-efim"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

  # github_team.contributors will be created
  + resource "github_team" "contributors" {
      + create_default_maintainer = false
      + description               = "Contributors"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Repository contributors"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.maintainers will be created
  + resource "github_team" "maintainers" {
      + create_default_maintainer = false
      + description               = "Maintainers"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Repository maintainers"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.contributors will be created
  + resource "github_team_repository" "contributors" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "devops-efim"
      + team_id    = (known after apply)
    }

  # github_team_repository.maintainers will be created
  + resource "github_team_repository" "maintainers" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "devops-efim"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.contributors: Creating...
github_team.maintainers: Creating...
github_repository.repository: Creating...
github_team.maintainers: Still creating... [10s elapsed]
github_team.contributors: Still creating... [10s elapsed]
github_repository.repository: Still creating... [10s elapsed]
github_team.contributors: Creation complete after 15s [id=12122253]
github_team.maintainers: Creation complete after 16s [id=12122254]
github_repository.repository: Creation complete after 17s [id=devops-efim]
github_branch_default.main_branch: Creating...
github_team_repository.contributors: Creating...
github_team_repository.maintainers: Creating...
github_branch_default.main_branch: Creation complete after 2s [id=devops-efim]
github_branch_protection.repo_protection: Creating...
github_team_repository.contributors: Creation complete after 7s [id=12122253:devops-efim]
github_team_repository.maintainers: Creation complete after 7s [id=12122254:devops-efim]
github_branch_protection.repo_protection: Creation complete after 9s [id=BPR_kwDON06eic4DieZq]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```
