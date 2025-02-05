output "name" {
  description = "Virtual machine name"
  value       = yandex_compute_instance.virtual_machine.name
}

output "address" {
  description = "Public IP"
  value       = yandex_compute_instance.virtual_machine.network_interface.0.nat_ip_address
}
