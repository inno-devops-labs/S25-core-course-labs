terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

#create subnet
resource "yandex_vpc_subnet" "default" {
  name           = "default-subnet"
  network_id     = yandex_vpc_network.network-1.id
  zone           = var.yandex_zone
  v4_cidr_blocks = ["10.0.0.0/16"]
}

#create compute instance -vm
resource "yandex_compute_instance" "vm_instance" {
  name        = "ayanami"
  platform_id = "standard-v1"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd87b75j9rhq6keh2e55" 
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

