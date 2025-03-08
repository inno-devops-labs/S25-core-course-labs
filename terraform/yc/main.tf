terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.76"
    }
  }
  required_version = ">= 1.0"
}

provider "yandex" {
  zone         = var.zone
  cloud_id     = var.cloud_id
  folder_id    = var.folder_id
  service_account_key_file = var.service_account_key_path
}

resource "yandex_vpc_network" "network" {
  name = "my-network"
}

resource "yandex_vpc_subnet" "subnet" {
  name           = "my-subnet"
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = var.zone
  network_id     = yandex_vpc_network.network.id
}

resource "yandex_compute_instance" "vm-1" {
  name        = "my-vm-1"
  platform_id = var.platform_id
  resources {
    cores  = var.cores
    memory = var.memory
  }
  boot_disk {
    initialize_params {
      image_id = var.image_id
      size     = var.disk_size
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
  metadata = {
    ssh-keys = "${var.vm_username}:${file(var.ssh_pubkey_path)}"
  }
}

resource "yandex_compute_instance" "vm-2" {
  name        = "my-vm-2"
  platform_id = var.platform_id
  resources {
    cores  = var.cores * 2
    memory = var.memory * 2
  }
  boot_disk {
    initialize_params {
      image_id = var.image_id
      size     = var.disk_size
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
  metadata = {
    ssh-keys = "${var.vm_username}:${file(var.ssh_pubkey_path)}"
  }
}