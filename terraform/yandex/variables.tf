variable "yc_token" {
  type        = string
  default     = "Print your token here"
}

variable "folder_id" {
  type        = string
  default     = "b1g5rr7vs8qnd5ikd5ee"
}

variable "cloud_id" {
  type        = string           
  default     = "b1gblh32diardc9mii5u"
}
 
variable "zone" {
  type        = string
  default     = "ru-central1-b"
}

variable "cores" {
  type        = number
  default     = 2
}

variable "memory" {
  type        = number
  default     = 2
}

variable "image_id" {
  type        = string
  default     = "fd800c7s2p483i648ifv"
}

variable "boot_size" {
  type        = number
  default     = 20
}

variable "ssh_key" {
  type        = string
  default     = "~/.ssh/id_ed25519.pub"
}


