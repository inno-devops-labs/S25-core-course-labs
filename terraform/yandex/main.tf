terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = ru-central1-a
}

resource "yandex_vpc_network" "devops" {
  name = "devops"
}

resource "yandex_vpc_subnet" "devops-subnet" {
  zone           = ru-central1-a
  network_id     = yandex_vpc_network.devops.id
  v4_cidr_blocks = ["192.168.0.0/16"]
}

resource "yandex_compute_disk" "vm-disk" {
  name     = "ubuntu-2404-lts-oslogin-v20250203"
  type     = var.disk_type
  size     = var.disk_gb
  zone     = ru-central1-a
  image_id = var.image_id
}

resource "yandex_compute_instance" "vm" {
  name = "devops-vm"
  zone = ru-central1-a

  resources {
    memory        = 4
    cores         = 2
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
    ssh-keys = "var.ssh_key"
  }
}
