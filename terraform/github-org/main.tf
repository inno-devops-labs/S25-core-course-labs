terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = var.github_org
}


resource "github_team" "developers" {
  name        = "Developers"
  description = "Team for developers (users)"
  privacy     = "closed"
}

resource "github_team" "admins" {
  name        = "Admins"
  description = "Administrators with full access"
  privacy     = "closed"
}


resource "github_team_repository" "dev_team_access" {
  team_id    = github_team.developers.id
  repository = var.repo_name
  permission = "push"
}

resource "github_team_repository" "admin_team_access" {
  team_id    = github_team.admins.id
  repository = var.repo_name
  permission = "admin"
}
