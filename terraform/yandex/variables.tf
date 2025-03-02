variable "sa_key_file" {
  type        = string
  description = "Path to the service account JSON key file"
  default     = "~/.yandex-cloud/key.json"
  sensitive   = true
}

variable "zone" {
  type    = string
  default = "ru-central1-b"
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
