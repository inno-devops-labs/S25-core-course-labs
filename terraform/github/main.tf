provider "github" {
  token = var.github_token
}

variable "github_token" {}

resource "github_repository" "core-course-labs" {
  name        = "DevOps-labs"
  description = "Terraform-managed repository"
  visibility  = "public"
  auto_init   = true
}
