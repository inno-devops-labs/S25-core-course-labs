# Description: Variables for Yandex Cloud resources

# Zone variable

variable "zone" {
  description = "The availability zone for the Yandex Cloud resources."
  type        = string
  default     = "ru-central1-a"
}

# Boot disk variables

variable "boot_disk_name" {
  description = "The name of the boot disk for the virtual machine."
  type        = string
  default     = "s25-devops-terraform-boot-disk"
}

variable "boot_disk_type" {
  description = "The type of the boot disk (e.g., network-hdd, network-ssd)."
  type        = string
  default     = "network-hdd"
}

variable "boot_disk_size" {
  description = "The size of the boot disk in gigabytes."
  type        = number
  default     = 20
}

variable "boot_disk_image_id" {
  description = "The ID of the image used for the boot disk (Ubuntu 22.04 LTS)."
  type        = string
  default     = "fd8308aanqma9v5n76aj" # ubuntu-22-04-lts-v20250127
}

# Virtual machine variables

variable "vm_name" {
  description = "The name of the virtual machine instance."
  type        = string
  default     = "s25-devops-terraform-vm"
}

variable "vm_cores" {
  description = "The number of CPU cores for the virtual machine."
  type        = number
  default     = 2
}

variable "vm_memory" {
  description = "The amount of RAM in gigabytes for the virtual machine."
  type        = number
  default     = 2
}

variable "vm_nat" {
  description = "Defines whether the virtual machine should have NAT enabled for internet access."
  type        = bool
  default     = true
}

# Network and subnet variables

variable "network_name" {
  description = "The name of the network to be created for the virtual machine."
  type        = string
  default     = "s25-devops-terraform-network"
}

variable "subnet_name" {
  description = "The name of the subnet within the network."
  type        = string
  default     = "s25-devops-terraform-subnet"
}

variable "subnet_v4_cidr_blocks" {
  description = "The list of IPv4 CIDR blocks for the subnet."
  type        = list(string)
  default     = ["192.168.0.0/16"]
}
