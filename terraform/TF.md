## Yandex Cloud Configuration

### Network Creation Problem

```
ERROR: rpc error: code = PermissionDenied desc = Operation is not permitted in the folder
```
When trying to execute the command:
```bash
yc vpc network create   --name first-network   --labels my-label=my-value   --description "first network"
```

### Solution:

Do not remember already exactly what was the solution ~~because the lab (not even two of them) drained 12 hours clean from two days of trying to configure yandex cloud with terraform~~, but probably I just have not completed setting the folder which is why it was inaccessible.

Yandex Cloud key generation via command ```yc iam key create   --service-account-id ajerlb62gkobr8luc06v --folder-name default   --output key.json``` resulted in successful message:

```bash
id: ajelp6r9582t3esjlu1f
service_account_id: ajerlb62gkobr8luc06v
created_at: "2025-02-06T13:58:14.144040985Z"
key_algorithm: RSA_2048

```

Yandex Cloud profile creation via ```yc config profile create lab04```:

```bash
Profile 'lab04' created and activated
```

Yandex Cloud profile configuration:
```bash
yc config set service-account-key key.json
yc config set cloud-id b1g9ua85karf2rfp4623
yc config set folder-id b1g3ilnki9iohh8d9lup
```

Now let's initialize terraform. These commands return as usual, so no need to look at output:
```bash
terraform init
terraform fmt
terraform validate
```
But the result of ```terraform plan``` command is as follows:
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd86juob74b0a8ev1muk"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-d"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

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
          + "user-data" = <<-EOT
                #cloud-config
                users:
                  - name: tjann
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh_authorized_keys:
                      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF6RqQKFdfLa3wJNUMcNOtp5DdCcRnnBmqdbk6qezVut
            EOT
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

          + initialize_params (known after apply)
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
      + zone           = "ru-central1-d"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

After successful output from planning, time to apply the changes via ```terraform apply```:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1g9ua85karf2rfp4623"
      + id          = (known after apply)
      + image_id    = "fd86juob74b0a8ev1muk"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-d"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

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
          + "user-data" = <<-EOT
                #cloud-config
                users:
                  - name: tjann
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh_authorized_keys:
                      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF6RqQKFdfLa3wJNUMcNOtp5DdCcRnnBmqdbk6qezVut
            EOT
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

          + initialize_params (known after apply)
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
      + folder_id                 = "b1g9ua85karf2rfp4623"
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
      + zone           = "ru-central1-d"
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
```

### SSH-key problem

Another problem arised ~~and drained multiple hours~~ because of yandex cloud could not see the key although it was written in the profile of yandex cloud organization and its entity account 

```bash
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_organizationmanager_user_ssh_key.my_user_ssh_key: Creating...
yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
╷
│ Error: Error while requesting API to create disk: client-request-id = d1766c63-bec0-4fc0-9f1b-2b071ed50063 client-trace-id = c1c20f9e-e41f-4078-a7e0-65421ff1643e iam token create failed: server-request-id = b5541413-9457-4f68-ac39-5124c3df679c server-trace-id = 75de0d6cb1e827f5:e9e8ca4c21ba8843:75de0d6cb1e827f5:1 client-request-id = 7db7dc5b-b2b0-4ab8-a437-ceb6e9450bd9 client-trace-id = c1c20f9e-e41f-4078-a7e0-65421ff1643e rpc error: code = Unauthenticated desc = OAuth token is invalid or expired
│ 
│   with yandex_compute_disk.boot-disk-1,
│   on main.tf line 15, in resource "yandex_compute_disk" "boot-disk-1":
│   15: resource "yandex_compute_disk" "boot-disk-1" {
│ 
╵
╷
│ Error: Error while requesting API to create user ssh key for organization "<bpfbcba0tj2d95p8792f>" and subject "<b1g9ua85karf2rfp4623>": client-request-id = 6dfb849d-19b9-4d08-8f33-7aac978d9472 client-trace-id = 8ec6de73-6102-4843-be6e-d25e599d733d iam token create failed: server-request-id = e1a84791-6e06-46a6-9de6-cea260fe5fa1 server-trace-id = 7417d93f761ea4c0:bfcb4c1b6346fec8:7417d93f761ea4c0:1 client-request-id = 635e34e1-4fd3-4642-90c8-083e7378e413 client-trace-id = 8ec6de73-6102-4843-be6e-d25e599d733d rpc error: code = Unauthenticated desc = OAuth token is invalid or expired
│ 
│   with yandex_organizationmanager_user_ssh_key.my_user_ssh_key,
│   on main.tf line 46, in resource "yandex_organizationmanager_user_ssh_key" "my_user_ssh_key":
│   46: resource "yandex_organizationmanager_user_ssh_key" "my_user_ssh_key" {
│ 
╵
╷
│ Error: Error while requesting API to create network: client-request-id = e6dba471-33d1-43fc-b242-65a2a45ab212 client-trace-id = c1c20f9e-e41f-4078-a7e0-65421ff1643e iam token create failed: server-request-id = 815d9ec4-72ee-4646-8ba4-641c5da319ef server-trace-id = 6f7829f69f16b56c:202e1f528109879d:6f7829f69f16b56c:1 client-request-id = 2c7edd11-9774-498e-a49a-4904578c6f8f client-trace-id = c1c20f9e-e41f-4078-a7e0-65421ff1643e rpc error: code = Unauthenticated desc = OAuth token is invalid or expired
│ 
│   with yandex_vpc_network.network-1,
│   on main.tf line 53, in resource "yandex_vpc_network" "network-1":
│   53: resource "yandex_vpc_network" "network-1" {
```


## Terraform Trying

This is the output of ```terraform state list```:

```bash
docker_container.moscow_time
docker_image.nginx
```

Ans this is the output of ```terraform state show docker_container.moscow_time```:

```bash
# docker_container.moscow_time:
resource "docker_container" "moscow_time" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python",
        "moscow_app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "11e2520e3fde"
    id                                          = "11e2520e3fde29d9a4710905fd40c88268df0e1ecbf060585d9032a891a61cc3"
    image                                       = "sha256:84734dc66571f02183134fc7def926a1d104ed84e8b90b69e3685ce07e8dcf62"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow_app"
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
    user                                        = "mark"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

