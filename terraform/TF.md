# Terraform

## Best practices

- enviroment variables for hiding secrets
- add `.gitignore` for Terraform
- use `terraform validate` and `terraform fmt` for well-written HCL code

## Docker

1. List: `terraform state list`

```bash
docker_container.moscow_time
```

2. `terraform state show docker_container.moscow_time`

```bash
resource "docker_container" "moscow_time" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "gunicorn",
        "--bind",
        "0.0.0.0:8080",
        "--workers",
        "2",
        "app:app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "14c6554dfcdf"
    id                                          = "14c6554dfcdfb67827a06f4f25315d4383fda47fae2787d100fbd83faa149069"
    image                                       = "sha256:54560d6673ae8742705bea60d05fd97256db024819e068bb5d6992d02cbd4d07"
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
    user                                        = "app_python_user"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

3. Apply changes: `terraform apply`

```bash
docker_container.moscow_time: Refreshing state... [id=14c6554dfcdfb67827a06f4f25315d4383fda47fae2787d100fbd83faa149069]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.moscow_time must be replaced
-/+ resource "docker_container" "moscow_time" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "gunicorn",
          - "--bind",
          - "0.0.0.0:8080",
          - "--workers",
          - "2",
          - "app:app",
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
      ~ hostname                                    = "14c6554dfcdf" -> (known after apply)
      ~ id                                          = "14c6554dfcdfb67827a06f4f25315d4383fda47fae2787d100fbd83faa149069" -> (known after apply)
      ~ image                                       = "sha256:54560d6673ae8742705bea60d05fd97256db024819e068bb5d6992d02cbd4d07" -> "adeepresession/app_python:v1.0" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "app_python"
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
      - user                                        = "app_python_user" -> null
      - working_dir                                 = "/app_python" -> null
        # (17 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id    = "14c6554dfcdfb67827a06f4f25315d4383fda47fae2787d100fbd83faa149069" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.moscow_time: Destroying... [id=14c6554dfcdfb67827a06f4f25315d4383fda47fae2787d100fbd83faa149069]
docker_container.moscow_time: Destruction complete after 0s
docker_container.moscow_time: Creating...
docker_container.moscow_time: Creation complete after 1s [id=987b55d4adff1580dbe173886658888eafee84447b59514ecda30b8bd1f7cdbc]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "987b55d4adff1580dbe173886658888eafee84447b59514ecda30b8bd1f7cdbc"
container_image = "adeepresession/app_python:v1.0"
container_name = "app_python"
container_port = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

5. Show outputs: `terraform output`

```bash
container_id = "987b55d4adff1580dbe173886658888eafee84447b59514ecda30b8bd1f7cdbc"
container_image = "adeepresession/app_python:v1.0"
container_name = "app_python"
container_port = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## GitHub

### `terraform apply`

```bash

var.token
  GitHub PAT

  Enter a value:

github_repository.repo: Refreshing state... [id=devops-terraform]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "devops-terraform"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = "devops-terraform"
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

github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 1s [id=devops-terraform]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDON0PfZM4DiTQA]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.


```

## Yandex Cloud

### Yandex `terraform state list`

```text
yandex_compute_instance.vm
yandex_vpc_network.network
yandex_vpc_subnet.subnet
```

### Yandex `terraform state show yandex_compute_instance.vm`

```text
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2025-02-04T20:43:36Z"
    folder_id                 = "b1go3pon6gei7cgqs6oi"
    fqdn                      = "epdrml36ofoa9dnspvgh.auto.internal"
    id                        = "epdrml36ofoa9dnspvgh"
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"
    boot_disk {
        auto_delete = true
        device_name = "epdf8do2c0li4j78r1h7"
        disk_id     = "epdf8do2c0li4j78r1h7"
        mode        = "READ_WRITE"
        initialize_params {
            block_size = 4096
            image_id   = "fd83s8u085j3mq231ago"
            size       = 8
            type       = "network-hdd"
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
        ip_address         = "192.168.20.24"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1b:b5:46:6c"
        nat                = true
        nat_ip_address     = "130.193.41.60"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e2lr1osdcac0p53dij7u"
    }
    placement_policy {
        host_affinity_rules       = []
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

### Yandex `terraform state show yandex_vpc_network.network`

```text
# yandex_vpc_network.network:
resource "yandex_vpc_network" "network" {
    created_at                = "2024-02-27T20:43:27Z"
    default_security_group_id = "enpgtreci0r4qulj8tsu"
    folder_id                 = "b1go3pon6gei7cgqs6oi"
    id                        = "enper1j3v785og413vo6"
    labels                    = {}
    name                      = "default"
    subnet_ids                = []
}
```

### Yandex `terraform state show yandex_vpc_subnet.subnet`

```text
# yandex_vpc_subnet.subnet:
resource "yandex_vpc_subnet" "subnet" {
    created_at     = "2024-02-27T20:43:29Z"
    folder_id      = "b1go3pon6gei7cgqs6oi"
    id             = "e2lr1osdcac0p53dij7u"
    labels         = {}
    name           = "Subnet 1"
    network_id     = "enper1j3v785og413vo6"
    v4_cidr_blocks = [
        "192.168.20.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}
```

### Yandex `terraform apply`

```text
var.cloud_id
  Cloud ID
  Enter a value:
var.folder_id
  Foder ID within the cloud
  Enter a value:
var.iam_token
  Specifies IAM token for auth in Yandex Cloud
  Enter a value:
Terraform used the selected providers to generate the following execution plan.
Resource actions are
indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # yandex_compute_instance.vm will be created
  + resource "yandex_compute_instance" "vm" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "terraform-vm"
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
              + image_id    = "fd83s8u085j3mq231ago"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
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
  # yandex_vpc_network.network will be created
  + resource "yandex_vpc_network" "network" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default"
      + subnet_ids                = (known after apply)
    }
  # yandex_vpc_subnet.subnet will be created
  + resource "yandex_vpc_subnet" "subnet" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "Subnet 1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-b"
    }
Plan: 3 to add, 0 to change, 0 to destroy.
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  Enter a value: yes
yandex_vpc_network.network: Creating...
yandex_vpc_network.network: Still creating... [10s elapsed]
yandex_vpc_network.network: Creation complete after 13s [id=enpfirhjkpi1as8edk7g]
yandex_vpc_subnet.subnet: Creating...
yandex_vpc_subnet.subnet: Creation complete after 1s [id=e2l0hp614mfg2d9qk519]
yandex_compute_instance.vm: Creating...
yandex_compute_instance.vm: Still creating... [10s elapsed]
yandex_compute_instance.vm: Still creating... [20s elapsed]
yandex_compute_instance.vm: Still creating... [30s elapsed]
yandex_compute_instance.vm: Still creating... [40s elapsed]
yandex_compute_instance.vm: Still creating... [50s elapsed]
yandex_compute_instance.vm: Still creating... [1m0s elapsed]
yandex_compute_instance.vm: Creation complete after 1m3s [id=epdkmaichijt7capejrp]
Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```
