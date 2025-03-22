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
  token     = var.iam_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  network_id     = yandex_vpc_network.network-1.id
  name           = "subnet1"
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = var.zone
}

resource "yandex_compute_instance" "virtual_machine" {
  name = var.virtual_machine_name
  zone = var.zone

  resources {
    cores         = var.cores
    memory        = var.memory
    core_fraction = var.core_fraction
  }

  boot_disk {
    initialize_params {
      image_id = var.image_id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = var.nat
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.ssh_path)}"
  }
}
