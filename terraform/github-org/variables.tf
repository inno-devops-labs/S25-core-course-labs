variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token"
  sensitive   = true
}

variable "github_org" {
  type        = string
  description = "Name of the organization"
  default     = "DevopsNikolaiLab4"
}

variable "repo_name" {
  type        = string
  description = "Name of the repo"
  default     = "Devops-Lab4-TF"
}
