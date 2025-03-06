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
  token = var.github_token
}


resource "github_team" "maintainers" {
  name        = "Repository maintainers"
  description = "Initial developers"
  privacy     = "closed"
}

resource "github_team" "contributors" {
  name        = "Repository contributors"
  description = "Contributors from open-source"
  privacy     = "closed"
}

resource "github_repository" "repository" {
  name        = "devops-teams"
  description = "Collaborative repository"
  visibility  = "public"
  has_issues  = true
  has_wiki    = false
  auto_init   = true
}

resource "github_branch_default" "main_branch" {
  repository = github_repository.repository.name
  branch     = "main"
}

resource "github_branch_protection" "repo_protection" {
  repository_id                   = github_repository.repository.id
  pattern                         = github_branch_default.main_branch.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team_repository" "maintainers" {
  team_id    = github_team.maintainers.id
  repository = github_repository.repository.name
  permission = "maintain"
}

resource "github_team_repository" "contributors" {
  team_id    = github_team.contributors.id
  repository = github_repository.repository.name
  permission = "push"
}
