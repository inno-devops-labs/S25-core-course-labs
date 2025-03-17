# Terraform

## Best Practicies

* Use `.gitignore` in order not to push sensitive data from `terraform.tfstate` file (It is better to keep it in your S3 bucket).

* Use `terraform fmt` and `terraform validate` to format and check correctness of your code.

* It is better to review changes with `terraform plan` first before agree on `terraform apply`

* Use `variables.tf` in order not to hardcode variables and mark sensitive with flag `sensitive = true`

* Specify exact versions in `terraform required_providers`

* Define variables in `.tfvars` or environment variables, but do not push them in repo

## Docker Infrastructure Using Terraform

### `terraform state list` command output

```bash
ebob@laptop docker_terraform % terraform state list

docker_container.app_python_container
docker_container.app_ruby_container
```

### `terraform state show <resource_address>` command output

```bash
ebob@laptop docker_terraform % terraform state show docker_container.app_python_container
# docker_container.app_python_container:
resource "docker_container" "app_python_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "gunicorn",
        "-w",
        "4",
        "-b",
        "0.0.0.0:8080",
        "app:app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "49cc30c669fa"
    id                                          = "49cc30c669fa8a39fab6ee8f89f43c269dd1a245a6f5629dafc7fa478dc69292"
    image                                       = "sha256:6dbe2f8b0f5e842457c6d2a4df1cae14e8f07dde54194a3b67fa6671be7d8d3b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "msk"
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
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### `terraform output` command

```bash
ebob@laptop docker_terraform % terraform output
container_id_python = "49cc30c669fa8a39fab6ee8f89f43c269dd1a245a6f5629dafc7fa478dc69292"
container_id_ruby = "053cc71da7897e90ef78158ff045377e56e1d228b340788a16ade2c91f49460c"
container_image_python = "ebob/moscow-time:v1.0"
container_image_ruby = "ebob/omsk-time:v1.0"
container_name_python = "msk"
container_name_ruby = "omsk"
container_port_python = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_port_ruby = tolist([
  {
    "external" = 8081
    "internal" = 4567
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud Using Terraform

### Getting started

First of all, read [official guide from Yandex Cloud about Terraform](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart). Then, visit [Yandex Cloud Provider on Terraform Registry](https://registry.terraform.io/providers/yandex-cloud/yandex/latest/docs). After that, we can start by creating service account and getting [IAM token](https://yandex.cloud/en-ru/docs/iam/operations/iam-token/create-for-sa).

### `terraform plan`

```bash
ebob@laptop yandex_cloud_terraform % terraform plan
var.cloud_id
  Yandex Cloud ID

  Enter a value:

var.folder_id
  Yandex Folder ID

  Enter a value:

var.iam_token
  Enter a value:


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.disk-1 will be created
  + resource "yandex_compute_disk" "disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8k2ed4jspu35gfde1u"
      + name        = "disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-b"

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
      + hostname                  = "vm-1"
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "vm-1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-b"

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
          + core_fraction = 20
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy {
          + preemptible = true
        }
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet-1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.1.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-b"
    }

Plan: 4 to add, 0 to change, 0 to destroy.
```

### `terraform apply`

```bash
ebob@laptop yandex_cloud_terraform % terraform apply
var.cloud_id
  Yandex Cloud ID

  Enter a value:

var.folder_id
  Yandex Folder ID

  Enter a value:

var.iam_token
  Enter a value:


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.disk-1 will be created
  + resource "yandex_compute_disk" "disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8k2ed4jspu35gfde1u"
      + name        = "disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-b"

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
      + hostname                  = "vm-1"
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "vm-1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-b"

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
          + core_fraction = 20
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy {
          + preemptible = true
        }
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet-1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.1.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-b"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 5s [id=enp5ntrp4t5tvdbp0052]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e2l1hqpsrv83hq97m16t]
yandex_compute_disk.disk-1: Still creating... [10s elapsed]
yandex_compute_disk.disk-1: Creation complete after 12s [id=epdh7buhebqifudk67p4]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Creation complete after 43s [id=epd6avjtflh4nqkrg2an]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```

### `terraform state list`

```bash
ebob@laptop yandex_cloud_terraform % terraform state list
yandex_compute_disk.disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### `terraform state show`

#### `yandex_vpc_network.network-1`

```bash
ebob@laptop yandex_cloud_terraform % terraform state show yandex_vpc_network.network-1
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-03T20:35:24Z"
    default_security_group_id = "enpno7pvi66b7gepf4sr"
    description               = null
    folder_id                 = "b1ghr0ljvdknal1p1q6g"
    id                        = "enp5ntrp4t5tvdbp0052"
    labels                    = {}
    name                      = "network-1"
    subnet_ids                = []
}
```

#### `yandex_vpc_subnet.subnet-1`

```bash
ebob@laptop yandex_cloud_terraform % terraform state show yandex_vpc_subnet.subnet-1
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-03T20:35:27Z"
    description    = null
    folder_id      = "b1ghr0ljvdknal1p1q6g"
    id             = "e2l1hqpsrv83hq97m16t"
    labels         = {}
    name           = "subnet-1"
    network_id     = "enp5ntrp4t5tvdbp0052"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.1.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}
```

#### `yandex_compute_disk.disk-1`

```bash
ebob@laptop yandex_cloud_terraform % terraform state show yandex_compute_disk.disk-1
# yandex_compute_disk.disk-1:
resource "yandex_compute_disk" "disk-1" {
    block_size  = 4096
    created_at  = "2025-02-03T20:35:24Z"
    description = null
    folder_id   = "b1ghr0ljvdknal1p1q6g"
    id          = "epdh7buhebqifudk67p4"
    image_id    = "fd8k2ed4jspu35gfde1u"
    name        = "disk-1"
    product_ids = [
        "f2ekpu3f32a5gg9e40kq",
    ]
    size        = 20
    snapshot_id = null
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-b"

    disk_placement_policy {
        disk_placement_group_id = null
    }

    hardware_generation {
        legacy_features {
            pci_topology = "PCI_TOPOLOGY_V1"
        }
    }
}
```

#### `yandex_compute_instance.vm-1`

```bash
ebob@laptop yandex_cloud_terraform % terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-03T20:35:35Z"
    description               = null
    folder_id                 = "b1ghr0ljvdknal1p1q6g"
    fqdn                      = "vm-1.ru-central1.internal"
    gpu_cluster_id            = null
    hardware_generation       = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    hostname                  = "vm-1"
    id                        = "epd6avjtflh4nqkrg2an"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "vm-1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v2"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epdh7buhebqifudk67p4"
        disk_id     = "epdh7buhebqifudk67p4"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd8k2ed4jspu35gfde1u"
            kms_key_id  = null
            name        = "disk-1"
            size        = 20
            snapshot_id = null
            type        = "network-hdd"
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
        ip_address         = "192.168.1.29"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:65:7e:7d:7d"
        nat                = true
        nat_ip_address     = "84.201.163.253"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e2l1hqpsrv83hq97m16t"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
        placement_group_partition = 0
    }

    resources {
        core_fraction = 20
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = true
    }
}
```

<img width="1399" alt="Yandex Cloud VM" src="https://github.com/user-attachments/assets/048762b4-3700-4909-a949-a3406ea2713f" />

## GitHub Terraform

### Import with `terraform import`

```bash
ebob@laptop github_terraform % terraform import "github_repository.repo" "devops-labs"
var.github_token
  GitHub personal access token

  Enter a value:

github_repository.repo: Importing from ID "devops-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=devops-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Apply changes

```bash
ebob@laptop github_terraform % terraform apply
var.github_token
  GitHub personal access token

  Enter a value:

github_repository.repo: Refreshing state... [id=devops-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-labs"
    }

  # github_branch_protection.master will be created
  + resource "github_branch_protection" "master" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "master"
      + repository_id                   = "R_kgDONuYNyA"
      + require_conversation_resolution = false
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + dismiss_stale_reviews           = true
          + require_code_owner_reviews      = true
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }

      + required_status_checks {
          + strict = true
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "Innopolis University DevOps Course Labs"
      ~ has_projects                = true -> false
      ~ has_wiki                    = true -> false
        id                          = "devops-labs"
        name                        = "devops-labs"
        # (33 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=devops-labs]
github_repository.repo: Modifications complete after 2s [id=devops-labs]
github_branch_default.master: Creating...
github_branch_protection.master: Creating...
github_branch_default.master: Creation complete after 3s [id=devops-labs]
github_branch_protection.master: Creation complete after 5s [id=BPR_kwDONuYNyM4DiLyy]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

## GitHub Teams Terraform

Organization: [Bobkunov](https://github.com/Bobkunov)

Repo: [phoenix-project](https://github.com/Bobkunov/phoenix-project)

Teams: [Developers, DevOps, QA](https://github.com/orgs/Bobkunov/teams)

```bash
ebob@laptop github_teams_terraform % terraform state list
github_branch_default.main
github_branch_protection.repo_protection
github_repository.repo
github_team.developers
github_team.devops
github_team.qa
github_team_repository.developers_access
github_team_repository.devops_access
github_team_repository.qa_access
```
