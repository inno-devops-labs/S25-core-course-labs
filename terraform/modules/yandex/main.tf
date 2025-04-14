terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

locals {
  ssh_key = length(var.ssh_key_content) > 0 ? var.ssh_key_content : file(var.ssh_key_file)
}

provider "yandex" {
  zone = var.availability-zone
}

resource "yandex_vpc_network" "network-tfproject" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-tfproject" {
  name           = "subnet-1"
  zone           = var.availability-zone
  network_id     = yandex_vpc_network.network-tfproject.id
  v4_cidr_blocks = var.subnet_masks
}


resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"
  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = var.image_id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-tfproject.id
    nat       = true # Assign a public IP
  }

  metadata = {
    user-data = templatefile("./metadata.tftpl", { ssh_key_string = local.ssh_key })
  }
}
