terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}


provider "github" {
  owner = var.github_organization
  token = file("${path.root}/token")
}
