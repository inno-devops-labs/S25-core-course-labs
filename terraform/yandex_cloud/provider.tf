terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = var.zone
  token = file("${path.root}/iam_token")
  folder_id = file("${path.root}/folder_id")
  cloud_id = file("${path.root}/cloud_id")
}