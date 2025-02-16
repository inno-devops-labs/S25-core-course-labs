variable "yc_token" {
  type    = string
  default = ""
}

variable "folder_id" {
  type    = string
  default = "b1gil461o5s88c4kdutr"
}

variable "cloud_id" {
  type    = string
  default = "b1gq935p4d4ee3ebk2uq"
}

variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "cores" {
  type    = number
  default = 2
}

variable "memory" {
  type    = number
  default = 2
}

variable "image_id" {
  type    = string
  default = "fd800c7s2p483i648ifv"
}

variable "boot_size" {
  type    = number
  default = 20
}

variable "ssh_key" {
  type    = string
  default = "~/.ssh/id_ed25519.pub"
}
