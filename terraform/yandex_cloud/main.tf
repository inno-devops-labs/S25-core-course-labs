terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  service_account_key_file = "/Users/demanzverev/PycharmProjects/S25-core-course-labs/terraform/yandex_cloud/key.json"
  zone                     = "ru-central1-d"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name      = "boot-disk-1"
  type      = "network-hdd"
  zone      = "ru-central1-d"
  size      = "20"
  image_id  = "fd865udut6b1gvgh5igh"
  folder_id = "b1gnpf3rtes5m5rrcjhm"
}

resource "yandex_compute_disk" "boot-disk-2" {
  name      = "boot-disk-2"
  type      = "network-hdd"
  zone      = "ru-central1-d"
  size      = "20"
  image_id  = "fd865udut6b1gvgh5igh"
  folder_id = "b1gnpf3rtes5m5rrcjhm"
}

resource "yandex_compute_instance" "vm-1" {
  name      = "terraform1"
  folder_id = "b1gnpf3rtes5m5rrcjhm"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = file("./meta.txt")
  }
}

resource "yandex_compute_instance" "vm-2" {
  name      = "terraform2"
  folder_id = "b1gnpf3rtes5m5rrcjhm"

  resources {
    cores  = 4
    memory = 4
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-2.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = file("./meta.txt")
  }
}

resource "yandex_vpc_network" "network-1" {
  name      = "network1"
  folder_id = "b1gnpf3rtes5m5rrcjhm"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-d"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  folder_id      = "b1gnpf3rtes5m5rrcjhm"
}