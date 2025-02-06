# Terraform

## Applied practices

- **Code separation**: terraform code is separated into `main.tf`, `providers.td`, `outputs.tf`, and `variables.tf` to ensure more readable and maintainable code.

- **Validating**: `terraform fmt` and `terrafomr fmt` are used to format and validate the code.

## Docker Infrastructure using Terraform

### By running this command:

```bash
terraform show
```

### We get:

```bash
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
    hostname                                    = "7da3c2dbf6b0"
    id                                          = "7da3c2dbf6b0b5582ef9b4bd28899278fb64faaecc647fb9f6bd09b0e992f2fa"
    image                                       = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial-container"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9bnginx:latest"
    image_id     = "sha256:c59e925d63f3aa135bfa9d82cb03fba9ee30edb22ebe6c9d4f43824312ba3d9b"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcef"
}


Outputs:

container_name = "tutorial-container"
container_ports = [
    {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    },
]
```

### By running this command:

```bash
terraform state list
```

### We get:

```bash
docker_container.nginx
docker_image.nginx
```

### By running this command:

```bash
terraform output
```

### We get:

```bash
container_name = "tutorial-container"
container_ports = tolist([
  {
    "external" = 8080
    "internal" = 80
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud Infrastracture Using Terraform

### These are the steps which were needed for me to use Yandex with Terraform:

1. First of all, I created `OAuth token` to be able to access Yandex CLI. This was done using `Yandex ID`.

2. After that I made a `service account` in Yandex cloud, and assigned roles to it.

3. After that I configured the CLI keys (Cloud and Folder ID's, etc.)

4. Then according to the guide, I created `VM` and `VPC` and used `SSH key` to connect to `VM`.

5. Lastly, I configured terraform files.

### Challenges

In my opinion, the guide is not very well structured. Moreover at some point after doing everything according to the guide, my `VM`'s were stopped working, and after spending quite sometime I found out that this was all because network zone on which they were created in the guide.

### Running `terraform show` after the yandex guide:

```bash
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2025-02-06T05:33:06Z"
    description = null
    folder_id   = "b1gh60mr8hd4rdim37e5"
    id          = "fhmf2b01roofr6pikdcb"
    image_id    = "fd8ldp0p1dtrfl09r797"
    labels      = {}
    name        = "boot-disk-1"
    product_ids = [
        "f2e5n6ia72e3dph94c8v",
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

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-06T05:33:46Z"
    description               = null
    folder_id                 = "b1gh60mr8hd4rdim37e5"
    fqdn                      = "fhm8hk3ec185kt97c8fj.auto.internal"
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
    id                        = "fhm8hk3ec185kt97c8fj"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMXqzO2M17DUG1siV2ZDtd7GIzVLV6TmQwiScUrg+APt yandexcloud
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmf2b01roofr6pikdcb"
        disk_id     = "fhmf2b01roofr6pikdcb"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd8ldp0p1dtrfl09r797"
            kms_key_id  = null
            name        = "boot-disk-1"
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
        ip_address         = "192.168.10.23"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:88:d0:6e:60"
        nat                = true
        nat_ip_address     = "89.169.138.225"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b21j60qrbfqlnfvskm"
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

# yandex_vpc_network.network-3:
resource "yandex_vpc_network" "network-3" {
    created_at                = "2025-02-06T05:32:50Z"
    default_security_group_id = "enpn3enm2sei7naaic67"
    description               = null
    folder_id                 = "b1gh60mr8hd4rdim37e5"
    id                        = "enpnb16bq2ccqlhl6q6t"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9b21j60qrbfqlnfvskm",
    ]
}

# yandex_vpc_subnet.subnet-3:
resource "yandex_vpc_subnet" "subnet-3" {
    created_at     = "2025-02-06T05:32:52Z"
    description    = null
    folder_id      = "b1gh60mr8hd4rdim37e5"
    id             = "e9b21j60qrbfqlnfvskm"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpnb16bq2ccqlhl6q6t"
    route_table_id = null
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}


Outputs:

external_ip_address_vm_1 = "89.169.138.225"
internal_ip_address_vm_1 = "192.168.10.23"
```

### Running `terraform state list`:

```bash
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-3
yandex_vpc_subnet.subnet-3
```

### Running `terraform output`:

```bash
external_ip_address_vm_1 = "89.169.138.225"
internal_ip_address_vm_1 = "192.168.10.23"
```