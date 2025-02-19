output "vm_id" {
  description = "ID of the VM instance"
  value       = yandex_compute_instance.vm.id
}

output "vm_external_ip" {
  description = "External IP of the VM"
  value       = yandex_compute_instance.vm.network_interface[0].nat_ip_address
}

output "vm_internal_ip" {
  description = "Internal IP of the VM"
  value       = yandex_compute_instance.vm.network_interface[0].ip_address
}
