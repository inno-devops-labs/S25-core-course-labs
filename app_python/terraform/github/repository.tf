resource "github_repository" "repo" {
  name        = var.repo_name
  description = "Core course labs repository managed by Terraform"
  visibility  = "public"
  auto_init   = true
  has_issues  = true
  has_wiki    = false
  has_projects = false
  default_branch = "master"
}
