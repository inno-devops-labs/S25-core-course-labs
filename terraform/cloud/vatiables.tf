variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "token" {
  type = string
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
  type    = string
  default = "20"
}

variable "image_id" {
  type    = string
  default = "fd87ap2ld09bjiotu5v0"
}

variable "disk_folder_id" {
  type = string
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

variable "subnet_name" {
  type    = string
  default = "subnet1"
}

variable "subnet_zone" {
  type    = string
  default = "ru-central1-a"
}

variable "subnet_cidr" {
  type    = string
  default = "192.168.10.0/24"
}

variable "network_name" {
  type    = string
  default = "network1"
}

variable "network_folder_id" {
  type = string
}

variable "metadata_ssh_keys_path" {
  type    = string
  default = "~/.ssh/id_ed25519.pub"
}

variable "vm_folder_id" {
  type = string
}