variable "image_id" {
  description = "Image ID for the virtual machine"
  type        = string
  default     = "fd8k2ed4jspu35gfde1u"
}

variable "platform_id" {
  description = "Platform ID for the virtual machine"
  type        = string
  default     = "standard-v2"
}

variable "cores" {
  description = "Number of CPU cores for the VM"
  type        = number
  default     = 2
}

variable "memory" {
  description = "Memory allocation in GB for the VM"
  type        = number
  default     = 2
}

variable "disk_size" {
  description = "Size of the boot disk in GB"
  type        = number
  default     = 20
}

variable "service_account_key_path" {
  description = "Path to the JSON key file for the Yandex service account"
  type        = string
  sensitive   = true
}

variable "vm_username" {
  description = "Username for SSH access"
  type        = string
  default     = "ubuntu"
  sensitive   = true
}

variable "ssh_pubkey_path" {
  description = "Path to the SSH public key file"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
  sensitive   = true
}

variable "cloud_id" {
  description = "ID of the Yandex Cloud"
  type        = string
  sensitive   = true
}

variable "folder_id" {
  description = "ID of the folder in Yandex Cloud"
  type        = string
  sensitive   = true
}

variable "zone" {
  description = "Availability zone for resources"
  type        = string
  default     = "ru-central1-b"
}