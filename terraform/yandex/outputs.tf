output "external_ip" {
  description = "Public IP address of the server"
  value       = yandex_compute_instance.app_server.network_interface[0].nat_ip_address
}

output "internal_ip" {
  description = "Internal IP address of the server"
  value       = yandex_compute_instance.app_server.network_interface[0].ip_address
} 