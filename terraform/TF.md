## First output

So, I did as guideline said. The first output is:

```bash
❯ terraform state list
docker_container.nginx
docker_image.nginx

❯ terraform state show docker_container.nginx
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
    hostname                                    = "021d5b5cd528"
    id                                          = "021d5b5cd528147b725647a9eeeb77ee4dc4c3b5aa89395f4cc4e017a5d6ea12"
    image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
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
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

## Second output with vairables

```bash
❯ terraform state list
docker_container.nginx
docker_image.nginx
❯ terraform state show docker_container.nginx
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
    hostname                                    = "d67e1204abb3"
    id                                          = "d67e1204abb36a63b011bb494e31b4beebb4ea9dcfe84a56a3ba907dfe814f46"
    image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "YetAnotherName"
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

## Outputs

```bash
❯ terraform output
container_id = "0e0462fbffa67b7697a0ee47e8f0534081338b825e3df7f107d6ac5d05e6c53e"
image_id = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx"
```

## Yandex Journey

1. Installed yc thing, completed authentification.
2. `terraform init`
3. Configurating using the guide:
    - add a payment method
    - ssh keys
    - main.tf
    - .terraformrc
    - fixed configuration
    - run `terraform plan`, got auth error, fixed by changing token parameter

```bash
Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  [32m+[0m create[0m

Terraform will perform the following actions:

[1m  # yandex_compute_disk.boot-disk-1[0m will be created
[0m  [32m+[0m[0m resource "yandex_compute_disk" "boot-disk-1" {
      [32m+[0m[0m block_size  = 4096
      [32m+[0m[0m created_at  = (known after apply)
      [32m+[0m[0m folder_id   = (known after apply)
      [32m+[0m[0m id          = (known after apply)
      [32m+[0m[0m image_id    = "fd87va5cc00gaq2f5qfb"
      [32m+[0m[0m name        = "boot-disk-1"
      [32m+[0m[0m product_ids = (known after apply)
      [32m+[0m[0m size        = 20
      [32m+[0m[0m status      = (known after apply)
      [32m+[0m[0m type        = "network-hdd"
      [32m+[0m[0m zone        = "ru-central1-d"

      [32m+[0m[0m disk_placement_policy (known after apply)

      [32m+[0m[0m hardware_generation (known after apply)
    }

[1m  # yandex_compute_disk.boot-disk-2[0m will be created
[0m  [32m+[0m[0m resource "yandex_compute_disk" "boot-disk-2" {
      [32m+[0m[0m block_size  = 4096
      [32m+[0m[0m created_at  = (known after apply)
      [32m+[0m[0m folder_id   = (known after apply)
      [32m+[0m[0m id          = (known after apply)
      [32m+[0m[0m image_id    = "fd87va5cc00gaq2f5qfb"
      [32m+[0m[0m name        = "boot-disk-2"
      [32m+[0m[0m product_ids = (known after apply)
      [32m+[0m[0m size        = 20
      [32m+[0m[0m status      = (known after apply)
      [32m+[0m[0m type        = "network-hdd"
      [32m+[0m[0m zone        = "ru-central1-d"

      [32m+[0m[0m disk_placement_policy (known after apply)

      [32m+[0m[0m hardware_generation (known after apply)
    }

[1m  # yandex_compute_instance.vm-1[0m will be created
[0m  [32m+[0m[0m resource "yandex_compute_instance" "vm-1" {
      [32m+[0m[0m created_at                = (known after apply)
      [32m+[0m[0m folder_id                 = (known after apply)
      [32m+[0m[0m fqdn                      = (known after apply)
      [32m+[0m[0m gpu_cluster_id            = (known after apply)
      [32m+[0m[0m hardware_generation       = (known after apply)
      [32m+[0m[0m hostname                  = (known after apply)
      [32m+[0m[0m id                        = (known after apply)
      [32m+[0m[0m maintenance_grace_period  = (known after apply)
      [32m+[0m[0m maintenance_policy        = (known after apply)
      [32m+[0m[0m metadata                  = {
          [32m+[0m[0m "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEgqO1wvBi9S8n9zJI54ngnHnfRnIybY6pa2t3z0lK/X yandex cloud
            EOT
        }
      [32m+[0m[0m name                      = "terraform1"
      [32m+[0m[0m network_acceleration_type = "standard"
      [32m+[0m[0m platform_id               = "standard-v1"
      [32m+[0m[0m service_account_id        = (known after apply)
      [32m+[0m[0m status                    = (known after apply)
      [32m+[0m[0m zone                      = (known after apply)

      [32m+[0m[0m boot_disk {
          [32m+[0m[0m auto_delete = true
          [32m+[0m[0m device_name = (known after apply)
          [32m+[0m[0m disk_id     = (known after apply)
          [32m+[0m[0m mode        = (known after apply)

          [32m+[0m[0m initialize_params (known after apply)
        }

      [32m+[0m[0m metadata_options (known after apply)

      [32m+[0m[0m network_interface {
          [32m+[0m[0m index              = (known after apply)
          [32m+[0m[0m ip_address         = (known after apply)
          [32m+[0m[0m ipv4               = true
          [32m+[0m[0m ipv6               = (known after apply)
          [32m+[0m[0m ipv6_address       = (known after apply)
          [32m+[0m[0m mac_address        = (known after apply)
          [32m+[0m[0m nat                = true
          [32m+[0m[0m nat_ip_address     = (known after apply)
          [32m+[0m[0m nat_ip_version     = (known after apply)
          [32m+[0m[0m security_group_ids = (known after apply)
          [32m+[0m[0m subnet_id          = (known after apply)
        }

      [32m+[0m[0m placement_policy (known after apply)

      [32m+[0m[0m resources {
          [32m+[0m[0m core_fraction = 100
          [32m+[0m[0m cores         = 2
          [32m+[0m[0m memory        = 2
        }

      [32m+[0m[0m scheduling_policy (known after apply)
    }

[1m  # yandex_compute_instance.vm-2[0m will be created
[0m  [32m+[0m[0m resource "yandex_compute_instance" "vm-2" {
      [32m+[0m[0m created_at                = (known after apply)
      [32m+[0m[0m folder_id                 = (known after apply)
      [32m+[0m[0m fqdn                      = (known after apply)
      [32m+[0m[0m gpu_cluster_id            = (known after apply)
      [32m+[0m[0m hardware_generation       = (known after apply)
      [32m+[0m[0m hostname                  = (known after apply)
      [32m+[0m[0m id                        = (known after apply)
      [32m+[0m[0m maintenance_grace_period  = (known after apply)
      [32m+[0m[0m maintenance_policy        = (known after apply)
      [32m+[0m[0m metadata                  = {
          [32m+[0m[0m "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEgqO1wvBi9S8n9zJI54ngnHnfRnIybY6pa2t3z0lK/X yandex cloud
            EOT
        }
      [32m+[0m[0m name                      = "terraform2"
      [32m+[0m[0m network_acceleration_type = "standard"
      [32m+[0m[0m platform_id               = "standard-v1"
      [32m+[0m[0m service_account_id        = (known after apply)
      [32m+[0m[0m status                    = (known after apply)
      [32m+[0m[0m zone                      = (known after apply)

      [32m+[0m[0m boot_disk {
          [32m+[0m[0m auto_delete = true
          [32m+[0m[0m device_name = (known after apply)
          [32m+[0m[0m disk_id     = (known after apply)
          [32m+[0m[0m mode        = (known after apply)

          [32m+[0m[0m initialize_params (known after apply)
        }

      [32m+[0m[0m metadata_options (known after apply)

      [32m+[0m[0m network_interface {
          [32m+[0m[0m index              = (known after apply)
          [32m+[0m[0m ip_address         = (known after apply)
          [32m+[0m[0m ipv4               = true
          [32m+[0m[0m ipv6               = (known after apply)
          [32m+[0m[0m ipv6_address       = (known after apply)
          [32m+[0m[0m mac_address        = (known after apply)
          [32m+[0m[0m nat                = true
          [32m+[0m[0m nat_ip_address     = (known after apply)
          [32m+[0m[0m nat_ip_version     = (known after apply)
          [32m+[0m[0m security_group_ids = (known after apply)
          [32m+[0m[0m subnet_id          = (known after apply)
        }

      [32m+[0m[0m placement_policy (known after apply)

      [32m+[0m[0m resources {
          [32m+[0m[0m core_fraction = 100
          [32m+[0m[0m cores         = 4
          [32m+[0m[0m memory        = 4
        }

      [32m+[0m[0m scheduling_policy (known after apply)
    }

[1m  # yandex_vpc_network.network-1[0m will be created
[0m  [32m+[0m[0m resource "yandex_vpc_network" "network-1" {
      [32m+[0m[0m created_at                = (known after apply)
      [32m+[0m[0m default_security_group_id = (known after apply)
      [32m+[0m[0m folder_id                 = (known after apply)
      [32m+[0m[0m id                        = (known after apply)
      [32m+[0m[0m labels                    = (known after apply)
      [32m+[0m[0m name                      = "network1"
      [32m+[0m[0m subnet_ids                = (known after apply)
    }

[1m  # yandex_vpc_subnet.subnet-1[0m will be created
[0m  [32m+[0m[0m resource "yandex_vpc_subnet" "subnet-1" {
      [32m+[0m[0m created_at     = (known after apply)
      [32m+[0m[0m folder_id      = (known after apply)
      [32m+[0m[0m id             = (known after apply)
      [32m+[0m[0m labels         = (known after apply)
      [32m+[0m[0m name           = "subnet1"
      [32m+[0m[0m network_id     = (known after apply)
      [32m+[0m[0m v4_cidr_blocks = [
          [32m+[0m[0m "192.168.10.0/24",
        ]
      [32m+[0m[0m v6_cidr_blocks = (known after apply)
      [32m+[0m[0m zone           = "ru-central1-d"
    }

[1mPlan:[0m 6 to add, 0 to change, 0 to destroy.
[0m
Changes to Outputs:
  [32m+[0m[0m external_ip_address_vm_1 = (known after apply)
  [32m+[0m[0m external_ip_address_vm_2 = (known after apply)
  [32m+[0m[0m internal_ip_address_vm_1 = (known after apply)
  [32m+[0m[0m internal_ip_address_vm_2 = (known after apply)
[90m
─────────────────────────────────────────────────────────────────────────────[0m

Note: You didn't use the -out option to save this plan, so Terraform can't
guarantee to take exactly these actions if you run "terraform apply" now.
```

Now I run `terraform apply` to execute the plan.
