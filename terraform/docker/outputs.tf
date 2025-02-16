# moscow_time_app_docker_image
output "moscow_time_app_container_id" {
  description = "Moscow's time app docker container ID"
  value       = docker_container.moscow_time_app_container.id
}

output "moscow_time_app_container_ports" {
  description = "Moscow's time app ports"
  value       = docker_container.moscow_time_app_container.ports
}
output "js_app_container_id" {
  description = "JS app's ID"
  value       = docker_container.js_app_container.id
}

output "js_app_container_ports" {
  description = "JS app's ports"
  value       = docker_container.js_app_container.ports
}
