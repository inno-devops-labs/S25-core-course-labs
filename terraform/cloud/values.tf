variable "yandex_token" {
  description = "Yandex Cloud API token"
  type        = string
  sensitive   = true
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
}

variable "folder_id" {
  description = "Yandex Folder ID"
  type        = string
}

variable "zone" {
  description = "Default availability zone"
  type        = string
  default     = "ru-central1-a"
}

variable "image_id" {
  description = "Image ID for the VM disk"
  type        = string
  default     = "fv4f6b8sd2mhqm4m2438"
}

variable "disk_size" {
  description = "Size of the VM disk in GB"
  type        = number
  default     = 10
}

variable "vm_memory" {
  description = "Memory for the VM in GB"
  type        = number
  default     = 4
}

variable "vm_cores" {
  description = "Number of CPU cores for the VM"
  type        = number
  default     = 2
}

variable "ssh_key" {
  description = "SSH key for accessing the VM"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}
