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

resource "yandex_vpc_network" "devops-net" {
  name = "devops-network"
}

resource "yandex_vpc_subnet" "devops-subnet" {
  zone           = var.zone
  network_id     = yandex_vpc_network.devops-net.id
  v4_cidr_blocks = ["192.168.0.0/16"]
}

resource "yandex_compute_disk" "vm-disk" {
  name     = "ubuntu-2404-lts-oslogin-v20250203"
  type     = var.disk_type
  size     = var.disk_gb
  zone     = var.zone
  image_id = var.disk_image_id
}

resource "yandex_compute_instance" "vm" {
  name = "devops-vm"
  zone = var.zone

  resources {
    memory        = var.ram_gb
    cores         = var.cores
    core_fraction = var.core_fraction
  }

  scheduling_policy {
    preemptible = var.preemptible
  }

  boot_disk {
    disk_id = yandex_compute_disk.vm-disk.id
  }

  network_interface {
    index     = 1
    subnet_id = yandex_vpc_subnet.devops-subnet.id
    nat       = true
  }

  metadata = {
    ssh-keys = "windows:${file(var.ssh_key)}"
  }
}