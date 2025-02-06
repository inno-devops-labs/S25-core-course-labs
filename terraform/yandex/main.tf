terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}

resource "yandex_vpc_network" "network-tfproject" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-tfproject" {
  name           = "subnet-1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-tfproject.id
  v4_cidr_blocks = ["10.0.100.0/24"]
}


resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"
  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd82odtq5h79jo7ffss3" # Ubuntu 24.04
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-tfproject.id
    nat       = true # Assign a public IP
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}
