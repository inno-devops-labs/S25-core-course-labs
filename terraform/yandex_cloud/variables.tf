// account

variable "iam_token" {
  type      = string
  sensitive = true
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
  sensitive   = true
}

variable "folder_id" {
  description = "Yandex Folder ID"
  type        = string
  sensitive   = true
}

variable "zone" {
  description = "Yandex Cloud availability zone"
  type        = string
  default     = "ru-central1-b"
}

variable "ssh_key_path" {
  description = "SSH key path"
  type        = string
  sensitive   = true
}

// disk

variable "disk_name" {
  description = "Disk name"
  type        = string
  default     = "disk-1"
}

variable "disk_size" {
  description = "Disk size in GB"
  type        = number
  default     = 10
}

variable "disk_type" {
  description = "Disk type (ssd or hdd)"
  type        = string
  default     = "network-hdd"
}

variable "image_id" {
  description = "Image ID"
  type        = string
  default     = "fd85u0rct32prepgjlv0"
}

// vm

variable "vm_username" {
  description = "Username"
  type        = string
  default     = "ubuntu"
  sensitive   = true
}

variable "vm_name" {
  description = "VM name"
  type        = string
  default     = "vm-1"
}


variable "cores" {
  description = "CPU cores amount"
  type        = number
  default     = 2
}


variable "memory" {
  description = "Memory amount in GB"
  type        = number
  default     = 2
}

// network

variable "network_name" {
  description = "Network name"
  type        = string
  default     = "network-1"
}

variable "subnet_name" {
  description = "Subnet name"
  type        = string
  default     = "subnet-1"
}

variable "nat" {
  description = "Nat status (on or off)"
  type        = bool
  default     = true
}