terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.github_token
  owner = "terraform-for-ali"
}

# New repository
resource "github_repository" "test" {
  name        = "test-repo"
  description = "This is testing"
  visibility  = "public"
}

resource "github_team" "QA" {
  name        = "QA"
  description = "This team is responsible for QA"
  privacy     = "closed"
}

resource "github_team_members" "QA" {
  team_id = github_team.QA.id

  members {
    username = "Ali12hamdan"
    role     = "member"
  }
}
