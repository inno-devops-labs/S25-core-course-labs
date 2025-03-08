# Configure Terraform to work with Yandex Cloud
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

# Configure the Yandex Cloud provider
provider "yandex" {}

# Start with a simple network configuration
resource "yandex_vpc_network" "network" {
  name = "network-1"
}

# Add a subnet
resource "yandex_vpc_subnet" "subnet" {
  name           = "subnet-1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}