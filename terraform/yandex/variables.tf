variable "token" {
  type      = string
  sensitive = true
}

variable "cloud_id" {
  type      = string
  sensitive = true
}

variable "folder_id" {
  type      = string
  sensitive = true
}

variable "zone" {
  type      = string
  default   = "ru-central1-a"
  sensitive = true
}

variable "vm_name" {
  type    = string
  default = "devops_lab4_vm"
}

variable "disk_name" {
  type    = string
  default = "disk-ubuntu-24-04-lts_devops_lab4"
}

variable "disk_type" {
  type    = string
  default = "network-ssd"
}

variable "disk_size" {
  type    = number
  default = 20
}

variable "disk_image_id" {
  type    = string
  default = "fd85hkli5dp6as39ali4"
}

variable "vm_cores" {
  type    = number
  default = 2
}

variable "vm_memory" {
  type    = number
  default = 2
}

variable "vm_nat" {
  type    = bool
  default = true
}

variable "network_name" {
  type    = string
  default = "devops_lab4_net"
}

variable "subnet_name" {
  type    = string
  default = "devops_lab4_subnet"
}

variable "subnet_v4_cidr_blocks" {
  type    = list(string)
  default = ["192.168.10.0/24"]
}