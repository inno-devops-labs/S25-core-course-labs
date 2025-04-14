# Terraform

## Best practices applied

1. `variables.tf` is used to manage variables.
2. `.gitignore` is used to avoid adding unnecessary files to git

## Docker

- `terraform show`:

```bash
# docker_container.moscow_time_app:
resource "docker_container" "moscow_time_app" {
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
    hostname                                    = "4b0e7e76bd13"
    id                                          = "4b0e7e76bd1302ec9a97595b7489de21de46bdf81babb2410b2f98e3230e076b"
    image                                       = "sha256:495150afe78cee4d34eac68ef323561976b01fd99318688076efd096d9545b22"
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
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

- `terraform state list`:

```bash
docker_container.moscow_time_app
```

- `terraform apply`:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.moscow_time_app will be created
  + resource "docker_container" "moscow_time_app" {
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
      + image                                       = "mishablin/devops-labs:latest"
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.moscow_time_app: Creating...
docker_container.moscow_time_app: Creation complete after 1s [id=4b0e7e76bd1302ec9a97595b7489de21de46bdf81babb2410b2f98e3230e076b]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

- `terraform output`:

```bash
container_image = "mishablin/devops-labs:latest"
container_name = "app_python"
container_port = tolist([
  {
    "external" = 5000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud Set Up

**Set up steps:**

1. Install cloud cli
2. Create service account
3. Generate tokens and ids
4. Set up the provider and resources
5. Run `terraform apply`

**Outputs**:

- `terraform state list`:

```bash
data.yandex_compute_image.ubuntu
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

- `terraform show`:

```bash
# data.yandex_compute_image.ubuntu:
data "yandex_compute_image" "ubuntu" {
    created_at          = "2025-02-03T11:06:30Z"
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
    id                  = "fd8j3fo8lqh4730j2ftd"
    image_id            = "fd8j3fo8lqh4730j2ftd"
    labels              = {}
    min_disk_size       = 8
    name                = "ubuntu-22-04-lts-v20250203"
    os_type             = "linux"
    pooled              = true
    product_ids         = [
        "f2ebj2oj0d2aeadn1j0m",
    ]
    size                = 7
    status              = "ready"
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-05T20:37:58Z"
    description               = null
    folder_id                 = "b1gfbs7j036gik9qg28a"
    fqdn                      = "fhmj7plmp00npe9hgmm3.auto.internal"
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
    id                        = "fhmj7plmp00npe9hgmm3"
    labels                    = {}
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
        device_name = "fhmspt4b17etjqsovdp2"
        disk_id     = "fhmspt4b17etjqsovdp2"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd8j3fo8lqh4730j2ftd"
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
        ip_address         = "192.168.20.31"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:13:3e:6b:6c"
        nat                = true
        nat_ip_address     = "89.169.131.82"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b503fimd5moima07hb"
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
    created_at                = "2025-02-05T20:35:15Z"
    default_security_group_id = "enpiv2r1fafj7fmp3249"
    description               = null
    folder_id                 = "b1gfbs7j036gik9qg28a"
    id                        = "enpgg0ui8ednp4ulk3od"
    labels                    = {}
    name                      = "Network-1"
    subnet_ids                = [
        "e9b503fimd5moima07hb",
    ]
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-05T20:37:57Z"
    description    = null
    folder_id      = "b1gfbs7j036gik9qg28a"
    id             = "e9b503fimd5moima07hb"
    labels         = {}
    name           = "Subnet-1"
    network_id     = "enpgg0ui8ednp4ulk3od"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.20.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Github

- `terraform state list`:

```bash
github_branch_default.master
github_branch_protection.default
github_repository.devops-labs
```

- `terraform show`:

```bash
# github_branch_default.master:
resource "github_branch_default" "master" {
    branch     = "master"
    etag       = "W/\"5c03d869a8244bb68ebe03acb7dfaa0600d72ade288c98cef51b68cd72f1b8e5\""
    id         = "S25-core-course-labs"
    rename     = false
    repository = "S25-core-course-labs"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = true
    id                              = "BPR_kwDONu9miM4Dif_L"
    lock_branch                     = false
    pattern                         = "master"
    repository_id                   = "S25-core-course-labs"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
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
    default_branch              = "master"
    delete_branch_on_merge      = false
    description                 = null
    etag                        = "W/\"5c03d869a8244bb68ebe03acb7dfaa0600d72ade288c98cef51b68cd72f1b8e5\""
    full_name                   = "MishaBlin/S25-core-course-labs"
    git_clone_url               = "git://github.com/MishaBlin/S25-core-course-labs.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    homepage_url                = null
    html_url                    = "https://github.com/MishaBlin/S25-core-course-labs"
    http_clone_url              = "https://github.com/MishaBlin/S25-core-course-labs.git"
    id                          = "S25-core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S25-core-course-labs"
    node_id                     = "R_kgDONu9miA"
    primary_language            = null
    private                     = false
    repo_id                     = 921659016
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:MishaBlin/S25-core-course-labs.git"
    svn_url                     = "https://github.com/MishaBlin/S25-core-course-labs"
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
