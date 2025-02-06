variable "github_token" {}

variable "repo_name" {
  default = "S25-core-course-labs"
}

variable "repo_description" {
  default = "DevOps course Terraform-managed repository"
}

variable "repo_visibility" {
  default = "private"
}

variable "default_branch" {
  default = "master"  # Updated to "master"
}
