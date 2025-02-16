terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = ">= 0.85.0"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = var.yandex_token
  cloud_id  = var.yandex_cloud_id
  folder_id = var.yandex_folder_id
  zone      = "ru-central1-a"
}

# Define variables
variable "yandex_token" {}
variable "yandex_cloud_id" {}
variable "yandex_folder_id" {}

# Network and Subnet
resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet-1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

# VM Instances
resource "yandex_compute_instance" "vm-1" {
  name        = "terraform1"
  platform_id = "standard-v1"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    initialize_params {
      image_id = "fd805qs1mn3n0casp7lt"
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
  metadata = {
    user-data = "${file("/Users/netpo4ki/PycharmProjects/S25-core-course-labs/terraform/yandex_cloud_tf/meta.txt")}"
  }
}

resource "yandex_compute_instance" "vm-2" {
  name        = "terraform2"
  platform_id = "standard-v1"
  resources {
    cores  = 4
    memory = 4
  }
  boot_disk {
    initialize_params {
      image_id = "fd805qs1mn3n0casp7lt"
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
  metadata = {
    user-data = "${file("/Users/netpo4ki/PycharmProjects/S25-core-course-labs/terraform/yandex_cloud_tf/meta.txt")}"
  }
}