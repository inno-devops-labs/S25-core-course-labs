variable "token" {
  description = "Yandex Cloud authorization token"
  type = string
  sensetive = true
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type = string
}

variable "folder_id" {
  description = "Yandex Folder ID"
  type = string
}

variable "vm_name" {
  description = "VM's name"
  type = string
  default = "voronm"
}

variable "zone" {
    description = "Availability zone"
    type = string
    defailt = "ru-central1-b"
}
