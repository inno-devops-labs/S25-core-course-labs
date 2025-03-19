# Terraform

## Terraform best practices

* Separate terraform files by their responsibility: providers, variables, network, outputs, etc.
* Split files by scopes of work (GitHub, Cloud, Docker)
* Preserve one variable naming style (e.g. snake_case)
* Use `terraform fmt` to keep configs consistent
* Use `terraform validate` to keep configs correct

## Docker

### Terraform state list

```shell
terraform state list

docker_container.nginx
docker_image.nginx
```

### Terraform state show

```shell
terraform state show docker_container.nginx

# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "5a783323a624"
    id                                          = "5a783323a6241eb1aba9915ec17102d364493fb3a949af1cbffd33d69753b410"
    image                                       = "sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206a"
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
            global_ipv6_address       = [90mnull[0m[0m
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = [90mnull[0m[0m
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = [90mnull[0m[0m
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
    user                                        = [90mnull[0m[0m
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = [90mnull[0m[0m

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Terraform outputs

```shell
terraform output
                           
container_id = "5a783323a6241eb1aba9915ec17102d364493fb3a949af1cbffd33d69753b410"
image_id = "sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206anginx:latest"
```

## YandexCloud

1. Init terraform

```shell
terraform init -backend-config="access_key=$ACCESS_KEY"-backend-config="secret_key=$SECRET_KEY"
```

2. Apply terraform

```shell
terraform apply -var="cloud_id=$YC_CLOUD_ID" -var="folder_id=$YC_CATALOG_ID" -var="service_account_key_file=$YC_KEY_PATH"
```

3. terraform state list

```shell
yandex_compute_image.ubuntu_2004
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

4. terraform show

```shell
# yandex_compute_image.ubuntu_2004:
resource "yandex_compute_image" "ubuntu_2004" {
    created_at    = "2025-02-05T20:18:46Z"
    folder_id     = "b1gqtkcc8ktga62edqu5"
    id            = "fd8m4rsmq1h574oau0as"
    min_disk_size = 5
    pooled        = false
    product_ids   = [
        "f2ed6k5slaamr94lfdqu",
    ]
    size          = 4
    source_family = "ubuntu-2004-lts"
    status        = "ready"
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2025-02-05T20:18:58Z"
    folder_id                 = "b1gqtkcc8ktga62edqu5"
    fqdn                      = "fhmcm18frvk6i0dhpd5g.auto.internal"
    id                        = "fhmcm18frvk6i0dhpd5g"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBg7zb98jwHYj0WUX13c9mYdzNqf5GWAjypJxwvak4S3 maksalena04@mail.ru
        EOT
    }
    name                      = "terraform1"
        network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm4m7b9iak2hil0gv1i"
        disk_id     = "fhm4m7b9iak2hil0gv1i"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8m4rsmq1h574oau0as"
            size       = 5
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
        ip_address         = "192.168.10.15"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:cb:05:0f:df"
        nat                = true
        nat_ip_address     = "158.160.120.130"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b2fo6cn6loi08v5mn7"
    }

    placement_policy {
        host_affinity_rules = []
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
    created_at                = "2025-02-05T20:22:51Z"
    default_security_group_id = "enp1q2cplpnm3cn3m5sv"
    folder_id                 = "b1gqtkcc8ktga62edqu6"
    id                        = "enptm3esh55lj9e46c8m"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9b2fo6cn6loi08v5mn7",
    ]
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2025-02-05T20:22:55Z"
    folder_id      = "b1gqtkcc8ktga62edqu6"
    id             = "e9b2fo6cn6loi08v5mn7"
    labels         = {}
    name           = "subnet1"
    network_id     = "enptm3esh55lj9e46c8m"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

5. terraform output

```shell
external_ip_address_vm_1 = "158.160.60.155"
internal_ip_address_vm_1 = "192.168.10.33"

```

## GitHub

### Terraform import

```shell
terraform import github_repository.terraform "S25-core-course-labs"

var.github_token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.terraform: Importing from ID "S25-core-course-labs"...
github_repository.terraform: Import prepared!
  Prepared github_repository for import
github_repository.terraform: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Outputs

```shell
terraform state show github_repository.terraform
terraform state list
terraform output
```

These outputs will give you details about infrastructure and applied changes.
