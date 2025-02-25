output "python_app_url" {
  description = "URL of python app"
  value       = "http://localhost:${var.python_host_port}"
}

output "kotlin_app_url" {
  description = "URL of Kotlin app"
  value       = "http://localhost:${var.kotlin_host_port}"
}