variable "ssh_key" {
  type      = string
  default   = "your ssh key"
  sensitive = true
}

variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "disk_type" {
  type    = string
  default = "network-hdd"
}

variable "disk_image_id" {
  type        = string
  description = "Ubuntu image"
  default     = "fd82193uebe069absqfq"
}

variable "disk_gb" {
  type    = number
  default = 20
}

variable "ram_gb" {
  type    = number
  default = 2
}

variable "cores" {
  type    = number
  default = 2
}

variable "token" {
  type = string
  default = "key.json"
}