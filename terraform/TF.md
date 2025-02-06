# Terraform

## Docker infrastructure

Command `terraform state show docker_container.python_app`:
   ```bash
    (venv) ➜  docker_tf git:(Lab-4) ✗ terraform state show docker_container.python_app
    # docker_container.python_app:
    resource "docker_container" "python_app" {
        attach                                      = false
        bridge                                      = null
        command                                     = [
            "uvicorn",
            "main:app",
            "--host",
            "0.0.0.0",
            "--port",
            "8000",
        ]
        container_read_refresh_timeout_milliseconds = 15000
        cpu_set                                     = null
        cpu_shares                                  = 0
        domainname                                  = null
        entrypoint                                  = []
        env                                         = []
        hostname                                    = "e34e82d2609a"
        id                                          = "e34e82d2609a09df7f922d285e8aa6d9076bfc6a91a7e0b4652c33071283d1d3"
        image                                       = "sha256:5416e2bad533a8c278c3c53384c1bc64393fa3ca36f0d6531d0c3a34acd05d33"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "python_app"
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
        user                                        = "appuser"
        userns_mode                                 = null
        wait                                        = false
        wait_timeout                                = 60
        working_dir                                 = "/app"
    
        ports {
            external = 8000
            internal = 80
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }
   ```

Command `terraform state list`:
   ```bash
   (venv) ➜  terraform git:(Lab-4) ✗ terraform state list                            
   docker_container.python_app
   ```

Command `terraform output`:
   ```bash
   (venv) ➜  docker_tf git:(Lab-4) ✗ terraform output                                
   python_app_container_id = "e34e82d2609a09df7f922d285e8aa6d9076bfc6a91a7e0b4652c33071283d1d3"
   ```

## Yandex Cloud infrastructure

### Overview

- A cloud network (`network-1`) with a subnet (`subnet-1`).
- Two VMs with different resource configurations:
  - `terraform1`: 2 vCPUs, 2 GB RAM.
  - `terraform2`: 4 vCPUs, 4 GB RAM.
- System users configured via cloud-init for SSH access and administrative privileges.

### Setup Steps

#### Prerequisites
1. **Yandex Cloud Account**
2. **Service Account** : Create a service account and generate an authorized key (`key.json`).
3. **SSH Key Pair**
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
4. **Terraform Installation**

#### Configure the Provider
   ```hcl
   terraform {
     required_providers {
       yandex = {
         source  = "yandex-cloud/yandex"
         version = ">= 0.85.0"
       }
     }
     required_version = ">= 0.13"
   }
    
   provider "yandex" {
     token     = var.yandex_token
     cloud_id  = var.yandex_cloud_id
     folder_id = var.yandex_folder_id
     zone      = "ru-central1-a"
   }
   ```
   ```hcl
   variable "yandex_token" {}
   variable "yandex_cloud_id" {}
   variable "yandex_folder_id" {}
   ```

Export these variables as environment variables

   ```bash
   export TF_VAR_yandex_token=$(yc iam create-token)
   export TF_VAR_yandex_cloud_id=$(yc config get cloud-id)
   export TF_VAR_yandex_folder_id=$(yc config get folder-id)
   ```

#### Network and Subnet

Cloud network (`network-1`) and a subnet (`subnet-1`) in the `ru-central1-a` availability zone

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

#### Virtual Machines

Two VMs (`terraform1` and `terraform2`) are created with different resource configurations. Users are added via cloud-init using the `meta.txt` file.

   ```hcl
   resource "yandex_compute_instance" "vm-1" {
     name        = "terraform1"
     platform_id = "standard-v1"
     resources {
       cores  = 2
       memory = 2
     }
     boot_disk {
       initialize_params {
         image_id = "fd805qs1mn3n0casp7lt"
       }
     }
     network_interface {
       subnet_id = yandex_vpc_subnet.subnet-1.id
       nat       = true
     }
     metadata = {
       user-data = "${file("/Users/netpo4ki/PycharmProjects/S25-core-course-labs/terraform/yandex_cloud_tf/meta.txt")}"
     }
   }
    
   resource "yandex_compute_instance" "vm-2" {
     name        = "terraform2"
     platform_id = "standard-v1"
     resources {
       cores  = 4
       memory = 4
     }
     boot_disk {
       initialize_params {
         image_id = "fd805qs1mn3n0casp7lt"
       }
     }
     network_interface {
       subnet_id = yandex_vpc_subnet.subnet-1.id
       nat       = true
     }
     metadata = {
       user-data = "${file("/Users/netpo4ki/PycharmProjects/S25-core-course-labs/terraform/yandex_cloud_tf/meta.txt")}"
     }
   }
   ```

   ```txt
   #cloud-config
   users:
     - name: adminuser
       groups: sudo
       shell: /bin/bash
       sudo: 'ALL=(ALL) NOPASSWD:ALL'
       ssh_authorized_keys:
         - <public_SSH_key_1>
         - <public_SSH_key_2>
   ```

### Validation and Formatting

   ```bash
   terraform validate
   ```

   ```bash
   terraform fmt
   ```

### Apply the Configuration

   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

## Terraform Best Practices

1. **Environment Variables for Sensitive Data**:
   - Avoided hardcoding the GitHub token in the code by using the `GITHUB_TOKEN` environment variable.
   - Marked the `github_token` variable as `sensitive` to prevent accidental exposure.
2. **Modular Configuration**:
   - Separated the configuration into multiple `.tf` files (`main.tf`, `variables.tf`, `outputs.tf`) for better organization and maintainability.
3. **Importing Existing Resources**:
   - Used the `terraform import` command to bring an existing GitHub repository under Terraform management without recreating it.
4. **Branch Protection Rules**:
   - Configured branch protection rules to enforce code quality and collaboration standards (e.g., requiring pull request reviews and passing CI checks).
5. **Outputs for Visibility**:
   - Defined outputs to display useful information, such as the repository URL and default branch, after applying the configuration.
6. **Version Control**:
   - Committed all `.tf` files to version control (e.g., Git) to track changes and collaborate effectively.
7. **Avoid Deprecated Attributes**:
   - Replaced deprecated attributes (e.g., `default_branch`) with their recommended alternatives (e.g., `github_branch_default`).
8. **Test Changes Locally**:
   - Always ran `terraform plan` before applying changes to preview their impact.

## Managing GitHub Teams with Terraform

### GitHub Teams

- **Teams**:
  - `developers`: Write access (`push` permission).
  - `admins`: Admin access (`admin` permission).
  - `readers`: Read-only access (`pull` permission).
- **Repository Access**: Each team was assigned specific permissions on the repository.

### Best Practices Applied
1. **Separation of Concerns**:
   - Created a dedicated `teams.tf` file to manage GitHub teams and their permissions separately from the main configuration.
2. **Granular Permissions**:
   - Assigned different permission levels (`push`, `admin`, `pull`) to teams based on their roles.
3. **Outputs for Visibility**:
   - Defined outputs to display team IDs after applying the configuration.
4. **Version Control**:
   - Committed all `.tf` files to version control (e.g., Git) to track changes and collaborate effectively.
5. **Preview Changes**:
   - Always ran `terraform plan` before applying changes to preview their impact.