resource "github_repository" "my_repo" {
  name        = "my-terraform-repo"
  description = "Managed by Terraform"
  visibility  = "public"
  auto_init   = true
}

resource "github_repository" "S25-core-course-labs" {
  name        = "S25-core-course-labs"
}

resource "github_branch_protection" "main_protection" {
  repository_id = github_repository.my_repo.node_id
  pattern       = "main"

  required_status_checks {
    strict = true
    contexts = []
  }

  enforce_admins = true
  required_pull_request_reviews {
    dismiss_stale_reviews = true
  }
}
