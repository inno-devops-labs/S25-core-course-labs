variable "token" {
  type    = string
}

variable "cloud_id" {
  type = string
}

variable "folder_id" {
  type = string
}

variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "vm_name" {
  type    = string
  default = "terraform-vm"
}


variable "cores" {
  type    = number
  default = 2
}

variable "memory" {
  type    = number
  default = 2
}

variable "image_id" {
  type    = string
  default = "fd805qs1mn3n0casp7lt" 
}

variable "subnet_id" {
  type = string
}

variable "nat" {
  type    = bool
  default = true
}

variable "ssh_key_path" {
  type    = string
  default = "~/.ssh/id_rsa.pub"
}
