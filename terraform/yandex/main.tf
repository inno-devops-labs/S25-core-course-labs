terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  service_account_key_file = var.service_account_key_file
  zone = var.zone
}

resource "yandex_vpc_network" "nikita-net" {
  name = "nikita-network"
  folder_id = var.folder_id
}

resource "yandex_vpc_subnet" "nikita-subnet" {
  folder_id = var.folder_id
  zone           = var.zone
  network_id     = yandex_vpc_network.nikita-net.id
  v4_cidr_blocks = ["192.168.0.0/16"]
}

resource "yandex_compute_disk" "vm-disk" {
  name     = "nikita-disk"
  type     = var.disk_type
  size     = var.disk_gb
  zone     = var.zone
  image_id = var.disk_image_id
  folder_id = var.folder_id
}

resource "yandex_compute_instance" "vm" {
  name = "nikita-vm"
  zone = var.zone
  folder_id = var.folder_id

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
    subnet_id = yandex_vpc_subnet.nikita-subnet.id
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.ssh_key)}"
  }
}