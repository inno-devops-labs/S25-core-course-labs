variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
  default     = "b1gi2d48766ue3t7op4e"
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
  default     = "b1gjsj40io2p61pl1jbh"
}

variable "zone" {
  description = "Yandex Cloud Zone"
  type        = string
  default     = "ru-central1-a"
}

variable "image_id" {
  description = "Ubuntu image ID"
  type        = string
  default     = "fd8308aanqma9v5n76aj"
}

variable "vm_resources" {
  description = "VM resources configuration"
  type = object({
    cores         = number
    memory        = number
    core_fraction = number
  })
  default = {
    cores         = 2
    memory        = 2
    core_fraction = 100
  }
}

variable "ssh_key" {
  description = "SSH public key for instance access"
  type        = string
  default     = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC+ybSn8gUISwZMz4NAEn5Qbjd6lkwSF7O7ppy05c3WqNAYisuw21JNBE71t4HRASHKT2uUkQ/EuTkrov/2WQwyk3QgxS+2lr6o2jlpBQUAikKk0y+X7ZoWYGNyDEtgHfbhtLp2vg4EquD/Z1+Q4VqTb2ELz2IyamismYc75+44rVKXX7luDyQ/GnVU4OWS3xO3diZi8h6KSmly1oxibAO8YU/FwIG63wvZafRIZIWBJFamhZtG5d4vbI29qrObdmVGza1JuffTbJMG2FsTE67lTktfRmu/XFh3N4hN4xmtEas1rM+Wju9PnYFS67GR707Ur4K/5lJZkcVgt/J/3d0JTmvZ7Wf+0BY24JnJrBYckQL7sQFNfNW89nyJjbQQd2mTYVGOYb5rHrpdcqMlTrPc2zwYwj9unNo/lbkad2fUXMHap6m2hYHAYbXa3ehVlmbODemm0gG41uh1aiqq12XVD2s+ZB59DdsihPCZ8SQTKO24Lui3P+/IaNeOxMZPplU= alexstrnik@mac-alex.local"
}

variable "app_port" {
  description = "Application port to expose"
  type        = number
  default     = 5000
}
