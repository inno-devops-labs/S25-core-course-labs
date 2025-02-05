provider "yandex" {
  service_account_key_file = "key.json"
  cloud_id  = "b1gjsj40io2p61pl1jbh"
  folder_id = "b1gi2d48766ue3t7op4e"
  zone      = var.zone
}

data "yandex_vpc_network" "default" {
  name = "default"
}

data "yandex_vpc_subnet" "default" {
  name = "default-ru-central1-a"
}

resource "yandex_compute_instance" "app" {
  name        = "python-app"
  platform_id = "standard-v1"
  zone        = var.zone

  resources {
    cores         = var.vm_resources.cores
    memory        = var.vm_resources.memory
    core_fraction = var.vm_resources.core_fraction
  }

  boot_disk {
    initialize_params {
      image_id = var.image_id
      type     = "network-hdd"
    }
  }

  network_interface {
    subnet_id = data.yandex_vpc_subnet.default.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${var.ssh_key}"
    user-data = <<-EOF
      #!/bin/bash
      # Install Docker
      apt-get update
      apt-get install -y apt-transport-https ca-certificates curl software-properties-common
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get update
      apt-get install -y docker-ce
      systemctl start docker
      systemctl enable docker
      
      # Pull and run the Python app
      docker pull alexstrnik/python-app:latest
      docker run -d -p ${var.app_port}:${var.app_port} -e ENVIRONMENT=production --name python-app alexstrnik/python-app:latest
    EOF
  }
}
