terraform {
  required_providers {
    github = {
      source = "hashicorp/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = "Kazan-Strelnikova"
}
