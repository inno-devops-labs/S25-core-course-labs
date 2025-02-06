# Provider: Yandex.Cloud

# General settings

terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

# Provider configuration

provider "yandex" {
  zone = var.zone
}

# Resources

# Boot disk

resource "yandex_compute_disk" "boot-disk" {
  name     = var.boot_disk_name
  type     = var.boot_disk_type
  size     = var.boot_disk_size
  image_id = var.boot_disk_image_id

  zone = var.zone
}

# Virtual machine

resource "yandex_compute_instance" "vm" {
  name = var.vm_name

  resources {
    cores  = var.vm_cores
    memory = var.vm_memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = var.vm_nat
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/azamat-pc.pub")}"
  }
}

# Network and subnet

resource "yandex_vpc_network" "network" {
  name = var.network_name
}

resource "yandex_vpc_subnet" "subnet" {
  zone       = var.zone
  network_id = yandex_vpc_network.network.id

  name           = var.subnet_name
  v4_cidr_blocks = var.subnet_v4_cidr_blocks
}
