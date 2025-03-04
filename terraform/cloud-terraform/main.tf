terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "<default_availability_zone>"
  token = "t1.9euelZqbl5KemcyXzoyVnpGKlZSdm-3rnpWai8bKy5WbjZCPl86Qx8vLnZPl8_c-Sm1C-e8PbCht_N3z9354akL57w9sKG38zef1656VmpiWnJOcnpqTxsuRnp2Mj5SK7_zF656VmpiWnJOcnpqTxsuRnp2Mj5SK.4jqqMEjdOEW2BzE8L5LVsps2aVvf8AlIreVft-csBkCcYqEOI4fOB-dzhPkbURcSE46D-3r6pqfbnfirT-r8Dw"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-d"
  size     = "20"
  image_id = "fd87va5cc00gaq2f5qfb"
}

resource "yandex_compute_disk" "boot-disk-2" {
  name     = "boot-disk-2"
  type     = "network-hdd"
  zone     = "ru-central1-d"
  size     = "20"
  image_id = "fd87va5cc00gaq2f5qfb"
}

resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"

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
    ssh-keys = "ubuntu:${file("~/.ssh/yandex_cloud.pub")}"
  }
}

resource "yandex_compute_instance" "vm-2" {
  name = "terraform2"

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
    ssh-keys = "ubuntu:${file("~/.ssh/yandex_cloud.pub")}"
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-d"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "internal_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.nat_ip_address
}





