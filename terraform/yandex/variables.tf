variable "yc_token" {
  type    = string
  default = "t1.9euelZqelMyenc6emozJzp7Jl5yemu3rnpWampDOnMiTypDIkoyRkYmJlZPl8_dTDnBC-e8oNzk__N3z9xM9bUL57yg3OT_8zef1656VmonIionGx8-Py8mKjJiRm4zK7_zF656VmonIionGx8-Py8mKjJiRm4zK.1FgxC-xsjZBJgGQPnIPZnYH7byPQ3T1pRw-59CZeWO8T_k4D7kKcoi-wkYKQAZh3QQtTmM_GKmOVwySrDRvlDQ"
}

variable "folder_id" {
  type    = string
  default = "b1gc5ps7gbb88cdmp0u2"
}

variable "cloud_id" {
  type    = string
  default = "b1g719qcjt3un5vps33i"
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
  default = "fd80bm0rh4rkepi5ksdi"
}

variable "boot_size" {
  type    = number
  default = 20
}

variable "ssh_key" {
  type    = string
  default = "~/.ssh/id_ed25519.pub"
}