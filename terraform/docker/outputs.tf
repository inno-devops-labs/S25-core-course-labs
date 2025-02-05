output "python_app_container_id" {
  description = "ID of Python app container"
  value       = docker_container.python_app_container.id
}

output "scala_app_container_id" {
  description = "ID of Scala app container"
  value       = docker_container.scala_app_container.id
}

output "python_app_ports" {
  description = "Ports for Python app container"
  value       = docker_container.python_app_container.ports
}

output "scala_app_ports" {
  description = "Ports for Scala app container"
  value       = docker_container.scala_app_container.ports
}
