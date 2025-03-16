terraform {
  required_version = "~> 1.2"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = file("${path.root}/token")
}