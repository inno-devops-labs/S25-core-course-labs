output "network_id" {
  description = "ID of created network"
  value       = yandex_vpc_network.network.id
}

output "subnet_id" {
  description = "ID of created subnet"
  value       = yandex_vpc_subnet.subnet.id
}

output "subnet_cidr" {
  description = "CIDR block for the subnet"
  value       = yandex_vpc_subnet.subnet.v4_cidr_blocks[0]
}

output "subnet_zone" {
  description = "Zone where subnet is created"
  value       = yandex_vpc_subnet.subnet.zone
}