# Terraform Infrastructure Documentation

## Docker Infrastructure Using Terraform

### 1. Installing Terraform

I downloaded and installed Terraform from the [official site](https://www.terraform.io/downloads.html). Verification was performed with:

```bash
  terraform -v
```
And obtained output
```text
  Terraform v1.10.5
  on darwin_arm64
```

### 2. Building the infrastructure
   1) I created the file **main.tf** with content:
      ```terraform
       terraform {
            required_providers {
            docker = {
                source  = "kreuzwerker/docker"
                version = "~> 3.0.1"
                }
            }
        }

        provider "docker" {}

        resource "docker_image" "nginx" {
            name         = "nginx:latest"
            keep_locally = false
        }

        resource "docker_container" "nginx" {
            image = docker_image.nginx.image_id
            name  = "MyNginx"
            ports {
                internal = 80
                external = 8000
            }
        }
      ```
   2) Then I applied these commands:
      ```bash
        terraform init
        terraform fmt
        terraform validate
        terraform apply
      ```
   3) And I saw that a new nginx container appeared in my local docker daemon
   4) I applied commands and obtained corresponding outputs:
      ```bash
        terraform show
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
            hostname                                    = "2f8256b22969"
            id                                          = "2f8256b229699f0a03712d52df0e7aea7339812cee14466b286e24d3c96b641a"
            image                                       = "sha256:0dff3f9967e3cb3482965cc57c30e171f1def88e574757def5474cd791f50a16"
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
            name                                        = "MyNginx"
            network_data                                = [
            {
            gateway                   = "192.168.215.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "192.168.215.2"
            ip_prefix_length          = 24
            ipv6_gateway              = null
            mac_address               = "02:42:c0:a8:d7:02"
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
            shm_size                                    = 6004
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
            id           = "sha256:0dff3f9967e3cb3482965cc57c30e171f1def88e574757def5474cd791f50a16nginx:latest"
            image_id     = "sha256:0dff3f9967e3cb3482965cc57c30e171f1def88e574757def5474cd791f50a16"
            keep_locally = false
            name         = "nginx:latest"
            repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
        }
      ```
         
      ```bash
        terraform state list
      ```
      ```
        docker_container.nginx
        docker_image.nginx
      ```
   5) Then I performed variables utilization
      
      I created file **variables.tf** with such content:
      ```terraform
        variable "container_name" {
            default = "default_nginx"
            description = "Container name for nginx"
        }
      ```
      And updated file **main.tf**:
      ```terraform
        terraform {
            required_providers {
                docker = {
                  source  = "kreuzwerker/docker"
                  version = "~> 3.0.1"
                }
            }
        }
        
        provider "docker" {}
        
        resource "docker_image" "nginx" {
          name         = "nginx:latest"
          keep_locally = false
        }
        
        resource "docker_container" "nginx" {
          image = docker_image.nginx.image_id
          name  = var.container_name
          ports {
            internal = 80
            external = 8000
          }
        }
      ```
      
      Then I applied new configuration with variable value
      ```bash
        terraform apply -var="container_name=named_nginx"
      ```
      And finally I saw that I have a container with name: **named_nginx**
  6) Finally, outputs
     I created a file **outputs.tf** with content:
     ```terraform
        output "container_id" {
            description = "ID of the Docker container"
            value       = docker_container.nginx.id
        }

        output "image_id" {
            description = "ID of the Docker image"
            value       = docker_image.nginx.id
       }
     ```
     Then I applied the configuration and executed command
     ```bash
       terraform output
     ```
     ```
       container_id = "a48694743c99266ca87ab82ec2ca766e27bac0648ea936d772b78d1d4c24ba33"
       image_id = "sha256:2ff7c3a067e3cb3482965cc57c30e171f1def88e574757def5474ef791f30a17nginx:latest"
     ```

## Integration with YandexCloud

1) I created a folder **yandex** inside **terraform** directory to locate terraform configuration for YandexCloud
2) I created a service account using Management Console
3) Then I gained an admin permission to my **default** directory in YC
4) I installed **yc**- YandexCloud CLI
5) Used command
   ```bash
     yc iam key create \
    --service-account-id <service_account_ID> \
    --folder-name <service_account_folder_name> \
    --output key.json
   ```
   to generate key for yandex infrastructure
6) Then I created new profile for my service account and configured it
   ```bash
     yc config profile create <profile_name>
     yc config set service-account-key key.json
     yc config set cloud-id <cloud_ID>
     yc config set folder-id <folder_ID>
     export YC_TOKEN=$(yc iam create-token)
     export YC_CLOUD_ID=$(yc config get cloud-id)
     export YC_FOLDER_ID=$(yc config get folder-id)
   ```
7) Now lets start with terraform initialization itself
   ```bash
     nano ~/.terraformrc
   ```
   and put this content:
   ```terraform
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
   to use YC terraform registry
8) I created **main.tf** with such content
   ```terraform
     terraform {
         required_providers {
             yandex = {
                 source = "yandex-cloud/yandex"
             }
         }
         required_version = ">= 0.13"
     }

     provider "yandex" {
         service_account_key_file = "<your-path-to>/key.json"
         zone = "ru-central1-b"
     }

     resource "yandex_compute_disk" "boot-disk-1" {
         name     = "boot-disk-1"
         type     = "network-hdd"
         zone     = "ru-central1-b"
         size     = "20"
         image_id = "fd865uon0af912uhk9cs"
         folder_id = "<here-was-my-folder-id>"
     }

     resource "yandex_compute_disk" "boot-disk-2" {
         name     = "boot-disk-2"
         type     = "network-hdd"
         zone     = "ru-central1-b"
         size     = "20"
         image_id = "fd865uon0af912uhk9cs"
         folder_id = "<here-was-my-folder-id>"
     }

     resource "yandex_compute_instance" "vm-1" {
         name = "terraform1"
         folder_id = "<here-was-my-folder-id>"

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
         name = "terraform2"
         folder_id = "<here-was-my-folder-id>"

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
         name = "network1"
         folder_id = "<here-was-my-folder-id>"
     }

     resource "yandex_vpc_subnet" "subnet-1" {
         name           = "subnet1"
         zone           = "ru-central1-b"
         network_id     = yandex_vpc_network.network-1.id
         v4_cidr_blocks = ["192.168.10.0/24"]
         folder_id = "<here-was-my-folder-id>"
     }
   ```
9) I created a file **meta.txt** to allow ssh connection from my machine to created vm
   ```text
     #cloud-config
     users:
       - name: misha
       groups: sudo
       shell: /bin/bash
       sudo: 'ALL=(ALL) NOPASSWD:ALL'
       ssh_authorized_keys:
         - <here-was-my-public-key>
   ```
10) ```bash
      terraform init
      terraform providers lock -net-mirror=https://terraform-mirror.yandexcloud.net -platform=darwin_arm64 -platform=linux_amd64 yandex-cloud/yandex
    ```
    to initialize terraform able to work with both **linux** and **macOS**
11) Created file **outputs.tf** to have an output with ip-addresses of created machines
    ```terraform
      output "internal_ip_address_vm_1" {
        value = yandex_compute_instance.vm-1.network_interface.0.ip_address
      }

      output "internal_ip_address_vm_2" {
        value = yandex_compute_instance.vm-2.network_interface.0.ip_address
      }

      output "external_ip_address_vm_1" {
        value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
      }

      output "external_ip_address_vm_2" {
        value = yandex_compute_instance.vm-2.network_interface.0.nat_ip_address
      }
    ```
12) Formatting and validation
    ```bash
      terraform validate
      terraform fmt
    ```
13) Check plan
    ```bash
      terraform plan
    ```
    Validated that deploy plan is valid
14) Deploy infrastructure
    ```bash
      terraform apply
    ```
    ```text
      Outputs:
      external_ip_address_vm_1 = "51.250.96.104"
      external_ip_address_vm_2 = "84.201.142.48"
      internal_ip_address_vm_1 = "192.168.10.21"
      internal_ip_address_vm_2 = "192.168.10.4"
    ```

## GitHub integration
1) I created a repo **S25-core-course-labs** in my GH account with private visibility and README
2) I generated PAT for my account using GitHub WEB interface
3) I created **github** folder inside **terraform** directory to store files for integration
4) I created **main.tf** with such content:
   ```terraform
     terraform {
       required_providers {
         github = {
           source  = "integrations/github"
           version = "~> 4.0"
         }
       }
     }

     provider "github" {
       token = var.token # or `GITHUB_TOKEN`
     }

     resource "github_repository" "repo" {
       name               = "S25-core-course-labs"
       description        = "Automated Terraform integration for my repository."
       visibility         = "private"
       auto_init          = true
       license_template   = "mit"
     }

     resource "github_branch_default" "main" {
       repository = github_repository.repo.name
       branch     = "main"
     }
   ```
5) I created file **variables.tf** to work with token variable
   ```terraform
     variable "token" {
       type        = string
       description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
       sensitive   = true
     }
   ```
6) Init terraform
   ```bash
     terraform init
   ```
7) I put my token to environment variable using such commands
   ```bash
     export GITHUB_TOKEN=<my_token>
     export TF_VAR_token=$GITHUB_TOKEN
   ```
8) Validate and format terraform config
   ```bash
     terraform validate
     terraform fmt
   ```
9) Import **existing** repo to terraform config
   ```bash
     terraform import "github_repository.repo" "S25-core-course-labs"
   ```
10) Apply terraform config to repo
    ```bash
      terraform apply
    ```


