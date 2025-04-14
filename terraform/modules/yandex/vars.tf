variable "availability-zone" {
  type    = string
  default = "ru-central1-a"
}

variable "subnet_masks" {
  type    = list(string)
  default = ["10.0.100.0/24"]
}

variable "image_id" {
  type    = string
  default = "fd801rku4j14mv7fs703" # Debian 12
}

variable "ssh_key_file" {
  description = "Path to the SSH key file"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
  sensitive = true
}

variable "ssh_key_content" {
  description = "Content of the SSH key"
  type        = string
  default     = ""
  sensitive = true
}
