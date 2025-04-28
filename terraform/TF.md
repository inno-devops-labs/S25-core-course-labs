# Terraform

## Creating the Container

**Command:**

```sh
  terraform state list
```

**Output:**

```sh
  docker_container.app_python
```

**Command:**

 ```sh
  terraform state show docker_container.app_python
```

**Output:**

```sh
  # docker_container.app_python:
  resource "docker_container" "app_python" {
      attach                                      = false
      bridge                                      = null
      command                                     = [
          "python",
          "app.py",
      ]
      container_read_refresh_timeout_milliseconds = 15000
      cpu_set                                     = null
      cpu_shares                                  = 0
      domainname                                  = null
      entrypoint                                  = []
      env                                         = []
      hostname                                    = "96c015fe133f"
      id                                          = "96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508"
      image                                       = "sha256:de4f047721fee1e47ab5a3be2dc3236d4e5104060db786b2b6a5c16ad7620840"
      init                                        = false
      ipc_mode                                    = "private"
      log_driver                                  = "json-file"
      logs                                        = false
      max_retry_count                             = 0
      memory                                      = 0
      memory_swap                                 = 0
      must_run                                    = true
      name                                        = "app_python_container"
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
      working_dir                                 = "/home/appuser"

      ports {
          external = 8000
          internal = 80
          ip       = "0.0.0.0"
          protocol = "tcp"
      }
  } 
```

## Changing the Port Number

```sh
  docker_container.app_python: Refreshing state... [id=96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508]

  Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
  following symbols:
  -/+ destroy and then create replacement

  Terraform will perform the following actions:

    # docker_container.app_python must be replaced
  -/+ resource "docker_container" "app_python" {
        + bridge                                      = (known after apply)
        ~ command                                     = [
            - "python",
            - "app.py",
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
        ~ hostname                                    = "96c015fe133f" -> (known after apply)
        ~ id                                          = "96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508" -> (known after apply)
        ~ image                                       = "sha256:de4f047721fee1e47ab5a3be2dc3236d4e5104060db786b2b6a5c16ad7620840" -> "anyarylova/app_python" # forces replacement
        ~ init                                        = false -> (known after apply)
        ~ ipc_mode                                    = "private" -> (known after apply)
        ~ log_driver                                  = "json-file" -> (known after apply)
        - log_opts                                    = {} -> null
        - max_retry_count                             = 0 -> null
        - memory                                      = 0 -> null
        - memory_swap                                 = 0 -> null
          name                                        = "app_python_container"
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
        - user                                        = "appuser" -> null
        - working_dir                                 = "/home/appuser" -> null
          # (17 unchanged attributes hidden)

        ~ healthcheck (known after apply)

        ~ labels (known after apply)

        ~ ports {
            ~ external = 8000 -> 8080 # forces replacement
              # (3 unchanged attributes hidden)
          }
      }

  Plan: 1 to add, 0 to change, 1 to destroy.

  Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

  docker_container.app_python: Destroying... [id=96c015fe133f87350803227bda7e8a12ad3450e427c2af2369081ab308b33508]
  docker_container.app_python: Destruction complete after 1s
  docker_container.app_python: Creating...
  docker_container.app_python: Creation complete after 0s [id=afd45f1fea4de5c76c690072420c9ccbbc80d816a0d58fdfdbe26ec3d2460c80]

  Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

## Output

```sh
  terraform output
```

```sh
  container_id = "588bfa1adc84b770c096b5f37bbce3964de2eb924a6751962a7a1d917e9dbeed"
  image_id = "anyarylova/app_python"
```

## Yandex Cloud Infrastracture

### Create service account

```sh
  > yc iam service-account create --name anyarylova
  id: ajee9o77dum38ubcgloh
  folder_id: b1gm8det1qvec4u1gk4o
  created_at: "2025-02-06T06:54:35.561039119Z"
  name: anyarylova
```

```sh
  > yc iam service-account list
  +----------------------+------------+--------+---------------------+-----------------------+
  |          ID          |    NAME    | LABELS |     CREATED AT      | LAST AUTHENTICATED AT |
  +----------------------+------------+--------+---------------------+-----------------------+
  | ajee9o77dum38ubcgloh | anyarylova |        | 2025-02-06 06:54:35 | 2025-04-28 18:40:00   |
  +----------------------+------------+--------+---------------------+-----------------------+
```

### Assign role to a service account in the management console 

![Service accout role](yandex_cloud\service_account_role.png)

### Set up the CLI profile 

#### Create an authorized key and save in `key.json`

```sh
  > yc iam key create --service-account-id ajee9o77dum38ubcgloh --folder-name default --output key.json

  id: aje682vtu2gijorvuchj
  service_account_id: ajee9o77dum38ubcgloh
  created_at: "2025-04-28T18:22:58.561039119Z"
  key_algorithm: RSA_2048
```

#### Set the profile configuration

```sh
  > yc config set service-account-key key.json
  > yc config set cloud-id b1g6jo90fmsfvk71v5ea
  > yc config set folder-id b1gm8det1qvec4u1gk4o
```

### Configure a provider

#### Create `main.tf`

```sh
  terraform {
    required_providers {
      yandex = {
        source = "yandex-cloud/yandex"
      }
    }
    required_version = ">= 0.13"
  }

  provider "yandex" {
    zone = "ru-central1-a"
  }
```

#### Run `terraform init`

```sh
  > terraform init                              

  Initializing the backend...
  Initializing provider plugins...                
  - Reusing previous version of yandex-cloud/yandex from the dependency lock file
  - Using previously-installed yandex-cloud/yandex v0.140.1
    
  Terraform has been successfully initialized!
    
  You may now begin working with Terraform. Try running "terraform plan" to see
  any changes that are required for your infrastructure. All Terraform commands
  should now work.

  If you ever set or change modules or backend configuration for Terraform,
  rerun this command to reinitialize your working directory. If you forget, other
  commands will detect it and remind you to do so if necessary.
```

### Create Windows VM

#### Update `main.tf`

```sh
  terraform {
    required_providers {
      yandex = {
        source = "yandex-cloud/yandex"
      }
    }
  }

  provider "yandex" {
    zone = var.zone
  }

  resource "yandex_vpc_network" "default" {
    name = var.network
  }

  resource "yandex_vpc_subnet" "default" {
    network_id     = yandex_vpc_network.default.id
    name           = var.subnet
    v4_cidr_blocks = var.subnet_v4_cidr_blocks
    zone           = var.zone
  }


  resource "yandex_compute_instance" "default" {
    name     = var.name
    hostname = var.name
    zone     = var.zone

    resources {
      cores  = var.cores
      memory = var.memory
    }

    boot_disk {
      initialize_params {
        image_id = var.image_id
        size     = var.disk_size
        type     = var.disk_type
      }
    }

    network_interface {
      subnet_id = yandex_vpc_subnet.default.id
      nat       = var.nat
    }

    timeouts {
      create = var.timeout_create
      delete = var.timeout_delete
    }
  }

  output "name" {
    value = yandex_compute_instance.default.name
  }

  output "address" {
    value = yandex_compute_instance.default.network_interface.0.nat_ip_address
  }
```

#### Create `variables.tf`

```sh
  variable "zone" {
    type    = string
    default = "ru-central1-d"
  }

  variable "network" {
    type    = string
    default = "ya-network"
  }

  variable "subnet" {
    type    = string
    default = "ya-network"
  }

  variable "subnet_v4_cidr_blocks" {
    type    = list(string)
    default = ["192.168.10.0/16"]
  }

  variable "nat" {
    type    = bool
    default = true
  }

  variable "image_id" {
      type = string
      default = "fd800c7s2p483i648ifv"
  }

  variable "name" {
    type = string
  }

  variable "cores" {
    type    = number
    default = 2
  }

  variable "memory" {
    type    = number
    default = 4
  }

  variable "disk_size" {
    type    = number
    default = 50
  }

  variable "disk_type" {
    type    = string
    default = "network-nvme"
  }


  variable "timeout_create" {
    default = "10m"
  }

  variable "timeout_delete" {
    default = "10m"
  }
```

#### Check and format the configuration files

```sh
  > terraform validate

  Success! The configuration is valid.
```

```sh
  > terraform fmt

  main.tf
  variables.tf
```

### Create Resources

#### `terraform plan`

```sh
  > terraform plan 

  var.name
    Enter a value: lab4

  yandex_vpc_network.default: Refreshing state... [id=enpj5ht7g6pnts2m3t66]
  yandex_vpc_subnet.default: Refreshing state... [id=fl8imkti9ldm09faur8h]

  Terraform used the selected providers to generate the following execution plan. Resource actions are
  indicated with the following symbols:
    + create
  -/+ destroy and then create replacement

  Terraform will perform the following actions:

    # yandex_compute_instance.default will be created
    + resource "yandex_compute_instance" "default" {
        + created_at                = (known after apply)
        + folder_id                 = (known after apply)
        + fqdn                      = (known after apply)
        + gpu_cluster_id            = (known after apply)
        + hardware_generation       = (known after apply)
        + hostname                  = "lab4"
        + id                        = (known after apply)
        + maintenance_grace_period  = (known after apply)
        + maintenance_policy        = (known after apply)
        + name                      = "lab4"
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
                + image_id    = "fd800c7s2p483i648ifv"
                + name        = (known after apply)
                + size        = 50
                + snapshot_id = (known after apply)
                + type        = "network-nvme"
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
            + memory        = 4
          }

        + scheduling_policy (known after apply)

        + timeouts {
            + create = "10m"
            + delete = "10m"
          }
      }

    # yandex_vpc_subnet.default must be replaced
  -/+ resource "yandex_vpc_subnet" "default" {
        ~ created_at     = "2025-04-28T20:46:22Z" -> (known after apply)
        ~ folder_id      = "b1gm8det1qvec4u1gk4o" -> (known after apply)
        ~ id             = "fl8imkti9ldm09faur8h" -> (known after apply)
        ~ labels         = {} -> (known after apply)
          name           = "ya-network"
        ~ v6_cidr_blocks = [] -> (known after apply)
        ~ zone           = "ru-central1-d" -> "ru-central1-a" # forces replacement
          # (4 unchanged attributes hidden)
      }

  Plan: 2 to add, 0 to change, 1 to destroy.

  Changes to Outputs:
    + address = (known after apply)
```

#### `terraform apply`

```sh
  > terraform apply

  var.name
    Enter a value: lab4

  yandex_vpc_network.default: Refreshing state... [id=enpj5ht7g6pnts2m3t66]
  yandex_vpc_subnet.default: Refreshing state... [id=fl8imkti9ldm09faur8h]

  Terraform used the selected providers to generate the following execution plan. Resource actions are
  indicated with the following symbols:
    + create
  -/+ destroy and then create replacement

  Terraform will perform the following actions:

    # yandex_compute_instance.default will be created
    + resource "yandex_compute_instance" "default" {
        + created_at                = (known after apply)
        + folder_id                 = (known after apply)
        + fqdn                      = (known after apply)
        + gpu_cluster_id            = (known after apply)
        + hardware_generation       = (known after apply)
        + hostname                  = "lab4"
        + id                        = (known after apply)
        + maintenance_grace_period  = (known after apply)
        + maintenance_policy        = (known after apply)
        + name                      = "lab4"
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
                + image_id    = "fd800c7s2p483i648ifv"
                + name        = (known after apply)
                + size        = 50
                + snapshot_id = (known after apply)
                + type        = "network-nvme"
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
            + memory        = 4
          }

        + scheduling_policy (known after apply)

        + timeouts {
            + create = "10m"
            + delete = "10m"
          }
      }

    # yandex_vpc_subnet.default must be replaced
  -/+ resource "yandex_vpc_subnet" "default" {
        ~ created_at     = "2025-04-28T20:46:22Z" -> (known after apply)
        ~ folder_id      = "b1gm8det1qvec4u1gk4o" -> (known after apply)
        ~ id             = "fl8imkti9ldm09faur8h" -> (known after apply)
        ~ labels         = {} -> (known after apply)
          name           = "ya-network"
        ~ v6_cidr_blocks = [] -> (known after apply)
        ~ zone           = "ru-central1-d" -> "ru-central1-a" # forces replacement
          # (4 unchanged attributes hidden)
      }

  Plan: 2 to add, 0 to change, 1 to destroy.

  Changes to Outputs:
    + address = (known after apply)

  Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

  yandex_vpc_subnet.default: Destroying... [id=fl8imkti9ldm09faur8h]
  yandex_vpc_subnet.default: Destruction complete after 1s
  yandex_vpc_subnet.default: Creating...
  yandex_vpc_subnet.default: Creation complete after 0s [id=e9b8oedqenq3gfgv6ose]
  yandex_compute_instance.default: Creating...
  yandex_compute_instance.default: Still creating... [10s elapsed]
  yandex_compute_instance.default: Still creating... [20s elapsed]
  yandex_compute_instance.default: Still creating... [30s elapsed]
  yandex_compute_instance.default: Still creating... [40s elapsed]
  yandex_compute_instance.default: Creation complete after 47s [id=fhmbpkaum2f6ne1ttvu9]

  Apply complete! Resources: 2 added, 0 changed, 1 destroyed.

  Outputs:

  address = "51.250.71.199"
  name = "lab4"
```

### Delete Resources

```sh
  > terraform destroy

  var.name
    Enter a value: lab4

  yandex_vpc_network.default: Refreshing state... [id=enpj5ht7g6pnts2m3t66]
  yandex_vpc_subnet.default: Refreshing state... [id=e9b8oedqenq3gfgv6ose]
  yandex_compute_instance.default: Refreshing state... [id=fhmbpkaum2f6ne1ttvu9]

  Terraform used the selected providers to generate the following execution plan. Resource actions are
  indicated with the following symbols:
    - destroy

  Terraform will perform the following actions:

    # yandex_compute_instance.default will be destroyed
    - resource "yandex_compute_instance" "default" {
        - created_at                = "2025-04-28T20:47:31Z" -> null
        - folder_id                 = "b1gm8det1qvec4u1gk4o" -> null
        - fqdn                      = "lab4.ru-central1.internal" -> null
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
        - hostname                  = "lab4" -> null
        - id                        = "fhmbpkaum2f6ne1ttvu9" -> null
        - labels                    = {} -> null
        - metadata                  = {} -> null
        - name                      = "lab4" -> null
        - network_acceleration_type = "standard" -> null
        - platform_id               = "standard-v1" -> null
        - status                    = "running" -> null
        - zone                      = "ru-central1-a" -> null
          # (4 unchanged attributes hidden)

        - boot_disk {
            - auto_delete = true -> null
            - device_name = "fhm6jrg4bn8fs60i887p" -> null
            - disk_id     = "fhm6jrg4bn8fs60i887p" -> null
            - mode        = "READ_WRITE" -> null

            - initialize_params {
                - block_size  = 4096 -> null
                - image_id    = "fd800c7s2p483i648ifv" -> null
                  name        = null
                - size        = 50 -> null
                - type        = "network-ssd" -> null
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
            - ip_address         = "192.168.0.26" -> null
            - ipv4               = true -> null
            - ipv6               = false -> null
            - mac_address        = "d0:0d:bc:d1:5e:b0" -> null
            - nat                = true -> null
            - nat_ip_address     = "51.250.71.199" -> null
            - nat_ip_version     = "IPV4" -> null
            - security_group_ids = [] -> null
            - subnet_id          = "e9b8oedqenq3gfgv6ose" -> null
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
            - memory        = 4 -> null
          }

        - scheduling_policy {
            - preemptible = false -> null
          }

        - timeouts {
            - create = "10m" -> null
            - delete = "10m" -> null
          }
      }

    # yandex_vpc_network.default will be destroyed
    - resource "yandex_vpc_network" "default" {
        - created_at                = "2025-04-28T20:36:44Z" -> null
        - default_security_group_id = "enp6u47lltst7us1141a" -> null
        - folder_id                 = "b1gm8det1qvec4u1gk4o" -> null
        - id                        = "enpj5ht7g6pnts2m3t66" -> null
        - labels                    = {} -> null
        - name                      = "ya-network" -> null
        - subnet_ids                = [
            - "e9b8oedqenq3gfgv6ose",
          ] -> null
          # (1 unchanged attribute hidden)
      }

    # yandex_vpc_subnet.default will be destroyed
    - resource "yandex_vpc_subnet" "default" {
        - created_at     = "2025-04-28T20:47:30Z" -> null
        - folder_id      = "b1gm8det1qvec4u1gk4o" -> null
        - id             = "e9b8oedqenq3gfgv6ose" -> null
        - labels         = {} -> null
        - name           = "ya-network" -> null
        - network_id     = "enpj5ht7g6pnts2m3t66" -> null
        - v4_cidr_blocks = [
            - "192.168.0.0/16",
          ] -> null
        - v6_cidr_blocks = [] -> null
        - zone           = "ru-central1-a" -> null
          # (2 unchanged attributes hidden)
      }

  Plan: 0 to add, 0 to change, 3 to destroy.

  Changes to Outputs:
    - address = "51.250.71.199" -> null
    - name    = "lab4" -> null

  Do you really want to destroy all resources?
    Terraform will destroy all your managed infrastructure, as shown above.
    There is no undo. Only 'yes' will be accepted to confirm.

    Enter a value: yes

  yandex_compute_instance.default: Destroying... [id=fhmbpkaum2f6ne1ttvu9]
  yandex_compute_instance.default: Still destroying... [id=fhmbpkaum2f6ne1ttvu9, 10s elapsed]
  yandex_compute_instance.default: Still destroying... [id=fhmbpkaum2f6ne1ttvu9, 20s elapsed]
  yandex_compute_instance.default: Still destroying... [id=fhmbpkaum2f6ne1ttvu9, 30s elapsed]
  yandex_compute_instance.default: Destruction complete after 35s
  yandex_vpc_subnet.default: Destroying... [id=e9b8oedqenq3gfgv6ose]
  yandex_vpc_subnet.default: Destruction complete after 3s
  yandex_vpc_network.default: Destroying... [id=enpj5ht7g6pnts2m3t66]
  yandex_vpc_network.default: Destruction complete after 1s

  Destroy complete! Resources: 3 destroyed.
```