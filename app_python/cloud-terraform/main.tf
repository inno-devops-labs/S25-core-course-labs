terraform {
  required_version = ">= 0.13"
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.89.0"
    }
  }
}

provider "yandex" {
  token      = "t1.9euelZqSks-ayMyLjs6PlI_JkMiJm-3rnpWanJeRxsqSz5aMxo2QncyTnZvl8_duKm9C-e99d0Qk_t3z9y5ZbEL57313RCT-zef1656VmoyTyZCel8iWi5qTjsyejpnH7_zF656VmoyTyZCel8iWi5qTjsyejpnH.I1UjQTLlkRdg7uiBk8j854jhKNkYeI9dXLk3CNIeqlXV68tS-9O60lb6U0aooKx-t0laV2vqb_5XHMQVybOKCg"
  cloud_id   = "b1gjvnfi85r3q2356sj8"
  folder_id  = "b1gvb9vtqd8c372vunb8"
  zone       = "ru-central1-b"
}


resource "yandex_vpc_network" "network_1" {
  name = "network-1"
}


resource "yandex_vpc_subnet" "subnet_1" {
  name           = "subnet-1"
  zone           = "ru-central1-b"
  network_id     = yandex_vpc_network.network_1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}


resource "yandex_compute_instance" "terraform1" {
  name = "terraform1"

  resources {
    core_fraction = 20
    cores  = 2
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = "fd86601pa1f50ta9dffg"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_1.id
    nat       = true
  }

  metadata = {
    user-data = file("meta.txt")
  }
}


resource "yandex_compute_instance" "terraform2" {
  name = "terraform2"

  resources {
    core_fraction = 20
    cores  = 4
    memory = 8
  }

  boot_disk {
    initialize_params {
      image_id = "fd86601pa1f50ta9dffg"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_1.id
    nat       = true
  }

  metadata = {
    user-data = file("meta.txt")
  }
}


output "terraform1_public_ip" {
  value = yandex_compute_instance.terraform1.network_interface.0.nat_ip_address
}

output "terraform2_public_ip" {
  value = yandex_compute_instance.terraform2.network_interface.0.nat_ip_address
}
