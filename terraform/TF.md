# Terraform

# Terraform Docker 

## Output from running `terraform state list`
```bash
docker_container.nginx
docker_image.nginx
```
## Output after running `terraform state show docker_container.nginx`
```bash
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
    hostname                                    = "5c6e23878ced"
    id                                          = "5c6e23878ced8a34347761ad18657c3afd97c94a8bfa66b986eca37ba0ed3690"
    image                                       = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my_docker_nginx_container"
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


## Output after running `terraform state show docker_image.nginx`
```bash
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58nginx"
    image_id     = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}
```

## `terraform output`
```bash
container_id = "5c6e23878ced8a34347761ad18657c3afd97c94a8bfa66b986eca37ba0ed3690"
image_id = "sha256:9b1b7be1ffa607d40d545607d3fdf441f08553468adec5588fb58499ad77fe58nginx"
```

<br>
<br>

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

After installation, close and reopen your terminal or run:
```bash
source ~/.bashrc
```

### 2. Initialize Yandex Cloud CLI

```bash
yc init
```

During initialization:
1. You'll be redirected to a browser window to log in to Yandex Cloud
2. After login, you'll receive an OAuth token
3. Copy and paste the OAuth token back to the terminal
4. Select your cloud and folder when prompted

To verify your configuration:
```bash
yc config list
```

Expected output should look like:
```
token: y0_AgAAAA...
cloud-id: b1g...
folder-id: b1g...
compute-default-zone: ru-central1-a
```

### 3. Create IAM Token

```bash
yc iam create-token
```

Expected output:
```
t1.9euelZr...
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
    created_at                = "2025-02-06T10:42:09Z"
    default_security_group_id = "enp2ge387a4o1ii2ri1r"
    description               = null
    folder_id                 = "b1gqt9kth27men0v81k3"
    id                        = "enplm3vvnkotc84epn87"
    labels                    = {}
    name                      = "terraform-network"
    subnet_ids                = []
}
```

#### `terraform state show yandex_vpc_subnet.subnet`
```bash
# yandex_vpc_subnet.subnet:
resource "yandex_vpc_subnet" "subnet" {
    created_at     = "2025-02-06T10:42:15Z"
    description    = null
    folder_id      = "b1gqt9kth27men0v81k3"
    id             = "e9btehkcvhsq0ib80ui6"
    labels         = {}
    name           = "terraform-subnet"
    network_id     = "enplm3vvnkotc84epn87"
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
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDEZ4jBqPN8WRcpyG+B4BbkIdXLd7TXaHy4KMyTstEyJyJ5+wpQrAR1H4zy/yAG2Ce0CfZOdOLjrnd2HLpWBLc4UFvTG6BPti16JVRYhgj7cHEvaoA+XTjJxNfGgFJNkbMkli4fRuQkgnWdwtzINhu1XCHq1AE2C+FEJsunJMThZGqZ/UFZUv4cExt1hsOCjwreT25TRMEkvqO+iKpjSZKo2yYugF9PcRYV4WzBeqcCksKbUwvcjDGce6rAQONolyQQ3wOJXf5oNvHFDJ/Pj7u2MrRV6vau/vp57JyxktTxM//8h4MYUq77hlDHoxP+LYBwMf0ctpk//LmHVJpANPs+Ry+j9grNsn2ES+mcPRApPJaJrH2xcLFHYroXmgltgLdYra4njK3K+UYgFb2LETG/C0zcZ+XT+YQg2zzeTHu/Wy7NtIwHgaN+KUKlwF0krbJDXORvlzBMm4JrzRY9zWX1W7/5snpaff5e0d5oSKQDMmw0Br5GQxVWMC+5GGyiIy0= timurzeksimbaev@MacBook-Pro-Timur.local
            EOT
        }
      + name                      = "compute-vm-2-2-20-ssd-1738835807410"
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
              + image_id    = "fd8s5j70eqong91qn54k"
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