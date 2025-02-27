# Terraform Infrastructure

## Preparation & Installing Terraform
### Install on Arch
```sh
sudo pacman -S terraform
```
### Add to path
```sh
export PATH=$PATH:/path/to/terraform
```
### Check
```sh
terraform --version
```
### Start docker-service
```sh
sudo systemctl start docker
```

## Test usage with python web-app
### terraform state list
```
docker_container.python_container
docker_image.python_app
```

### terraform state show
#### docker_container.python_container:
```
resource "docker_container" "python_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python",
        "web.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "589f151df519"
    id                                          = "589f151df5190a33436fc6e84753f6f0be1d2a83ef4295c9cd37b616256f8699"
    image                                       = "sha256:a5c2a8018de16fc6f2546861f9e710a4a169ef14d8304a68fb223fc208c37c6f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
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
    stop_signal                                 = null
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "flask_app_user"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

#### docker_image.python_app:
```
resource "docker_image" "python_app" {
    id          = "sha256:78a74fb73bfb12a8641cc50cbc82f57c610aaafa73b628896cb71a475497922cpython:3.11"
    image_id    = "sha256:78a74fb73bfb12a8641cc50cbc82f57c610aaafa73b628896cb71a475497922c"
    name        = "python:3.11"
    repo_digest = "python@sha256:14b4620f59a90f163dfa6bd252b68743f9a41d494a9fde935f9d7669d98094bb"
}
```

### terraform output
```
python_container_id = "589f151df5190a33436fc6e84753f6f0be1d2a83ef4295c9cd37b616256f8699"
python_container_image = "petrel312/flask_app:latest"
python_container_name = "app_python"
```

## Integration with YandexCloud

I used this guide [https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#linux_1](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#linux_1)

### Prepare YandexCloud
1. Go to [https://console.yandex.cloud/](https://console.yandex.cloud/)
2. Create account
3. Create billing account. It should have status either `ACTIVE` or `TRIAL_ACTIVE`
4. Create Authorized Key and download `.json` with private and public key
5. Configure user
```sh
yc config profile create <profile_name>
yc config set service-account-key key.json
yc config set cloud-id <cloud_ID>
yc config set folder-id <folder_ID>
```
6. Export env variables
```sh
export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)
```

### Install YC on Arch
```sh
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
```
### Check
```sh
yc --version
```

### Configure ssh key for user:
```sh
ssh-keygen
yc organization-manager organization list
yc organization-manager user list --organization-id <organization-id>
yc organization-manager oslogin user-ssh-key create \
--organization-id <organization-id> \
--name "terraform-key" \
--subject-id <user-id> \
--data "<public ssh key>"
--expires-at 2026-01-02T15:04:05Z
```

### Prepare workspace for terraform for YandexCloud
```sh
mkdir -p terraform/yandex
cd terraform/yandex
touch main.tf
touch variables.tf
```

### Select image for VM
```sh
yc compute image list --folder-id standard-images
```

### Fill `main.tf` and `variables.tf` (if needed) with your data
```sh
vim main.tf
vim variables.tf
```

### terraform init
```
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of yandex-cloud/yandex from the dependency lock file
- Using previously-installed yandex-cloud/yandex v0.136.0
Terraform has made some changes to the provider dependency selections recorded
in the .terraform.lock.hcl file. Review those changes and commit them to your
version control system if they represent changes you intended to make.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

### terraform validate
```
Success! The configuration is valid.
```

### terraform fmt
```
main.tf
variables.tf
```

### terraform plan
```
Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

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
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJt96sjTJIW3FqlQIHgDaMcyPRMV1IbbjUGP/mQ4p45G ivans@ivan-systemproductname
            EOT
        }
      + name                      = "terraform-vm-1"
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

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd80bm0rh4rkepi5ksdi"
              + name        = (known after apply)
              + size        = 20
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
        }

      + metadata_options (known after apply)

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

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = (known after apply)
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.
```

### terraform apply
```
Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

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
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJt96sjTJIW3FqlQIHgDaMcyPRMV1IbbjUGP/mQ4p45G ivans@ivan-systemproductname
            EOT
        }
      + name                      = "terraform-vm-1"
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

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd80bm0rh4rkepi5ksdi"
              + name        = (known after apply)
              + size        = 20
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
        }

      + metadata_options (known after apply)

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

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = (known after apply)
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Creation complete after 2s [id=enprlcfrmf00nd0ceirr]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e9bd1sa39e34qmfqfh3h]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Creation complete after 41s [id=fhmrjisl997h4frvggi1]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

### terraform state list
```
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### terraform state show
#### yandex_compute_instance.vm-1:
```
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-06T00:40:32Z"
    description               = null
    folder_id                 = "b1gc5ps7gbb88cdmp0u2"
    fqdn                      = "fhmrjisl997h4frvggi1.auto.internal"
    gpu_cluster_id            = null
    hardware_generation       = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    hostname                  = null
    id                        = "fhmrjisl997h4frvggi1"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJt96sjTJIW3FqlQIHgDaMcyPRMV1IbbjUGP/mQ4p45G ivans@ivan-systemproductname
        EOT
    }
    name                      = "terraform-vm-1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmhpl9iut0p69fi6i43"
        disk_id     = "fhmhpl9iut0p69fi6i43"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd80bm0rh4rkepi5ksdi"
            kms_key_id  = null
            name        = null
            size        = 20
            snapshot_id = null
            type        = "network-hdd"
        }
    }

    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }

    network_interface {
        index              = 0
        ip_address         = "192.168.20.14"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:1b:9c:b9:54"
        nat                = true
        nat_ip_address     = "89.169.154.202"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bd1sa39e34qmfqfh3h"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}
```

#### yandex_vpc_network.network-1:
```
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-06T00:40:30Z"
    default_security_group_id = "enpe0e80or2msilrnhiv"
    description               = null
    folder_id                 = "b1gc5ps7gbb88cdmp0u2"
    id                        = "enprlcfrmf00nd0ceirr"
    labels                    = {}
    name                      = "default-1"
    subnet_ids                = []
}
```

#### yandex_vpc_subnet.subnet-1:
```
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-06T00:40:31Z"
    description    = null
    folder_id      = "b1gc5ps7gbb88cdmp0u2"
    id             = "e9bd1sa39e34qmfqfh3h"
    labels         = {}
    name           = null
    network_id     = "enprlcfrmf00nd0ceirr"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.20.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Github

### Prepare workspace
```sh
mkdir -p terraform/github
cd terraform/github
touch main.tf # fill it
touch variables.tf #fill it, if needed
```

### Create Access Token on GitHub
1. Settings -> Developer settings -> personal access tokens -> Tokens (classic)
2. Create new Token (classic)
3. Save it

### terraform import "github_repository.repo" "S25-core-course-labs"
```
github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### terraform apply
```
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.default will be created
  + resource "github_branch_default" "default" {
      + branch     = "lab4-solution"
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
      + pattern                         = "lab4-solution"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.default: Creating...
github_branch_default.default: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDONxdSs84DigsZ]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```
