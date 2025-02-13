terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.87"
    }
  }
}
variable "yc_token" {
  description = "Yandex Cloud IAM Token"
  type        = string
  sensitive   = true
}

variable "cloud_id" {
  description = "Yandex Cloud Cloud ID"
  type        = string
}

variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
}
provider "yandex" {
  token     = var.yc_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

variable "instance_name" {
  description = "Имя виртуальной машины"
  type        = string
  default     = "yc-vm"
}

resource "yandex_compute_instance" "vm" {
  name = var.instance_name
  zone = "ru-central1-a"
  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd86jl8gechvgkabt374"
    }
  }

  network_interface {
    subnet_id = "e9bftvjtppp5p6pnu9oc"
    nat       = true
  }
}

output "instance_name" {
  value = yandex_compute_instance.vm.name
}

output "instance_ip" {
  value = yandex_compute_instance.vm.network_interface[0].nat_ip_address
}

