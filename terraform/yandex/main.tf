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
  cloud_id                 = "b1gpnamgq8jefkt1777t"
  folder_id                = "b1ghcrf8i2l4oiqvhfso"
  zone                     = "ru-central1-d"
}

resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet-1"
  zone           = "ru-central1-d"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "vm-1" {
  name        = "terraform1"
  platform_id = "standard-v3"
  zone        = "ru-central1-d"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd800c7s2p483i648ifv"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = "${file("/Users/nikitadrozdov/DevOps/S25-core-course-labs/terraform/yandex/data.txt")}"
  }

}

resource "yandex_compute_instance" "vm-2" {
  name        = "terraform2"
  platform_id = "standard-v3"
  zone        = "ru-central1-d"

  resources {
    cores  = 4
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = "fd800c7s2p483i648ifv"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = "${file("/Users/nikitadrozdov/DevOps/S25-core-course-labs/terraform/yandex/data.txt")}"
  }
}

