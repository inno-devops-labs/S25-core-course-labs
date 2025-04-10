terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = var.yandex_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = var.zone
}

resource "yandex_vpc_network" "lab4" {
  name = "lab4"
}

resource "yandex_vpc_subnet" "lab4-subnet" {
  zone           = var.zone
  network_id     = yandex_vpc_network.lab4.id
  v4_cidr_blocks = ["192.168.0.0/16"]
}

resource "yandex_compute_disk" "vm-disk" {
  name     = "ubuntu-disk"
  type     = "network-hdd"
  size     = var.disk_size
  zone     = var.zone
  image_id = var.image_id
}

resource "yandex_compute_instance" "vm-1" {
  name = "vm-lab-4"
  resources {
    memory = var.vm_memory
    cores  = var.vm_cores
  }

  boot_disk {
    disk_id = yandex_compute_disk.vm-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.lab4-subnet.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.ssh_key)}"
  }
}
