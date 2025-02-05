resource "github_repository" "infrastructure" {
  name = "learn-terraform-github-organization-infrastructure"
}

# Add memberships for infrastructure repository
resource "github_team_repository" "infrastructure" {
  for_each = {
    for team in local.repo_teams_files["infrastructure"] :
    team.team_name => {
      team_id    = github_team.all[team.team_name].id
      permission = team.permission
    } if lookup(github_team.all, team.team_name, false) != false
  }

  team_id    = each.value.team_id
  repository = github_repository.infrastructure.id
  permission = each.value.permission
}

# Create application repository
resource "github_repository" "application" {
  name = "learn-terraform-github-organization-application"
}

# Add memberships for application repository
resource "github_team_repository" "application" {
  for_each = {
    for team in local.repo_teams_files["application"] :
    team.team_name => {
      team_id    = github_team.all[team.team_name].id
      permission = team.permission
    } if lookup(github_team.all, team.team_name, false) != false
  }

  team_id    = each.value.team_id
  repository = github_repository.application.id
  permission = each.value.permission
}
