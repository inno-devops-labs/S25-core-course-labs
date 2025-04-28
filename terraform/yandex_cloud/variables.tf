variable "zone" {
  description = "The availability zone for the virtual machine."
  type        = string
  default     = "ru-central1-a"
}

variable "disk_name" {
  description = "The name of the boot disk."
  type        = string
  default     = "devops-terraform-disk"
}

variable "disk_type" {
  description = "The type of the boot disk."
  type        = string
  default     = "network-hdd"
}

variable "disk_size" {
  description = "The size of the boot disk in gigabytes."
  type        = number
  default     = 10
}

variable "disk_image_id" {
  description = "The ID of the image to use for the boot disk."
  type        = string
  default     = "fd8308aanqma9v5n76aj" # ubuntu-22-04-lts-v20250127
}

variable "vm_name" {
  description = "The name of the virtual machine."
  type        = string
  default     = "devops-terraform-vm"
}

variable "vm_cores" {
  description = "The number of CPU cores for the virtual machine."
  type        = number
  default     = 2
}

variable "vm_memory" {
  description = "The amount of memory in gigabytes for the virtual machine."
  type        = number
  default     = 2
}

variable "vm_nat" {
  description = "Whether to enable NAT for the virtual machine."
  type        = bool
  default     = true
}

variable "network_name" {
  description = "The name of the network."
  type        = string
  default     = "devops-terraform-network"
}

variable "subnet_name" {
  description = "The name of the subnet."
  type        = string
  default     = "devops-terraform-subnet"
}

variable "subnet_v4_cidr_blocks" {
  description = "IPv4 CIDR blocks for the subnet."
  type        = list(string)
  default     = ["192.168.0.0/16"]
}
