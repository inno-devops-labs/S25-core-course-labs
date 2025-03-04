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
  cloud_id = var.cloud-id
  folder_id = var.folder-id
  token = "t1.9euelZqRl8iRlJqXkIvNnZjGk5fOke3rnpWam5LIlJ2WlZSVycmOjY2Qm47l9PdzVzhC-e9KSh-Q3fT3MwY2QvnvSkofkM3n9euelZrJicmQjMuQyovPkInIzc-LyO_8zef1656VmpiOnczLxo-anM6MmZGVlsvG7_3F656VmsmJyZCMy5DKi8-QicjNz4vI.lAgQ8Ds4dzQaWy0SzYj32yBsS1zX8s8D82yfs2heXFAEvEazZMdvQGL4e9JN0CM_--jg2wdWdXaISWuBZjkRAg"
}

resource "yandex_compute_disk" "drive" {
  name = "drive"
  type = "network-hdd"
  zone = "ru-central1-a"
  size = "21"
  image_id = "fd8t8vqitgjou20saanq"
}

resource "yandex_compute_instance" "virtual-machine" {
  name = "virtual-machine"
  allow_stopping_for_update = true
  zone = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.drive.id
  }

  network_interface {
    subnet_id = "${yandex_vpc_subnet.lab-subnet.id}"
    nat = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519_neww.pub")}"
  }
}

resource "yandex_vpc_network" "network-lab" {
  name = "network-lab"
}

resource "yandex_vpc_subnet" "lab-subnet" {
  name = "lab-subnet"
  zone = "ru-central1-a"
  v4_cidr_blocks = ["192.168.50.0/24"]
  network_id = yandex_vpc_network.network-lab.id
}