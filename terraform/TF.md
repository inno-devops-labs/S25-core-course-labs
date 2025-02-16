# Terraform

## Docker

1. ```terraform state list```

    ```commandline
    docker_container.python_container
    docker_image.python_app
    ```

2. ```terraform state show docker_container.python_container```

    ```commandline
    # docker_container.python_container:
    resource "docker_container" "python_container" {
        attach                                      = false
        bridge                                      = null
        command                                     = [
            "python",
            "-u",
            "app/app.py",
        ]
        container_read_refresh_timeout_milliseconds = 15000
        cpu_set                                     = null
        cpu_shares                                  = 0
        domainname                                  = null
        entrypoint                                  = []
        env                                         = []
        hostname                                    = "a8fecafe5641"
        id                                          = "a8fecafe5641dce7ae219b736c99b1313eddf07ec7daebd85bcf5db60f5ce18f"
        image                                       = "sha256:da008578d0e7f2300583fc26c9eb5b1f63e5446e2481eca0c2d0bfea01883410"
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
                ip_address                = "172.17.0.4"
                ip_prefix_length          = 16
                ipv6_gateway              = null
                mac_address               = "02:42:ac:11:00:04"
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
        user                                        = "webUser"
        userns_mode                                 = null
        wait                                        = false
        wait_timeout                                = 60
        working_dir                                 = "/app"
    
        ports {
            external = 5000
            internal = 5000
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }
    ```

3. ```terraform state show docker_image.python_app```

    ```commandline
    # docker_image.python_app:
    resource "docker_image" "python_app" {
        id          = "sha256:78a74fb73bfb12a8641cc50cbc82f57c610aaafa73b628896cb71a475497922cpython:3.11"
        image_id    = "sha256:78a74fb73bfb12a8641cc50cbc82f57c610aaafa73b628896cb71a475497922c"
        name        = "python:3.11"
        repo_digest = "python@sha256:14b4620f59a90f163dfa6bd252b68743f9a41d494a9fde935f9d7669d98094bb"
    }
    ```

4. ```terraform output```

```commandline
python_container_id = "a8fecafe5641dce7ae219b736c99b1313eddf07ec7daebd85bcf5db60f5ce18f"
python_container_image = "leha0704/morozov_devops_webapp:latest"
python_container_name = "app_python"
```

## Yandex Cloud

I used this [tutorial](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart`).
There were no complications.

1. ```terraform state list```

    ```commandline
    yandex_compute_instance.vm-1
    yandex_vpc_network.network-1
    yandex_vpc_subnet.subnet-1
    ```

2. ```terraform state show yandex_compute_instance.vm-1```

    ```commandline
    # yandex_compute_instance.vm-1:
    resource "yandex_compute_instance" "vm-1" {
        created_at                = "2025-02-06T00:40:02Z"
        description               = null
        folder_id                 = "b1gil461o5s88c4kdutr"
        fqdn                      = "fhmjg4grjci4flb6e3au.auto.internal"
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
        id                        = "fhmjg4grjci4flb6e3au"
        maintenance_grace_period  = null
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE8M66Dza0bLVtbYGtaj5v0ikDK986gNjXJP8YfgxAod user_maa@DESKTOP-OG7VOP3
            EOT
        }
        name                      = "terraform-vm-1"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        service_account_id        = null
        status                    = "running"
        zone                      = "ru-central1-a"
    
        boot_disk {
            auto_delete = true
            device_name = "fhmr9a29imh0rq9kkfpo"
            disk_id     = "fhmr9a29imh0rq9kkfpo"
            mode        = "READ_WRITE"
    
            initialize_params {
                block_size  = 4096
                description = null
                image_id    = "fd800c7s2p483i648ifv"
                kms_key_id  = null
                name        = null
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
            ip_address         = "172.16.10.20"
            ipv4               = true
            ipv6               = false
            ipv6_address       = null
            mac_address        = "d0:0d:13:81:21:b9"
            nat                = true
            nat_ip_address     = "89.169.148.200"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e9b8f6vo5hm22804aoc5"
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
    ```

3. ```terraform state show yandex_vpc_network.network-1```

    ```commandline
    # yandex_compute_instance.vm-1:
    resource "yandex_compute_instance" "vm-1" {
        created_at                = "2025-02-06T00:40:02Z"
        description               = null
        folder_id                 = "b1gil461o5s88c4kdutr"
        fqdn                      = "fhmjg4grjci4flb6e3au.auto.internal"
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
        id                        = "fhmjg4grjci4flb6e3au"
        maintenance_grace_period  = null
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE8M66Dza0bLVtbYGtaj5v0ikDK986gNjXJP8YfgxAod user_maa@DESKTOP-OG7VOP3
            EOT
        }
        name                      = "terraform-vm-1"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        service_account_id        = null
        status                    = "running"
        zone                      = "ru-central1-a"
    
        boot_disk {
            auto_delete = true
            device_name = "fhmr9a29imh0rq9kkfpo"
            disk_id     = "fhmr9a29imh0rq9kkfpo"
            mode        = "READ_WRITE"
    
            initialize_params {
                block_size  = 4096
                description = null
                image_id    = "fd800c7s2p483i648ifv"
                kms_key_id  = null
                name        = null
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
            ip_address         = "172.16.10.20"
            ipv4               = true
            ipv6               = false
            ipv6_address       = null
            mac_address        = "d0:0d:13:81:21:b9"
            nat                = true
            nat_ip_address     = "89.169.148.200"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e9b8f6vo5hm22804aoc5"
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
    PS C:\Users\User_MAA\PycharmProjects\devops\S25-core-course-labs\terraform\yandex> terraform state show yandex_vpc_network.network-1
    # yandex_vpc_network.network-1:
    resource "yandex_vpc_network" "network-1" {
        created_at                = "2025-02-06T00:39:58Z"
        default_security_group_id = "enpr67s6clorft2i7on6"
        description               = null
        folder_id                 = "b1gil461o5s88c4kdutr"
        id                        = "enpsb2hi3ffqs5u626cc"
        labels                    = {}
        name                      = "default-1"
        subnet_ids                = []
    }
    ```

4. ```terraform state show yandex_vpc_subnet.subnet-1```

    ```commandline
    # yandex_vpc_subnet.subnet-1:
    resource "yandex_vpc_subnet" "subnet-1" {
        created_at     = "2025-02-06T00:40:00Z"
        description    = null
        folder_id      = "b1gil461o5s88c4kdutr"
        id             = "e9b8f6vo5hm22804aoc5"
        labels         = {}
        name           = null
        network_id     = "enpsb2hi3ffqs5u626cc"
        route_table_id = null
        v4_cidr_blocks = [
            "172.16.10.0/24",
        ]
        v6_cidr_blocks = []
        zone           = "ru-central1-a"
    }
    ```

## Github

1. ```terraform init```

    ```commandline
    Initializing the backend...
    Initializing provider plugins...
    - Reusing previous version of integrations/github from the dependency lock file
    - Using previously-installed integrations/github v4.31.0
    
    Terraform has been successfully initialized!
    
    You may now begin working with Terraform. Try running "terraform plan" to see
    any changes that are required for your infrastructure. All Terraform commands
    should now work.
    
    If you ever set or change modules or backend configuration for Terraform,
    rerun this command to reinitialize your working directory. If you forget, other
    commands will detect it and remind you to do so if necessary.
    ```

2. ```terraform validate```

    ```commandline
    Success! The configuration is valid.
    ```

3. ```terraform fmt```

4. ```terraform import "github_repository.repo" "S25-core-course-labs"```

   ```commandline
    var.token
      Personal access token
    
      Enter a value:
    
    
    github_repository.repo: Importing from ID "S25-core-course-labs"...
    github_repository.repo: Import prepared!
      Prepared github_repository for import
    github_repository.repo: Refreshing state... [id=S25-core-course-labs]
    
    Import successful!
    
    The resources that were imported are shown above. These resources are now in
    your Terraform state and will henceforth be managed by Terraform.
    ```

5. ```terraform apply```

    ```commandline
    var.token
      Personal access token
    
      Enter a value:
    
    
    github_repository.repo: Refreshing state... [id=S25-core-course-labs]
    
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
      + create
      ~ update in-place
    
    Terraform will perform the following actions:
    
      # github_branch_default.default will be created
      + resource "github_branch_default" "default" {
          + branch     = "feature/lab4"
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
          + pattern                         = "feature/lab4"
          + repository_id                   = "S25-core-course-labs"
          + require_conversation_resolution = true
          + require_signed_commits          = false
          + required_linear_history         = false
    
          + required_pull_request_reviews {
              + required_approving_review_count = 1
            }
        }
    
      # github_repository.repo will be updated in-place
      ~ resource "github_repository" "repo" {
          ~ auto_init                   = false -> true
          + description                 = "Good description"
          - has_downloads               = true -> null
          ~ has_issues                  = false -> true
          - has_projects                = true -> null
          - has_wiki                    = true -> null
            id                          = "S25-core-course-labs"
            name                        = "S25-core-course-labs"
            # (27 unchanged attributes hidden)
        }
    
    Plan: 2 to add, 1 to change, 0 to destroy.
    
    Do you want to perform these actions?
      Terraform will perform the actions described above.
      Only 'yes' will be accepted to approve.
    
      Enter a value: yes
    
    github_repository.repo: Modifying... [id=S25-core-course-labs]
    github_repository.repo: Modifications complete after 2s [id=S25-core-course-labs]
    github_branch_default.default: Creating...
    github_branch_default.default: Creation complete after 2s [id=S25-core-course-labs]
    github_branch_protection.default: Creating...
    github_branch_protection.default: Creation complete after 4s [id=BPR_kwDONwbclc4Dig2F]
    
    Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
    ```

## Best practises

- Most secret information is not hardcoded in files but used as env variables.
- ```terraform fmt``` and ```terraform validate``` were used to format and validate.
- There exist variables.tf and main.tf, so that files would be well-structured.
- Specified version constraints
