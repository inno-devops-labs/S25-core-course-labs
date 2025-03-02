# Create a VPC Network
resource "yandex_vpc_network" "default" {
  name = "${var.vm_name}-network"
}

# Create a Subnet inside that network
resource "yandex_vpc_subnet" "default" {
  name           = "${var.vm_name}-subnet"
  zone           = var.zone
  network_id     = yandex_vpc_network.default.id
  v4_cidr_blocks = ["10.128.0.0/24"]
}

# Create a VM
resource "yandex_compute_instance" "vm" {
  name        = var.vm_name
  zone        = var.zone
  folder_id   = var.folder_id
  platform_id = "standard-v3"  

  resources {
    cores  = var.vm_core_count
    memory = var.vm_memory_size
  }

  boot_disk {
    initialize_params {
      image_id = "b1g5alo1m2okd6nrap65"
      size      = var.vm_disk_size
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = true  # so you can SSH or connect publicly
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}" 
  }
}
