variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "disk_image_id" {
  type    = string
  default = "fd85u0rct32prepgjlv0"
}

variable "disk_size" {
  type    = string
  default = "20"
}

variable "vm_cores" {
  type    = number
  default = 2
}

variable "vm_memory" {
  type    = number
  default = 2
}
