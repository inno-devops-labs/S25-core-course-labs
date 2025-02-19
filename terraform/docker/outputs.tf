output "python_container_id" {
  value = docker_container.moscow_time_app.id
}

output "python_container_ip" {
  value = docker_container.moscow_time_app.network_data[0].ip_address
}

output "js_container_id" {
  value = docker_container.countdown_timer_app.id
}

output "js_container_ip" {
  value = docker_container.countdown_timer_app.network_data[0].ip_address
}
