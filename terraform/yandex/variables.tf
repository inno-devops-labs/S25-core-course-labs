variable "yc_token" {
  type        = string
  description = "IAM token for Yandex Cloud authentication"
  sensitive   = true
}

variable "cloud_id" {
  type        = string
  description = "The Yandex Cloud ID"
  sensitive   = false
}

variable "folder_id" {
  type        = string
  description = "The Folder ID within Yandex Cloud"
  sensitive   = false
}

variable "zone" {
  type        = string
  description = "Yandex Cloud zone to deploy resources"
  default     = "ru-central1-a"
}

variable "vm_name" {
  type        = string
  description = "Name for the VM"
  default     = "my-terraform-vm"
}

variable "vm_core_count" {
  type        = number
  description = "Number of CPU cores"
  default     = 2
}

variable "vm_memory_size" {
  type        = number
  description = "Amount of RAM in GB"
  default     = 2
}

variable "vm_disk_size" {
  type        = number
  description = "Boot disk size in GB"
  default     = 10
}
