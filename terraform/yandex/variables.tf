variable "iam_token" {
  description = "IAM token in Yandex Cloud"
  type        = string
  sensitive   = true
}

variable "zone" {
  type    = string
  default = "ru-central1-b"
}

variable "cloud_id" {
  description = "Cloud ID in Yandex.Cloud"
  type        = string
  sensitive   = true
}

variable "folder_id" {
  description = "Foder ID in Yandex.Cloud"
  type        = string
  sensitive   = true
}

variable "vm_name" {
  description = "Virtual Machine Name"
  type        = string
  default     = "terraform-1"
}

variable "vm_memory" {
  description = "Virtual Machine RAM in GB"
  type        = number
  default     = 2
}

variable "vm_cores" {
  description = "Virtual Machine CPU cores"
  type        = number
  default     = 2
}

variable "vm_core_fraction" {
  description = "Virtual Machine Core Fraction (20/50/100)"
  type        = number
  default     = 20
}

variable "vm_image" {
  description = "Virtual Machine Image (default is Ubuntu 24.04 LTS)"
  type        = string
  default     = "fd8bpal18cm4kprpjc2m"
}

variable "ssh_username" {
  description = "SSH username"
  type        = string
  default     = "root"
  sensitive   = true
}

variable "ssh_key_pub_path" {
  description = "Path to the SSH public key"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
  sensitive   = true
}
