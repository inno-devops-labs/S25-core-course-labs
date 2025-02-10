variable "cores" {
  type    = number
  default = 2
}

variable "memory" {
  type    = number
  default = 2
}

variable "disk-size" {
  type    = number
  default = 20
}

variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "ssh_key" {
  type      = string
default   = "~/.ssh/id_ed25519.pub"
  sensitive = true
}