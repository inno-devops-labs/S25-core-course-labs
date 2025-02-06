terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.89"
    }
  }
}

provider "yandex" {
  token     = var.yc_token  
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = "ru-central1-a"
}

resource "yandex_compute_instance" "vm_instance" {
  name        = "terraform-vm"
  platform_id = "standard-v1"

  resources {
    cores         = 2
    memory        = 2
    core_fraction = 20
  }
  
  boot_disk {
    initialize_params {
      image_id = var.image_id 
    }
  }

  network_interface {
    subnet_id = var.subnet_id
    nat       = true
  }
}

variable "yc_token" {
  description = "API Token for Yandex Cloud"
  type        = string
}

variable "cloud_id" {
  description = "ID of the Yandex Cloud"
  type        = string
}

variable "folder_id" {
  description = "ID of the Folder in Yandex Cloud"
  type        = string
}

variable "image_id" {
  description = "ID of the Yandex Cloud Image"
  type        = string
  default     = "fd80bm0rh4rkepi5ksdi" 
}

variable "subnet_id" {
  description = "Subnet ID for Yandex Cloud"
  type        = string
}

output "vm_public_ip" {
  description = "Public IP of the created virtual machine"
  value       = yandex_compute_instance.vm_instance.network_interface[0].nat_ip_address
}
