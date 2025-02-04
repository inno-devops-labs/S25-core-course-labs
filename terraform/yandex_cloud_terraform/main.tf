terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
      version = "0.136.0"
    }
  }
}

locals {
  folder_id = b1g1p4pm73gn0m0dj1s3
  cloud_id = b1gejb877g675jgaqrt1
}


provider "yandex" {
  token                    = "auth_token_here"
  cloud_id                 = "cloud_id_here"
  folder_id                = "folder_id_here"
  zone                     = "ru-central1-d"
}