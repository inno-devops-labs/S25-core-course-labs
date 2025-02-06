terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.84"
    }
  }
}

provider "yandex" {
  token     = "t1.9euelZrLjJaKms2cmM7NxpKVk5mOzu3rnpWakJ7Lx5XGy87KjZqKlM7GnJ7l8_daRmxC-e9BYV0W_t3z9xp1aUL570FhXRb-zef1656VmpOamZCXi5eLkZiNi5eNksqd7_zF656VmpOamZCXi5eLkZiNi5eNksqd.vupmIgNkmfKIDIDHHNTLqyouzfg_jQLSLq2YMDBasq3V55c8mh7pNJQMLzmAvTtic68E_Fm3uFBzZk5uTkQLAA"
  cloud_id  = "b1g6juhil8j8o6m19tj3"
  folder_id = "b1g0u5p8fg45gkiq8600"
  zone      = "ru-central1-a"
}

resource "yandex_compute_instance" "vm-1" {
  name        = "my-vm"
  platform_id = "standard-v1"
  resources {
    cores         = 2
    memory        = 2
    core_fraction = 20
  }
  
  boot_disk {
    initialize_params {
      image_id = "fd80bca9kcrb3ubq7eaf"
    }
  }
  
  network_interface {
    subnet_id = "e2lt5i47a9sld9hoprnf"
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/ssh_keys.pub")}"
  }
}
