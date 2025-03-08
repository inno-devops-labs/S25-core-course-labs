variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "description" {
  type        = string
  description = "This is a short paraphrase that desecripe the goal of the repository"
  default     = "This repository contains course materials and exercises for learning DevOps practices. It covers topics such as continuous integration, continuous deployment, infrastructure as code, containerization, and monitoring. The course is designed to provide hands-on experience with tools like GitHub Actions, Docker, Terraform, and Kubernetes."
}

variable "description" {
  type        = string
  description = "This is the name of the github organization"
  default     = "lab4-teams-terraform"
}

