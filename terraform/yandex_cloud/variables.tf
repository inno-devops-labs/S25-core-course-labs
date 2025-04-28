variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "network" {
  type    = string
  default = "ya-network"
}

variable "subnet" {
  type    = string
  default = "ya-network"
}

variable "subnet_v4_cidr_blocks" {
  type    = list(string)
  default = ["192.168.0.0/16"]
}

variable "nat" {
  type    = bool
  default = true
}

variable "image_id" {
    type = string
    default = "fd800c7s2p483i648ifv"
}

variable "name" {
  type = string
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


variable "timeout_create" {
  default = "10m"
}

variable "timeout_delete" {
  default = "10m"
}
