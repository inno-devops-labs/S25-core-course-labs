terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}

resource "yandex_compute_disk" "yc-disk" {
  name = "yc-vm-disk"
  zone = var.zone
  size = var.disk_size
  type = var.disk_type
}

resource "yandex_vpc_network" "yc-iface" {
  name = var.network
}

resource "yandex_compute_instance" "yc-vm" {
  name = "terraform1"

  boot_disk {
    disk_id = yandex_compute_disk.yc-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_network.yc-iface.id
    nat       = var.nat
  }

  resources {
    cores  = var.cpu
    memory = var.ram
  }
}