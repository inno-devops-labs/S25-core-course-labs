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
  name           = "Subnet 1"
  zone           = var.zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "vm-1" {
  name = var.vm_name

  resources {
    memory = var.vm_ram_gb
    cores  = var.vm_cpu_cores
  }

  boot_disk {
    initialize_params {
      image_id = var.vm_image_id
    }
  }

  metadata = {
    ssh-keys = format("%s:%s", var.vm_username, file(var.ssh_pubkey_path))
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
}