terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

variable "github_token" {}

resource "github_repository" "S25-core-course-labs" {
  name        = "S25-core-course-labs"
  description = "Repository managed by Terraform"
  visibility  = "public"
}