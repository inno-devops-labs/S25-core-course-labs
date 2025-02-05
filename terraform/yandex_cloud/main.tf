terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = var.zone
}

resource "yandex_compute_disk" "boot-disk" {
  name     = var.disk_config.name
  type     = var.disk_config.type
  zone     = var.zone
  size     = var.disk_config.size
  image_id = var.disk_config.image_id
}

resource "yandex_compute_instance" "vm" {
  name = var.vm_config.name

  resources {
    cores  = var.vm_config.cores
    memory = var.vm_config.memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = var.vm_config.nat
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

resource "yandex_vpc_network" "network" {
  name = var.network_name
}

resource "yandex_vpc_subnet" "subnet" {
  name           = var.subnet_config.name
  zone           = var.zone
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = var.subnet_config.v4_cidr_blocks
}
