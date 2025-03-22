variable "token" {
  description = "GitHub token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "Repository name"
  type        = string
  default     = "S25-core-course-labs"
}

variable "repository_description" {
  description = "Repository description"
  type        = string
  default     = "DevOps 2025 labs | Minnemullin Nail"
}

variable "visibility" {
  description = "Repository visibility"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "Default branch name"
  type        = string
  default     = "master"
}

variable "organization_name" {
  description = "Name of organization"
  type        = string
  default     = "DevOps2025-n.minnemullin"
}