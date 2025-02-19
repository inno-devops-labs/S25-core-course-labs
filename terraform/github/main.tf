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

resource "github_repository" "my_repo" {
  name        = "S25-core-course-labs"
  description = "Terraform-managed repository"
  visibility  = "public"
  auto_init   = true
  default_branch = "main"
}

