resource "yandex_compute_instance" "vm-1" {
  name = var.name

  resources {
    memory = var.memory
    cores  = var.cores
  }

  boot_disk {
    initialize_params {
      image_id = "fd83s8u085j3mq231ago"
      size = var.disk_size
      type = var.disk_type
    }
  }

  metadata = {
    ssh-keys = format("%s:%s", var.name, file("C:/Users/PC/.ssh/id_rsa"))
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.my-vm-subnet.id
    nat       = var.nat
  }
}

resource "yandex_vpc_network" "my-vm-network" {
  name = "Network"
}

resource "yandex_vpc_subnet" "my-vm-subnet" {
  name           = "Subnet"
  zone           = var.zone
  network_id     = yandex_vpc_network.my-vm-network.id
  v4_cidr_blocks = var.subnet_v4_cidr_blocks
}

