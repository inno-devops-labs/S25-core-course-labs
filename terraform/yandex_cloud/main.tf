locals {
  zone             = "ru-central1-a"
  username         = "g3nd4"
  ssh_key_path     = "C:/Users/Adel/Desktop/ssh/id_ed25519.pub"
  target_folder_id = "b1g4sbc0hc4kkm627mj5"
  registry_name    = "myregistry"
  sa_name          = "terraform_yandex_devops_lab_4"
  network     = "terraform_yandex_devops_lab_4_net"
  subnet      = "terraform_yandex_devops_lab_4_subnet"
  vm_name          = "terraform_yandex_devops_lab_4"
  image_id         = "fd8epq5qp2v73a23oir4"
  folder_id = "b1g4sbc0hc4kkm627mj5"
  cloud_id = "b1g5vfgv55ptonukr16k"
}

terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = local.zone
  cloud_id = local.cloud_id
  folder_id = local.folder_id
  service_account_key_file = "key.json"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = local.zone
  size     = "20"
  image_id = local.image_id
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
}

resource "yandex_vpc_network" "network-1" {
  name = local.network
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = local.subnet
  zone           = local.zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}
