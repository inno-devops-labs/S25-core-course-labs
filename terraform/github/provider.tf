terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.0"
}

provider "github" {
  token        = var.github_token         
  owner        = var.MohamadSafi
}
