terraform {
   required_providers {
     github = {
       source  = "integrations/github"
       version = "~> 4.0"
     }
   }
 }

resource "github_repository" "repo" {
   name               = "My-incredible-repo"
   description        = "My awesome automated codebase"
   visibility         = "public"
   has_issues         = true
   has_wiki           = true
   auto_init          = true
   license_template   = "mit"
   gitignore_template = "VisualStudio"
 }

provider "github" {
  token = var.token
  owner = "SomeDevOpsOrg"
}

resource "github_team" "team1" {
  name        = "dev"
  description = "push"
  privacy     = "closed"
}

resource "github_team" "team2" {
  name        = "qa"
  description = "read"
  privacy     = "closed"
}

resource "github_team" "team3" {
  name        = "student"
  description = "full"
  privacy     = "closed"
}

resource "github_team_repository" "devss" {
  team_id    = github_team.team1.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "qass" {
  team_id    = github_team.team2.id
  repository = github_repository.repo.name
  permission = "pull"
}

resource "github_team_repository" "studentss" {
  team_id    = github_team.team3.id
  repository = github_repository.repo.name
  permission = "admin"
}