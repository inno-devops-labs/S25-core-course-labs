variable "zone" {
  description = "Default zone"
  type        = string
  default     = "ru-central1-a"
}

variable "virtual_machine_name" {
  description = "Default virtual machine name"
  type        = string
  default     = "virtual-machine"
}

variable "memory" {
  description = "Number of memory in GB"
  type        = number
  default     = 2
}

variable "cores" {
  description = "Number of cores"
  type        = number
  default     = 2
}

variable "core_fraction" {
  type    = number
  default = 5
}

variable "nat" {
  type    = bool
  default = true
}

variable "ssh_path" {
  description = "Path to ssh public key"
  type        = string
  sensitive   = true
  default     = "~/.ssh/id_rsa.pub"
}

variable "image_id" {
  type        = string
  description = "Image for virtual machine"
  default     = "fd83s8u085j3mq231ago"
}

variable "iam_token" {
  description = "Token for auth"
  type        = string
  sensitive   = true
}

variable "cloud_id" {
  default   = "Cloud id where all the folders"
  type      = string
  sensitive = true
}

variable "folder_id" {
  description = "Folder id in cloud"
  type        = string
  sensitive   = true
}
