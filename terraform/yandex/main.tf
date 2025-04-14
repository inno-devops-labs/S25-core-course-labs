terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 1.5"
}

provider "yandex" {
  zone = var.zone
}

resource "yandex_compute_image" "ubuntu" {
  source_family = "ubuntu-2204-lts"
}

resource "yandex_compute_disk" "boot-disk" {
  name     = "main_disk"
  type     = "network-hdd"
  zone     = var.zone
  size     = var.disk-size
  image_id = yandex_compute_image.ubuntu.id
}

resource "yandex_compute_instance" "vm-1" {
  name                      = "devops-instance"
  allow_stopping_for_update = true
  platform_id               = "standard-v3"
  zone                      = var.zone

  resources {
    cores  = var.cores
    memory = var.memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.ssh_key)}"
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = var.zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.0.0/16"]
}

