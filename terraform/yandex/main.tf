provider "yandex" {
  token     = var.yandex_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

resource "yandex_compute_instance" "vm" {
  name = "my-yandex-vm"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd8mcobggdsq5lllt0l5"
    }
  }

  network_interface {
    subnet_id = var.subnet_id
    nat       = true
  }
}
