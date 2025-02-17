variable "iam_token" {
  type        = string
  description = "Specifies IAM token for auth in Yandex Cloud"
  sensitive   = true
}

variable "zone" {
  type    = string
  default = "ru-central1-d"
}

variable "cloud_id" {
  type        = string
  description = "Cloud ID"
  sensitive   = true
}

variable "folder_id" {
  type        = string
  description = "Folder ID within the cloud"
  sensitive   = true
}

variable "vm_image_id" {
  type        = string
  description = "Base image for virtual machines"
  default     = "fd83s8u085j3mq231ago" # ubuntu-22-04-lts-v20240129
}

variable "vm_name" {
  type    = string
  default = "terraform-vm"
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

variable "ssh_pubkey_path" {
  description = "Path to the SSH public key"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
  sensitive   = true
}
