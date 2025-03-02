# Terraform

## Docker Infrastructure

`terraform state list`:
```
docker_container.app
docker_image.app
```

`terraform state show docker_container.app`:
```
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "gunicorn",
        "-b",
        "0.0.0.0:8000",
        "wsgi",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "f233c7b6cb87"
    id                                          = "f233c7b6cb8729b31e383e82b84b82a8f15e9828ec316f82e4c4389cedf83d2a"
    image                                       = "sha256:30e803389ca53823bf9d179dea53aaa1dd656799bc8794970e52a5308114e947"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app"
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
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

`terraform output`:
```
container_id = "f233c7b6cb8729b31e383e82b84b82a8f15e9828ec316f82e4c4389cedf83d2a"
image_id = "sha256:30e803389ca53823bf9d179dea53aaa1dd656799bc8794970e52a5308114e947app:latest"
```

## Yandex Cloud Infrastracture

First of all i created a service account:
```
yc iam service-account create --name denisnesterov
```

Then i assigned the editor role:

```
yc resource-manager folder add-access-binding b1ga70f94f0o5e4c2sgl \
  --role editor \
  --subject serviceAccount:ajenkda1onu306cffn96
```
Then i configure terraform provider, and created resources:
```
terraform apply
```

`terraform state list`:
```
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

`terraform state show yandex_compute_instance.vm-1`:
```
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-06T20:13:35Z"
    description               = null
    folder_id                 = "b1ga70f94f0o5e4c2sgl"
    fqdn                      = "fhma896s1cj8i8qbsp3i.auto.internal"
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
    id                        = "fhma896s1cj8i8qbsp3i"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDnxCH3MVZjOxhg4RfrPL7cC8JBWG4WjEjDKhGkEq+TUEUmMwxSjnbfYwERp46/pByqsNdZp0xRENjFvDVhitEWF2w4Ptaq5lk921p6xouj2GoX3pVxE1qSDgCGBC0fyrBf9aw8icbJU4qtNbzsfRWZgl6tJqgbgSH+4CC6h9J7QnoiHJXA4XTmDVymExID9uVRUmVt+L1CrFJczGKOWAsKrX7DCIsQPi/twtwVdacN1fcjpAeMZphUYdpohMYgdDDSFXAtZrooKx6ps69OZSXIypf7Mp1XNW5+rChKPKPhGNgd0rgxXrUbEVU5v4wm7jXL5JCL+rGskpJvFPOi0QOhmFoa8QNwEwZci6nUTcG6HpzC7UnmCf/f4K/Tc8dza+Q+NR7I4BJ8wOLrv+rkS5zpvXO4rhCd+ZaQ5OY5v/HXMhOIuK0u9mhnCLoPOyeZCalxjLqrZRy9x5TwO/EiyfPaklnxr6jCXnAfnQ0Zi7XM6f/Q+24bbwj9/yVZ7FULCbwE8I0yzrNsOn7gKsxjmmVhQK15tSs60xbLL980BWGBV8NbiuqF6fEDQqJOdktC9XLUCAeQ9KF2mAv6aW6M6LvCiqQBh7lYYgbGAtNb3EFFESt0/o95iy85ty4OiFym+vFezjyh140ZNxu+nfFIG2ReYMKn3fQ+iWYmWuC/NC5Lqw== denisnesterov3005@yandex.ru
        EOT
    }
    name                      = "denisnesterov"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmfoi67uorcrg2j1tb3"
        disk_id     = "fhmfoi67uorcrg2j1tb3"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd86jl8gechvgkabt374"
            kms_key_id  = null
            name        = null
            size        = 5
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
        ip_address         = "192.168.10.17"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:a4:24:dc:0b"
        nat                = true
        nat_ip_address     = "89.169.147.5"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bnp6r2t6b46u1q67j2"
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
