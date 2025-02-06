terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "~> 0.9" # or your chosen version
    }
  }
  required_version = ">= 1.0"
}

provider "yandex" {
  # Option A: Provide token/IDs via environment variables
  #    export YC_TOKEN="<your token>"
  #    export YC_CLOUD_ID="<your cloud id>"
  #    export YC_FOLDER_ID="<your folder id>"
  # or Option B: Provide them as variables in variables.tf.

  token     = var.yc_token      # from variables.tf
  cloud_id  = var.cloud_id      # from variables.tf
  folder_id = var.folder_id     # from variables.tf

  zone = var.zone
}
