terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
    service_account_key_file = "key.json"
    cloud_id  = var.yc_cloud_id
    folder_id = "b1guv9r3njoqnl13l8aa"
    zone      = "ru-central1-a"
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "vm-1" {
  name = "terraform-vm"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd86p66mh3vpkbjsl7qp"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
}

output "internal_ip" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}