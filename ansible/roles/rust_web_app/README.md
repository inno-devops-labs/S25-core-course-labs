# Web App Role

This role deploys and manages Docker containers for web applications using Docker Compose. It handles container deployment, configuration management, and cleanup operations.

## Requirements

- Docker (can be installed using the `docker` role)
- Docker Compose plugin

## Role Variables

### Docker Configuration

- `docker_image`: Docker image to deploy (required)
- `container_name`: Name for the deployed container (default: `web_app`)
- `web_app_full_wipe`: Enable complete cleanup of containers and files (default: `false`)

### Docker Compose Configuration

Variables used in the docker-compose.yml template:

- `app_port`: Port to expose the application (default: `8000`)
- `container_port`: Internal container port to map to app_port
- `docker_image`: Docker image to deploy (required)

## Dependencies

- `docker` role (for Docker installation and configuration)
