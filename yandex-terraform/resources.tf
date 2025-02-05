resource "yandex_vpc_network" "my_network" {
  name = "my_network"
  folder_id = var.folder_id
}

resource "yandex_vpc_subnet" "public_subnet" {
  name           = "public"
  network_id     = yandex_vpc_network.my_network.id
  v4_cidr_blocks = ["10.0.1.0/24"]
  zone = "ru-central1-a"
}

resource "yandex_compute_instance" "vm" {
  name = "my-vm"
  zone = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = var.image_id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.public_subnet.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}