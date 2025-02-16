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
  owner = var.github_organization
}

resource "github_repository" "repo" {
  name               = var.repo_name
  description        = var.repo_desc
  visibility         = var.repo_visibility
  has_issues         = var.repo_has_issues
  has_wiki           = var.repo_has_wiki
  auto_init          = var.repo_auto_init
  license_template   = var.repo_license
  gitignore_template = var.repo_gitignore
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = var.default_branch
  depends_on = [github_repository.repo]
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = var.default_branch
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins

  required_pull_request_reviews {
    required_approving_review_count = var.required_approving_review_count
  }
}

resource "github_team" "dev_team" {
  name        = var.dev_team_name
  description = var.dev_team_desc
  privacy     = var.dev_team_privacy
}

resource "github_team" "qa_team" {
  name        = var.qa_team_name
  description = var.qa_team_desc
  privacy     = var.qa_team_privacy
}

resource "github_team_repository" "dev_team_access" {
  team_id    = github_team.dev_team.id
  repository = github_repository.repo.name
  permission = var.dev_team_permission
}

resource "github_team_repository" "qa_team_access" {
  team_id    = github_team.qa_team.id
  repository = github_repository.repo.name
  permission = var.qa_team_permission
}
