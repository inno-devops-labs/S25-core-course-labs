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
  owner = var.organization
}

resource "github_repository" "repo" {
  name        = var.repo_name
  description = var.repo_description
  visibility  = var.repo_visibility
  auto_init   = true
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = var.default_branch
}

resource "github_team" "dev_team" {
  name           = "Developers"
  description    = "Team for developers"
  privacy        = "closed"
}

resource "github_team" "qa_team" {
  name           = "QA"
  description    = "Team for QA engineers"
  privacy        = "closed"
}

resource "github_team" "admins" {
  name           = "Admins"
  description    = "Administrators with full access"
  privacy        = "closed"
}

resource "github_team" "secret_team" {
  name           = "SecretTeam"
  description    = "A private team with restricted visibility"
  privacy        = "secret"
}

resource "github_team_repository" "developers_access" {
  team_id    = github_team.dev_team.id
  repository = var.repo_name
  permission = "push"
}

resource "github_team_repository" "admins_access" {
  team_id    = github_team.admins.id
  repository = var.repo_name
  permission = "admin"
}

resource "github_team_repository" "qa_access" {
  team_id    = github_team.qa_team.id
  repository = var.repo_name
  permission = "pull"
}

resource "github_team_repository" "secret_access" {
  team_id    = github_team.secret_team.id
  repository = var.repo_name
  permission = "maintain"
}
