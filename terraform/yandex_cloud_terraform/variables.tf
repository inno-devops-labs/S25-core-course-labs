variable "zone" {
  description = "Cloud zone"
  type        = string
  default     = "ru-central1-a"
}

variable "iam_token" {
  description = "IAM token"
  type        = string
  sensitive   = true
}

variable "cloud_id" {
  description = "Cloud id"
  type        = string
  sensitive   = true
}

variable "folder_id" {
  description = "Folder id"
  type        = string
  sensitive   = true
}
