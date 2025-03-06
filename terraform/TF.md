# Terraform

## Best practices

1. Gitignore for Terraform.
2. Use variables for hiding secrets such as Yandex cloud/folder IDs, IAM token,
and the whole configuration via variables with default values.
3. Use `terraform plan` before any applying anything.
4. Use `terraform validate` and `terraform fmt`.
5. Use outputs for verbosity.
6. Use `terraform import` for repos.

## Docker

### Docker `terraform state list`
docker_container.custom_container_python
```text

```

### Docker `terraform state show docker_container.custom_container_python`

```text
# docker_container.custom_container_python:
resource "docker_container" "custom_container_python" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "sh",
        "-c",
        "python3 -m gunicorn --bind 0.0.0.0:8080 app.app:wsgi_app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "3269ef71cf46"
    id                                          = "3269ef71cf466c50bb79c26e6430a3efe923b931e0ed0ce02bd5db1addeec6e1"
    image                                       = "sha256:b55cc9507c69f5b293b57d24e00fbaaade6b1c5ecd68394fef252905879f9bc4"
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
    user                                        = "user"
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

### Docker `terraform apply`

```text
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.custom_container_python will be created
  + resource "docker_container" "custom_container_python" {
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
      + image                                       = "mihdenis85/app_python"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app_python"
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
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

  + python_container_id    = (known after apply)
  + python_container_image = "mihdenis85/app_python"
  + python_container_name  = "app_python"
  + python_container_port  = [
      + {
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.custom_container_python: Creating...
docker_container.custom_container_python: Still creating... [10s elapsed]
docker_container.custom_container_python: Creation complete after 16s [id=1d82cfb7686f0083c385b94b26ddf8f3ee97bad91f7564e7a6f4d1f0f76b44fe]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

python_container_id = "1d82cfb7686f0083c385b94b26ddf8f3ee97bad91f7564e7a6f4d1f0f76b44fe"
python_container_image = "mihdenis85/app_python"
python_container_name = "app_python"
python_container_port = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

### Docker Outputs (terraform output)

```text
python_container_id = "1d82cfb7686f0083c385b94b26ddf8f3ee97bad91f7564e7a6f4d1f0f76b44fe"
python_container_image = "mihdenis85/app_python"
python_container_name = "app_python"
python_container_port = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud

### Yandex `terraform state list`

```text
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Yandex `terraform state show yandex_compute_instance.vm-1`

```text
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-03T19:46:40Z"
    folder_id                 = "b1gujabb231edu4eq25l"
    fqdn                      = "f9k3m2n7b4c6d1p8s0v5.auto.internal"
    id                        = "f9k3m2n7b4c6d1p8s0v5"
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-d"

    boot_disk {
        auto_delete = true
        device_name = "k3m9a1b4c7d2e8f5g0h6"
        disk_id     = "k3m9a1b4c7d2e8f5g0h6"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "x5n2b7v1z4k9m3c6t8p0"
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
        ip_address         = "192.168.10.24"
        ipv4               = true
        ipv6               = false
        mac_address        = "f1:e2:d3:c4:b5:a6"
        nat                = true
        nat_ip_address     = "130.193.41.60"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "a9pl3kty7qwe4z8r1nv7"
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

### Yandex `terraform state show yandex_vpc_network.network-1`

```text
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-03T19:47:40Z"
    default_security_group_id = "defgrp12345abc8eq78y"
    folder_id                 = "b1gujabb231edu4eq25l"
    id                        = "id9q8w7e6r5t4y3vop71"
    labels                    = {}
    name                      = "default"
    subnet_ids                = []
}
```

### Yandex `terraform state show yandex_vpc_subnet.subnet-1`

```text
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-03T19:47:40Z"
    folder_id      = "b1gujabb231edu4eq25l"
    id             = "e2lr1osdcac0p53dij7u"
    labels         = {}
    name           = "Subnet 1"
    network_id     = "enper1j3v785og413vo6"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-d"
}
```

### Yandex `terraform apply`

```text
var.cloud_id
  Cloud ID

  Enter a value:

var.folder_id
  Folder ID within the cloud

  Enter a value:

var.iam_token
  Specifies IAM token for auth in Yandex Cloud

  Enter a value:


Terraform used the selected providers to generate the following execution plan.
Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
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
              + image_id    = "img5ju8mw1zt3ld89ago"
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

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "default"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "Subnet 1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-d"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Still creating... [10s elapsed]
yandex_vpc_network.network-1: Creation complete after 15s [id=enpfrijhpki1as8edk7g]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e2l0hp614mfg2d9qk519]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Still creating... [50s elapsed]
yandex_compute_instance.vm-1: Still creating... [1m0s elapsed]
yandex_compute_instance.vm-1: Creation complete after 1m6s [id=epdkchtamijt6capejrp]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

## Github

### Github `terraform import "github_repository.core-course-labs" "S25-core-course-labs"`

Importing my existing repository:

```text
var.github_pat
  Provides the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value:

github_repository.core-course-labs: Importing from ID "S25-core-course-labs"...
github_repository.core-course-labs: Import prepared!
  Prepared github_repository for import
github_repository.core-course-labs: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Github `terraform apply`

```text
var.github_pat
  Provides the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value:

github_branch_default.main: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.repo_main: Refreshing state... [id=BPR_kwDONvjays4DiJ-0]
github_repository.core-course-labs: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  - destroy

Terraform will perform the following actions:

  # github_branch_default.main will be destroyed
  # (because github_branch_default.main is not in configuration)
  - resource "github_branch_default" "main" {
      - branch     = "master" -> null
      - etag       = "W/\"0497488bd8afc2373e544a51b76c5e8a01b3d192ff201602ba382171bd7d659e\"" -> null
      - id         = "S25-core-course-labs" -> null
      - rename     = false -> null
      - repository = "S25-core-course-labs" -> null
    }

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.repo_main will be destroyed
  # (because github_branch_protection.repo_main is not in configuration)
  - resource "github_branch_protection" "repo_main" {
      - allows_deletions                = false -> null
      - allows_force_pushes             = false -> null
      - enforce_admins                  = true -> null
      - id                              = "BPR_kwDONvjays4DiJ-0" -> null
      - lock_branch                     = false -> null
      - pattern                         = "master" -> null
      - repository_id                   = "S25-core-course-labs" -> null
      - require_conversation_resolution = true -> null
      - require_signed_commits          = false -> null
      - required_linear_history         = false -> null

      - required_pull_request_reviews {
          - dismiss_stale_reviews           = false -> null
          - require_code_owner_reviews      = false -> null
          - require_last_push_approval      = false -> null
          - required_approving_review_count = 1 -> null
          - restrict_dismissals             = false -> null
        }
    }

  # github_branch_protection.repo_master will be created
  + resource "github_branch_protection" "repo_master" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "master"
      + repository_id                   = "S25-core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }
Plan: 2 to add, 0 to change, 2 to destroy.

github_branch_protection.repo_main: Destroying... [id=BPR_kwDONvjays4DiJ-0]
github_branch_default.master: Creating...
github_branch_protection.repo_main: Destruction complete after 1s
github_branch_default.main: Destroying... [id=S25-core-course-labs]
github_branch_default.main: Destruction complete after 3s
github_branch_default.master: Creation complete after 5s [id=S25-core-course-labs]
github_branch_protection.repo_master: Creating...
github_branch_protection.repo_master: Creation complete after 4s [id=BPR_kwDONvjays4DiJ_V]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

default_branch = "master"
repository_id = "S25-core-course-labs"
repository_name = "S25-core-course-labs"
```
