terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = var.zone
}

resource "yandex_vpc_network" "network" {
  name = var.network_name
}

resource "yandex_compute_disk" "disk" {
  name     = var.disk_name
  type     = var.disk_type
  zone     = var.zone
  size     = var.disk_size
  image_id = var.disk_image_id
}

resource "yandex_compute_instance" "vm" {
  name = var.vm_name

  resources {
    cores  = var.vm_cores
    memory = var.vm_memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = var.vm_nat
  }

  metadata = {
    ssh-keys =  "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKAPSzaVP5qlXeUTM7N9dEVIWlnkBvcsS/1sy5jvMe3Y"
  }
}

resource "yandex_vpc_subnet" "subnet" {
  network_id     = yandex_vpc_network.network.id
  name           = var.subnet_name
  v4_cidr_blocks = var.subnet_v4_cidr_blocks
  zone           = var.zone
}
