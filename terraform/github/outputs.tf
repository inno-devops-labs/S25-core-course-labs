output "repository_name" {
  value = github_repository.core-course-labs.name
}

output "repository_id" {
  value = github_repository.core-course-labs.id
}

output "default_branch" {
  value = github_branch_default.master.branch
}
