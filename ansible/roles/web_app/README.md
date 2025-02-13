# Docker image deployment role

This Ansible role manages the deployment of web applications using Docker and Docker Compose.

## Requirements

- Ansible 2.9 or higher
- Docker and Docker Compose installed on the target host (handled by role dependency)
- Docker Python module installed on the target host (handled by role dependency)
- Ansible collection `community.docker` installed on the target host (used `docker_compose_v2` for better idempotency)

## Role Variables

### Default Variables

```yaml
# Docker image configuration
docker_image: "your-docker-image:latest"  # Replace with your actual image
app_port: 8080  # Default application port

# Docker compose configuration
docker_compose_dir: "/opt/web_app"
docker_compose_file: "docker-compose.yml"

# Application environment variables
app_environment: {}
```

## Dependencies

- `docker` role - Ensures Docker is installed and configured

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: web_app
      vars:
        docker_image: "fallenchromium/moscow-timezone-app:distroless"
        app_port: 8000
        app_bind_port: "80"
```

## Tags

- `setup`: Configure the environment
- `docker`: Docker-specific operations
- `deploy`: Deploy the application
- `wipe`: Clean up deployment

## Usage

### Wipe the application

```bash
ansible-playbook playbooks/dev/main.yaml --tags "wipe" -i inventory/yacloud_compute.yml
```

### Reinstall the application

```bash
ansible-playbook playbooks/dev/main.yaml -e "app_clean_install=true" -i inventory/yacloud_compute.yml
```

## License

MIT
