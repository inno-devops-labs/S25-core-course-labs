terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  owner = var.org_name
  token = var.token
}

resource "github_team" "terrainers" {
  name        = var.org_editors_name
  description = var.org_editors_description
  privacy     = var.org_editors_privacy
}

resource "github_team" "watchers" {
  name        = var.org_viewers_name
  description = var.org_viewers_description
  privacy     = var.org_viewers_privacy
}

resource "github_repository" "repo" {
  name             = var.org_repo_name
  description      = var.org_repo_description
  visibility       = var.org_repo_visibility
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = var.org_repo_license
}

resource "github_branch" "master" {
  repository = github_repository.repo.name
  branch     = var.org_repo_default_branch
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = github_branch.master.branch
}

resource "github_branch_protection" "default" {
  repository_id = github_repository.repo.id
  pattern       = github_branch_default.default.branch
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
  require_conversation_resolution = true
  enforce_admins                  = true
}

resource "github_team_repository" "terrainers" {
  team_id    = github_team.terrainers.id
  repository = github_repository.repo.name
  permission = var.org_editors_permission
}

resource "github_team_repository" "watchers" {
  team_id    = github_team.watchers.id
  repository = github_repository.repo.name
  permission = var.org_viewers_permission
}