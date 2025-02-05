variable "yc_token" {
  description = "OAuth token for Yandex Cloud authentication"
  type        = string
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
}

variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
}

variable "zone" {
  description = "Yandex Cloud availability zone"
  type        = string
  default     = "ru-central1-b"
}

variable "vm_name" {
  description = "Name of the virtual machine"
  type        = string
  default     = "terraform-instance"
}

variable "vm_cores" {
  description = "Number of CPU cores for the VM"
  type        = number
  default     = 2
}

variable "vm_memory" {
  description = "Amount of RAM in GB"
  type        = number
  default     = 2
}

variable "vm_image_id" {
  description = "Image ID for the VM (Ubuntu free-tier)"
  type        = string
  default     = "fd86idv7gmqapoeiq5ld"
}

variable "subnet_id" {
  description = "Subnet ID for the VM"
  type        = string
}
