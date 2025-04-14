variable "key_file" {
  type      = string
  default   = "key.json"
  sensitive = true
}

variable "yc_zone" {
  type    = string
  default = "ru-central1-a"
}

variable "cloud_id" {
  type      = string
  sensitive = true
}

variable "folder_id" {
  sensitive = true
}

variable "vm_ram_gb" {
  type    = number
  default = 2
}

variable "vm_cpu_cores" {
  type    = number
  default = 2
}

variable "vm_username" {
  type      = string
  default   = "ubuntu"
  sensitive = true
}

variable "ssh_key_path" {
  type      = string
  default   = "/home/mikha/.ssh/id_ed25519.pub"
  sensitive = true
}

variable "vm_name" {
  type    = string
  default = "terraform1"
}