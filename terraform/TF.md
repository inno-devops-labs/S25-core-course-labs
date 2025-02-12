# Terraform (adventures)

## Best Practices

- Clear structure - the terraform files are broken down into individual files like `variables.tf` or `main.tf` for better readability
- No secrets in the files - we are safe with out secrets
- The changes are checked with `terraform plan` to ensure that everything goes smoothly, and later `validate` and `fmt` can be used as well
- Files that contain intermidiate, secret-full information like `.tfvars` are properly ignored in git

## Docker

### Terraform list

```bash
❯ terraform state list
docker_container.js_app_container
docker_container.moscow_time_app_container
```

### Terraform show (main app)

```bash
❯ terraform state show docker_container.moscow_time_app_container
# docker_container.moscow_time_app_container:
resource "docker_container" "moscow_time_app_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "uvicorn",
        "app.main:app",
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
    hostname                                    = "9d919397d34f"
    id                                          = "9d919397d34f6b447561f81fce89eabac1c5c8ad2eab540aa6ae92d9ea6ed944"
    image                                       = "sha256:f8a03f3bc6ae2cde8c20d8ec47d98a2772a4e244f819dc6ca516f6297483e51e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time-app"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:03"
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
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Terraform show (js app)

```bash
❯ terraform state show docker_container.js_app_container
# docker_container.js_app_container:
resource "docker_container" "js_app_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "server.js",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/nodejs/bin/node",
    ]
    env                                         = []
    hostname                                    = "4aac3d60252e"
    id                                          = "4aac3d60252e00d5dae65da6010f3724406b8635220aacd392252a3204694023"
    image                                       = "sha256:32cc67dcb0ce78389b99b7e42bd0e3d3ebe45c35f68acc3a5cc310ad320abd2b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "js-app-distroless"
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
    user                                        = "0"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 3000
        internal = 3000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Terraform apply

# Terraform apply
```bash
❯ terraform apply -auto-approve
docker_container.moscow_time_app_container: Refreshing state... [id=15415a8d4df81c3c94f5d345eed296543189db79411c3127b95f66e01d7a716e]
docker_container.js_app_container: Refreshing state... [id=e4227250e1886e9ddaa1842e04fcce30a8559abc1fd26e4972f195bf9e7d7139]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

  # docker_container.js_app_container has been deleted
  - resource "docker_container" "js_app_container" {
      - id                                          = "e4227250e1886e9ddaa1842e04fcce30a8559abc1fd26e4972f195bf9e7d7139" -> null
        name                                        = "js-app-distroless"
        # (16 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

  # docker_container.moscow_time_app_container has been deleted
  - resource "docker_container" "moscow_time_app_container" {
      - id                                          = "15415a8d4df81c3c94f5d345eed296543189db79411c3127b95f66e01d7a716e" -> null
        name                                        = "moscow-time-app"
        # (16 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following plan may include
actions to undo or respond to these changes.

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.js_app_container will be created
  + resource "docker_container" "js_app_container" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = "gendiro/js-app-distroless:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "js-app-distroless"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + healthcheck (known after apply)

      + labels (known after apply)

      + ports {
          + external = 3000
          + internal = 3000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.moscow_time_app_container will be created
  + resource "docker_container" "moscow_time_app_container" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = "gendiro/moscow-time-app:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "moscow-time-app"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + healthcheck (known after apply)

      + labels (known after apply)

      + ports {
          + external = 8000
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + js_app_container_id             = (known after apply)
  + moscow_time_app_container_id    = (known after apply)
docker_container.js_app_container: Creating...
docker_container.moscow_time_app_container: Creating...
docker_container.js_app_container: Creation complete after 1s [id=4aac3d60252e00d5dae65da6010f3724406b8635220aacd392252a3204694023]
docker_container.moscow_time_app_container: Creation complete after 1s [id=9d919397d34f6b447561f81fce89eabac1c5c8ad2eab540aa6ae92d9ea6ed944]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

js_app_container_id = "4aac3d60252e00d5dae65da6010f3724406b8635220aacd392252a3204694023"
js_app_container_ports = tolist([
  {
    "external" = 3000
    "internal" = 3000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
moscow_time_app_container_id = "9d919397d34f6b447561f81fce89eabac1c5c8ad2eab540aa6ae92d9ea6ed944"
moscow_time_app_container_ports = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

### Terraform output

```bash
❯ terraform output
js_app_container_id = "4aac3d60252e00d5dae65da6010f3724406b8635220aacd392252a3204694023"
js_app_container_ports = tolist([
  {
    "external" = 3000
    "internal" = 3000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
moscow_time_app_container_id = "9d919397d34f6b447561f81fce89eabac1c5c8ad2eab540aa6ae92d9ea6ed944"
moscow_time_app_container_ports = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex

There isn't much to say about the setup as the whole process is described in <https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart>.
I went through the standard procedure of logging into yandex with their CLI tool `yc init`, configured terraform files (like `main.tf`) and did steps similar
to that of the previous one (after suffering through horrible yandex UI for cloud).

### Terraform plan

```bash
❯ terraform plan

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
      + image_id    = "e9bthv3k33m30an455e8"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-d"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
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
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDTyc6fE0uFRIk+TROYOIK9t9FIgUVGB+7krNSJ1Rv/Y5SqJph+G8BVacjtQQLHH8cTlcIll6aOoedxHMRrgazWsYJNHTIaS5GCXNeYferibKvtLlSrztzbncYjxbxU+Bfha1HPcW8ltiAu/b3/MSnBhyDO6YKkrncTp8Hd2RuX5m22DTqVbIAr8g3h4a/5/pfHS9yIDPanuESrCsVV76LQx/72pioDmdjdMmEXOm6w1t27qahhck6UUilIK/0Rx5+tHNi6qyAdL4/DxE1YJ91FhKfjbflKOJ5CGrmasFjj57b/6xLB+2vXU2pLg/Pj9rv1qGSip5IHV4ZaTrztQqctVPEJHvbWX3FNRBD1T+zWzpuFPjodvvua7roSxQ7RcWzn2vS3UQPzPqG0sZKM62l8Sb2Uohv6//nB3MsB0bp8OwJ81YabtrWQj5dm6Dr847RjLDVQeeSrmqNX4v1brZTMLXD5kD+FDZg5xpaIo4C47iaaG/6dvu8d5d/l6EqXjZ2Wh7IaocN18ffkwMYLqXb6dUj+Qn4t0EEzJG2Sb8Sd/a/TERcYbDGnqqscOYgKFi57dJgRi6KckQX0iCd+VGWxON3YFbUKairy/NYN85oVqmQ0pz0uc4sXyn+YWlhtv1nsDn1pVoOJ3iYBZOharWF2pG3dAhxZVmTovMbmIce2IQ==
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

          + initialize_params (known after apply)
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
          + "192.168.10.0/16",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-d"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if
you run "terraform apply" now.
```

### Terraform apply

```bash
❯ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8bpal18cm4kprpjc2m"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
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
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCzrvNOOAYlN9olo7mIalI+4akrnJG4ITJwegUHsmF1qrY2mIaPUGt2/ZSwNe6vEW0mfBJ98/0yzOiDLK4bmqXurwwR7Voo/V3Jotrb6G9o2lEfXr0HNoiSil2OkbGvlfv8yfOhl31wrz+fu6E5fMuyc9POEg6zZIRvpdSdNAaDq1I62sbpuqPZOEzbk695i8SBfaQm+GvejiHYeEZUUojvXcDf7w6+pYAyVzACjl4LftHmbvj/ae8qNkjRh1tiS38HBAO8rG8ElOkxGX5Fcf3FVLxWpBDoo3KB0oa3e/kYlOt1GQ3hqL39cuuc/y0JEWTa0aQ6RZYhPfI4iLmvR62M98xsuT03Gu2FUVrzUwTfwfRe0Bm3t7LReSt0y0EqlCV0vzqLeaAHKpt9VgmUFAvtvgc21eS43QxvLjLRrYwsLlYYlVN3QEtdqyMaH5vZ6tn6xGFi+R+Nw/ynsvsOw7FeZcAb7HTBWhTuaolg/LftdqjV+YtBzjXQ0DasobrqwgU= magic@DESKTOP-5I2CL7J
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

          + initialize_params (known after apply)
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
          + "192.168.0.0/16",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 3s [id=enpkvl1gsjvvrh4t309n]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bseoiagoshe4goshhk]
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=fhmpng3juj247cdqnsn6]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 35s [id=fhm8t4ej0ershfvl1a8a]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "89.169.141.93"
internal_ip_address_vm_1 = "192.168.0.11"
```

### Terraform output

```bash
❯ terraform output
external_ip_address_vm_1 = "89.169.141.93"
internal_ip_address_vm_1 = "192.168.0.11"
```

## GitHub

### Terraform import

```bash
❯ terraform import "github_repository.repo" "S25-core-course-labs"
var.token
  GitHub Token

  Enter a value:

github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Terraform apply

```bash
❯ terraform apply -auto-approve
var.token
  GitHub Token

  Enter a value:

github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "My very incredible solution for DevOps Labs"
      + gitignore_template          = "Python"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
      ~ has_wiki                    = true -> false
        id                          = "S25-core-course-labs"
      + license_template            = "mit"
        name                        = "S25-core-course-labs"
        # (28 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.
github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_protection.default: Creating...
github_branch_default.master: Creation complete after 3s [id=S25-core-course-labs]
github_branch_protection.default: Creation complete after 6s [id=BPR_kwDONxSdk84DioEr]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

## Github Teams

### Terraform apply

```bash
❯ terraform apply -auto-approve
var.token
  GitHub token

  Enter a value:

github_branch_default.main: Refreshing state... [id=BasedLangsRepo]
github_repository.repo: Refreshing state... [id=BasedLangsRepo]
github_branch_protection.default: Refreshing state... [id=BPR_kwDON1iTjc4DioRL]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place
  - destroy

Terraform will perform the following actions:

  # github_branch_default.main will be destroyed
  # (because github_branch_default.main is not in configuration)
  - resource "github_branch_default" "main" {
      - branch     = "main" -> null
      - id         = "BasedLangsRepo" -> null
      - repository = "BasedLangsRepo" -> null
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      - has_downloads               = true -> null
      - has_projects                = true -> null
      ~ has_wiki                    = true -> false
        id                          = "BasedLangsRepo"
        name                        = "BasedLangsRepo"
      - vulnerability_alerts        = true -> null
        # (31 unchanged attributes hidden)
    }

  # github_team.golang_team will be created
  + resource "github_team" "golang_team" {
      + create_default_maintainer = false
      + description               = "Team consisting of (slightly less) based go devs"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Golangers"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.rust_team will be created
  + resource "github_team" "rust_team" {
      + create_default_maintainer = false
      + description               = "Team consisting of based rust devs"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Rustaceans"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.golang_team_access will be created
  + resource "github_team_repository" "golang_team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "BasedLangsRepo"
      + team_id    = (known after apply)
    }

  # github_team_repository.rust_team_access will be created
  + resource "github_team_repository" "rust_team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "BasedLangsRepo"
      + team_id    = (known after apply)
    }

Plan: 4 to add, 1 to change, 1 to destroy.
github_branch_default.main: Destroying... [id=BasedLangsRepo]
github_team.golang_team: Creating...
github_team.rust_team: Creating...
github_branch_default.main: Destruction complete after 1s
github_repository.repo: Modifying... [id=BasedLangsRepo]
github_team.golang_team: Still creating... [10s elapsed]
github_team.rust_team: Still creating... [10s elapsed]
github_repository.repo: Still modifying... [id=BasedLangsRepo, 10s elapsed]
github_team.golang_team: Creation complete after 12s [id=12132304]
github_team.rust_team: Creation complete after 13s [id=12132305]
github_repository.repo: Modifications complete after 13s [id=BasedLangsRepo]
github_team_repository.rust_team_access: Creating...
github_team_repository.golang_team_access: Creating...
github_team_repository.rust_team_access: Creation complete after 3s [id=12132305:BasedLangsRepo]
github_team_repository.golang_team_access: Creation complete after 4s [id=12132304:BasedLangsRepo]

Apply complete! Resources: 4 added, 1 changed, 1 destroyed.
```
