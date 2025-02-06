variable "yandex_zone" {
  type    = string
  default = "ru-central1-a"
}

variable "vm_cores" {
  type    = number
  default = 2
}

variable "vm_memory" {
  type    = number
  default = 2
}

variable "vm_image_id" {
  type    = string
  default = "fd800c7s2p483i648ifv"
}

variable "vm_boot_size" {
  type    = number
  default = 20
}

variable "ssh_pub_key_path" {
  type    = string
  default = "~/.ssh/id_ed25519.pub"
}
