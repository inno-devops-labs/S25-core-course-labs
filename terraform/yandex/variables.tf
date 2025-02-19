variable "token" {
  type      = string
  default   = "t1.9euelZrIx5OUyZOLnMaUlZyOjJyRm-3rnpWay5mbzM7HnImMkcmMicqTzozl8_c3cm5C-e8UUTgk_d3z93cgbEL57xRROCT9zef1656VmpiTjY6WjpWYkcabncvIzpyU7_zF656VmpiTjY6WjpWYkcabncvIzpyU.b7mP0v3G9XEvZVjgHaCvP3J3v8-kFwDKdSiiSDXF1WLh8wk6Ff_W0ClS2QK0eEBekieh0u7BfEiROxY93EMXDw"
}

variable "zone" {
  type    = string
  default = "ru-central1-b"
}

variable "cloud_id" {
  type      = string
  default   = "b1gnu9vfradetrgfse66"
  sensitive = true
}

variable "folder_id" {
  default = "b1gvo4he6qfdthdc6fm3"
  sensitive = true
}

variable "image_id" {
  default = "fd869umlvb3mfbj2lrks"
  sensitive = true
}

