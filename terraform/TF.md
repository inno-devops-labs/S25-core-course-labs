# Terraform

## Table of Contents

- [Yandex Cloud](#Yandex)
- [Docker](#Docker)
- [Github](#Github)
- [Best practises](#Best)

# Yandex
1. First of all I created folder 'yandex' and work there
2. Since I have yandex cloud account, I installed `yc-` YandexCloud CLI
3. I created an authorized key for the service account and write down its file
    ```
    yc iam key create \
      --service-account-id <идентификатор_сервисного_аккаунта> \
      --folder-name <имя_каталога_с_сервисным_аккаунтом> \
      --output key.json
    ```
4. Set the profile configuration:
    ```
    yc config set service-account-key key.json
    yc config set cloud-id <идентификатор_облака>
    yc config set folder-id <идентификатор_каталога>
    
    export YC_TOKEN=$(yc iam create-token)
    export YC_CLOUD_ID=$(yc config get cloud-id)
    export YC_FOLDER_ID=$(yc config get folder-id)
    ```
5. Opened the Terraform CLI configuration file and added the following to it
    ```
    nano ~/.terraformrc
        
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
6. Created main.tf and put this config 
    ```
    terraform {
      required_providers {
        yandex = {
          source = "yandex-cloud/yandex"
        }
      }
      required_version = ">= 0.13"
    }
    
    provider "yandex" {
      service_account_key_file = "/Users/emildavlityarov/key.json"
      zone                     = "ru-central1-b"
    }
    ```
7. Run this command
    ```
    terraform providers lock -net-mirror=https://terraform-mirror.yandexcloud.net -platform=darwin_arm64 yandex-cloud/yandex
    ```
   for able macOs platform
8. For initialize used this command:

    ```
    terraform init
   
    terraform providers lock
   ```

9. And after this I planned Infrastructure by documentation Yandex Cloud:
    ```
    terraform {
      required_providers {
        yandex = {
          source = "yandex-cloud/yandex"
        }
      }
      required_version = ">= 0.13"
    }
    
    provider "yandex" {
      service_account_key_file = "/Users/emildavlityarov/key.json"
      zone                     = "ru-central1-b"
    }
    
    resource "yandex_compute_disk" "boot-disk-1" {
      name      = "boot-disk-1"
      type      = "network-hdd"
      zone      = "ru-central1-b"
      size      = "20"
      image_id  = "fd865udut6b1gvgh5igh"
      folder_id = "b1groi4d5f4vkh0nq7sr"
    }
    
    resource "yandex_compute_disk" "boot-disk-2" {
      name      = "boot-disk-2"
      type      = "network-hdd"
      zone      = "ru-central1-b"
      size      = "20"
      image_id  = "fd865udut6b1gvgh5igh"
      folder_id = "b1groi4d5f4vkh0nq7sr"
    }
    
    resource "yandex_compute_instance" "vm-1" {
      name      = "terraform1"
      folder_id = "b1groi4d5f4vkh0nq7sr"
    
      resources {
        cores  = 2
        memory = 2
      }
    
      boot_disk {
        disk_id = yandex_compute_disk.boot-disk-1.id
      }
    
      network_interface {
        subnet_id = yandex_vpc_subnet.subnet-1.id
        nat       = true
      }
    
      metadata = {
        user-data = file("./meta.txt")
      }
    }
    
    resource "yandex_compute_instance" "vm-2" {
      name      = "terraform2"
      folder_id = "b1groi4d5f4vkh0nq7sr"
    
      resources {
        cores  = 4
        memory = 4
      }
    
      boot_disk {
        disk_id = yandex_compute_disk.boot-disk-2.id
      }
    
      network_interface {
        subnet_id = yandex_vpc_subnet.subnet-1.id
        nat       = true
      }
    
      metadata = {
        user-data = file("./meta.txt")
      }
    }
    
    resource "yandex_vpc_network" "network-1" {
      name      = "network1"
      folder_id = "b1groi4d5f4vkh0nq7sr"
    }
    
    resource "yandex_vpc_subnet" "subnet-1" {
      name           = "subnet1"
      zone           = "ru-central1-b"
      network_id     = yandex_vpc_network.network-1.id
      v4_cidr_blocks = ["192.168.10.0/24"]
      folder_id      = "b1groi4d5f4vkh0nq7sr"
    }
    ```
10. Created meta.txt for access using by SSH:
    ```
    #cloud-config
    users:
      - name: <имя_пользователя>
        groups: sudo
        shell: /bin/bash
        sudo: 'ALL=(ALL) NOPASSWD:ALL'
        ssh_authorized_keys:
          - <публичный_SSH-ключ_1>
          - <публичный_SSH-ключ_2>
          - ...
    ```
11. Follow this command I get result, for Terraform will create all the required resources, and the terminal will specify the IP addresses of the created virtual machines:
    ```
    terraform validate
    
    terraform plan
    
    terraform apply
    ```

12. Got this result and destroyed resources:
    ```
        emildavlityarov@emapfff yandex % terraform apply
    
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
      + create
    
    Terraform will perform the following actions:
    
      # yandex_compute_disk.boot-disk-1 will be created
      + resource "yandex_compute_disk" "boot-disk-1" {
          + block_size  = 4096
          + created_at  = (known after apply)
          + folder_id   = "b1groi4d5f4vkh0nq7sr"
          + id          = (known after apply)
          + image_id    = "fd865udut6b1gvgh5igh"
          + name        = "boot-disk-1"
          + product_ids = (known after apply)
          + size        = 20
          + status      = (known after apply)
          + type        = "network-hdd"
          + zone        = "ru-central1-b"
        }
    
      # yandex_compute_disk.boot-disk-2 will be created
      + resource "yandex_compute_disk" "boot-disk-2" {
          + block_size  = 4096
          + created_at  = (known after apply)
          + folder_id   = "b1groi4d5f4vkh0nq7sr"
          + id          = (known after apply)
          + image_id    = "fd865udut6b1gvgh5igh"
          + name        = "boot-disk-2"
          + product_ids = (known after apply)
          + size        = 20
          + status      = (known after apply)
          + type        = "network-hdd"
          + zone        = "ru-central1-b"
        }
    
      # yandex_compute_instance.vm-1 will be created
      + resource "yandex_compute_instance" "vm-1" {
          + created_at                = (known after apply)
          + folder_id                 = "b1groi4d5f4vkh0nq7sr"
          + fqdn                      = (known after apply)
          + gpu_cluster_id            = (known after apply)
          + hardware_generation       = (known after apply)
          + hostname                  = (known after apply)
          + id                        = (known after apply)
          + maintenance_grace_period  = (known after apply)
          + maintenance_policy        = (known after apply)
          + metadata                  = {
              + "user-data" = <<-EOT
                    #cloud-config
                      users:
                        - name: emapfff
                        groups: sudo
                        shell: /bin/bash
                        sudo: 'ALL=(ALL) NOPASSWD:ALL'
                        ssh_authorized_keys:
                          - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAptjY+nqXxe+YucSCz+Y9LXEa4Zhv3HXaD5GvzOVtUeEJeBNvmgrM0NBuhTk5zScKjyLrGOW4Bj35vTyNaNkCxtGYa5SSpW3vJYmcYdVAkU1Fz3YU1Fz2xdDLMuFXenkynmHOaPhqLCtJ5dj3EVEujfceWG6XG0DE69ESY2g25nkEHOIFi0PTke7Z8qi7FGSkBB8X6IeiEZx3jvIKfUvhDzVbEqKEauwd0u1BYimYVW/wYIrSXjlJkIohVnN3c9nH3THspfznjoaJZa2idkI//IObedoE/LYjbKq/KT8/hcSkw7uixJJAYHKOO92omdGNez5Eb88eehJ21wcZib92NQqyb3wIBA+T23xjUy1gYx99uZXSLapViW2DkGqfuZyR+fzhmwJ7tFyBIHq9KS3khFiD1ssgXNPG47l4/cbTTWPMsfTnJNrkLrmnTiE0h8asmj4Cyi4zL55DBE0RTmhd48D23QXN9H2mKi2U9L/pkSLs30E38MOj+IAMsRKd7lM= emildavlityarov@MacBook-Pro-Emil.local
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
          + folder_id                 = "b1groi4d5f4vkh0nq7sr"
          + fqdn                      = (known after apply)
          + gpu_cluster_id            = (known after apply)
          + hardware_generation       = (known after apply)
          + hostname                  = (known after apply)
          + id                        = (known after apply)
          + maintenance_grace_period  = (known after apply)
          + maintenance_policy        = (known after apply)
          + metadata                  = {
              + "user-data" = <<-EOT
                    #cloud-config
                      users:
                        - name: emapfff
                        groups: sudo
                        shell: /bin/bash
                        sudo: 'ALL=(ALL) NOPASSWD:ALL'
                        ssh_authorized_keys:
                          - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAptjY+nqXxe+YucSCz+Y9LXEa4Zhv3HXaD5GvzOVtUeEJeBNvmgrM0NBuhTk5zScKjyLrGOW4Bj35vTyNaNkCxtGYa5SSpW3vJYmcYdVAkU1Fz3YU1Fz2xdDLMuFXenkynmHOaPhqLCtJ5dj3EVEujfceWG6XG0DE69ESY2g25nkEHOIFi0PTke7Z8qi7FGSkBB8X6IeiEZx3jvIKfUvhDzVbEqKEauwd0u1BYimYVW/wYIrSXjlJkIohVnN3c9nH3THspfznjoaJZa2idkI//IObedoE/LYjbKq/KT8/hcSkw7uixJJAYHKOO92omdGNez5Eb88eehJ21wcZib92NQqyb3wIBA+T23xjUy1gYx99uZXSLapViW2DkGqfuZyR+fzhmwJ7tFyBIHq9KS3khFiD1ssgXNPG47l4/cbTTWPMsfTnJNrkLrmnTiE0h8asmj4Cyi4zL55DBE0RTmhd48D23QXN9H2mKi2U9L/pkSLs30E38MOj+IAMsRKd7lM= emildavlityarov@MacBook-Pro-Emil.local
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
          + folder_id                 = "b1groi4d5f4vkh0nq7sr"
          + id                        = (known after apply)
          + labels                    = (known after apply)
          + name                      = "network1"
          + subnet_ids                = (known after apply)
        }
    
      # yandex_vpc_subnet.subnet-1 will be created
      + resource "yandex_vpc_subnet" "subnet-1" {
          + created_at     = (known after apply)
          + folder_id      = "b1groi4d5f4vkh0nq7sr"
          + id             = (known after apply)
          + labels         = (known after apply)
          + name           = "subnet1"
          + network_id     = (known after apply)
          + v4_cidr_blocks = [
              + "192.168.10.0/24",
            ]
          + v6_cidr_blocks = (known after apply)
          + zone           = "ru-central1-b"
        }
    
    Plan: 6 to add, 0 to change, 0 to destroy.
    
    Changes to Outputs:
      + external_ip_address_vm_1 = (known after apply)
      + external_ip_address_vm_2 = (known after apply)
      + internal_ip_address_vm_1 = (known after apply)
      + internal_ip_address_vm_2 = (known after apply)
    
    Do you want to perform these actions?
      Terraform will perform the actions described above.
      Only 'yes' will be accepted to approve.
    
      Enter a value: yes
    
    yandex_vpc_network.network-1: Creating...
    yandex_compute_disk.boot-disk-1: Creating...
    yandex_compute_disk.boot-disk-2: Creating...
    yandex_vpc_network.network-1: Creation complete after 2s [id=enpo92jebjjlmj0m7fmp]
    yandex_vpc_subnet.subnet-1: Creating...
    yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e2l31o7vqgll92aj6dmg]
    yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
    yandex_compute_disk.boot-disk-2: Still creating... [10s elapsed]
    yandex_compute_disk.boot-disk-2: Creation complete after 11s [id=epd7bqssqh5ardg3qhp6]
    yandex_compute_instance.vm-2: Creating...
    yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=epdoose01tjr11c0ohgg]
    yandex_compute_instance.vm-1: Creating...
    yandex_compute_instance.vm-2: Still creating... [10s elapsed]
    yandex_compute_instance.vm-1: Still creating... [10s elapsed]
    yandex_compute_instance.vm-2: Still creating... [20s elapsed]
    yandex_compute_instance.vm-1: Still creating... [20s elapsed]
    yandex_compute_instance.vm-2: Creation complete after 29s [id=epdm3r8jppi3c1dgtv1s]
    yandex_compute_instance.vm-1: Still creating... [30s elapsed]
    yandex_compute_instance.vm-1: Creation complete after 33s [id=epdss41q4f847kju3rp6]
    
    Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
    
    Outputs:
    
    external_ip_address_vm_1 = "89.169.173.176"
    external_ip_address_vm_2 = "89.169.172.143"
    internal_ip_address_vm_1 = "192.168.10.22"
    internal_ip_address_vm_2 = "192.168.10.21"
    ```

# Docker

We don't need any external info, just make sure Docker Daemon is running.
After `terraform apply`:

```
emildavlityarov@emapfff docker % terraform state list
docker_container.app_python
docker_image.app_python
emildavlityarov@emapfff docker % terraform state show docker_container.app_python
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "aaf275a1064d"
    id                                          = "aaf275a1064d0959c9f98c8edcffbeedb25122c0ce1c1b2c230d8aa471b2a7e9"
    image                                       = "sha256:45516097ab1c4f67dfa49d1088ad16be2a6a462c378c74221b2318b249b7b5a2"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {
        "max-file" = "5"
        "max-size" = "20m"
    }
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
    network_data                                = [
        {
            gateway                   = "192.168.215.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "192.168.215.2"
            ip_prefix_length          = 24
            ipv6_gateway              = ""
            mac_address               = "02:42:c0:a8:d7:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 3998
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "nobody"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
emildavlityarov@emapfff docker % terraform output                                
container_id = "aaf275a1064d0959c9f98c8edcffbeedb25122c0ce1c1b2c230d8aa471b2a7e9"
image_id = "sha256:45516097ab1c4f67dfa49d1088ad16be2a6a462c378c74221b2318b249b7b5a2emapfff/app_python:latest"

```

# Github
1. I created repo 'terraform-course' and push default README.md file
2. In `github` folder I created main.tf and put this config:
```
terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
  required_version = ">= 0.13"
}

provider "github" {
  token = var.token
}

resource "github_repository" "terraform-course" {
  name             = "terraform-course"
  description      = "Test terraform for creating repository"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

# Set default branch to "main"
resource "github_branch_default" "main" {
  repository = github_repository.terraform-course.name
  branch     = "main"
}

# Create branch protection rule to protect the default branch
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.terraform-course.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
```
3. After this on I generated Github access token and save in environment variables:
    ```
    export GITHUB_TOKEN=<my_token>
    export TF_VAR_token=$GITHUB_TOKEN
    ```
4. Then I used command for import resources:
    ```
    emildavlityarov@emapfff github % terraform import "github_repository.terraform-course" "terraform-course" 
    github_repository.terraform-course: Importing from ID "terraform-course"...
    github_repository.terraform-course: Import prepared!
      Prepared github_repository for import
    github_repository.terraform-course: Refreshing state... [id=terraform-course]
    
    Import successful!
    
    The resources that were imported are shown above. These resources are now in
    your Terraform state and will henceforth be managed by Terraform.
    ```
5. And apply Terraform config:
    ```
    emildavlityarov@emapfff github % terraform apply                                                          
    github_repository.terraform-course: Refreshing state... [id=terraform-course]
    github_branch_default.main: Refreshing state... [id=terraform-course]
    github_branch_protection.default: Refreshing state... [id=BPR_kwDON1hDzs4Din_p]
    
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
      ~ update in-place
    
    Terraform will perform the following actions:
    
      # github_repository.terraform-course will be updated in-place
      ~ resource "github_repository" "terraform-course" {
          ~ description                 = "Test terraform for multiple teams" -> "Test terraform for creating repository"
            id                          = "terraform-course"
            name                        = "terraform-course"
            # (34 unchanged attributes hidden)
    
            # (1 unchanged block hidden)
        }
    
    Plan: 0 to add, 1 to change, 0 to destroy.
    
    Do you want to perform these actions?
      Terraform will perform the actions described above.
      Only 'yes' will be accepted to approve.
    
      Enter a value: yes
    
    github_repository.terraform-course: Modifying... [id=terraform-course]
    github_repository.terraform-course: Modifications complete after 2s [id=terraform-course]
    
    Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
    
    ```
7. And my results:
![img.png](img.png)

# Best

- I've seperated tf config files corresponding to its need, `variables.tf` stores variables and etc. (instead Yandex cloud)

- Each project has its own folder to avoid intersection with condigurations

- Validating and formating terraform config files
