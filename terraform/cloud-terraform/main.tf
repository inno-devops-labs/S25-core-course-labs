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
  token      = "t1.9euelZqSmZ2KjZ3Pl8mLyM6Rno2Qne3rnpWanJeRxsqSz5aMxo2QncyTnZvl8_c8TSNC-e8DaUFp_N3z93x7IEL57wNpQWn8zef1656VmpScyszGypGcz8fLjc-Mz8zI7_zF656VmpScyszGypGcz8fLjc-Mz8zI.ZdD19J8ilxgtT63rNxOlTSQwQuz9q_05h-5vT698Qhq5DUS2mbL1GtIhwvUho0dM4I1al8NW5W_wEHJ85NoqBg"
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
    ssh-keys = "ubuntu:${file("/home/a/.ssh/id_rsa.pub")}"
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
    ssh-keys = "ubuntu:${file("/home/a/.ssh/id_rsa.pub")}"
  }
}


output "terraform1_public_ip" {
  value = yandex_compute_instance.terraform1.network_interface.0.nat_ip_address
}

output "terraform2_public_ip" {
  value = yandex_compute_instance.terraform2.network_interface.0.nat_ip_address
}


