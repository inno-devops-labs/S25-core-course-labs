variable "availability-zone" {
  type    = string
  default = "ru-central1-a"
}

variable "subnet_masks" {
  type    = list(string)
  default = ["10.0.100.0/24"]
}

variable "image_id" {
  type    = string
  default = "fd82odtq5h79jo7ffss3"  # Ubuntu 24.04
}

variable "ssh_keys" {
  type    = string
  default = null
}
