# Terraform

# Terraform Docker 

## Output from running `terraform state list`
```bash
docker_container.nginx
docker_image.nginx
```
## Output after running `terraform state show docker_container.nginx`
```bash
# docker_container.nginx will be created
  + resource "docker_container" "nginx" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = (known after apply)
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = (known after apply)
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "my-terraform-docker"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false

      + ports {
          + external = 8080
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id          = (known after apply)
      + latest      = (known after apply)
      + name        = "nginx:latest"
      + output      = (known after apply)
      + repo_digest = (known after apply)
    }
```

## `terraform output`
```bash
container_id = "a54b37bd1127e3e0526dc4430766335ea48621e448000123faea386a1bb1f5d8"
```

# Yandex Terraform

### Prerequisites
- **Ubuntu 24.04 LTS**
- **Terraform installed**
- **Yandex Cloud account**
- **Yandex Cloud CLI**

# Yandex Cloud Terraform Setup Guide

## Prerequisites

- Ubuntu 24.04 LTS
- Terraform installed
- Yandex Cloud account
- Yandex Cloud CLI

## Initial Setup

### 1. Install Yandex Cloud CLI

```bash
curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
```

After installation, close and reopen terminal or run:
```bash
source ~/.bashrc
```

### 2. Initialize Yandex Cloud CLI

```bash
yc init
```

```bash
yc config list
```

### 3. Create IAM Token

```bash
yc iam create-token
```

### 4. Set Up Environment Variables

```bash
export TF_VAR_yc_token="<your-iam-token>"
export TF_VAR_yc_cloud_id="<your-cloud-id>"
export TF_VAR_yc_folder_id="<your-folder-id>"
```

#### `terraform state list`
```bash
yandex_vpc_network.network
yandex_vpc_subnet.subnet
```


#### `terraform state show yandex_vpc_network.network`
```bash
# yandex_vpc_network.network:
resource "yandex_vpc_network" "network" {
    created_at                = ""
    default_security_group_id = ""
    description               = null
    folder_id                 = ""
    id                        = ""
    labels                    = {}
    name                      = "terraform-network"
    subnet_ids                = []
}
```

#### `terraform state show yandex_vpc_subnet.subnet`
```bash
# yandex_vpc_subnet.subnet:
resource "yandex_vpc_subnet" "subnet" {
    created_at     = ""
    description    = null
    folder_id      = ""
    id             = ""
    labels         = {}
    name           = "terraform-subnet"
    network_id     = ""
    route_table_id = null
    v4_cidr_blocks = [
        "10.2.0.0/16",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

#### `terraform plan`
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.vm will be created
  + resource "yandex_compute_instance" "vm" {
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
            EOT
        }
      + name                      = "compute-vm-2-2-20-ssd-1739836808536"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd8ff470ekogg10bn64f"
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

  # yandex_vpc_network.network will be created
  + resource "yandex_vpc_network" "network" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "terraform-network"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet will be created
  + resource "yandex_vpc_subnet" "subnet" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "terraform-subnet"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "10.2.0.0/16",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address = (known after apply)
  + internal_ip_address = (known after apply)
```




































<br>


# Terraform GitHub 

## Commands Used
```bash
terraform init
terraform import "github_repository.core-course-labs" "S25-core-course-labs"
terraform plan
terraform apply
```

### State Commands Output
```bash
terraform state list
# Output:
github_repository.core-course-labs
github_branch_protection.main
```

## Best Practices

### Version Control
- Provider version pinning `version = "~> 5.0"`
- Separated provider configuration in `providers.tf`
- Clear file organization (main.tf, providers.tf)

### Security
- Branch protection rules implementation
- Required status checks for CI/CD
- Code review requirements
- No hardcoded credentials

### Resource Management
- Consistent resource naming
- Clear resource dependencies
- Proper resource importing using `terraform import`
- Regular state verification with `terraform plan`

### GitHub Configuration
- Repository visibility and feature settings
- Branch protection and merge settings
- Status checks for CI/CD pipeline
- Pull request review requirements