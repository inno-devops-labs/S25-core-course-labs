variable "token" {
  description = "IAM-token"
  type        = string
  sensitive   = true
}

variable "cloud_id" {
  description = "Cloud ID"
  type        = string
  sensitive   = true
}

variable "folder_id" {
  description = "Folder ID"
  type        = string
  sensitive   = true
}

variable "image_id" {
  description = "Image id"
  default     = "fd89ls0nj4oqmlhhi568"
  type        = string
}