# Terraform

## Docker

### Output of `terraform state show`

```markdown
# docker_container.nginx:
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
    hostname                                    = "56a7d1ba20c5"
    id                                          = "56a7d1ba20c559ae334349e0457e06182fcc8848c72682b4fda3a2301d10e83d"
    image                                       = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "ExampleNginxContainer"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

### Output of `terraform state list`

```markdown
docker_container.nginx
docker_image.nginx
```

### Output of `terraform apply` 

Terraform used the selected providers to generate the following
execution plan. Resource actions are indicated with the
following symbols:
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
      + name                                        = "ExampleNginxContainer"
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

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Creation complete after 17s [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=56a7d1ba20c559ae334349e0457e06182fcc8848c72682b4fda3a2301d10e83d]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "56a7d1ba20c559ae334349e0457e06182fcc8848c72682b4fda3a2301d10e83d"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest"

# docker_container.nginx must be replaced

-/+ resource "docker_container" "nginx" {
+ bridge = (known after apply)
~ command = [
- "nginx",
- "-g",
- "daemon off;",
] -> (known after apply)
+ container_logs = (known after apply)
- cpu_shares = 0 -> null
- dns = [] -> null
- dns_opts = [] -> null
- dns_search = [] -> null
~ entrypoint = [
- "/docker-entrypoint.sh",
] -> (known after apply)
~ env = [] -> (known after apply)
+ exit_code = (known after apply)
- group_add = [] -> null
~ hostname = "8162814cd1bc" -> (known after apply)
~ id = "8f29a3e4d5c6b7a8e9f0123456789abcdeffedcba9876543210abcdedf012345" -> (known after apply)
~ init = false -> (known after apply)
~ ipc_mode = "private" -> (known after apply)
~ log_driver = "json-file" -> (known after apply)
- log_opts = {} -> null
- max_retry_count = 0 -> null
- memory = 0 -> null
- memory_swap = 0 -> null
name = "tutorial"
~ network_data = [
- {
- gateway = "172.17.0.1"
- global_ipv6_address = ""
- global_ipv6_prefix_length = 0
- ip_address = "172.17.0.2"
- ip_prefix_length = 16
- ipv6_gateway = ""
- mac_address = "02:42:ac:11:00:02"
- network_name = "bridge"
},
] -> (known after apply)
- network_mode = "default" -> null
- privileged = false -> null
- publish_all_ports = false -> null
~ runtime = "runc" -> (known after apply)
~ security_opts = [] -> (known after apply)
~ shm_size = 64 -> (known after apply)
~ stop_signal = "SIGQUIT" -> (known after apply)
~ stop_timeout = 0 -> (known after apply)
- storage_opts = {} -> null
- sysctls = {} -> null
- tmpfs = {} -> null
# (14 unchanged attributes hidden)

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

docker_container.nginx: Destroying... [id=8f29a3e4d5c6b7a8e9f0123456789abcdeffedcba9876543210abcdedf012345]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=f67e0747bb827c2ba874393f1424e511bf8651814b7219a41c984b359eb33617]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.


# terraform state show docker_container.nginx
``` 
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
    hostname                                    = "56a7d1ba20c5"
    id                                          = "56a7d1ba20c559ae334349e0457e06182fcc8848c72682b4fda3a2301d10e83d"
    image                                       = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "ExampleNginxContainer"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
sh-3.2$ terraform output
container_id = "56a7d1ba20c559ae334349e0457e06182fcc8848c72682b4fda3a2301d10e83d"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest"
```

### Output of `terraform output`

```markdown
container_id = "56a7d1ba20c559ae334349e0457e06182fcc8848c72682b4fda3a2301d10e83d"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx:latest"
```

## Yandex Cloud

### Output of `terraform apply`

```markdown
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
with the following symbols:
+ create
Terraform will perform the following actions:
# yandex_compute_disk.boot-disk-1 will be created
+ resource "yandex_compute_disk" "boot-disk-1" {
    + block_size  = 4096
    + created_at  = (known after apply)
    + folder_id   = (known after apply)
    + id          = (known after apply)
    + image_id    = "fd8t8vqitgjou20saanq"
    + name        = "boot-disk-1"
    + product_ids = (known after apply)
    + size        = 20
    + status      = (known after apply)
    + type        = "network-hdd"
    + zone        = "ru-central1-a"
    }
# yandex_compute_instance.vm-1 will be created
+ resource "yandex_compute_instance" "vm-1" {
    + created_at                = (known after apply)
    + folder_id                 = (known after apply)
    + fqdn                      = (known after apply)
    + gpu_cluster_id            = (known after apply)
    + hostname                  = (known after apply)
    + id                        = (known after apply)
    + maintenance_grace_period  = (known after apply)
    + maintenance_policy        = (known after apply)
    + metadata                  = {
        + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOa7qiTifRZeFREx3ukKUmI2kKK2BAMl3jRYbd+0STxn ag5274606@gmail.com
            EOT
        }
    + name                      = "terraform1"
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
        }
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
    + resources {
        + core_fraction = 100
        + cores         = 2
        + memory        = 2
        }
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
Plan: 4 to add, 0 to change, 0 to destroy.
Changes to Outputs:
+ external_ip_address_vm_1 = (known after apply)
+ internal_ip_address_vm_1 = (known after apply)
Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.
Enter a value: yes
yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 2s [id=enpm579u5mn0fd3f7dmo]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e9bqt7i476ec6btt1m4m]
yandex_compute_disk.boot-disk-1: Creation complete after 6s [id=fhmgcvu2ld689l09aimp]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 30s [id=fhmamghpkdpq8tp2s49d]
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
Outputs:
external_ip_address_vm_1 = "155.160.40.14"
internal_ip_address_vm_1 = "192.168.10.7"
```

### Output of `terraform state list`

```markdown
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Output of `terraform state show yandex_compute_instance.vm-1`

```markdown
# yandex_compute_instance.vm-1:

resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T20:41:12Z"
    folder_id                 = "8045ffb6736203e80d50"
    fqdn                      = "db751b249c18ee60ca94.auto.internal"
    id                        = "db751b249c18ee60ca94"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOa7qiTifRZeFREx3ukKUmI2kKK2BAMl3jRYbd+0STxn ag5274606@gmail.com
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"
    boot_disk {
        auto_delete = true
        device_name = "c7c7a0bc2578b05ef450"
        disk_id     = "c7c7a0bc2578b05ef450"
        mode        = "READ_WRITE"
        initialize_params {
            block_size = 4096
            image_id   = "fd8t8vqitgjou20saanq"
            name       = "boot-disk-1"
            size       = 20
            type       = "network-hdd"
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
        ip_address         = "192.168.10.7"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:ab:42:39:a3"
        nat                = true
        nat_ip_address     = "155.160.40.14"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "535a066de42d1ba555e4"
    }
    placement_policy {
        host_affinity_rules       = []
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
```

### Output of `terraform output`

```markdown
external_ip_address_vm_1 = "155.160.40.14"
internal_ip_address_vm_1 = "192.168.10.7"
```

## GitHub
``` terraform state show github_repository.terraform
# github_repository.terraform:
resource "github_repository" "terraform" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = false
    default_branch              = "master"
    delete_branch_on_merge      = false
    description                 = null
    etag                        = "W/\"54bd9b6d88ede98093f789cef6734ce7bf08443bada86d1881baf26086b6d491\""
    full_name                   = "kurkune/S25-core-course-labs"
    git_clone_url               = "git://github.com/kurkune/S25-core-course-labs.git"
    has_discussions             = false
    has_downloads               = true
    has_issues                  = false
    has_projects                = true
    has_wiki                    = true
    homepage_url                = null
    html_url                    = "https://github.com/kurkune/S25-core-course-labs"
    http_clone_url              = "https://github.com/kurkune/S25-core-course-labs.git"
    id                          = "S25-core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S25-core-course-labs"
    node_id                     = "R_kgDONxUYig"
    primary_language            = null
    private                     = false
    repo_id                     = 924129418
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:kurkune/S25-core-course-labs.git"
    svn_url                     = "https://github.com/kurkune/S25-core-course-labs"
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
# terraform state list
```github_repository.terraform
```

## Best Practises

- Version Control: Store Terraform configurations in Git to track changes and collaborate.
- Modularization: Use reusable modules to simplify maintenance and reduce duplication.
- State Management: Store state files remotely for collaboration and integrity.
- Provider Versions: Lock provider versions to prevent unexpected updates.
- Environment Separation: Maintain separate environments (dev, staging, prod) using variables.
- Immutable Infrastructure: Recreate resources instead of modifying them to avoid drift.
- Variable Management: Use input variables for flexibility across environments.
- Sensitive Data Handling: Store credentials securely using environment variables or secrets management.
- Monitoring & Logging: Track changes and troubleshoot efficiently with monitoring tools.
- Testing: Use automated testing (e.g., Terratest) to catch errors early.