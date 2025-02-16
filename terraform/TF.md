# Terraform

## Docker

- `terraform apply`

```bash
(devopss) daniilzimin@MacBook-Pro docker % terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.devopsapp will be created
  + resource "docker_container" "devopsapp" {
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
      + image                                       = "daniilzimin4/devopsapp:latest"
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
          + external = 9200
          + internal = 9200
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_image = "daniilzimin4/devopsapp:latest"
  + container_name  = "app_python"
  + container_port  = [
      + {
          + external = 9200
          + internal = 9200
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.devopsapp: Creating...
docker_container.devopsapp: Still creating... [10s elapsed]
docker_container.devopsapp: Creation complete after 13s [id=6c06a8a85c62c20d262f0a098e77bcd4e6b4c2a1b2405f615a28f586db886e15]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

container_image = "daniilzimin4/devopsapp:latest"
container_name = "app_python"
container_port = tolist([
  {
    "external" = 9200
    "internal" = 9200
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

- `terraform show`:

```bash
(devopss) daniilzimin@MacBook-Pro docker % terraform show
# docker_container.devopsapp:
resource "docker_container" "devopsapp" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python",
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "6c06a8a85c62"
    id                                          = "6c06a8a85c62c20d262f0a098e77bcd4e6b4c2a1b2405f615a28f586db886e15"
    image                                       = "sha256:14b7876ee546c97fd21096e28d1e1477a856d7c0d6ff1a28b94ed12a752bfd55"
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
    user                                        = "nonroot"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/src"

    ports {
        external = 9200
        internal = 9200
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}


Outputs:

container_image = "daniilzimin4/devopsapp:latest"
container_name = "app_python"
container_port = [
    {
        external = 9200
        internal = 9200
        ip       = "0.0.0.0"
        protocol = "tcp"
    },
]
```

- `terraform state list`

```bash
(devopss) daniilzimin@MacBook-Pro docker % terraform state list
docker_container.devopsapp
```

- `terraform output`

```bash
(devopss) daniilzimin@MacBook-Pro docker % terraform output
container_image = "daniilzimin4/devopsapp:latest"
container_name = "app_python"
container_port = tolist([
  {
    "external" = 9200
    "internal" = 9200
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```


## Yandex Cloud

- `terraform apply`

```bash
(devopss) daniilzimin@MacBook-Pro yandex % terraform apply
var.cloud_id
  Enter a value: 

var.folder_id
  Enter a value: 

data.yandex_compute_image.ubuntu: Reading...
data.yandex_compute_image.ubuntu: Read complete after 0s [id=fd89sohb28dqsoq35u7j]

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
          + "ssh-keys" = (sensitive value)
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

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd89sohb28dqsoq35u7j"
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
      + name                      = "Network-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "Subnet-1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Creation complete after 4s [id=enp1h49c7q8mg1pon06j]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9b559rvso94ufcbvn81]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Still creating... [50s elapsed]
yandex_compute_instance.vm-1: Still creating... [1m0s elapsed]
yandex_compute_instance.vm-1: Still creating... [1m10s elapsed]
yandex_compute_instance.vm-1: Creation complete after 1m11s [id=fhm8qr3dr14vtp68pddh]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

- `terraform show`

```bash
(devopss) daniilzimin@MacBook-Pro yandex % terraform show
# data.yandex_compute_image.ubuntu:
data "yandex_compute_image" "ubuntu" {
    created_at          = "2025-02-10T11:05:25Z"
    description         = "ubuntu 22.04 lts"
    family              = "ubuntu-2204-lts"
    folder_id           = "standard-images"
    hardware_generation = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    id                  = "fd89sohb28dqsoq35u7j"
    image_id            = "fd89sohb28dqsoq35u7j"
    labels              = {}
    min_disk_size       = 8
    name                = "ubuntu-22-04-lts-v20250210"
    os_type             = "linux"
    pooled              = true
    product_ids         = [
        "f2el9c6r6lhur23mp6m7",
    ]
    size                = 7
    status              = "ready"
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-16T17:53:48Z"
    description               = null
    folder_id                 = "b1g3423lfomjlllv0geo"
    fqdn                      = "fhm8qr3dr14vtp68pddh.auto.internal"
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
    id                        = "fhm8qr3dr14vtp68pddh"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm6n61avoo3il94k587"
        disk_id     = "fhm6n61avoo3il94k587"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd89sohb28dqsoq35u7j"
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
        ip_address         = "192.168.20.18"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:8d:6c:6d:d8"
        nat                = true
        nat_ip_address     = "51.250.75.238"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b559rvso94ufcbvn81"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
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

# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2025-02-16T17:53:42Z"
    default_security_group_id = "enpvrga9tausqem506ak"
    description               = null
    folder_id                 = "b1g3423lfomjlllv0geo"
    id                        = "enp1h49c7q8mg1pon06j"
    labels                    = {}
    name                      = "Network-1"
    subnet_ids                = []
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-16T17:53:45Z"
    description    = null
    folder_id      = "b1g3423lfomjlllv0geo"
    id             = "e9b559rvso94ufcbvn81"
    labels         = {}
    name           = "Subnet-1"
    network_id     = "enp1h49c7q8mg1pon06j"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.20.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

- `terraform state list`

```bash
(devopss) daniilzimin@MacBook-Pro yandex % terraform state list
data.yandex_compute_image.ubuntu
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

## Github

- `terraform aapply`

```bash
(devopss) daniilzimin@MacBook-Pro github % terraform apply
var.token
  Enter a value: 

github_repository.devops-labs: Refreshing state... [id=S25-core-course-labs]
github_branch_default.master: Refreshing state... [id=S25-core-course-labs]
github_branch_protection.default: Refreshing state... [id=BPR_kwDONx6t084Dj3Ni]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.master will be updated in-place
  ~ resource "github_branch_default" "master" {
      ~ branch     = "lab-4" -> "master"
        id         = "S25-core-course-labs"
        # (3 unchanged attributes hidden)
    }

  # github_branch_protection.default will be updated in-place
  ~ resource "github_branch_protection" "default" {
        id                              = "BPR_kwDONx6t084Dj3Ni"
      ~ pattern                         = "lab-4" -> "master"
        # (9 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 0 to add, 2 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.master: Modifying... [id=S25-core-course-labs]
github_branch_default.master: Modifications complete after 2s [id=S25-core-course-labs]
github_branch_protection.default: Modifying... [id=BPR_kwDONx6t084Dj3Ni]
github_branch_protection.default: Modifications complete after 5s [id=BPR_kwDONx6t084Dj3Ni]

Apply complete! Resources: 0 added, 2 changed, 0 destroyed.
```

- `terraform show`

```bash
(devopss) daniilzimin@MacBook-Pro github % terraform show
# github_branch_default.master:
resource "github_branch_default" "master" {
    branch     = "master"
    etag       = "W/\"67ccc2ec3da93823c3f042c083c58ed0793e8611eb271e73fd87bd4d1f5e2748\""
    id         = "S25-core-course-labs"
    rename     = false
    repository = "S25-core-course-labs"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = true
    force_push_bypassers            = []
    id                              = "BPR_kwDONx6t084Dj3Ni"
    lock_branch                     = false
    pattern                         = "master"
    repository_id                   = "S25-core-course-labs"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}

# github_repository.devops-labs:
resource "github_repository" "devops-labs" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "lab-4"
    delete_branch_on_merge      = false
    description                 = null
    etag                        = "W/\"17cea6d061919ebd472b1862f7dfbc738419d66b1e7b8119d0bdce2ed59f15fd\""
    full_name                   = "daniilzimin4/S25-core-course-labs"
    git_clone_url               = "git://github.com/daniilzimin4/S25-core-course-labs.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    homepage_url                = null
    html_url                    = "https://github.com/daniilzimin4/S25-core-course-labs"
    http_clone_url              = "https://github.com/daniilzimin4/S25-core-course-labs.git"
    id                          = "S25-core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S25-core-course-labs"
    node_id                     = "R_kgDONx6t0w"
    primary_language            = null
    private                     = false
    repo_id                     = 924757459
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:daniilzimin4/S25-core-course-labs.git"
    svn_url                     = "https://github.com/daniilzimin4/S25-core-course-labs"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
    web_commit_signoff_required = false

    security_and_analysis {
        secret_scanning {
            status = "enabled"
        }
        secret_scanning_push_protection {
            status = "enabled"
        }
    }
}
```

- `terraform state list`

```bash
(devopss) daniilzimin@MacBook-Pro github % terraform state list 
github_branch_default.master
github_branch_protection.default
github_repository.devops-labs
```