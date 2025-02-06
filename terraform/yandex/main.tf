terraform {
  required_providers {
      yandex = {
      source = "yandex-cloud/yandex"
      }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}


resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"
}