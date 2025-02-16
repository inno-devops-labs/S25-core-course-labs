locals {
  username         = "dew1769"
  ssh_key_path     = "C:/Users/User/.ssh/id_ed25519.pub"
  target_folder_id = "b1ggdftbcp0pgbf5cqiq"
  registry_name    = "python-application"
  sa_name          = "user"
  network_name     = "default"
  subnet_name      = "default-ru-central1-a"
  vm_name          = "vm-1"
  image_id         = "fd8aphn6s5hrmjaa3qas"
}

terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.47.0"
}

provider "yandex" {
  zone                     = var.zone
  service_account_key_file = "C:/Users/S25-core-course-labs/terraform/Yandex/key.json"
  cloud_id                 = "b1gbl7q6t66c0u3qahg0"
  folder_id                = "b1ggdftbcp0pgbf5cqiq"
}

resource "yandex_container_registry" "my-registry" {
  name      = local.registry_name
  folder_id = local.target_folder_id
}

resource "yandex_vpc_network" "docker-vm-network" {
  name = local.network_name
}

resource "yandex_vpc_subnet" "docker-vm-network-subnet-a" {
  name           = local.subnet_name
  zone           = var.zone
  v4_cidr_blocks = ["192.168.1.0/24"]
  network_id     = yandex_vpc_network.docker-vm-network.id
}

resource "yandex_compute_disk" "boot-disk" {
  name     = "bootvmdisk"
  type     = "network-hdd"
  zone     = var.zone
  size     = "10"
  image_id = local.image_id
}

resource "yandex_compute_instance" "docker-vm" {
  name               = local.vm_name
  platform_id        = "standard-v3"
  zone               = var.zone

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.docker-vm-network-subnet-a.id
    nat       = true
  }

  metadata = {
    user-data = "#cloud-config\nusers:\n  - name: ${local.username}\n    groups: sudo\n    shell: /bin/bash\n    sudo: 'ALL=(ALL) NOPASSWD:ALL'\n    ssh-authorized-keys:\n      - ${file("${local.ssh_key_path}")}"
  }
}


