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
  name = "default"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "default"
  zone           = var.zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.20.0/24"]
}

resource "yandex_compute_instance" "vm-1" {
  name = var.vm_name

  resources {
    memory        = var.vm_memory
    cores         = var.vm_cores
    core_fraction = var.vm_core_fraction
  }

  boot_disk {
    initialize_params {
      image_id = var.vm_image
    }
  }

  metadata = {
    ssh-keys = format("%s:%s", var.ssh_username, file(var.ssh_key_pub_path))
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
}
