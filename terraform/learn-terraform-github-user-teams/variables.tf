variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}


variable "github_organization" {
  type        = string
  description = "This is the name of the github organization"
  default     = "lab4-teams-terraform"
}

