variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "disk_config" {
  type = object({
    name     = string
    type     = string
    size     = number
    image_id = string
  })
  default = {
    name     = "boot-disk-1"
    type     = "network-hdd"
    size     = 20
    image_id = "fd86idv7gmqapoeiq5ld"
  }
}

variable "vm_config" {
  type = object({
    name   = string
    cores  = number
    memory = number
    nat    = bool
  })
  default = {
    name   = "terraform1"
    cores  = 2
    memory = 2
    nat    = true
  }
}

variable "network_name" {
  type    = string
  default = "network1"
}

variable "subnet_config" {
  type = object({
    name           = string
    v4_cidr_blocks = list(string)
  })
  default = {
    name           = "subnet1"
    v4_cidr_blocks = ["192.168.0.0/24"]
  }
}
