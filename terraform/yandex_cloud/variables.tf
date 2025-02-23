variable "zone" {
  type    = string
  default = "ru-central1-d"
}

variable "disk_image_id" {
  type    = string
  default = "fd86juob74b0a8ev1muk" # fedora 38
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

variable "fid" {
  type    = string
  default = "b1g9ua85karf2rfp4623"
}
