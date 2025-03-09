resource "github_repository" "devops" {
  name = "S25-core-course-labs"
  visibility = "public"
}

resource "github_branch_default" "master" {
  repository = github_repository.devops.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}