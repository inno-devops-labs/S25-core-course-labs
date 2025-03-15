variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "disk_name" {
  type    = string
  default = "boot-disk-1"
}

variable "disk_type" {
  type    = string
  default = "network-hdd"
}

variable "disk_size" {
  type    = number
  default = 20
}

variable "disk_image_id" {
  type    = string
  default = "fd8bpal18cm4kprpjc2m"
}

variable "vm_name" {
  type    = string
  default = "terraform1"
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
  default = "network1"
}

variable "subnet_name" {
  type    = string
  default = "subnet1"
}

variable "subnet_v4_cidr_blocks" {
  type    = list(string)
  default = ["192.168.0.0/16"]
}
