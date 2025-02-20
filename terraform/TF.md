# Terraform

## Best Practices

- __Code structure__ - used `main.tf`, `variables.tf`, `outputs.tf` files for each configuration
- __Provider versions__ - specified versions of providers
- __Code formatting__ - used code formatting with `terraform fmt` command
- __Secrets storing__ - secrets are stored locally and such variables are marked as sensitive

## Docker Configuration

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/docker$ terraform init
```

__Output__:

```
Initializing the backend...
Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "~> 3.0.1"...
- Installing kreuzwerker/docker v3.0.2...
- Installed kreuzwerker/docker v3.0.2 (unauthenticated)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

╷
│ Warning: Incomplete lock file information for providers
│ 
│ Due to your customized provider installation methods, Terraform was forced to calculate lock file checksums locally for the following providers:
│   - kreuzwerker/docker
│ 
│ The current .terraform.lock.hcl file only includes checksums for linux_amd64, so Terraform running on another platform will fail to install these providers.
│ 
│ To calculate additional checksums for another platform, run:
│   terraform providers lock -platform=linux_amd64
│ (where linux_amd64 is the platform to generate)
╵
Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/docker$ terraform apply
```

__Output__:

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.go_app_container will be created
  + resource "docker_container" "go_app_container" {
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
      + image                                       = "azamatbayramov/s25-devops-go-dl:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "go-app"
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
          + external = 8012
          + internal = 8002
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.python_app_container will be created
  + resource "docker_container" "python_app_container" {
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
      + image                                       = "azamatbayramov/s25-devops-py-dl:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "python-app"
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
          + external = 8011
          + internal = 8001
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + go_app_container_id        = (known after apply)
  + python_app_container_id    = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.python_app_container: Creating...
docker_container.go_app_container: Creating...
docker_container.go_app_container: Creation complete after 0s [id=cb7b5cc6d079df291be793253673bf7478b9cbd10211f7e1b3b986c78b115b1a]
docker_container.python_app_container: Creation complete after 0s [id=1d0bd85b4726903f2b9bf71a0b2eb6e03fabce8d1b78ad5566d15988cfc1bf81]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

go_app_container_id = "cb7b5cc6d079df291be793253673bf7478b9cbd10211f7e1b3b986c78b115b1a"
go_app_container_ports = tolist([
  {
    "external" = 8012
    "internal" = 8002
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
python_app_container_id = "1d0bd85b4726903f2b9bf71a0b2eb6e03fabce8d1b78ad5566d15988cfc1bf81"
python_app_container_ports = tolist([
  {
    "external" = 8011
    "internal" = 8001
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/docker$ terraform state list
```

__Output__:

```
docker_container.go_app_container
docker_container.python_app_container
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/docker$ terraform state show docker_container.go_app_container
```

__Output__:

```
# docker_container.go_app_container:
resource "docker_container" "go_app_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "./app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "cb7b5cc6d079"
    id                                          = "cb7b5cc6d079df291be793253673bf7478b9cbd10211f7e1b3b986c78b115b1a"
    image                                       = "sha256:3e315f88700de75841ac79e21770a16c3f15e3741d0a0c1fc7c52871d195d600"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "go-app"
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
        external = 8012
        internal = 8002
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/docker$ terraform state show docker_container.python_app_container
```

__Output__:

```
# docker_container.python_app_container:
resource "docker_container" "python_app_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/venv/bin/python3",
        "main.py",
    ]
    env                                         = []
    hostname                                    = "1d0bd85b4726"
    id                                          = "1d0bd85b4726903f2b9bf71a0b2eb6e03fabce8d1b78ad5566d15988cfc1bf81"
    image                                       = "sha256:af1a9398a4efea8864a86200d8e8451410dd63a186d1beeba99d0235489dc473"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python-app"
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
        external = 8011
        internal = 8001
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

Here I changed the container names in variables file

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/docker$ terraform apply
```

__Output__:

```
docker_container.go_app_container: Refreshing state... [id=cb7b5cc6d079df291be793253673bf7478b9cbd10211f7e1b3b986c78b115b1a]
docker_container.python_app_container: Refreshing state... [id=1d0bd85b4726903f2b9bf71a0b2eb6e03fabce8d1b78ad5566d15988cfc1bf81]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.go_app_container must be replaced
-/+ resource "docker_container" "go_app_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "./app",
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
      ~ hostname                                    = "cb7b5cc6d079" -> (known after apply)
      ~ id                                          = "cb7b5cc6d079df291be793253673bf7478b9cbd10211f7e1b3b986c78b115b1a" -> (known after apply)
      ~ image                                       = "sha256:3e315f88700de75841ac79e21770a16c3f15e3741d0a0c1fc7c52871d195d600" -> "azamatbayramov/s25-devops-go-dl:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "go-app" -> "go-app-edited" # forces replacement
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

  # docker_container.python_app_container must be replaced
-/+ resource "docker_container" "python_app_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/venv/bin/python3",
          - "main.py",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "1d0bd85b4726" -> (known after apply)
      ~ id                                          = "1d0bd85b4726903f2b9bf71a0b2eb6e03fabce8d1b78ad5566d15988cfc1bf81" -> (known after apply)
      ~ image                                       = "sha256:af1a9398a4efea8864a86200d8e8451410dd63a186d1beeba99d0235489dc473" -> "azamatbayramov/s25-devops-py-dl:latest" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "python-app" -> "python-app-edited" # forces replacement
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

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ go_app_container_id        = "cb7b5cc6d079df291be793253673bf7478b9cbd10211f7e1b3b986c78b115b1a" -> (known after apply)
  ~ python_app_container_id    = "1d0bd85b4726903f2b9bf71a0b2eb6e03fabce8d1b78ad5566d15988cfc1bf81" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.go_app_container: Destroying... [id=cb7b5cc6d079df291be793253673bf7478b9cbd10211f7e1b3b986c78b115b1a]
docker_container.python_app_container: Destroying... [id=1d0bd85b4726903f2b9bf71a0b2eb6e03fabce8d1b78ad5566d15988cfc1bf81]
docker_container.go_app_container: Destruction complete after 0s
docker_container.go_app_container: Creating...
docker_container.python_app_container: Destruction complete after 0s
docker_container.python_app_container: Creating...
docker_container.go_app_container: Creation complete after 1s [id=cf440aa69b5e379d15bc3505758c1995d0d1d37425643ce8bceb513f4ee68459]
docker_container.python_app_container: Creation complete after 1s [id=05797eb39acbecf7b1f0b55e32ff338d0353760c88af04e6fd5711f6bbacfe88]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

go_app_container_id = "cf440aa69b5e379d15bc3505758c1995d0d1d37425643ce8bceb513f4ee68459"
go_app_container_ports = tolist([
  {
    "external" = 8012
    "internal" = 8002
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
python_app_container_id = "05797eb39acbecf7b1f0b55e32ff338d0353760c88af04e6fd5711f6bbacfe88"
python_app_container_ports = tolist([
  {
    "external" = 8011
    "internal" = 8001
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/docker$ terraform output
```

__Output__:

```
go_app_container_id = "cf440aa69b5e379d15bc3505758c1995d0d1d37425643ce8bceb513f4ee68459"
go_app_container_ports = tolist([
  {
    "external" = 8012
    "internal" = 8002
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
python_app_container_id = "05797eb39acbecf7b1f0b55e32ff338d0353760c88af04e6fd5711f6bbacfe88"
python_app_container_ports = tolist([
  {
    "external" = 8011
    "internal" = 8001
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud Configuration

- Used following tutorial: https://yandex.cloud/ru/docs/tutorials/infrastructure-management/terraform-quickstart
- Installed `yc` on my pc and configured it
- Configured service account on Yandex Cloud
- Sent some money to balance
- Configured Terraform to work with Yandex Cloud using `.terraformrc`
- Created Terraform configuration
- Used following commands:

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/yandex_cloud$ terraform init
```

__Output__:

```
Initializing the backend...
Initializing provider plugins...
- Finding latest version of yandex-cloud/yandex...
- Installing yandex-cloud/yandex v0.136.0...
- Installed yandex-cloud/yandex v0.136.0 (unauthenticated)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

╷
│ Warning: Incomplete lock file information for providers
│ 
│ Due to your customized provider installation methods, Terraform was forced to calculate lock file checksums locally for the following providers:
│   - yandex-cloud/yandex
│ 
│ The current .terraform.lock.hcl file only includes checksums for linux_amd64, so Terraform running on another platform will fail to install these providers.
│ 
│ To calculate additional checksums for another platform, run:
│   terraform providers lock -platform=linux_amd64
│ (where linux_amd64 is the platform to generate)
╵
Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/yandex_cloud$ terraform apply
```

__Output__:

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk will be created
  + resource "yandex_compute_disk" "boot-disk" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8308aanqma9v5n76aj"
      + name        = "s25-devops-terraform-boot-disk"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

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
                ubuntu:ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX azamat@azamat-pc
            EOT
        }
      + name                      = "s25-devops-terraform-vm"
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

  # yandex_vpc_network.network will be created
  + resource "yandex_vpc_network" "network" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "s25-devops-terraform-network"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet will be created
  + resource "yandex_vpc_subnet" "subnet" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "s25-devops-terraform-subnet"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.0.0/16",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm = (known after apply)
  + internal_ip_address_vm = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network: Creating...
yandex_compute_disk.boot-disk: Creating...
yandex_vpc_network.network: Creation complete after 3s [id=enpg1hoh2bf07b6jo6o7]
yandex_vpc_subnet.subnet: Creating...
yandex_vpc_subnet.subnet: Creation complete after 0s [id=e9b1d25g8d6vo02h2hqp]
yandex_compute_disk.boot-disk: Creation complete after 7s [id=fhmd853fp3fdalr276kg]
yandex_compute_instance.vm: Creating...
yandex_compute_instance.vm: Still creating... [10s elapsed]
yandex_compute_instance.vm: Still creating... [20s elapsed]
yandex_compute_instance.vm: Creation complete after 30s [id=fhm2d04obkl6tqs0dqip]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm = "51.250.5.141"
internal_ip_address_vm = "192.168.0.15"
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/yandex_cloud$ terraform destroy
```

__Output__:

```
yandex_vpc_network.network: Refreshing state... [id=enpg1hoh2bf07b6jo6o7]
yandex_compute_disk.boot-disk: Refreshing state... [id=fhmd853fp3fdalr276kg]
yandex_vpc_subnet.subnet: Refreshing state... [id=e9b1d25g8d6vo02h2hqp]
yandex_compute_instance.vm: Refreshing state... [id=fhm2d04obkl6tqs0dqip]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk will be destroyed
  - resource "yandex_compute_disk" "boot-disk" {
      - block_size  = 4096 -> null
      - created_at  = "2025-02-06T19:47:08Z" -> null
      - folder_id   = "b1gfnm5rm6vsvks6ucq4" -> null
      - id          = "fhmd853fp3fdalr276kg" -> null
      - image_id    = "fd8308aanqma9v5n76aj" -> null
      - labels      = {} -> null
      - name        = "s25-devops-terraform-boot-disk" -> null
      - product_ids = [
          - "f2e4lbir1thld1d4j0f6",
        ] -> null
      - size        = 20 -> null
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
      - created_at                = "2025-02-06T19:47:15Z" -> null
      - folder_id                 = "b1gfnm5rm6vsvks6ucq4" -> null
      - fqdn                      = "fhm2d04obkl6tqs0dqip.auto.internal" -> null
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
      - id                        = "fhm2d04obkl6tqs0dqip" -> null
      - labels                    = {} -> null
      - metadata                  = {
          - "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX azamat@azamat-pc
            EOT
        } -> null
      - name                      = "s25-devops-terraform-vm" -> null
      - network_acceleration_type = "standard" -> null
      - platform_id               = "standard-v1" -> null
      - status                    = "running" -> null
      - zone                      = "ru-central1-a" -> null
        # (5 unchanged attributes hidden)

      - boot_disk {
          - auto_delete = true -> null
          - device_name = "fhmd853fp3fdalr276kg" -> null
          - disk_id     = "fhmd853fp3fdalr276kg" -> null
          - mode        = "READ_WRITE" -> null

          - initialize_params {
              - block_size  = 4096 -> null
              - image_id    = "fd8308aanqma9v5n76aj" -> null
              - name        = "s25-devops-terraform-boot-disk" -> null
              - size        = 20 -> null
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
          - ip_address         = "192.168.0.15" -> null
          - ipv4               = true -> null
          - ipv6               = false -> null
          - mac_address        = "d0:0d:26:80:98:5d" -> null
          - nat                = true -> null
          - nat_ip_address     = "51.250.5.141" -> null
          - nat_ip_version     = "IPV4" -> null
          - security_group_ids = [] -> null
          - subnet_id          = "e9b1d25g8d6vo02h2hqp" -> null
            # (1 unchanged attribute hidden)
        }

      - placement_policy {
          - host_affinity_rules       = [] -> null
          - placement_group_partition = 0 -> null
            # (1 unchanged attribute hidden)
        }

      - resources {
          - core_fraction = 100 -> null
          - cores         = 2 -> null
          - gpus          = 0 -> null
          - memory        = 2 -> null
        }

      - scheduling_policy {
          - preemptible = false -> null
        }
    }

  # yandex_vpc_network.network will be destroyed
  - resource "yandex_vpc_network" "network" {
      - created_at                = "2025-02-06T19:47:08Z" -> null
      - default_security_group_id = "enpiqe2m6kg09ru192qj" -> null
      - folder_id                 = "b1gfnm5rm6vsvks6ucq4" -> null
      - id                        = "enpg1hoh2bf07b6jo6o7" -> null
      - labels                    = {} -> null
      - name                      = "s25-devops-terraform-network" -> null
      - subnet_ids                = [
          - "e9b1d25g8d6vo02h2hqp",
        ] -> null
        # (1 unchanged attribute hidden)
    }

  # yandex_vpc_subnet.subnet will be destroyed
  - resource "yandex_vpc_subnet" "subnet" {
      - created_at     = "2025-02-06T19:47:10Z" -> null
      - folder_id      = "b1gfnm5rm6vsvks6ucq4" -> null
      - id             = "e9b1d25g8d6vo02h2hqp" -> null
      - labels         = {} -> null
      - name           = "s25-devops-terraform-subnet" -> null
      - network_id     = "enpg1hoh2bf07b6jo6o7" -> null
      - v4_cidr_blocks = [
          - "192.168.0.0/16",
        ] -> null
      - v6_cidr_blocks = [] -> null
      - zone           = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm = "51.250.5.141" -> null
  - internal_ip_address_vm = "192.168.0.15" -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

yandex_compute_instance.vm: Destroying... [id=fhm2d04obkl6tqs0dqip]
yandex_compute_instance.vm: Still destroying... [id=fhm2d04obkl6tqs0dqip, 10s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhm2d04obkl6tqs0dqip, 20s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhm2d04obkl6tqs0dqip, 30s elapsed]
yandex_compute_instance.vm: Destruction complete after 32s
yandex_vpc_subnet.subnet: Destroying... [id=e9b1d25g8d6vo02h2hqp]
yandex_compute_disk.boot-disk: Destroying... [id=fhmd853fp3fdalr276kg]
yandex_compute_disk.boot-disk: Destruction complete after 0s
yandex_vpc_subnet.subnet: Destruction complete after 3s
yandex_vpc_network.network: Destroying... [id=enpg1hoh2bf07b6jo6o7]
yandex_vpc_network.network: Destruction complete after 1s

Destroy complete! Resources: 4 destroyed.
```

## GitHub Configuration

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/github$ terraform import "github_repository.repository" "S25-core-course-labs"
```

__Output__:

```
var.token
  GitHub token

  Enter a value: 

github_repository.repository: Importing from ID "S25-core-course-labs"...
github_repository.repository: Import prepared!
  Prepared github_repository for import
github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/github$ terraform apply
```

__Output__:

```
var.token
  GitHub token

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]

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

  # github_repository.repository will be updated in-place
  ~ resource "github_repository" "repository" {
      ~ auto_init                   = false -> true
      + description                 = "S25 DevOps course labs"
      + gitignore_template          = "VisualStudio"
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

github_repository.repository: Modifying... [id=S25-core-course-labs]
github_repository.repository: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_protection.default: Creating...
github_branch_default.master: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDONueDiM4DioVX]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

## GitHub Teams Configuration

__Input__:

```
azamat@azamat-pc:~/S25-core-course-labs/terraform/github_teams$ terraform apply
```

__Output__:

```
var.token
  GitHub token

  Enter a value: 


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "S25-DevOps-Test-Org-Repo-1"
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

  # github_repository.repository will be created
  + resource "github_repository" "repository" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + branches                    = (known after apply)
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "S25 DevOps course labs test repository"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + gitignore_template          = "VisualStudio"
      + has_issues                  = false
      + has_wiki                    = false
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "S25-DevOps-Test-Org-Repo-1"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

  # github_team.team_backend will be created
  + resource "github_team" "team_backend" {
      + create_default_maintainer = false
      + description               = "Backend team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "backend"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.team_frontend will be created
  + resource "github_team" "team_frontend" {
      + create_default_maintainer = false
      + description               = "Frontend team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "frontend"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.team_backend_in_repo will be created
  + resource "github_team_repository" "team_backend_in_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "S25-DevOps-Test-Org-Repo-1"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_frontend_in_repo will be created
  + resource "github_team_repository" "team_frontend_in_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "triage"
      + repository = "S25-DevOps-Test-Org-Repo-1"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.team_backend: Creating...
github_team.team_frontend: Creating...
github_repository.repository: Creating...
github_team.team_frontend: Still creating... [10s elapsed]
github_team.team_backend: Still creating... [10s elapsed]
github_repository.repository: Still creating... [10s elapsed]
github_team.team_backend: Creation complete after 13s [id=12132502]
github_team.team_frontend: Creation complete after 14s [id=12132501]
github_repository.repository: Creation complete after 15s [id=S25-DevOps-Test-Org-Repo-1]
github_branch_default.master: Creating...
github_team_repository.team_backend_in_repo: Creating...
github_team_repository.team_frontend_in_repo: Creating...
github_branch_protection.default: Creating...
github_branch_default.master: Creation complete after 2s [id=S25-DevOps-Test-Org-Repo-1]
github_team_repository.team_frontend_in_repo: Creation complete after 7s [id=12132501:S25-DevOps-Test-Org-Repo-1]
github_team_repository.team_backend_in_repo: Creation complete after 7s [id=12132502:S25-DevOps-Test-Org-Repo-1]
github_branch_protection.default: Creation complete after 9s [id=BPR_kwDON1jnWs4DiojG]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```
