# Docker terraform
- `.tf` files are in `terraform/Docker` folder

## terraform state show

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
    hostname                                    = "ef77f5a92478"
    id                                          = "ef77f5a924788e5b737eae0765461f3876a3738d51327efc90303c73124bb3a7"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "lab4"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8888
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}
```

## terraform state list

```
docker_container.nginx
docker_image.nginx
```

## Output:

```
container_id = "ef77f5a924788e5b737eae0765461f3876a3738d51327efc90303c73124bb3a7"
```

# Yandex

## Setup Steps:

1. Making an authorization key for service account: 
```
yc iam key create \
  --service-account-id <put_your_id> \
  --folder-name default \
  --output key.json
```

2. CLI profile setup:
```
yc config profile create dew1769
yc config set service-account-key key.json
yc config set cloud-id b1gbl7q6t66c0u3qahg0
yc config set folder-id b1ggdftbcp0pgbf5cqiq
```

3. Environment setup:
```
$Env:YC_TOKEN=$(yc iam create-token)
$Env:YC_CLOUD_ID=$(yc config get cloud-id)
$Env:YC_FOLDER_ID=$(yc config get folder-id)
```

4. Creating terraform.rc in $env:APPDATA:
```
provider_installation {
  network_mirror {
    url = "https://terraform-mirror.yandexcloud.net/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

## Configuration files in terraform/Yandex
- main.tf
- output.tf
- variables.tf

## Results

### terraform show:
```
# yandex_compute_disk.boot-disk:
resource "yandex_compute_disk" "boot-disk" {
    block_size  = 4096
    created_at  = "2025-02-06T06:05:33Z"
    description = null
    folder_id   = "b1ggdftbcp0pgbf5cqiq"
    id          = "fhmaio4mbpkm0t859gis"
    image_id    = "fd8aphn6s5hrmjaa3qas"
    name        = "bootvmdisk"
    product_ids = [
        "f2e74g0dehclk2e86j52",
    ]
    size        = 10
    snapshot_id = null
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {
        disk_placement_group_id = null
    }

    hardware_generation {
        legacy_features {
            pci_topology = "PCI_TOPOLOGY_V1"
        }
    }
}

# yandex_compute_instance.docker-vm:
resource "yandex_compute_instance" "docker-vm" {
    created_at                = "2025-02-06T06:05:46Z"
    description               = null
    folder_id                 = "b1ggdftbcp0pgbf5cqiq"
    fqdn                      = "fhmj6nn6lb966tttgm36.auto.internal"
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
    id                        = "fhmj6nn6lb966tttgm36"
    maintenance_grace_period  = null
    metadata                  = {
        "user-data" = <<-EOT
            #cloud-config
            users:
              - name: dew1769
                groups: sudo
                shell: /bin/bash
                sudo: 'ALL=(ALL) NOPASSWD:ALL'
                ssh-authorized-keys:
                  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKvRvedEWoO4xvXfLy6V4mgDSaXMkIUYNQCU6uu4w3Hz User@dew
        EOT
    }
    name                      = "vm-1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v3"
    service_account_id        = "aje294bd0309oh2mano9"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmaio4mbpkm0t859gis"
        disk_id     = "fhmaio4mbpkm0t859gis"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd8aphn6s5hrmjaa3qas"
            kms_key_id  = null
            name        = "bootvmdisk"
            size        = 10
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
        ip_address         = "192.168.1.14"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:13:35:ee:6a"
        nat                = true
        nat_ip_address     = "158.160.56.2"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bvhro5f8dfkaloulib"
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

# yandex_container_registry.my-registry:
resource "yandex_container_registry" "my-registry" {
    created_at = "2025-02-06T06:05:33Z"
    folder_id  = "b1ggdftbcp0pgbf5cqiq"
    id         = "crpn9kaeuh2ikdm41kp5"
    name       = "python-application"
    status     = "active"
}

# yandex_iam_service_account.registry-sa:
resource "yandex_iam_service_account" "registry-sa" {
    created_at  = "2025-02-06T05:52:20Z"
    description = null
    folder_id   = "b1ggdftbcp0pgbf5cqiq"
    id          = "aje294bd0309oh2mano9"
    name        = "user"
}

# yandex_resourcemanager_folder_iam_member.registry-sa-role-images-puller:
resource "yandex_resourcemanager_folder_iam_member" "registry-sa-role-images-puller" {
    folder_id = "b1ggdftbcp0pgbf5cqiq"
    id        = "b1ggdftbcp0pgbf5cqiq/container-registry.images.puller/serviceAccount:aje294bd0309oh2mano9"
    member    = "serviceAccount:aje294bd0309oh2mano9"
    role      = "container-registry.images.puller"
}

# yandex_vpc_network.docker-vm-network:
resource "yandex_vpc_network" "docker-vm-network" {
    created_at                = "2025-02-06T06:05:33Z"
    default_security_group_id = "enp6ktaigsj30blhb60p"
    description               = null
    folder_id                 = "b1ggdftbcp0pgbf5cqiq"
    id                        = "enpeu25odfmmfld0glhg"
    labels                    = {}
    name                      = "default"
    subnet_ids                = []
}

# yandex_vpc_subnet.docker-vm-network-subnet-a:
resource "yandex_vpc_subnet" "docker-vm-network-subnet-a" {
    created_at     = "2025-02-06T06:05:36Z"
    description    = null
    folder_id      = "b1ggdftbcp0pgbf5cqiq"
    id             = "e9bvhro5f8dfkaloulib"
    labels         = {}
    name           = "default-ru-central1-a"
    network_id     = "enpeu25odfmmfld0glhg"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.1.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

### terraform state list:
```
yandex_compute_disk.boot-disk
yandex_compute_instance.docker-vm
yandex_container_registry.my-registry
yandex_iam_service_account.registry-sa
yandex_resourcemanager_folder_iam_member.registry-sa-role-images-puller
yandex_vpc_network.docker-vm-network
yandex_vpc_subnet.docker-vm-network-subnet-a
```

### terraform output:
```
Outputs:

service_account_id_on_vm = "aje294bd0309oh2mano9"
```

**Note**: I've deleted files, especially, `key.json` and terraform auto-created files from the `Yandex` folder while commiting

# Github

## Setup:
- Get the Github API token from the Developer settings
- Create `main.tf` and `variables.tf` files
- Export Github Token as environment variable: `$env:GITHUB_TOKEN="your_token_here"`
- Run commands:
```
terraform init
terraform apply -auto-approve
```

## Results

### terraform show:
```
# github_branch.main_branch:
resource "github_branch" "main_branch" {
    branch        = "main"
    etag          = "W/\"79eb7de0c3bae7a4cde608d9b5b313b2dee21dbd77a4ce215740afc36ec14d68\""
    id            = "lab:main"
    ref           = "refs/heads/main"
    repository    = "lab"
    sha           = "22c6994f97e9bb11ee2269b6675191feb5ae0331"
    source_branch = "main"
    source_sha    = "22c6994f97e9bb11ee2269b6675191feb5ae0331"
}

# github_branch_default.default:
resource "github_branch_default" "default" {
    branch     = "main"
    etag       = "W/\"40b17791f2d8fd9d4efa4bb91d3f32ea1553f4e5c1df309fcd385776fede3df2\""
    id         = "lab"
    rename     = false
    repository = "lab"
}

# github_branch_protection.main_branch_protection:
resource "github_branch_protection" "main_branch_protection" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = false
    id                              = "BPR_kwDOIbnG6M4DijCF"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "lab"
    require_conversation_resolution = false
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = true
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }

    required_status_checks {
        strict = true
    }
}
```

### terraform state list:
```
github_branch.main_branch
github_branch_default.default
github_branch_protection.main_branch_protection
```

### Best Practices Applied:

1. **Security**: Usage of `sensitive = true` for sensitive variables
2. **Variable usage**
3. **Provider configuration**: terraform config is specified including authenfication setting
4. **Branch protection rule**: prevent branch deletion and force push