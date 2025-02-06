# Task 1: Introduction to Terraform

## 1. Installing terraform

## 2. Docker configuraion

1. terraform state list

```bash
$ cd terrafrom/docker
$ terraform state list
docker_container.python_app
docker_image.python_app
```

2. commands output:

```bash
$ terraform state show docker_container.python_app
# docker_container.nginx_container:
# docker_container.python_app:
resource "docker_container" "python_app" {
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
    hostname                                    = "d3b6216c8e9e"
    id                                          = "d3b6216c8e9e3b7c6a10617bb2bc12b8593e89bf7cdb5aae952b5f2df887415a"
    image                                       = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_web_app"
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
    restart                                     = "unless-stopped"
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
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

$ terraform state show docker_image.nginx 
# docker_image.python_app:
resource "docker_image" "python_app" {
    id           = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest"
    image_id     = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461"
    keep_locally = false
    name         = "jlfkajlkifj/app_python:latest"
    repo_digest  = "jlfkajlkifj/app_python@sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461"
}

```

3. terraform apply log

```bash
docker_image.nginx: Refreshing state... [id=sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcefnginx]
docker_container.nginx_container: Refreshing state... [id=c32efdcff7910807f6382be46315febcccfdbcdea62ab430c8daa3170d406f1b]

...

[id=c32efdcff7910807f6382be46315febcccfdbcdea62ab430c8daa3170d406f1b]
docker_image.python_app: Creating...
docker_container.nginx_container: Destruction complete after 1s
docker_image.nginx: Destroying... [id=sha256:bc2f6a7c8ddbccf55bdb19659ce3b0a92ca6559e86d42677a5a02ef6bda2fcefnginx]
docker_image.nginx: Destruction complete after 1s
docker_image.python_app: Still creating... [10s elapsed]
docker_image.python_app: Creation complete after 11s [id=sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest]
docker_container.python_app: Creating...
docker_container.python_app: Creation complete after 3s [id=d3b6216c8e9e3b7c6a10617bb2bc12b8593e89bf7cdb5aae952b5f2df887415a]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

container_id = "d3b6216c8e9e3b7c6a10617bb2bc12b8593e89bf7cdb5aae952b5f2df887415a"
container_ports = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_status = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest"
```

4. utilizing input variables to rename docker container

```bash
$ terraform apply -var="container_name=whatever"

$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                    NAMES
59f1bebfbbdc   ce9d72aa69bf   "uvicorn app:app --h…"   7 seconds ago   Up 6 seconds   0.0.0.0:8000->8000/tcp   whatever
```

5.output of the `terraform output`

```bash
$ terraform output
container_id = "59f1bebfbbdcdf22a12cd8856a622b257f3002fc3570d5d36e256c68079d3ee0"
container_ports = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_status = "sha256:ce9d72aa69bf109217ce191194a9b4144df7c9c67c32eb1361c13738c04f5461jlfkajlkifj/app_python:latest"
```

## 3. Yandex Cloud

1. get yandex cloud account
2. Following instructions from official documentation (instructions with the use of yandex cli tool)

```bash
$ yc iam service-account create --name terraform-user
$ yc resource-manager folder add-access-binding default --role editor --subject serviceAccount:$(yc iam service-account get terraform-user --format=json | jq -r '.id')
$ yc iam key create --service-account-name terraform-user --output key.json
$ yc config profile create sa-terraform
$ yc config set cloud-id <ID>
$ yc config set folder-id <ID>

# using command with prefilled .env file (cp .env.example .env)
$ export $(grep -v '^#' .env | tr -d '\r' | xargs)

```

3. prepare and run terraform

```bash
$ terraform init
$ terraform plan
$ terraform apply
yandex_compute_instance.vm: Creating...
yandex_compute_instance.vm: Still creating... [10s elapsed]
yandex_compute_instance.vm: Still creating... [20s elapsed]
yandex_compute_instance.vm: Still creating... [30s elapsed]
yandex_compute_instance.vm: Still creating... [40s elapsed]
yandex_compute_instance.vm: Creation complete after 43s [id=fhm198ofngo67keno0oo]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

external_ip = "62.84.114.182"
internal_ip = "10.128.0.20"
vm_id = "fhm198ofngo67keno0oo"

$ terraform state list
yandex_compute_instance.vm
$ terraform state show yandex_compute_instance.vm
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2025-02-06T07:33:47Z"
    description               = null
    folder_id                 = "b1gi6gaakrk344s01bdb"
    fqdn                      = "fhm198ofngo67keno0oo.auto.internal"
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
    id                        = "fhm198ofngo67keno0oo"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa 
        EOT
    }
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm0258udefiejbena7o"
        disk_id     = "fhm0258udefiejbena7o"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd805qs1mn3n0casp7lt"
            kms_key_id  = null
            name        = null
            size        = 15
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
        ip_address         = "10.128.0.20"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:14:a3:0f:bc"
        nat                = true
        nat_ip_address     = "62.84.114.182"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bdrdmagsihu74fvkp5"
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

VM setup: 
- 2 cores
- 2GB RAM
- Ubuntu 20.04 LTS
- NAT enabled for external access
- SSH key authentication




