variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "disk_image_id" {
  description = "Image id"
  default     = "fd8bpal18cm4kprpjc2m"
  type        = string
}

variable "network_name" {
  type    = string
  default = "network1"
}
