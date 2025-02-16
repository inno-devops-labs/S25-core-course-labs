terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"      
      version = "~> 0.90"
    }
  }
}

provider "yandex" {
  service_account_key_file = "key.json"
  cloud_id  = "b1g0cgibme1tkt1grrno"
  folder_id = "b1g4tcfpcoa8e7f4srd8"
  zone      = "ru-central1-a"
}

resource "yandex_compute_instance" "vm" {
  name = "terraform-vm"
  platform_id = "standard-v3"
  zone        = "ru-central1-d"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    initialize_params {
      image_id = "jg6vmfee6rfd862fimj1"
    }
  }
  network_interface {
    subnet_id = "ufo6e9boq1cg38dkvb39"
    nat       = true
  }
}