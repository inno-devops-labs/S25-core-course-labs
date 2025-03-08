terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = var.yandex_zone
}

resource "yandex_vpc_network" "network_1" {
  name = "default-1"
}

resource "yandex_vpc_subnet" "subnet_1" {
  zone           = var.yandex_zone
  network_id     = yandex_vpc_network.network_1.id
  v4_cidr_blocks = ["192.168.20.0/24"]
}

resource "yandex_compute_instance" "vm_1" {
  name = "terraform-vm-1"

  resources {
    cores  = var.vm_cores
    memory = var.vm_memory
  }

  boot_disk {
    initialize_params {
      image_id = var.vm_image_id
      size     = var.vm_boot_size
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file(var.ssh_pub_key_path)}"
  }
}
