terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = ">= 6.5.0"
    }
  }
}

provider "github" {
  owner = var.organization
  token = var.token
}

resource "github_repository" "repo" {
  name             = var.repository_name
  description      = var.repository_description
  visibility       = var.repository_visibility
  has_downloads    = var.has_downloads
  has_issues       = var.has_issues
  has_wiki         = var.has_wiki
  has_projects     = var.has_projects
  license_template = var.license_template
  auto_init        = var.auto_init
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_branch_protection" "default" {
  repository_id = github_repository.repo.id
  pattern       = github_branch_default.main.branch

  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 0
  }
}

resource "github_team" "developers" {
  name        = "Development Team"
  description = "Development Team"
  privacy     = "closed"
}

resource "github_team" "devops" {
  name        = "DevOps Team"
  description = "DevOps Team"
  privacy     = "closed"
}

resource "github_team_repository" "developers_repo" {
  team_id    = github_team.developers.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "devops_repo" {
  team_id    = github_team.devops.id
  repository = github_repository.repo.name
  permission = "maintain"
}