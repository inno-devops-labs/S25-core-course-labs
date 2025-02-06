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
  cloud_id  = "b1gp380nnf41ranokstj"
  folder_id = "b1gfn5mtuidfco6jdpms"
  zone      = "ru-central1-a"
}

resource "yandex_compute_instance" "vm" {
  name = "terraform-vm"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    initialize_params {
      image_id = "fd842fimj1jg6vmfee6r"
    }
  }
  network_interface {
    subnet_id = "e9boq5eg33dkufo6vb39"
    nat       = true
  }
}
