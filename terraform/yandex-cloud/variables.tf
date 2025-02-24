variable "ssh_key" {
  type      = string
  default   = "C:\\Users\\Artur\\.ssh\\id_ed25519"
  sensitive = true
}

variable "zone" {
  type    = string
  default = "ru-central1-b"
}

variable "disk_type" {
  type    = string
  default = "network-ssd"
}

variable "disk_image_id" {
  type    = string
  default = "fd8bpal18cm4kprpjc2m"
}

variable "disk_gb" {
  type    = number
  default = 10
}

variable "ram_gb" {
  type    = number
  default = 2
}

variable "preemptible" {
  type    = bool
  default = true
}

variable "cores" {
  type    = number
  default = 2
}

variable "core_fraction" {
  type    = number
  default = 20
}