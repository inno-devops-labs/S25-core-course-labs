terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  service_account_key_file = var.key_file
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  zone                     = var.yc_zone
}


data "yandex_compute_image" "ubuntu" {
  family = "ubuntu-2204-lts"
}

resource "yandex_vpc_network" "network-1" {
  name = "Network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "Subnet-1"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.20.0/24"]
  zone           = var.yc_zone
}

resource "yandex_compute_instance" "vm-1" {
  name = var.vm_name

  resources {
    memory = var.vm_ram_gb
    cores  = var.vm_cpu_cores
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.ubuntu.id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = format("%s:%s", var.vm_username, file(var.ssh_key_path))
  }
}