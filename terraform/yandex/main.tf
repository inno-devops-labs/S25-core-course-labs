# Configure the Yandex Cloud provider
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

# Provider configuration
provider "yandex" {
  token     = var.yc_token
  cloud_id  = var.yc_cloud_id
  folder_id = var.yc_folder_id
  zone      = var.yc_zone
}

# Network Configuration
resource "yandex_vpc_network" "network" {
  name = "terraform-network"
}

resource "yandex_vpc_subnet" "subnet" {
  name           = "terraform-subnet"
  zone           = var.yc_zone
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = ["10.2.0.0/16"]
}

# Compute Instance
resource "yandex_compute_instance" "vm" {
  name = "compute-vm-2-2-20-ssd-1738835807410"
  zone = var.yc_zone

  resources {
    cores  = 2
    memory = 2 # GB
  }

  boot_disk {
    initialize_params {
      image_id = "fd8s5j70eqong91qn54k" # Ubuntu 24.04 LTS
      size     = 20 # GB
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

# Outputs
output "external_ip_address" {
  value = yandex_compute_instance.vm.network_interface.0.nat_ip_address
}

output "internal_ip_address" {
  value = yandex_compute_instance.vm.network_interface.0.ip_address
}