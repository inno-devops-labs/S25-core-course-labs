variable "token" {
  description = "token"
  type        = string
  sensitive   = true
}

variable "zone" {
  type    = string
  default = "ru-central1-b"
}

variable "cloud_id" {
  description = "cloud id"
  type        = string
  sensitive   = true
}

variable "folder_id" {
  description = "folder id"
  type        = string
  sensitive   = true
}
