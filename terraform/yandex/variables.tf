variable "token" {
  description = "Yandex Cloud API token"
  type        = string
  sensitive   = true
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
}

variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
}

variable "zone" {
  description = "Yandex Cloud Zone"
  type        = string
  default     = "ru-central1-b"
}

variable "image_id" {
  description = "Ubuntu 20.04 LTS image ID"
  type        = string
  default     = "fd805qs1mn3n0casp7lt"
}

variable "subnet_id" {
  description = "Subnet ID for the instance"
  type        = string
}

variable "public_key_path" {
  description = "Path to public SSH key"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
} 