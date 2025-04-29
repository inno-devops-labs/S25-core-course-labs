variable "github_token" {
    description = "GitHub personal access token"
    type        = string
    sensitive   = true
}

variable "github_owner" {
    description = "GitHub team name"
    type        = string
    sensitive   = true
}

variable "github_repository" {
    description = "GitHub repository name"
    type        = string
    default     = "core-course-labs"
}
