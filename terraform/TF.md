# Terraform

## Best practices
1. `.gitignore` for Terraform
2. Variables for secrets
3. `terraform fmt`, `terraform validate`, `terraform plan`
4. Outputs

## Docker

I deployed both apps, so there are two containers

### Docker `terraform state list`

```
docker_container.app_python_container
docker_container.app_typescript_container
```

### Docker `terraform state show docker_container.app_python_container`

```
# docker_container.app_python_container:
resource "docker_container" "app_python_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/usr/bin/python3.11",
    ]
    env                                         = []
    hostname                                    = "920ee46e91aa"
    id                                          = "920ee46e91aa7272ff635bb8290b3c2aef1e62c978172d94d0d608a4a439fe4a"
    image                                       = "sha256:088c0c103fd038a11c390a615c2c051b73b7b760f1293d5927ae618639857b37"       
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "inno_devops_lab2_python_bonus"
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
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Docker `terraform state show docker_container.app_typescript_container`

```
# docker_container.app_typescript_container:
resource "docker_container" "app_typescript_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "node_modules/vite/dist/node/cli.js",
        "preview",
        "--host",
        "0.0.0.0",
        "--port",
        "8080",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/nodejs/bin/node",
    ]
    env                                         = []
    hostname                                    = "b698ed14df16"
    id                                          = "b698ed14df1657dfaf643b0bf7d1a85567f41d8ad0a33f42160781035dfa8c61"
    image                                       = "sha256:36529a8f8c43aea6c2b3018481828ac90b0d32bf267cd15641f481deabe0cb0d"       
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "inno_devops_lab2_typescript_bonus"
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
    working_dir                                 = "/usr/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Docker `terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following 
symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_python_container will be created
  + resource "docker_container" "app_python_container" {
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
      + image                                       = "dmhd6219/inno_devops_lab2_python_bonus:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "inno_devops_lab2_python_bonus"
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

  # docker_container.app_typescript_container will be created
  + resource "docker_container" "app_typescript_container" {
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
      + image                                       = "dmhd6219/inno_devops_lab2_typescript_bonus:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "inno_devops_lab2_typescript_bonus"
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

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id_python        = (known after apply)
  + container_id_typescript    = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_typescript_container: Creating...
docker_container.app_python_container: Creating...
docker_container.app_python_container: Still creating... [10s elapsed]
docker_container.app_typescript_container: Still creating... [10s elapsed]
docker_container.app_python_container: Creation complete after 10s [id=920ee46e91aa7272ff635bb8290b3c2aef1e62c978172d94d0d608a4a439fe4a]
docker_container.app_typescript_container: Creation complete after 12s [id=b698ed14df1657dfaf643b0bf7d1a85567f41d8ad0a33f42160781035dfa8c61]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id_python = "920ee46e91aa7272ff635bb8290b3c2aef1e62c978172d94d0d608a4a439fe4a"
container_id_typescript = "b698ed14df1657dfaf643b0bf7d1a85567f41d8ad0a33f42160781035dfa8c61"
container_image_python = "dmhd6219/inno_devops_lab2_python_bonus:latest"
container_image_typescript = "dmhd6219/inno_devops_lab2_typescript_bonus:latest"
container_name_python = "inno_devops_lab2_python_bonus"
container_name_typescript = "inno_devops_lab2_typescript_bonus"
container_port_python = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_port_typescript = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud

### Yandex Cloud `terraform state list`

```
yandex_compute_disk.disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Yandex Cloud `terraform state show yandex_compute_disk.disk-1`

```
# yandex_compute_disk.disk-1:
resource "yandex_compute_disk" "disk-1" {
    block_size  = 4096
    created_at  = "2025-02-06T10:56:01Z"
    description = null
    folder_id   = "b1gggn7t8mre67kepjo2"
    id          = "epdpj4cjj4gfi7ridcun"
    image_id    = "fd85u0rct32prepgjlv0"
    name        = "disk-1"
    product_ids = [
        "f2ef01lju2nsansfdahf",
    ]
    size        = 10
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

### Yandex Cloud `terraform state show yandex_compute_disk.disk-1`

```
# yandex_compute_disk.disk-1:
resource "yandex_compute_disk" "disk-1" {
    block_size  = 4096
    created_at  = "2025-02-06T10:56:01Z"
    description = null
    folder_id   = "b1gggn7t8mre67kepjo2"
    id          = "epdpj4cjj4gfi7ridcun"
    image_id    = "fd85u0rct32prepgjlv0"
    name        = "disk-1"
    product_ids = [
        "f2ef01lju2nsansfdahf",
    ]
    size        = 10
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

### Yandex Cloud `terraform state show yandex_vpc_network.network-1`

```
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-06T10:56:01Z"
    default_security_group_id = "enptvd8dupkkj45jk0ij"
    description               = null
    folder_id                 = "b1gggn7t8mre67kepjo2"
    id                        = "enpd8v45mlkp943g3vp2"
    labels                    = {}
    name                      = "network-1"
    subnet_ids                = []
}
```

### Yandex Cloud `terraform state show yandex_vpc_subnet.subnet-1`

```
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-06T10:56:05Z"
    description    = null
    folder_id      = "b1gggn7t8mre67kepjo2"
    id             = "e2lmbu3142pat17n78dn"
    labels         = {}
    name           = "subnet-1"
    network_id     = "enpd8v45mlkp943g3vp2"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.1.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}
```

### Yandex Cloud `terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following 
symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.disk-1 will be created
  + resource "yandex_compute_disk" "disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd85u0rct32prepgjlv0"
      + name        = "disk-1"
      + product_ids = (known after apply)
      + size        = 10
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
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "vm-1"
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
yandex_vpc_network.network-1: Creation complete after 4s [id=enpd8v45mlkp943g3vp2]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e2lmbu3142pat17n78dn]
yandex_compute_disk.disk-1: Still creating... [10s elapsed]
yandex_compute_disk.disk-1: Creation complete after 11s [id=epdpj4cjj4gfi7ridcun]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Creation complete after 30s [id=epdfd4irurp3qcfar08s]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```

## Github

I created repository [devops-lab4-terraform-repo](https://github.com/dmhd6219/devops-lab4-terraform-repo) for this task.

### Github `terraform import "github_repository.repo" "devops-lab4-terraform-repo"`

```
github_repository.repo: Importing from ID "devops-lab4-terraform-repo"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=devops-lab4-terraform-repo]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Github `terraform apply`

```
github_repository.repo: Refreshing state... [id=devops-lab4-terraform-repo]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following 
symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-lab4-terraform-repo"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "devops-lab4-terraform-repo"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 0
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
      + description                 = "Repo created from terraform for lab4 at DevOps course in Innopolis University"
      ~ has_issues                  = true -> false
      ~ has_projects                = true -> false
      ~ has_wiki                    = true -> false
        id                          = "devops-lab4-terraform-repo"
      + license_template            = "mit"
        name                        = "devops-lab4-terraform-repo"
        # (31 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  + default_branch  = "main"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=devops-lab4-terraform-repo]
github_repository.repo: Modifications complete after 2s [id=devops-lab4-terraform-repo]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=devops-lab4-terraform-repo]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDON1R_ac4DiktD]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

Outputs:

default_branch = "main"
repository_id = "devops-lab4-terraform-repo"
repository_name = "devops-lab4-terraform-repo"
```

## Github Teams

I created a [organization](https://github.com/inno-devops-lab4) for this task.

### Github Teams `terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following 
symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-lab4-terraform-teams-repo"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
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
      + description                 = "Repo created from terraform for lab4 at DevOps course in Innopolis University"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_downloads               = true
      + has_issues                  = false
      + has_projects                = false
      + has_wiki                    = false
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-lab4-terraform-teams-repo"
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

  # github_team.developers will be created
  + resource "github_team" "developers" {
      + create_default_maintainer = false
      + description               = "Development Team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Development Team"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.devops will be created
  + resource "github_team" "devops" {
      + create_default_maintainer = false
      + description               = "DevOps Team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "DevOps Team"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.developers_repo will be created
  + resource "github_team_repository" "developers_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "devops-lab4-terraform-teams-repo"
      + team_id    = (known after apply)
    }

  # github_team_repository.devops_repo will be created
  + resource "github_team_repository" "devops_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "devops-lab4-terraform-teams-repo"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + repositories = [
      + {
          + default_branch = "main"
          + id             = (known after apply)
          + name           = "devops-lab4-terraform-teams-repo"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.devops: Creating...
github_team.developers: Creating...
github_repository.repo: Creating...
github_team.developers: Still creating... [10s elapsed]
github_team.devops: Still creating... [10s elapsed]
github_repository.repo: Still creating... [10s elapsed]
github_team.devops: Creation complete after 13s [id=12127797]
github_team.developers: Creation complete after 13s [id=12127798]
github_repository.repo: Creation complete after 14s [id=devops-lab4-terraform-teams-repo]
github_team_repository.devops_repo: Creating...
github_branch_default.main: Creating...
github_team_repository.developers_repo: Creating...
github_branch_default.main: Creation complete after 4s [id=devops-lab4-terraform-teams-repo]
github_branch_protection.default: Creating...
github_team_repository.devops_repo: Creation complete after 5s [id=12127797:devops-lab4-terraform-teams-repo]
github_team_repository.developers_repo: Creation complete after 5s [id=12127798:devops-lab4-terraform-teams-repo]
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDON1R31s4Dikrb]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

repositories = [
  {
    "default_branch" = "main"
    "id" = "devops-lab4-terraform-teams-repo"
    "name" = "devops-lab4-terraform-teams-repo"
  },
]
```