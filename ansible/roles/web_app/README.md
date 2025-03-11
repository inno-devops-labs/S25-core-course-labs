# Web Application Role

This role deploys a web application using Docker Compose.

## Requirements

- **Docker**: Installed and configured using the `docker` role.
- **Docker Compose**: Installed and configured using the `docker` role.

## Role Variables

- `docker_image`: The Docker image to deploy (default: `sonyaiv/python_app:latest`).
- `internal_port` and `external_port`: The port to expose the application on (default: `8000` and `8080`).
- `web_app_full_wipe`: Whether to wipe the Docker environment (default: `false`).

## Tasks

1. **Setup Docker Compose**:
   - Installs Docker Compose.
   - Creates a Docker Compose file from a template.
   - Starts the Docker Compose services.

2. **Wipe Docker Environment**:
   - Stops and removes Docker containers.
   - Removes the Docker Compose file.

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: web_app
      vars:
        docker_image: "sonyaiv/python_app:latest"
        docker_container: "python_app"
        docker_compose_filename: "docker-compose.yml"

        web_app_dir: "/webapp"

        internal_port: 8000
        external_port: 80

        web_app_full_wipe: true
```

