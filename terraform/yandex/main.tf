terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

locals {
    folder_id = "b1gr8jhv3q33005l8fjd"
    cloud_id = "b1gv2sepcm2vkhrnoa94"
}

provider "yandex" {
  zone = "ru-central1-a"
  cloud_id = local.cloud_id
  folder_id = local.folder_id
  service_account_key_file = "./authorized_key.json"
  
  max_retries = 3
  endpoint = "api.cloud.yandex.net:443"
  timeouts {
    create = "10m"
    update = "10m"
    delete = "10m"
  }
}

# Network
resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

# Disk
resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = 15
  image_id = "fd8snjpoq85qqv0mk9gi"  # Ubuntu 20.04 LTS
}

# VM Instance
resource "yandex_compute_instance" "vm-1" {
  name        = "terraform1"
  zone        = "ru-central1-a"
  platform_id = "standard-v3"

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
    ssh-keys = "ubuntu:${file("~/.ssh/yandex-terraform.pub")}"  
  }
}

# Output the public IP
output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

