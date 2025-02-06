terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-d"
}

resource "yandex_vpc_network" "network" {
  name = "moscow-time-net"
}

resource "yandex_vpc_subnet" "subnet" {
  name           = "moscow-time-subnet"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "vm" {
  name        = "moscow-time-vm"
  platform_id = "standard-v1"
  
  resources {
    cores  = 2
    memory = 1
  }

  boot_disk {
    initialize_params {
      image_id = "fd81hgrcf6fl..."
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
}






