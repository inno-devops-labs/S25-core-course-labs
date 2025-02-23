terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  owner = var.organization
  token = var.token
}


resource "github_team" "developers" {
  name           = "Development team"
  description    = "Guys chase jsons"
  privacy        = "closed"
  parent_team_id = null
}

resource "github_team" "devops" {
  name           = "DevOps team"
  description    = "Guys build and deploy code"
  privacy        = "closed"
  parent_team_id = null
}

resource "github_team" "qa" {
  name           = "Quality assurance Team"
  description    = "Guys check the code (and break it)"
  privacy        = "closed"
  parent_team_id = null
}

resource "github_team" "sa" {
  name           = "System analysts Team"
  description    = "Guys make tasks and know the system"
  privacy        = "closed"
  parent_team_id = null
}

resource "github_repository" "repo" {
  name             = "Cool-project"
  description      = "The Cool Project"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "repo_protection" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team_repository" "devops_access" {
  team_id    = github_team.devops.id
  repository = github_repository.repo.name
  permission = "admin"
}

resource "github_team_repository" "developers_access" {
  team_id    = github_team.developers.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "qa_access" {
  team_id    = github_team.qa.id
  repository = github_repository.repo.name
  permission = "pull"
}

resource "github_team_repository" "sa_access" {
  team_id    = github_team.sa.id
  repository = github_repository.repo.name
  permission = "pull"
}