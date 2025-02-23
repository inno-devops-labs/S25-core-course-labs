provider "yandex" {
  token     = var.yandex_token   # OAuth token from Yandex Cloud
  cloud_id  = var.yandex_cloud_id  # Yandex Cloud ID
  folder_id = var.yandex_folder_id # foler ID within Yandex Cloud
  zone      = var.yandex_zone      # zone ("ru-central1-a")
}

