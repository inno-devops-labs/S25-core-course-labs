terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = var.organization_name
}

resource "github_repository" "repo" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.visibility

  auto_init    = true
  has_issues   = true
  has_projects = true
  has_wiki     = false
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.repo.node_id
  pattern       = var.default_branch

  required_pull_request_reviews {
    required_approving_review_count = 1
  }

  enforce_admins = true
}

resource "github_team" "admin_team" {
  name        = "admin"
  description = "Administrators"
  privacy     = "closed"
}

resource "github_team_repository" "admin_team_access" {
  team_id    = github_team.admin_team.id
  repository = github_repository.repo.name
  permission = "admin"
}

resource "github_team" "dev_team" {
  name        = "developers"
  description = "Developers"
  privacy     = "closed"
}

resource "github_team_repository" "dev_team_access" {
  team_id    = github_team.dev_team.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team" "view_team" {
  name        = "viewers"
  description = "Viewers"
  privacy     = "closed"
}

resource "github_team_repository" "view_team_access" {
  team_id    = github_team.view_team.id
  repository = github_repository.repo.name
  permission = "pull"
}