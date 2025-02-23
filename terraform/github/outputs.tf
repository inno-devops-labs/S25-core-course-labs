
output "repository_name" {
  value = github_repository.repo.name
}

output "repository_id" {
  value = github_repository.repo.id
}

output "default_branch" {
  value = github_branch_default.main.branch
}