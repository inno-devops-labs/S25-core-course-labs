# Terraform

## Docker

```
terraform init
Initializing the backend...
Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "~> 3.0.1"...
- Installing kreuzwerker/docker v3.0.2...
- Installed kreuzwerker/docker v3.0.2 (self-signed, key ID BD080C4571C6104C)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```
terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_container will be created
  + resource "docker_container" "app_container" {
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
      + image                                       = "darrpyy/app_python:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app"
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + app_container_id    = (known after apply)
  + app_container_ports = [
      + {
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform
apply" now.
```

```
terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_container will be created
  + resource "docker_container" "app_container" {
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
      + image                                       = "darrpyy/app_python:latest"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app"
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + app_container_id    = (known after apply)
  + app_container_ports = [
      + {
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_container: Creating...
docker_container.app_container: Still creating... [10s elapsed]
docker_container.app_container: Creation complete after 16s [id=7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

app_container_id = "7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a"
app_container_ports = tolist([
  {
    "external" = 5000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

```
docker ps
CONTAINER ID   IMAGE                       COMMAND            CREATED          STATUS          PORTS                    NAMES
7541fccc95e2   darrpyy/app_python:latest   "python main.py"   36 seconds ago   Up 35 seconds   0.0.0.0:5000->5000/tcp   app
```

```
terraform destroy
docker_container.app_container: Refreshing state... [id=7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # docker_container.app_container will be destroyed
  - resource "docker_container" "app_container" {
      - attach                                      = false -> null
      - command                                     = [] -> null
      - container_read_refresh_timeout_milliseconds = 15000 -> null
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      - entrypoint                                  = [
          - "python",
          - "main.py",
        ] -> null
      - env                                         = [] -> null
      - group_add                                   = [] -> null
      - hostname                                    = "7541fccc95e2" -> null
      - id                                          = "7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a" -> null
      - image                                       = "sha256:af78391c56a05c0e85dcf9e98fa9527b8969fa101fe6334f90fd4ca41b0bcd66" -> null
      - init                                        = false -> null
      - ipc_mode                                    = "private" -> null
      - log_driver                                  = "json-file" -> null
      - log_opts                                    = {} -> null
      - logs                                        = false -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      - must_run                                    = true -> null
      - name                                        = "app" -> null
      - network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> null
      - network_mode                                = "bridge" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      - read_only                                   = false -> null
      - remove_volumes                              = true -> null
      - restart                                     = "no" -> null
      - rm                                          = false -> null
      - runtime                                     = "runc" -> null
      - security_opts                               = [] -> null
      - shm_size                                    = 64 -> null
      - start                                       = true -> null
      - stdin_open                                  = false -> null
      - stop_timeout                                = 0 -> null
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - tty                                         = false -> null
      - user                                        = "appuser" -> null
      - wait                                        = false -> null
      - wait_timeout                                = 60 -> null
      - working_dir                                 = "/code" -> null
        # (6 unchanged attributes hidden)

      - ports {
          - external = 5000 -> null
          - internal = 5000 -> null
          - ip       = "0.0.0.0" -> null
          - protocol = "tcp" -> null
        }
    }

Plan: 0 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  - app_container_id    = "7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a" -> null
  - app_container_ports = [
      - {
          - external = 5000
          - internal = 5000
          - ip       = "0.0.0.0"
          - protocol = "tcp"
        },
    ] -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

docker_container.app_container: Destroying... [id=7541fccc95e2e875b305fe5944dd49caddd663bb54ee98161e5917f4a02a507a]
docker_container.app_container: Destruction complete after 0s

Destroy complete! Resources: 1 destroyed.
```

```
docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Yandex Cloud

Using tutorial I set up the yandex cloud provider and created a VM instance.

```
terraform init
Initializing the backend...
Initializing provider plugins...
- Finding latest version of yandex-cloud/yandex...
- Installing yandex-cloud/yandex v0.138.0...
- Installed yandex-cloud/yandex v0.138.0 (unauthenticated)
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

```
terraform apply
yandex_vpc_network.network: Refreshing state... [id=enp1nacqff18d8eu1cjl]
yandex_compute_disk.disk: Refreshing state... [id=fhme2co1ibae62snpv0a]
yandex_vpc_subnet.subnet: Refreshing state... [id=e9bbnvq6ag2ehc0pl987]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

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
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICCydFBFk+I0Wwy7kQ0pH5n6nO3xIQhH6wuyPBjBvETZ azamat@azamat-pc
            EOT
        }
      + name                      = "devops-terraform-vm"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = "fhme2co1ibae62snpv0a"
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
          + subnet_id          = "e9bbnvq6ag2ehc0pl987"
        }

      + placement_policy (known after apply)

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm = (known after apply)
  + internal_ip_address_vm = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_compute_instance.vm: Creating...
yandex_compute_instance.vm: Still creating... [10s elapsed]
yandex_compute_instance.vm: Still creating... [20s elapsed]
yandex_compute_instance.vm: Still creating... [30s elapsed]
yandex_compute_instance.vm: Creation complete after 35s [id=fhmhbdv6aur8mue092l8]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm = "51.250.71.157"
internal_ip_address_vm = "192.168.0.30"
```

```
terraform destroy
yandex_vpc_network.network: Refreshing state... [id=enp1nacqff18d8eu1cjl]
yandex_compute_disk.disk: Refreshing state... [id=fhme2co1ibae62snpv0a]
yandex_vpc_subnet.subnet: Refreshing state... [id=e9bbnvq6ag2ehc0pl987]
yandex_compute_instance.vm: Refreshing state... [id=fhmhbdv6aur8mue092l8]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # yandex_compute_disk.disk will be destroyed
  - resource "yandex_compute_disk" "disk" {
      - block_size  = 4096 -> null
      - created_at  = "2025-02-23T01:50:17Z" -> null
      - folder_id   = "b1gfnm5rm6vsvks6ucq4" -> null
      - id          = "fhme2co1ibae62snpv0a" -> null
      - image_id    = "fd8308aanqma9v5n76aj" -> null
      - labels      = {} -> null
      - name        = "devops-terraform-disk" -> null
      - product_ids = [
          - "f2e4lbir1thld1d4j0f6",
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
      - created_at                = "2025-02-23T02:23:55Z" -> null
      - folder_id                 = "b1gfnm5rm6vsvks6ucq4" -> null
      - fqdn                      = "fhmhbdv6aur8mue092l8.auto.internal" -> null
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
      - id                        = "fhmhbdv6aur8mue092l8" -> null
      - labels                    = {} -> null
      - metadata                  = {
          - "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICCydFBFk+I0Wwy7kQ0pH5n6nO3xIQhH6wuyPBjBvETZ azamat@azamat-pc
            EOT
        } -> null
      - name                      = "devops-terraform-vm" -> null
      - network_acceleration_type = "standard" -> null
      - platform_id               = "standard-v1" -> null
      - status                    = "running" -> null
      - zone                      = "ru-central1-a" -> null
        # (5 unchanged attributes hidden)

      - boot_disk {
          - auto_delete = true -> null
          - device_name = "fhme2co1ibae62snpv0a" -> null
          - disk_id     = "fhme2co1ibae62snpv0a" -> null
          - mode        = "READ_WRITE" -> null

          - initialize_params {
              - block_size  = 4096 -> null
              - image_id    = "fd8308aanqma9v5n76aj" -> null
              - name        = "devops-terraform-disk" -> null
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
          - ip_address         = "192.168.0.30" -> null
          - ipv4               = true -> null
          - ipv6               = false -> null
          - mac_address        = "d0:0d:11:5b:7e:65" -> null
          - nat                = true -> null
          - nat_ip_address     = "51.250.71.157" -> null
          - nat_ip_version     = "IPV4" -> null
          - security_group_ids = [] -> null
          - subnet_id          = "e9bbnvq6ag2ehc0pl987" -> null
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
      - created_at                = "2025-02-23T01:50:17Z" -> null
      - default_security_group_id = "enpi98pbc6lmh339985d" -> null
      - folder_id                 = "b1gfnm5rm6vsvks6ucq4" -> null
      - id                        = "enp1nacqff18d8eu1cjl" -> null
      - labels                    = {} -> null
      - name                      = "devops-terraform-network" -> null
      - subnet_ids                = [
          - "e9bbnvq6ag2ehc0pl987",
        ] -> null
        # (1 unchanged attribute hidden)
    }

  # yandex_vpc_subnet.subnet will be destroyed
  - resource "yandex_vpc_subnet" "subnet" {
      - created_at     = "2025-02-23T01:50:20Z" -> null
      - folder_id      = "b1gfnm5rm6vsvks6ucq4" -> null
      - id             = "e9bbnvq6ag2ehc0pl987" -> null
      - labels         = {} -> null
      - name           = "devops-terraform-subnet" -> null
      - network_id     = "enp1nacqff18d8eu1cjl" -> null
      - v4_cidr_blocks = [
          - "192.168.0.0/16",
        ] -> null
      - v6_cidr_blocks = [] -> null
      - zone           = "ru-central1-a" -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - external_ip_address_vm = "51.250.71.157" -> null
  - internal_ip_address_vm = "192.168.0.30" -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

yandex_compute_instance.vm: Destroying... [id=fhmhbdv6aur8mue092l8]
yandex_compute_instance.vm: Still destroying... [id=fhmhbdv6aur8mue092l8, 10s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhmhbdv6aur8mue092l8, 20s elapsed]
yandex_compute_instance.vm: Still destroying... [id=fhmhbdv6aur8mue092l8, 30s elapsed]
yandex_compute_instance.vm: Destruction complete after 38s
yandex_vpc_subnet.subnet: Destroying... [id=e9bbnvq6ag2ehc0pl987]
yandex_compute_disk.disk: Destroying... [id=fhme2co1ibae62snpv0a]
yandex_compute_disk.disk: Destruction complete after 0s
yandex_vpc_subnet.subnet: Destruction complete after 3s
yandex_vpc_network.network: Destroying... [id=enp1nacqff18d8eu1cjl]
yandex_vpc_network.network: Destruction complete after 1s

Destroy complete! Resources: 4 destroyed.
```

## GitHub

I set up the GitHub provider and imported the repository.

```
terraform init
Initializing the backend...
Initializing provider plugins...
- Finding integrations/github versions matching "~> 4.0"...
- Installing integrations/github v4.31.0...
- Installed integrations/github v4.31.0 (signed by a HashiCorp partner, key ID 38027F80D7FD5FB2)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```
terraform import "github_repository.repository" "S25-core-course-labs"
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Importing from ID "S25-core-course-labs"...
github_repository.repository: Import prepared!
  Prepared github_repository for import
github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

Then I started to set up the GitHub repository, but I got an error.

```
terraform apply
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.default_branch will be created
  + resource "github_branch_default" "default_branch" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default_branch_protection will be created
  + resource "github_branch_protection" "default_branch_protection" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
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
      + description                 = "Repository for the S25 core course labs"
      - has_downloads               = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repository: Modifying... [id=S25-core-course-labs]
github_repository.repository: Modifications complete after 3s [id=S25-core-course-labs]
github_branch_default.default_branch: Creating...
github_branch_protection.default_branch_protection: Creating...
github_branch_protection.default_branch_protection: Creation complete after 6s [id=BPR_kwDONxWB-84Dkwxc]
╷
│ Error: PATCH https://api.github.com/repos/darrpyy/S25-core-course-labs: 422 Validation Failed [{Resource:Repository Field:default_branch Code:invalid Message:The branch main was not found. Please push that ref first or create it via the Git Data API.}]
│ 
│   with github_branch_default.default_branch,
│   on main.tf line 20, in resource "github_branch_default" "default_branch":
│   20: resource "github_branch_default" "default_branch" {
│ 
╵
```

I changed the default branch to master and applied the changes.

```
terraform apply
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Refreshing state... [id=BPR_kwDONxWB-84Dkwxc]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.default_branch will be created
  + resource "github_branch_default" "default_branch" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default_branch_protection will be updated in-place
  ~ resource "github_branch_protection" "default_branch_protection" {
        id                              = "BPR_kwDONxWB-84Dkwxc"
      ~ pattern                         = "main" -> "master"
        # (9 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.default_branch: Creating...
github_branch_protection.default_branch_protection: Modifying... [id=BPR_kwDONxWB-84Dkwxc]
github_branch_default.default_branch: Creation complete after 3s [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Modifications complete after 7s [id=BPR_kwDONxWB-84Dkwxc]

Apply complete! Resources: 1 added, 1 changed, 0 destroyed.
```

Then I decided to destroy the resource, to return to the initial state.

```
terraform destroy
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]
github_branch_default.default_branch: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Refreshing state... [id=BPR_kwDONxWB-84Dkwxc]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # github_branch_default.default_branch will be destroyed
  - resource "github_branch_default" "default_branch" {
      - branch     = "master" -> null
      - id         = "S25-core-course-labs" -> null
      - repository = "S25-core-course-labs" -> null
    }

  # github_branch_protection.default_branch_protection will be destroyed
  - resource "github_branch_protection" "default_branch_protection" {
      - allows_deletions                = false -> null
      - allows_force_pushes             = false -> null
      - blocks_creations                = false -> null
      - enforce_admins                  = true -> null
      - id                              = "BPR_kwDONxWB-84Dkwxc" -> null
      - pattern                         = "master" -> null
      - push_restrictions               = [] -> null
      - repository_id                   = "S25-core-course-labs" -> null
      - require_conversation_resolution = true -> null
      - require_signed_commits          = false -> null
      - required_linear_history         = false -> null

      - required_pull_request_reviews {
          - dismiss_stale_reviews           = false -> null
          - dismissal_restrictions          = [] -> null
          - pull_request_bypassers          = [] -> null
          - require_code_owner_reviews      = false -> null
          - required_approving_review_count = 1 -> null
          - restrict_dismissals             = false -> null
        }
    }

  # github_repository.repository will be destroyed
  - resource "github_repository" "repository" {
      - allow_auto_merge            = false -> null
      - allow_merge_commit          = true -> null
      - allow_rebase_merge          = true -> null
      - allow_squash_merge          = true -> null
      - archived                    = false -> null
      - auto_init                   = false -> null
      - branches                    = [
          - {
              - name      = "lab1"
              - protected = false
            },
          - {
              - name      = "lab2"
              - protected = false
            },
          - {
              - name      = "lab3"
              - protected = false
            },
          - {
              - name      = "lab4"
              - protected = false
            },
          - {
              - name      = "master"
              - protected = false
            },
        ] -> null
      - default_branch              = "master" -> null
      - delete_branch_on_merge      = false -> null
      - description                 = "Repository for the S25 core course labs" -> null
      - etag                        = "W/\"c3728206ce2eaad86737a82536de6306e2f0bf9aea3626bdd4f4543a35b0c3d0\"" -> null
      - full_name                   = "darrpyy/S25-core-course-labs" -> null
      - git_clone_url               = "git://github.com/darrpyy/S25-core-course-labs.git" -> null
      - has_downloads               = false -> null
      - has_issues                  = false -> null
      - has_projects                = false -> null
      - has_wiki                    = false -> null
      - html_url                    = "https://github.com/darrpyy/S25-core-course-labs" -> null
      - http_clone_url              = "https://github.com/darrpyy/S25-core-course-labs.git" -> null
      - id                          = "S25-core-course-labs" -> null
      - is_template                 = false -> null
      - merge_commit_message        = "PR_TITLE" -> null
      - merge_commit_title          = "MERGE_MESSAGE" -> null
      - name                        = "S25-core-course-labs" -> null
      - node_id                     = "R_kgDONxWB-w" -> null
      - private                     = false -> null
      - repo_id                     = 924156411 -> null
      - squash_merge_commit_message = "COMMIT_MESSAGES" -> null
      - squash_merge_commit_title   = "COMMIT_OR_PR_TITLE" -> null
      - ssh_clone_url               = "git@github.com:darrpyy/S25-core-course-labs.git" -> null
      - svn_url                     = "https://github.com/darrpyy/S25-core-course-labs" -> null
      - topics                      = [] -> null
      - visibility                  = "public" -> null
      - vulnerability_alerts        = false -> null
        # (1 unchanged attribute hidden)
    }

Plan: 0 to add, 0 to change, 3 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

github_branch_default.default_branch: Destroying... [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Destroying... [id=BPR_kwDONxWB-84Dkwxc]
github_branch_default.default_branch: Destruction complete after 1s
github_branch_protection.default_branch_protection: Destruction complete after 2s
github_repository.repository: Destroying... [id=S25-core-course-labs]
github_repository.repository: Destruction complete after 2s

Destroy complete! Resources: 3 destroyed.
```

But I deleted my repository...

Then I created a new one and imported it.

```
terraform init
Initializing the backend...
Initializing provider plugins...
- Finding integrations/github versions matching "~> 4.0"...
- Installing integrations/github v4.31.0...
- Installed integrations/github v4.31.0 (signed by a HashiCorp partner, key ID 38027F80D7FD5FB2)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```
terraform import "github_repository.repository" "S25-core-course-labs"
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Importing from ID "S25-core-course-labs"...
github_repository.repository: Import prepared!
  Prepared github_repository for import
github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

Then I set up the GitHub repository again.

```
terraform plan
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.default_branch will be created
  + resource "github_branch_default" "default_branch" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default_branch_protection will be created
  + resource "github_branch_protection" "default_branch_protection" {
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
      + description                 = "Repository for the S25 core course labs"
      - has_downloads               = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform
apply" now.
```

```
terraform apply
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.default_branch will be created
  + resource "github_branch_default" "default_branch" {
      + branch     = "master"
      + id         = (known after apply)
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default_branch_protection will be created
  + resource "github_branch_protection" "default_branch_protection" {
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
      + description                 = "Repository for the S25 core course labs"
      - has_downloads               = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "S25-core-course-labs"
        name                        = "S25-core-course-labs"
        # (29 unchanged attributes hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repository: Modifying... [id=S25-core-course-labs]
github_repository.repository: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_default.default_branch: Creating...
github_branch_protection.default_branch_protection: Creating...
github_branch_default.default_branch: Creation complete after 3s [id=S25-core-course-labs]
╷
│ Error: Your token has not been granted the required scopes to execute this query. The 'id' field requires one of the following scopes: ['read:org', 'read:discussion'], but your token has only been granted the: ['repo', 'workflow'] scopes. Please modify your token's scopes at: https://github.com/settings/tokens.
│ 
│   with github_branch_protection.default_branch_protection,
│   on main.tf line 25, in resource "github_branch_protection" "default_branch_protection":
│   25: resource "github_branch_protection" "default_branch_protection" {
```

```
terraform apply
var.token
  Token for GitHub

  Enter a value: 

github_repository.repository: Refreshing state... [id=S25-core-course-labs]
github_branch_default.default_branch: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.default_branch_protection: Refreshing state... [id=BPR_kwDON9-MJc4DkxOJ]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # github_branch_protection.default_branch_protection is tainted, so must be replaced
-/+ resource "github_branch_protection" "default_branch_protection" {
      ~ id                              = "BPR_kwDON9-MJc4DkxOJ" -> (known after apply)
      - push_restrictions               = [] -> null
        # (9 unchanged attributes hidden)

      ~ required_pull_request_reviews {
          - dismiss_stale_reviews           = false -> null
          - dismissal_restrictions          = [] -> null
          - pull_request_bypassers          = [] -> null
          - require_code_owner_reviews      = false -> null
          - restrict_dismissals             = false -> null
            # (1 unchanged attribute hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_protection.default_branch_protection: Destroying... [id=BPR_kwDON9-MJc4DkxOJ]
github_branch_protection.default_branch_protection: Destruction complete after 1s
github_branch_protection.default_branch_protection: Creating...
github_branch_protection.default_branch_protection: Creation complete after 5s [id=BPR_kwDON9-MJc4DkxQ5]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```
