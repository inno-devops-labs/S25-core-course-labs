terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
}

## TEAMS

resource "github_team" "maintainers_team" {
  name = "maintainers-team"
}

resource "github_team_membership" "maintainer_member_1" {
  team_id  = github_team.maintainers_team.id
  username = "CatOrLeader"
}

resource "github_team" "admins_team" {
  name = "admin-team"
}

resource "github_team_membership" "admin_member_1" {
  team_id  = github_team.admins_team.id
  username = "CatOrLeader"
}

## MEMBERSHIP

resource "github_team_repository" "maintainers_team" {
  team_id    = github_team.maintainers_team.id
  repository = github_repository.repo.name
  permission = "maintain"
}

resource "github_team_repository" "admins_team" {
  team_id    = github_team.admins_team.id
  repository = github_repository.repo.name
  permission = "admin"
}

## REPOSITORY

resource "github_repository" "repo" {
  name               = var.repo_name
  description        = var.repo_description
  visibility         = var.repo_visibility
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = var.repo_ignore_template
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = github_repository.repo.default_branch
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

