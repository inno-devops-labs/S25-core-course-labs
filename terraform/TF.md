# Terraform

## Docker

### `terraform state show` command:
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
    hostname                                    = "e70ea0b9adbf"
    id                                          = "e70ea0b9adbf74f94aef1adf217b428c60f3c61694e7c532fcf387c31dbde08c"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.18.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.18.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:12:00:02"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}
```

### `terraform state list` command:
```bash
docker_container.nginx
docker_image.nginx
```

### `terraform apply` command:
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
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
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "tutorial"
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
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "nginx:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Creation complete after 22s [id=sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=e70ea0b9adbf74f94aef1adf217b428c60f3c61694e7c532fcf387c31dbde08c]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

### Docker `terraform apply` command:
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.moscow_time will be created
  + resource "docker_container" "moscow_time" {
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
      + image                                       = "zerohalf/moscow-time-app:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "moscow-time"
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
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + py_container_id    = (known after apply)
  + py_container_ports = [
      + {
          + external = 8080
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.moscow_time: Creating...
docker_container.moscow_time: Creation complete after 1s [id=86d3af762178771050ee14e56aa0f799d8bff7b36ddbf5a01649dd76048b4ae6]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

### Docker `terraform output` command:
```bash
py_container_id = "86d3af762178771050ee14e56aa0f799d8bff7b36ddbf5a01649dd76048b4ae6"
py_container_ports = tolist([
  {
    "external" = 8080
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

### Yandex Cloud `terraform apply` command:
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.vm-disk will be created
  + resource "yandex_compute_disk" "vm-disk" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1g8vmvbqqgf9d94hnv1"
      + id          = (known after apply)
      + image_id    = "fd85u0rct32prepgjlv0"
      + name        = "nikita-disk"
      + product_ids = (known after apply)
      + size        = 10
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_instance.vm will be created
  + resource "yandex_compute_instance" "vm" {
      + created_at                = (known after apply)
      + folder_id                 = "b1g8vmvbqqgf9d94hnv1"
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hardware_generation       = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "nikita-vm"
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

          + initialize_params (known after apply)
        }

      + metadata_options (known after apply)

      + network_interface {
          + index              = 1
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = false
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 20
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy {
          + preemptible = true
        }
    }

  # yandex_vpc_network.nikita-net will be created
  + resource "yandex_vpc_network" "nikita-net" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = "b1g8vmvbqqgf9d94hnv1"
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "nikita-network"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.nikita-subnet will be created
  + resource "yandex_vpc_subnet" "nikita-subnet" {
      + created_at     = (known after apply)
      + folder_id      = "b1g8vmvbqqgf9d94hnv1"
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = (known after apply)
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.0.0/16",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.nikita-net: Creating...
yandex_compute_disk.vm-disk: Creating...
yandex_vpc_network.nikita-net: Creation complete after 1s [id=enpodc0e8tlv0kka8ih4]
yandex_vpc_subnet.nikita-subnet: Creating...
yandex_vpc_subnet.nikita-subnet: Creation complete after 1s [id=e9bllm8me53jej753ke0]
yandex_compute_disk.vm-disk: Creation complete after 7s [id=fhmo4c9liv83re0vnhc7]
yandex_compute_instance.vm: Creating...
yandex_compute_instance.vm: Still creating... [10s elapsed]
yandex_compute_instance.vm: Still creating... [20s elapsed]
yandex_compute_instance.vm: Still creating... [30s elapsed]
yandex_compute_instance.vm: Still creating... [40s elapsed]
yandex_compute_instance.vm: Creation complete after 47s [id=fhmuair6ugmnbqacmtrj]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```

### Yandex Cloud `terraform destroy` command:
```bash
yandex_vpc_network.nikita-net: Refreshing state... [id=enpodc0e8tlv0kka8ih4]
yandex_compute_disk.vm-disk: Refreshing state... [id=fhmo4c9liv83re0vnhc7]
yandex_vpc_subnet.nikita-subnet: Refreshing state... [id=e9bllm8me53jej753ke0]
yandex_compute_instance.vm: Refreshing state... [id=fhmuair6ugmnbqacmtrj]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # yandex_compute_disk.vm-disk will be destroyed
  - resource "yandex_compute_disk" "vm-disk" {
      - block_size  = 4096 -> null
      - created_at  = "2025-02-05T19:01:57Z" -> null
      - folder_id   = "b1g8vmvbqqgf9d94hnv1" -> null
      - id          = "fhmo4c9liv83re0vnhc7" -> null
      - image_id    = "fd85u0rct32prepgjlv0" -> null
      - labels      = {} -> null
      - name        = "nikita-disk" -> null
      - product_ids = [
          - "f2ef01lju2nsansfdahf",
        ] -> null
      - size        = 10 -> null
      - status      = "ready" -> null
      - type        = "network-hdd" -> null
      - zone        = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)

      - disk_placement_policy {
            # (1 unchanged attribute hidden)
        }

      - hardware_generation {
          - legacy_features {
              - pci_topology = "PCI_TOPOLOGY_V1" -> null
            }
        }
    }

  # yandex_compute_instance.vm will be destroyed
  - resource "yandex_compute_instance" "vm" {
      - created_at                = "2025-02-05T19:02:04Z" -> null
      - folder_id                 = "b1g8vmvbqqgf9d94hnv1" -> null
      - fqdn                      = "fhmuair6ugmnbqacmtrj.auto.internal" -> null
      - hardware_generation       = [
          - {
              - generation2_features = []
              - legacy_features      = [
                  - {
                      - pci_topology = "PCI_TOPOLOGY_V1"
                    },
                ]
            },
        ] -> null
      - id                        = "fhmuair6ugmnbqacmtrj" -> null
      - labels                    = {} -> null
      - metadata                  = {
          - "ssh-keys" = (sensitive value)
        } -> null
      - name                      = "nikita-vm" -> null
      - network_acceleration_type = "standard" -> null
      - platform_id               = "standard-v1" -> null
      - status                    = "running" -> null
      - zone                      = "ru-central1-a" -> null
        # (5 unchanged attributes hidden)

      - boot_disk {
          - auto_delete = true -> null
          - device_name = "fhmo4c9liv83re0vnhc7" -> null
          - disk_id     = "fhmo4c9liv83re0vnhc7" -> null
          - mode        = "READ_WRITE" -> null

          - initialize_params {
              - block_size  = 4096 -> null
              - image_id    = "fd85u0rct32prepgjlv0" -> null
              - name        = "nikita-disk" -> null
              - size        = 10 -> null
              - type        = "network-hdd" -> null
                # (3 unchanged attributes hidden)
            }
        }

      - metadata_options {
          - aws_v1_http_endpoint = 1 -> null
          - aws_v1_http_token    = 2 -> null
          - gce_http_endpoint    = 1 -> null
          - gce_http_token       = 1 -> null
        }

      - network_interface {
          - index              = 0 -> null
          - ip_address         = "192.168.0.4" -> null
          - ipv4               = true -> null
          - ipv6               = false -> null
          - mac_address        = "d0:0d:1e:54:b6:6f" -> null
          - nat                = false -> null
          - security_group_ids = [] -> null
          - subnet_id          = "e9bllm8me53jej753ke0" -> null
            # (3 unchanged attributes hidden)
        }

      - placement_policy {
          - host_affinity_rules       = [] -> null
          - placement_group_partition = 0 -> null
            # (1 unchanged attribute hidden)
        }

      - resources {
          - core_fraction = 20 -> null
          - cores         = 2 -> null
          - gpus          = 0 -> null
          - memory        = 2 -> null
        }

      - scheduling_policy {
          - preemptible = true -> null
        }
    }

  # yandex_vpc_network.nikita-net will be destroyed
  - resource "yandex_vpc_network" "nikita-net" {
      - created_at                = "2025-02-05T19:01:57Z" -> null
      - default_security_group_id = "enp4cdldouagsagt63rd" -> null
      - folder_id                 = "b1g8vmvbqqgf9d94hnv1" -> null
      - id                        = "enpodc0e8tlv0kka8ih4" -> null
      - labels                    = {} -> null
      - name                      = "nikita-network" -> null
      - subnet_ids                = [
          - "e9bllm8me53jej753ke0",
        ] -> null
        # (1 unchanged attribute hidden)
    }

  # yandex_vpc_subnet.nikita-subnet will be destroyed
  - resource "yandex_vpc_subnet" "nikita-subnet" {
      - created_at     = "2025-02-05T19:01:58Z" -> null
      - folder_id      = "b1g8vmvbqqgf9d94hnv1" -> null
      - id             = "e9bllm8me53jej753ke0" -> null
      - labels         = {} -> null
        name           = null
      - network_id     = "enpodc0e8tlv0kka8ih4" -> null
      - v4_cidr_blocks = [
          - "192.168.0.0/16",
        ] -> null
      - v6_cidr_blocks = [] -> null
      - zone           = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

yandex_compute_instance.vm: Destroying... [id=fhmuair6ugmnbqacmtrj]
yandex_compute_instance.vm: Still destroying... [id=fhmuair6ugmnbqacmtrj, 10s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhmuair6ugmnbqacmtrj, 20s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhmuair6ugmnbqacmtrj, 30s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhmuair6ugmnbqacmtrj, 40s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhmuair6ugmnbqacmtrj, 50s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhmuair6ugmnbqacmtrj, 1m0s elapsed]
yandex_compute_instance.vm: Destruction complete after 1m3s
yandex_vpc_subnet.nikita-subnet: Destroying... [id=e9bllm8me53jej753ke0]
yandex_compute_disk.vm-disk: Destroying... [id=fhmo4c9liv83re0vnhc7]
yandex_compute_disk.vm-disk: Destruction complete after 0s
yandex_vpc_subnet.nikita-subnet: Destruction complete after 3s
yandex_vpc_network.nikita-net: Destroying... [id=enpodc0e8tlv0kka8ih4]
yandex_vpc_network.nikita-net: Destruction complete after 1s

Destroy complete! Resources: 4 destroyed.
```

### Challenges of working with Yandex Cloud provider:
1. Hard to understand what roles should be applied to service-account to successfully work with compute resources.
2. Hard to get free-tier compute instances because of already spent money in Yandex Cloud.

### Github `terraform apply` command:
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "S25-core-course-labs-terraform"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "master"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 0
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
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Repository for DevOps Course"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "S25-core-course-labs-terraform"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
      + web_commit_signoff_required = false

      + security_and_analysis (known after apply)
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes
```

### GitHub `terraform apply` command:
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main_branch will be created
  + resource "github_branch_default" "main_branch" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-teams"
    }

  # github_branch_protection.repo_protection will be created
  + resource "github_branch_protection" "repo_protection" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repository will be created
  + resource "github_repository" "repository" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Collaborative repository"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = false
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-teams"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
      + web_commit_signoff_required = false

      + security_and_analysis (known after apply)
    }

  # github_team.contributors will be created
  + resource "github_team" "contributors" {
      + create_default_maintainer = false
      + description               = "Contributors from open-source"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Repository contributors"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.maintainers will be created
  + resource "github_team" "maintainers" {
      + create_default_maintainer = false
      + description               = "Initial developers"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Repository maintainers"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.contributors will be created
  + resource "github_team_repository" "contributors" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "devops-teams"
      + team_id    = (known after apply)
    }

  # github_team_repository.maintainers will be created
  + resource "github_team_repository" "maintainers" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "devops-teams"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes
```