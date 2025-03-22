# Terraform 

### Best practices
* **Lint**: checked with `terraform validate` and `terraform fmt`, everything is valid
* **Gitignore**: use of `.gitignore` at the terraform folder for all
sub directories
* **Security**: secret info is stored securely

## Docker

### `terraform state list`

```
docker_container.node_app
docker_container.python_app
docker_image.node_app
docker_image.python_app
```

* ### `terraform state show docker_container.python_app`

```
# docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python3",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "8fd2f30cca87"
    id                                          = "8fd2f30cca87534eecb45529ca7da9c1480e5130384ae93f120d4c1b2d5d7c93"
    image                                       = "sha256:1f60cf72a6c610abebcceb0dc5f251d8583b9d5704b5c5e6914339cb545730d7"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python-msk-time"
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
    network_mode                                = "default"
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
        external = 5000
        internal = 50
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```


* ### `terraform state show docker_container.node_app`

```
# docker_container.node_app:
resource "docker_container" "node_app" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "node",
        "server.js",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/usr/bin/tini",
        "--",
    ]
    env                                         = []
    hostname                                    = "1e67ea338f77"
    id                                          = "1e67ea338f772e0821e444e2319d3816d15fcec9b9147bfa1a92e9d52ac4f272"
    image                                       = "sha256:f64483641fccde2e8c58e52b11cd1a46e1b3e75b19256b3999e408eb36ef3f79"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "js-cities-dist"
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
    network_mode                                = "default"
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
        external = 3000
        internal = 30
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

### `terraform output`

```
container_id_node = "1e67ea338f772e0821e444e2319d3816d15fcec9b9147bfa1a92e9d52ac4f272"
container_id_py = "8fd2f30cca87534eecb45529ca7da9c1480e5130384ae93f120d4c1b2d5d7c93"
image_id_node = "sha256:f64483641fccde2e8c58e52b11cd1a46e1b3e75b19256b3999e408eb36ef3f79nickolaus899/js-cities-dist:latest"
image_id_py = "sha256:1f60cf72a6c610abebcceb0dc5f251d8583b9d5704b5c5e6914339cb545730d7nickolaus899/python-msk-time:latest"
```

## Yandex Cloud

* Created account, then linked a card to it
* According to the tutorial, created a service account for this lab
* Installed `yc` and configured `key.json` (authorization stage)
* Created folder *yandex* and corresponding files `main.tf`, `variables.tf`, `outputs.tf`
* Then, described a VM in terms of its resources
* Repeated the same steps as for Docker stage (init / validate / apply)

#### Difficulties
I created a folder (as the `default`) for the project. However, I didn't know that resources
(`network` actually) will be copied to the new folder. Consequently, there are two same 
networks which hit the quota of two possible networks. Therefore, during the allocation of
resources I received an error with Quota limit. The solution was to delete one network
from the `default` folder.

### `terraform plan`

```
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
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQD3okRhJuOPJdejQjTAaJo8FLz/2HXhv1q/sE94pnnDSP1tVC2Xit9Rv4MzTQv9jta3nV+ZOOp8H0XLYxWINb+2xSJhCwqGqmAmurjfuEFFNKJ+J9UBlLvMV4MtbAWI7oJBlmKzSC2nBvqSymiekZbWel/Tw5UOWfARyIRynoz4mKRYU7UOB5PyvRml5EexF7Up5bb/9MdM0JYh6YJuq3alk5im4Tq5xVXUfRyBOB5yxUxwdnN47g08gKpZ3o1JutKqHQ38toesHDanxtNB5A+WkPQfx38FSVcsm2XOPPcOk3hHWwx5WaD14Q5l6oais15fxanI45zZsLLY0PVK2Fj5kwHctUOfpLrSIJmfNrJdWN4dk2BqpMIFRX71CeuG1ZM+HnOwMrTMWz/sNKOCP3oEgBQJUPntvAQHPBCTfsojcLtYsGsKT5utCHp8HRc6DtkgQRAc74fLH3W4cl0i3IAEwpJ3SVSd8mnA3ylwLgG7tB93xOY5p82PlFta37hE/Zc= nickolaus-sdr@nickolaussdr-VirtualBox
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
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-d"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

```

### `terraform apply`
```
yandex_compute_disk.boot-disk-1: Refreshing state... [id=fhmglfl5e3238nglan7t]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

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
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQD3okRhJuOPJdejQjTAaJo8FLz/2HXhv1q/sE94pnnDSP1tVC2Xit9Rv4MzTQv9jta3nV+ZOOp8H0XLYxWINb+2xSJhCwqGqmAmurjfuEFFNKJ+J9UBlLvMV4MtbAWI7oJBlmKzSC2nBvqSymiekZbWel/Tw5UOWfARyIRynoz4mKRYU7UOB5PyvRml5EexF7Up5bb/9MdM0JYh6YJuq3alk5im4Tq5xVXUfRyBOB5yxUxwdnN47g08gKpZ3o1JutKqHQ38toesHDanxtNB5A+WkPQfx38FSVcsm2XOPPcOk3hHWwx5WaD14Q5l6oais15fxanI45zZsLLY0PVK2Fj5kwHctUOfpLrSIJmfNrJdWN4dk2BqpMIFRX71CeuG1ZM+HnOwMrTMWz/sNKOCP3oEgBQJUPntvAQHPBCTfsojcLtYsGsKT5utCHp8HRc6DtkgQRAc74fLH3W4cl0i3IAEwpJ3SVSd8mnA3ylwLgG7tB93xOY5p82PlFta37hE/Zc= nickolaus-sdr@nickolaussdr-VirtualBox
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
          + disk_id     = "fhmglfl5e3238nglan7t"
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
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)
yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Creation complete after 3s [id=enp4t0920dd50tqh58nq]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bd6i6u166f7g87mb4i]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 36s [id=fhmflial3dkskbuhnv3u]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "51.250.13.152"
internal_ip_address_vm_1 = "192.168.10.34"
```


### `terraform output`
```
external_ip_address_vm_1 = "51.250.13.152"
internal_ip_address_vm_1 = "192.168.10.34"
```


## GitHub

### Best practices
* Placed token as env variable
* Used `terraform validate` and `terraform fmt` -> everything is ok


I created a repo with name `Devops-Lab4-TF` (https://github.com/Nickolaus-899/Devops-Lab4-TF)

### `terraform apply`
```
github_repository.repo: Refreshing state... [id=Devops-Lab4-TF]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "Devops-Lab4-TF"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = "Devops-Lab4-TF"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 2s [id=Devops-Lab4-TF]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDON1Crfc4Digcf]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

```

## GitHub Organizations

Organization name: `DevopsNikolaiLab4`
Repository of this organization: `Devops-Lab4-TF` (https://github.com/DevopsNikolaiLab4/Devops-Lab4-TF)


### `terraform apply`
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_team.admins will be created
  + resource "github_team" "admins" {
      + create_default_maintainer = false
      + description               = "Administrators with full access"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Admins"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.developers will be created
  + resource "github_team" "developers" {
      + create_default_maintainer = false
      + description               = "Team for developers (users)"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Developers"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.admin_team_access will be created
  + resource "github_team_repository" "admin_team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "Devops-Lab4-TF"
      + team_id    = (known after apply)
    }

  # github_team_repository.dev_team_access will be created
  + resource "github_team_repository" "dev_team_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "Devops-Lab4-TF"
      + team_id    = (known after apply)
    }

Plan: 4 to add, 0 to change, 0 to destroy.
github_team.developers: Creating...
github_team.admins: Creating...
github_team.admins: Creation complete after 7s [id=12124781]
github_team_repository.admin_team_access: Creating...
github_team.developers: Still creating... [10s elapsed]
github_team.developers: Creation complete after 10s [id=12124777]
github_team_repository.dev_team_access: Creating...
github_team_repository.admin_team_access: Creation complete after 3s [id=12124781:Devops-Lab4-TF]
github_team_repository.dev_team_access: Creation complete after 2s [id=12124777:Devops-Lab4-TF]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```


### In the settings, two teams appeared: *Admins* and *Developers*
