terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.87"
    }
  }
}

provider "yandex" {
  token = "y0__xC6s-3PBBjB3RMghcHQlxLmGLprAkyFoA68OFblvfKh4fG5iQ"
  cloud_id  = "b1ghbtq5gj9uf3o742m3"
  folder_id = "b1guu2aobu6m1g2af9ou"
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

