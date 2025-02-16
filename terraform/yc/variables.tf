variable "image_id" {
  description = "Image ID"
  type        = string
}

variable "zone" {
  description = "Availability zone"
  type        = string
}

variable "size" {
  description = "Size of Disk"
  type        = string
}

variable "ssh_path" {
  description = "Path to the SSH keys"
  type        = string
}
