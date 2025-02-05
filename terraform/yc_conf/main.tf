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
  cloud_id                 = "b1gp7t0qpnmu38si8eir"
  folder_id                = "b1gimkng7ujh1sldefn0"
  zone                     = "<default_availability_zone>"
}

resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet-1"
  network_id     = yandex_vpc_network.network-1.id
  zone           = "ru-central1-d"
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "terraform1" {
  name        = "terraform1"
  zone        = "ru-central1-d"
  platform_id = "standard-v3"

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
    user-data = "${file("${path.module}/meta.txt")}"
  }
}

resource "yandex_compute_instance" "terraform2" {
  name        = "terraform2"
  zone        = "ru-central1-d"
  platform_id = "standard-v3"

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
    user-data = "${file("${path.module}/meta.txt")}"
  }
}
