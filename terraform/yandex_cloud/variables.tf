variable "zone" {
  type    = string
  default = "ru-central1-b"
}

variable "subnet_v4_cidr_blocks" {
  type    = list(string)
  default = ["192.168.10.0/24"]
}

variable "nat" {
  type    = bool
  default = true
}

variable "name" {
  type    = string
  default = "ubuntu"
}

variable "cores" {
  type    = number
  default = 2
}

variable "memory" {
  type    = number
  default = 4
}

variable "disk_size" {
  type    = number
  default = 50
}

variable "disk_type" {
  type    = string
  default = "network-nvme"
}
