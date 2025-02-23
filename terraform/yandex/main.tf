terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = var.availability_zone
}

resource "yandex_compute_disk" "ya_vm_disk_1" {
  name     = "${var.vm_name}-disk1"
  type     = "network-hdd"
  zone     = var.availability_zone
  size     = "20"
  image_id = "fd85hkli5dp6as39ali4"
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = var.availability_zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "ya_vm" {
  name = var.vm_name

  resources {
    cores = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.ya_vm_disk_1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

output "internal_ip_address" {
  value = yandex_compute_instance.ya_vm.network_interface.0.ip_address
}

output "external_ip_address" {
  value = yandex_compute_instance.ya_vm.network_interface.0.nat_ip_address
}

