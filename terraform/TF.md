# Terraform

## terraform state list

docker_container.app_python

## terraform state show docker_container.app_python

## docker_container.app_python

```terraform
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "uvicorn",
        "app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "03bff3ffac9e"
    id                                          = "03bff3ffac9eebd23cb91861026a0fe9a9737aaa7b1144584e13bb68c852cc0e"
    image                                       = "sha256:dae538cf8d322f71c2eb5c999b8ba99df8d0bf250fadcd5edc0118889d111874"
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
    user                                        = "appuser"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## terraform output

container_id = "03bff3ffac9eebd23cb91861026a0fe9a9737aaa7b1144584e13bb68c852cc0e"
docker_container_name = "app_python"
docker_image_name = "dsaee/app"

## YandexCloud

### YandexCloud Steps

1. Install Yandex Cloud CLI
2. Create an account using `yc iam service-account create --name <service_account_name>`
3. Create a profile and set profile configuration(`service-account-key`, `cloud_id`, `folder_id`)
4. Add credentials to ENV
5. Create configuration file `main.tf`, `variables.tf` and `outputs.tf`. Content of this files can be copied from Yandex Cloud documentation
6. Configure files `main.tf`, `variables.tf` and `outputs.tf`, in other words change names to (`network-1`, `subnet-1`, use variables from `variables.tf`, print `outputs.tf`) according to guide
7. Check everything with `terraform validate` and `terraform fmt`
8. Next `terraform plan`
9. `terraform apply`, complete with all the credentials, and our VM is created

### Errors

1. The first error I encountered is about zone, first time I used `ru-central1-d`, but there were said that I can't create VM within this region, so I changed it to `ru-central1-a`
2. Problem with authentication, problem was solved when I added `token`, `cloud_id` and `folder_id` to `provider "yandex"`

### YandexCloud terraform apply

```terraform
var.folder_id
  Folder id in cloud

  Enter a value:

var.iam_token
  Token for auth

  Enter a value:


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.virtual_machine will be created
  + resource "yandex_compute_instance" "virtual_machine" {
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
      + name                      = "virtual-machine"
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
              + image_id    = "fd83s8u085j3mq231ago"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
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
          + core_fraction = 5
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
  + address = (known after apply)
  + name    = "virtual-machine"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Creation complete after 1s [id=enp3oe1ic3s1ne2r5gcb]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e9bca84s4doeu2md2ak4]
yandex_compute_instance.virtual_machine: Creating...
yandex_compute_instance.virtual_machine: Still creating... [10s elapsed]
yandex_compute_instance.virtual_machine: Still creating... [20s elapsed]
yandex_compute_instance.virtual_machine: Still creating... [30s elapsed]
yandex_compute_instance.virtual_machine: Still creating... [40s elapsed]
yandex_compute_instance.virtual_machine: Still creating... [50s elapsed]
yandex_compute_instance.virtual_machine: Creation complete after 56s [id=fhmptoqggpj1osvpchqs]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

address = "51.250.7.30"
name = "virtual-machine"
```

### YandexCloud terraform state list

yandex_compute_instance.virtual_machine
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1

### terraform state show yandex_compute_instance.virtual_machine

```terraform
# yandex_compute_instance.virtual_machine:
resource "yandex_compute_instance" "virtual_machine" {
    created_at                = "2025-02-05T15:05:48Z"
    description               = null
    folder_id                 = "b1g85gbq9ic08ortds9l"
    fqdn                      = "fhm2eojm9lv4gemr6to3.auto.internal"
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
    hostname                  = null
    id                        = "fhm2eojm9lv4gemr6to3"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "virtual-machine"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmo56b190so247egjjf"
        disk_id     = "fhmo56b190so247egjjf"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd83s8u085j3mq231ago"
            kms_key_id  = null
            name        = null
            size        = 8
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
        ip_address         = "192.168.10.32"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:27:62:76:4d"
        nat                = true
        nat_ip_address     = "84.201.156.161"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b0db060d5b26hm7gfl"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
        placement_group_partition = 0
    }

    resources {
        core_fraction = 5
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}
```

### terraform state show yandex_vpc_network.network-1

```terraform
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-05T15:25:23Z"
    default_security_group_id = "enpefh2vn1sqnv55rvpj"
    description               = null
    folder_id                 = "b1g85gbq9ic08ortds9l"
    id                        = "enp3oe1ic3s1ne2r5gcb"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}
```

### terraform state show yandex_vpc_subnet.subnet-1

```terraform
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-05T15:25:24Z"
    description    = null
    folder_id      = "b1g85gbq9ic08ortds9l"
    id             = "e9bca84s4doeu2md2ak4"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp3oe1ic3s1ne2r5gcb"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Github

### Github terraform state list

```terraform
github_branch_default.master
github_branch_protection.default
github_repository.repo
```

### Github Steps

1. Import already existing repo using `terraform import "github_repository.repo" "S25-core-course-labs"`
2. Use `terraform apply`

### terraform import "github_repository.repo" "S25-core-course-labs"

```terraform
var.token
  GITHUB Token

  Enter a value:

github_repository.repo: Importing from ID "S25-core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

```

### terraform apply

```terraform
var.token
  GITHUB Token

  Enter a value:

github_repository.repo: Refreshing state... [id=S25-core-course-labs]

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
      + repository = "S25-core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
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

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
      + description                 = "Core course labs repository"
      + gitignore_template          = "VisualStudio"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "S25-core-course-labs"
      + license_template            = "mit"
        name                        = "S25-core-course-labs"
        # (31 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  + branch      = "master"
  ~ description = "" -> "Core course labs repository"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=S25-core-course-labs]
github_repository.repo: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDONwOphc4DiehD]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

Outputs:

branch = "master"
description = "Core course labs repository"
name = "S25-core-course-labs"
visibility = "public"
```

## Best practices

1. Use of file `variable.tf` and `outputs.tf` in order to easily maintain and understand what is written, security(sensitive parameter) to output the necessary data such as a token in order to avoid data leaks
2. Use of `terraform import` in order to recreate already existing resources
3. Use of `terraform fmt` and `terraform validate` to check whether file is correct and format if needed
4. Provider versioning in order to avoid unexpected changes when updating external components
