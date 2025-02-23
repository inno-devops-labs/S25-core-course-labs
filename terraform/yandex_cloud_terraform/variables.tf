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

variable "image_id" {
  description = "ID image"
  type        = string
  default     = "fd8k2ed4jspu35gfde1u"
}

variable "vm_name" {
  description = "Name of the virtual machine"
  type        = string
  default     = "vm-1"
}

variable "platform_id" {
  description = "ID of the platform"
  type        = string
  default     = "standard-v2"
}

variable "hostname" {
  description = "Hostname of the virtual machine"
  type        = string
  default     = "vm-1"
}

variable "cores" {
  description = "Number of CPU cores"
  type        = number
  default     = 2
}

variable "core_fraction" {
  description = "CPU core fraction"
  type        = number
  default     = 20
}

variable "memory" {
  description = "Amount of memory in GB"
  type        = number
  default     = 2
}

variable "preemptible" {
  description = "Preemptible instance"
  type        = bool
  default     = true
}

variable "disk_name" {
  description = "Name of the disk"
  type        = string
  default     = "disk-1"
}

variable "disk_size" {
  description = "Size of the disk in GB"
  type        = number
  default     = 20
}

variable "disk_type" {
  description = "Type of the disk"
  type        = string
  default     = "network-hdd"
}

variable "network_name" {
  description = "Name of the network"
  type        = string
  default     = "network-1"
}

variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
  default     = "subnet-1"
}

variable "nat" {
  description = "Enable NAT"
  type        = bool
  default     = true
}

variable "vm_username" {
  description = "Username for SSH access"
  type        = string
  default     = "ubuntu"
  sensitive   = true
}

variable "ssh_pubkey_path" {
  description = "Path to the SSH public key"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
  sensitive   = true
}
