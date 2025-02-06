terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = ">= 0.13"
    }
  }
}

provider "yandex" {
  service_account_key_file = "key.json"
  cloud_id                 = "b1g6096s38c4otri9d96"
  folder_id                = "b1gmqp4v027a52li2ref"
  zone                     = "<default_availability_zone>"
}

resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet-1"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = "ru-central1-d"
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
    user-data = file("${path.module}/meta.txt")
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
    user-data = file("${path.module}/meta.txt")
  }
}