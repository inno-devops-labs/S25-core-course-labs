variable "ssh_key" {
  type      = string
  default   = "~/.ssh/id_rsa.pub"
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
  default     = "fd859s00ru90mn31cjf4"
}

variable "disk_gb" {
  type    = number
  default = 20
}

variable "ram_gb" {
  type    = number
  default = 2
}

variable "preemptible" {
  type    = bool
  default = true
}

variable "cores" {
  type    = number
  default = 2
}

variable "core_fraction" {
  type    = number
  default = 20
}

variable "service_account_key_file" {
  type        = string
  description = "Path to Yandex Cloud service account key file"
  default     = "service-account-key.json"
}
