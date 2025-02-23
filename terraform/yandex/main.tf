terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token      = var.token
  cloud_id   = var.cloud_id
  folder_id  = var.folder_id
  zone = var.zone
}

resource "yandex_vpc_network" "network_1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet_1" {
  name           = "subnet-1"
  zone           = var.zone
  network_id     = yandex_vpc_network.network_1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "terraform1" {
  name = "terraform1"

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = var.image_id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_1.id
    nat       = true
  }
  metadata = {
    ssh-keys = "ubuntu:${file("/home/akvadevka/.ssh/id_rsa.pub")}"
  }
}

resource "yandex_compute_instance" "terraform2" {
  name = "terraform2"

  resources {
    cores  = 4
    memory = 8
  }

  boot_disk {
    initialize_params {
      image_id = var.image_id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_1.id
    nat       = true
  }
  metadata = {
    ssh-keys = "ubuntu:${file("/home/akvadevka/.ssh/id_rsa.pub")}"
  }

}


output "terraform1_public_ip" {
  value = yandex_compute_instance.terraform1.network_interface.0.nat_ip_address
}

output "terraform2_public_ip" {
  value = yandex_compute_instance.terraform2.network_interface.0.nat_ip_address
}
