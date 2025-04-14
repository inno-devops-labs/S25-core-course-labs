terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}   

# define the organization and the token
provider "github" {
  token = var.token
  owner = "MyOrganizationLab4"
}

resource "github_repository" "repo" {
  name        = "my-team"
  description = "Repository for DevOps Labs"
  visibility  = "public"
}

# teams with their privellages
resource "github_team" "admins" {
  name        = "Admins"
  description = "Admins have full control"
  privacy     = "closed"
}

resource "github_team" "developers" {
  name        = "Developers"
  description = "Developers have write access"
  privacy     = "closed"
}

resource "github_team" "viewers" {
  name        = "Viewers"
  description = "Viewers have read-only access"
  privacy     = "closed"
}

resource "github_team_repository" "admin_access" {
  team_id    = github_team.admins.id
  repository = github_repository.repo.name
  permission = "admin"
}

resource "github_team_repository" "developer_access" {
  team_id    = github_team.developers.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "viewer_access" {
  team_id    = github_team.viewers.id
  repository = github_repository.repo.name
  permission = "pull"
}
