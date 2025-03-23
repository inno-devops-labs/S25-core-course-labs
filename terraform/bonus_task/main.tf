terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_token 
  owner = var.org_name     
}

# Create teams with different access levels
resource "github_team" "admins" {
  name        = "administrators-${var.org_name}"
  description = "Team with admin access"
  privacy     = "closed"
}

resource "github_team" "developers" {
  name        = "developers-${var.org_name}"
  description = "Team with write access"
  privacy     = "closed"
}

resource "github_team" "viewers" {
  name        = "viewers-${var.org_name}"
  description = "Team with read access"
  privacy     = "closed"
}

# Assign repository permissions to teams
resource "github_team_repository" "admin_repo" {
  team_id    = github_team.admins.id
  repository = var.repository_name
  permission = "admin"
}

resource "github_team_repository" "dev_repo" {
  team_id    = github_team.developers.id
  repository = var.repository_name
  permission = "push"
}

resource "github_team_repository" "viewer_repo" {
  team_id    = github_team.viewers.id
  repository = var.repository_name
  permission = "pull"
} 