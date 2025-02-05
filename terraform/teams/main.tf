terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token        = var.github_token
  organization = var.organization_name
}

resource "github_team" "teams" {
  for_each    = var.teams
  name        = each.key
  description = each.value.description
  privacy     = "closed" 
}

resource "github_team_repository" "team_access" {
  for_each    = var.teams
  team_id     = github_team.teams[each.key].id
  repository  = var.repository_name
  permission  = each.value.permission
}
