terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.GITHUB_TOKEN
}

resource "github_repository" "my-repo" {
  name        = "my-repo"
  description = "This is my imported GitHub repository"
  visibility  = "public" # или "private"
}
