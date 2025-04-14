terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
      version = "0.136.0"
    }
  }
}

locals {
    folder_id = "b1gt8olbpdgmsces3tni"    # новый folder_id
    cloud_id = "b1gpqbb1khso30unqusm"     # новый cloud_id
}

provider "yandex" {
  cloud_id = local.cloud_id
  folder_id = local.folder_id
  service_account_key_file = "authorized_key.json"
}

resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet-1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}


resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"
  zone = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd85u0rct32prepgjlv0"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

metadata = { ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}" }
}