terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone  = var.zone
  token = var.token
}

resource "yandex_compute_disk" "boot-disk-1" {
  name      = var.disk_name
  type      = var.disk_type
  zone      = var.zone
  size      = var.disk_size
  image_id  = var.image_id
  folder_id = var.disk_folder_id
}

resource "yandex_compute_instance" "vm-1" {
  name = var.vm_name

  resources {
    cores  = var.vm_cores
    memory = var.vm_memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.metadata_ssh_keys_path)}"
  }
  folder_id = var.vm_folder_id
}

resource "yandex_vpc_network" "network-1" {
  name      = var.network_name
  folder_id = var.network_folder_id
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = var.subnet_name
  zone           = var.subnet_zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = [var.subnet_cidr]
  folder_id      = var.network_folder_id
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}