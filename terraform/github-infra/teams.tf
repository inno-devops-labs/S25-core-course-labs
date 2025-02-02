# Team 1: Developers (Write Access)
resource "github_team" "developers" {
  name        = "Developers"
  description = "Team responsible for development tasks."
  privacy     = "closed"
}

# Team 2: QA (Read Access)
resource "github_team" "qa" {
  name        = "QA"
  description = "Team responsible for quality assurance."
  privacy     = "closed"
}

# Team 3: Managers (Admin Access)
resource "github_team" "managers" {
  name        = "Managers"
  description = "Team responsible for administrative tasks."
  privacy     = "closed"
}

# Grant Write Access to Developers
resource "github_team_repository" "developers_push_access" {
  team_id    = github_team.developers.id
  repository = github_repository.devops.name
  permission = "push"
}

# Grant Read Access to QA
resource "github_team_repository" "qa_pull_access" {
  team_id    = github_team.qa.id
  repository = github_repository.devops.name
  permission = "pull"
}

# Grant Admin Access to Managers
resource "github_team_repository" "managers_admin_access" {
  team_id    = github_team.managers.id
  repository = github_repository.devops.name
  permission = "admin"
}