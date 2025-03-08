# Terraform

## ✅ Best Practices

### Code organization

Terraform code is separated into `main.tf`, `variables.tf`, and `outputs.tf` files to ensure modularity.

### Version Constraints

Specifying Terraform and provider versions to avoid unexpected updates.

### Secrets

Secrets are stored in a `terraform.tfvars` file, which is added to the `.gitignore` file to prevent accidental pushes to VCS.

### Validating and Formating

Using `terraform validate` and `terraform fmt` to ensure the code is correct.

### Checking Changes

Using `terraform plan` to check the changes and review them.

## 🐳 Docker

### `terraform state list`

<details>
<summary>Open output</summary>

```cmd
terraform\docker> terraform state list
docker_container.go_webapp_container
docker_container.python_webapp_container
```

</details>

### `terraform state show`

<details>
<summary>Open output for <code>go_webapp_container</code></summary>

```cmd
terraform\docker> terraform state show "docker_container.go_webapp_container"
# docker_container.go_webapp_container:
resource "docker_container" "go_webapp_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "./main",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "bca5ec05c65b"
    id                                          = "bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5"
    image                                       = "sha256:6d0d98f28c37ef4532818791d4ab3dbfff3c1a44ef5ec659a0049e0c2d0902da"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "simple-go-web-app"
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
    user                                        = "65532"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8889
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

</details>

<details>
<summary>Open output for <code>python_webapp_container</code></summary>

```cmd
terraform\docker> terraform state show "docker_container.python_webapp_container"
# docker_container.python_webapp_container:
resource "docker_container" "python_webapp_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "python3",
        "-m",
        "uvicorn",
        "src.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    env                                         = []
    hostname                                    = "086c159c3c0f"
    id                                          = "086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd"
    image                                       = "sha256:59ec04c580e02fa680d711283a4453ed3ef952efcf2254349b6f0b3642bf164d"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "simple-python-web-app"
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
    user                                        = "65532"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8888
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

</details>

### `terraform apply`

<details>
<summary>Open output</summary>

```cmd
terraform\docker> terraform apply
docker_container.go_webapp_container: Refreshing state... [id=bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5]
docker_container.python_webapp_container: Refreshing state... [id=086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.go_webapp_container must be replaced
-/+ resource "docker_container" "go_webapp_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "./main",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "bca5ec05c65b" -> (known after apply)
      ~ id                                          = "bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5" -> (known after apply)
      ~ image                                       = "sha256:6d0d98f28c37ef4532818791d4ab3dbfff3c1a44ef5ec659a0049e0c2d0902da" -> "magicwinnie/simple-go-web-app-distroless:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "simple-go-web-app"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.3"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:03"
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
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "65532" -> null
      - working_dir                                 = "/app" -> null
        # (17 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

  # docker_container.python_webapp_container must be replaced
-/+ resource "docker_container" "python_webapp_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python3",
          - "-m",
          - "uvicorn",
          - "src.main:app",
          - "--host",
          - "0.0.0.0",
          - "--port",
          - "8000",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "086c159c3c0f" -> (known after apply)
      ~ id                                          = "086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd" -> (known after apply)
      ~ image                                       = "sha256:59ec04c580e02fa680d711283a4453ed3ef952efcf2254349b6f0b3642bf164d" -> "magicwinnie/simple-python-web-app-distroless:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "simple-python-web-app"
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
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "65532" -> null
      - working_dir                                 = "/app" -> null
        # (17 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ go_webapp_container_id        = "bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5" -> (known after apply)
  ~ python_webapp_container_id    = "086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.python_webapp_container: Destroying... [id=086c159c3c0f4b79f25dd25976be3dcc82822c303f757cacf77e3f50f095f6fd]
docker_container.go_webapp_container: Destroying... [id=bca5ec05c65bd4389925295b5574fa0420f3e292783e7b5399b472e445b297d5]
docker_container.python_webapp_container: Destruction complete after 1s
docker_container.python_webapp_container: Creating...
docker_container.go_webapp_container: Destruction complete after 1s
docker_container.go_webapp_container: Creating...
docker_container.python_webapp_container: Creation complete after 1s [id=9b5a080d975792982f448bf6e0e4483a8ee22a82d41ea35ac432f85d3c117879]
docker_container.go_webapp_container: Creation complete after 1s [id=4543e13edccd66550643ea88efc43fabe8c0e9c0882e44d2cacd35aa745ba496]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

go_webapp_container_id = "4543e13edccd66550643ea88efc43fabe8c0e9c0882e44d2cacd35aa745ba496"
go_webapp_container_ports = tolist([
  {
    "external" = 8889
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
python_webapp_container_id = "9b5a080d975792982f448bf6e0e4483a8ee22a82d41ea35ac432f85d3c117879"
python_webapp_container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

### `terraform output`

<details>
<summary>Open output</summary>

```cmd
terraform\docker> terraform output
go_webapp_container_id = "4543e13edccd66550643ea88efc43fabe8c0e9c0882e44d2cacd35aa745ba496"
go_webapp_container_ports = tolist([
  {
    "external" = 8889
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
python_webapp_container_id = "9b5a080d975792982f448bf6e0e4483a8ee22a82d41ea35ac432f85d3c117879"
python_webapp_container_ports = tolist([
  {
    "external" = 8888
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

</details>

## ☁️ Yandex Cloud

I followed the tutorial: <https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart>.

There was a difficulty following it, in my opinion, the tutorial could be structured much better.

Terraform was already installed on my laptop, also I had already a Yandex Cloud account, but with not activated free trial.

I decided to follow the steps using the Yandex Cloud CLI, which I had to install. It was very easy.

I chose managing resources on behalf of my Yandex account, which looked simplier than using the service accounts. Using `yc init` I logged into my account and set the default cloud and folder. Also, using provided commands for PowerShell, I set the needed environmental variables and setup a `terraform.rc` file.

I created minimal `main.tf` file with `required_providers` section per tutorial and ran `terraform init`.

Then using their full template, I modified it to exclude second VM settings. Then I separated `main.tf` into `outputs.tf` and `variables.tf`.

### `terraform plan`

<details>
<summary>Open output</summary>

```cmd
terraform\yandex_cloud> terraform plan

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
      + image_id    = "fd8bpal18cm4kprpjc2m"
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

</details>

### `terraform apply`

<details>
<summary>Open output</summary>

```cmd
terraform\yandex_cloud> terraform apply

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

</details>

### `terraform output`

<details>
<summary>Open output</summary>

```cmd
terraform\yandex_cloud> terraform output
external_ip_address_vm_1 = "89.169.141.93"
internal_ip_address_vm_1 = "192.168.0.11"
```

</details>

## 👾 Github

### `terraform import`

<details>
<summary>Open output</summary>

```cmd
terraform\github> terraform import "github_repository.repo" "S25-core-course-labs"
github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

</details>

### `terraform apply`

<details>
<summary>Open output</summary>

```cmd
terraform\github> terraform apply
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
      ~ auto_init                   = false -> true
      + description                 = "DevOps course labs solution"
      + gitignore_template          = "Python"
      - has_downloads               = true -> null
      - has_projects                = true -> null
      ~ has_wiki                    = true -> false
        id                          = "S25-core-course-labs"
      + license_template            = "mit"
        name                        = "S25-core-course-labs"
        # (28 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDONudjxc4DicAO]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

</details>

## 🤝 Github Teams

<details>
<summary>Open output</summary>

```cmd
terraform\github_teams> terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "Sus25-core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
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
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + branches                    = (known after apply)
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "DevOps course labs solution"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + gitignore_template          = "Go"
      + has_issues                  = false
      + has_wiki                    = false
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "Sus25-core-course-labs"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

  # github_team.dev_team will be created
  + resource "github_team" "dev_team" {
      + create_default_maintainer = false
      + description               = "Team responsible for development"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Developers"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.qa_team will be created
  + resource "github_team" "qa_team" {
      + create_default_maintainer = false
      + description               = "Quality assurance team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "QA"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.dev_team_access will be created
  + resource "github_team_repository" "dev_team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "Sus25-core-course-labs"
      + team_id    = (known after apply)
    }

  # github_team_repository.qa_team_access will be created
  + resource "github_team_repository" "qa_team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "triage"
      + repository = "Sus25-core-course-labs"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.dev_team: Creating...
github_team.qa_team: Creating...
github_repository.repo: Creating...
github_team.dev_team: Still creating... [10s elapsed]
github_team.qa_team: Still creating... [10s elapsed]
github_repository.repo: Still creating... [10s elapsed]
github_team.dev_team: Creation complete after 14s [id=12119265]
github_team.qa_team: Creation complete after 14s [id=12119266]
github_repository.repo: Creation complete after 14s [id=Sus25-core-course-labs]
github_team_repository.qa_team_access: Creating...
github_branch_default.main: Creating...
github_team_repository.dev_team_access: Creating...
github_branch_protection.default: Creating...
github_branch_default.main: Creation complete after 2s [id=Sus25-core-course-labs]
github_team_repository.qa_team_access: Creation complete after 8s [id=12119266:Sus25-core-course-labs]
github_team_repository.dev_team_access: Creation complete after 9s [id=12119265:Sus25-core-course-labs]
github_branch_protection.default: Still creating... [10s elapsed]
github_branch_protection.default: Creation complete after 10s [id=BPR_kwDON0waXs4DicR4]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```

</details>
