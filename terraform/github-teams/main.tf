terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}


provider "github" {
  owner = var.github_organization
  token = var.github_pat
}


resource "github_team" "developers" {
  name        = "Development Team"
  description = "The team that always does everything on the verge of deadline"
  privacy     = "closed"
}

resource "github_team" "devops" {
  name        = "DevOps Team"
  description = "The team that manages on time"
  privacy     = "closed"
}

resource "github_repository" "repo" {
  name             = "devops-test-team-repo"
  description      = ""
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch_default" "repo_main" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "repo_protection" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.repo_main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
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
