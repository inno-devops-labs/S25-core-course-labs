# main.tf
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"  # Для Windows
}

resource "docker_network" "app_network" {
  name = "times-network"
}


resource "docker_image" "db" {
  name = "jmartynova123/dev-lab3-db:latest"
}

resource "docker_container" "db" {
  name  = "db"
  image = docker_image.db.image_id
  networks_advanced {
    name = docker_network.app_network.name
  }
  
  env = [
    "POSTGRES_USER=${var.db_user}",
    "POSTGRES_PASSWORD=${var.db_password}",
    "POSTGRES_DB=${var.db_name}"
  ]

  ports {
    internal = 5432
    external = 5432
  }

  healthcheck {
    test     = ["CMD-SHELL", "pg_isready -U ${var.db_user} -d ${var.db_name}"]
    interval = "30s"
    timeout  = "10s"
    retries  = 5
  }
}

resource "docker_image" "backend" {
  name = "jmartynova123/dev-lab3-back:latest"
}

resource "docker_container" "backend" {
  name  = "backend"
  image = docker_image.backend.image_id
  networks_advanced {
    name = docker_network.app_network.name
  }

  env = [
    "DATABASE_URI=postgres://${var.db_user}:${var.db_password}@db:5432/${var.db_name}"
  ]

  ports {
    internal = 8080
    external = 8080
  }

  healthcheck {
    test     = ["CMD-SHELL", "curl -f http://localhost:8080/times || exit 1"]
    interval = "30s"
    timeout  = "10s"
    retries  = 5
  }

  restart = "unless-stopped"

  depends_on = [
    docker_container.db
  ]
}


resource "docker_image" "frontend" {
  name = "jmartynova123/dev-lab3-front:latest"
}

resource "docker_container" "frontend" {
  name  = "frontend"
  image = docker_image.frontend.image_id
  networks_advanced {
    name = docker_network.app_network.name
  }

  ports {
    internal = 3000
    external = 3000
  }

  healthcheck {
    test     = ["CMD-SHELL", "curl -f http://localhost:3000 || exit 1"]
    interval = "30s"
    timeout  = "10s"
    retries  = 5
  }

  depends_on = [
    docker_container.backend
  ]
}

output "db_container_id" {
  description = "Database container id"
  value       = docker_container.db.id
}

output "db_image_id" {
  description = "Database image id"
  value       = docker_image.db.id
}

output "backend_container_id" {
  description = "Backend container id"
  value       = docker_container.backend.id
}

output "backend_image_id" {
  description = "Backend image id"
  value       = docker_image.backend.id
}

output "frontend_container_id" {
  description = "Frontend container id"
  value       = docker_container.frontend.id
}

output "frontend_image_id" {
  description = "Frontend image id"
  value       = docker_image.frontend.id
}