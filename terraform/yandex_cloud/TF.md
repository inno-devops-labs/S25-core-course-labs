```commandline
demanzverev@MacBook-Pro-Deman yandex_cloud % terraform apply                                                                                                         

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1gnpf3rtes5m5rrcjhm"
      + id          = (known after apply)
      + image_id    = "fd865udut6b1gvgh5igh"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-d"

      + disk_placement_policy (known after apply)

      + hardware_generation (known after apply)
    }

  # yandex_compute_disk.boot-disk-2 will be created
  + resource "yandex_compute_disk" "boot-disk-2" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1gnpf3rtes5m5rrcjhm"
      + id          = (known after apply)
      + image_id    = "fd865udut6b1gvgh5igh"
      + name        = "boot-disk-2"
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
      + folder_id                 = "b1gnpf3rtes5m5rrcjhm"
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
                  - name: demyanzverev
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh_authorized_keys:
                        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDKmUl3PYWpatEWY4UGufevITlGpxIXL4PLxYBG7a6bXbGRCEXMFICESQr7CUgWn9mVU3r6C1TQoZCeRTcC9DPGsBdrwxBq84dWPRC+focMLaPziVXxbnz6kCv0hGQPa/nZzIvAhYxwunMSzF7dJZBKMfvFZ/xLbJFRJlf1GyDtBSDLxi+yIGdJo1B5p9DkKjEN+AOR//azIciieW5JMgeUoPoCjN96SgAS00oSsbFw1DYg6A76w5zYP5UManJRf9zsikZOg3+lypM7yFX+A0WMB4ABZz0QwhbnTjHW71bP/qgFmDUJL23FVrxBOJEb2pi1/DlRENQhX+xs0GGqDEWSjpwy3auAsSZtsJIeK/+NgOboKauWKFncFBUWibexq8OszLLB9QUCsGhdPMJ4AxXs++DB/CqRcDenlmXkGD2cnVxzj0gzdPQefGqEI6WGiXPlcyc+W5XLEXtRcWfLZmumVIb3ce1/BDMTrcLiVRM+5FudSU6BsTSlqT33GO3KPvXWoqEq4Dfktio3tqHLCV2FUp/ZuHOfwva75xWeP8u7LPHWt/1Pup3KkUTnVIT2PlEjhH2LGAU4NAjtfAPIICFrixjZE6jL2WB4kp5wsfiY5zVMnqU15pMlBEFnloOsAbF3lG3nBlY2iySPJytY6NUGNo83/EtgSU5RxEFGGXrC+w== asotruzikovic@gmail.com
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

  # yandex_compute_instance.vm-2 will be created
  + resource "yandex_compute_instance" "vm-2" {
      + created_at                = (known after apply)
      + folder_id                 = "b1gnpf3rtes5m5rrcjhm"
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
                  - name: demyanzverev
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh_authorized_keys:
                        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDKmUl3PYWpatEWY4UGufevITlGpxIXL4PLxYBG7a6bXbGRCEXMFICESQr7CUgWn9mVU3r6C1TQoZCeRTcC9DPGsBdrwxBq84dWPRC+focMLaPziVXxbnz6kCv0hGQPa/nZzIvAhYxwunMSzF7dJZBKMfvFZ/xLbJFRJlf1GyDtBSDLxi+yIGdJo1B5p9DkKjEN+AOR//azIciieW5JMgeUoPoCjN96SgAS00oSsbFw1DYg6A76w5zYP5UManJRf9zsikZOg3+lypM7yFX+A0WMB4ABZz0QwhbnTjHW71bP/qgFmDUJL23FVrxBOJEb2pi1/DlRENQhX+xs0GGqDEWSjpwy3auAsSZtsJIeK/+NgOboKauWKFncFBUWibexq8OszLLB9QUCsGhdPMJ4AxXs++DB/CqRcDenlmXkGD2cnVxzj0gzdPQefGqEI6WGiXPlcyc+W5XLEXtRcWfLZmumVIb3ce1/BDMTrcLiVRM+5FudSU6BsTSlqT33GO3KPvXWoqEq4Dfktio3tqHLCV2FUp/ZuHOfwva75xWeP8u7LPHWt/1Pup3KkUTnVIT2PlEjhH2LGAU4NAjtfAPIICFrixjZE6jL2WB4kp5wsfiY5zVMnqU15pMlBEFnloOsAbF3lG3nBlY2iySPJytY6NUGNo83/EtgSU5RxEFGGXrC+w== asotruzikovic@gmail.com
            EOT
        }
      + name                      = "terraform2"
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
          + cores         = 4
          + memory        = 4
        }

      + scheduling_policy (known after apply)
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = "b1gnpf3rtes5m5rrcjhm"
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = "b1gnpf3rtes5m5rrcjhm"
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

Plan: 6 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_compute_disk.boot-disk-2: Creating...
yandex_vpc_network.network-1: Creation complete after 2s [id=enpo92jebjjlmj0m7fmp]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e2l31o7vqgll92aj6dmg]
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-2: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-2: Creation complete after 11s [id=epd7bqssqh5ardg3qhp6]
yandex_compute_instance.vm-2: Creating...
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=epdoose01tjr11c0ohgg]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-2: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-2: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-2: Creation complete after 29s [id=epdm3r8jppi3c1dgtv1s]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 33s [id=epdss41q4f847kju3rp6]

Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "89.169.173.176"
external_ip_address_vm_2 = "89.169.172.143"
internal_ip_address_vm_1 = "192.168.10.22"
internal_ip_address_vm_2 = "192.168.10.21"
```