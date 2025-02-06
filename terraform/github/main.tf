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
  owner = "GFTeamGF"
}

resource "github_repository" "repo" {
  name               = "My-incredible-repo"
  description        = "My awesome codebase"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

#Set default branch 'master'
resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "dev_team" {
  name        = "Developers"
  description = "Development Team with push access"
  privacy     = "closed"
}

resource "github_team" "qa_team" {
  name        = "QA"
  description = "Quality Assurance Team with read access"
  privacy     = "closed"
}

resource "github_team" "admin_team" {
  name        = "Administrators"
  description = "Admins with full control over the repo"
  privacy     = "closed"
}

resource "github_team_repository" "dev_access" {
  team_id    = github_team.dev_team.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "qa_access" {
  team_id    = github_team.qa_team.id
  repository = github_repository.repo.name
  permission = "pull"
}

resource "github_team_repository" "admin_access" {
  team_id    = github_team.admin_team.id
  repository = github_repository.repo.name
  permission = "admin"
}
