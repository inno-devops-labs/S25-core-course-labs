terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.136.0"
    }
  }
}

provider "yandex" {
  zone      = var.zone
  token     = var.iam_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

resource "yandex_compute_instance" "vm-1" {
  name        = var.vm_name
  platform_id = var.platform_id
  zone        = var.zone
  hostname    = var.hostname

  resources {
    cores         = var.cores
    core_fraction = var.core_fraction
    memory        = var.memory
  }

  scheduling_policy {
    preemptible = var.preemptible
  }

  boot_disk {
    disk_id = yandex_compute_disk.disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = var.nat
  }

  metadata = {
    "ssh-keys" = format("%s:%s", var.vm_username, file(var.ssh_pubkey_path))
  }

}

resource "yandex_compute_disk" "disk-1" {
  name     = var.disk_name
  zone     = var.zone
  size     = var.disk_size
  type     = var.disk_type
  image_id = var.image_id
}

resource "yandex_vpc_network" "network-1" {
  name = var.network_name
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = var.subnet_name
  zone           = var.zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.1.0/24"]
}
