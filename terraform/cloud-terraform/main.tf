terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
    token = "t1.9euelZqMlYyOj57ImIrGzpHMzZXLie3rnpWalI7Gl8ybncrPipGSysielYzl8_dJR2tC-e8HHDUw_t3z9wl2aEL57wccNTD-zef1656VmprHmZvOks-MzY3OyouJjM2M7_zN5_XrnpWalcaTipidnZOLj5SbzZLHzc_v_cXrnpWamseZm86Sz4zNjc7Ki4mMzYw.XCDYW_c3eVfjVDRZcQUWHRowqrlctm4U2P0vp_a4CpVJ3grS7VSEk5Y-mmq1CX6NJUN9B7G-lkZcO41JX3YECA"
    cloud_id = "b1g6juhil8j8o6m19tj3"
    folder_id = "b1g0u5p8fg45gkiq8600"
    zone = "ru-central1-a"
}

# Create a VPC Network
resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

# Create a Subnet
resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-d"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

# Create Boot Disks
resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-d"
  size     = "20"
  image_id = "fd86p66mh3vpkbjsl7qp"
}

resource "yandex_compute_disk" "boot-disk-2" {
  name     = "boot-disk-2"
  type     = "network-hdd"
  zone     = "ru-central1-d"
  size     = "20"
  image_id = "fd86p66mh3vpkbjsl7qp"
}

# Create VM 1
resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = file("/home/sg/DevOps/S25-core-course-labs/terraform/cloud-terraform/meta.txt")
  }
}

# Create VM 2
resource "yandex_compute_instance" "vm-2" {
  name = "terraform2"

  resources {
    cores  = 4
    memory = 4
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-2.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = file("/home/sg/DevOps/S25-core-course-labs/terraform/cloud-terraform/meta.txt")
  }
}

# Output Public and Internal IPs
output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "internal_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.nat_ip_address
}
