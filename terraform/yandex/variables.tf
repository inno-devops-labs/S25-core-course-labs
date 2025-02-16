variable "disk_image_id" {
  type    = string
  default = "fv4t9iv97540b03belgi"
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

variable "net_name" {
  type    = string
  default = "network1"
}

variable "subnet_name" {
  type    = string
  default = "subnet1"
}

variable "subnet_cidr_blocks" {
  type    = list(string)
  default = ["10.130.0.0/24"]
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

variable "zone" {
  type    = string
  default = "ru-central1-d"
}