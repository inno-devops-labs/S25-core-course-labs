terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
  token = var.github_token
}

# Teams
resource "github_team" "maintainers" {
  name        = "Project maintainers"
  description = "Core project developers"
  privacy     = "closed"
}

resource "github_team" "contributors" {
  name        = "Project contributors"
  description = "Well-known open-source contributors"
  privacy     = "closed"
}

# Repository
resource "github_repository" "repository" {
  name         = "devops-teams-test"
  description  = "Collaborative project for test"
  visibility   = "public"
  has_issues   = true
  has_wiki     = false
  auto_init    = true
}

# Default Branch
resource "github_branch_default" "main_branch" {
  repository = github_repository.repository.name
  branch     = "main"
}

# Branch Protection (Fixed)
resource "github_branch_protection" "repo_protection" {
  repository_id                   = github_repository.repository.node_id # Fix: Use node_id instead of name
  pattern                         = "main"
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

# Assign Teams to Repository
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
