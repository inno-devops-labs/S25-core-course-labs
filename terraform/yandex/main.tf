resource "yandex_compute_instance" "vm" {
  name  = "terraform-vm"
  zone  = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd8t3vfi2ga6de7op8l2"  # This is a standard Linux image
    }
  }

  network_interface {
    subnet_id = var.subnet_id
    nat       = true
  }
}
