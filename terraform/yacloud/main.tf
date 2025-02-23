terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.89"
    }
  }
}

provider "yandex" {
  service_account_key_file = "key.json"
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = "ru-central1-a"
}

resource "yandex_compute_instance" "vm" {
  name        = "my-yandex-vm"
  platform_id = "standard-v1"
  resources {
    cores  = 2
    memory = 2
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
  description = "Yandex Cloud API Token"
  type        = string
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
}

variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
}

variable "image_id" {
  description = "Yandex Cloud Image ID"
  type        = string
  default     = "fd80bm0rh4rkepi5ksdi" 
}

variable "subnet_id" {
  description = "Yandex Cloud Subnet ID"
  type        = string
}

output "vm_ip" {
  value = yandex_compute_instance.vm.network_interface[0].nat_ip_address
}
