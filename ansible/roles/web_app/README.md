# Web Application Deployment Role

This Ansible role manages the deployment of web applications using Docker Compose. It provides a flexible and maintainable way to deploy containerized applications with proper configuration management.

## Requirements

- Ansible 2.9 or higher
- Docker installed on target hosts (this role depends on the `docker` role)
- Docker Compose v2 or higher
- Target system: Ubuntu (Focal/Jammy)

## Role Variables

### Required Variables

- `docker_image_name`: Name of the Docker image to deploy
- `app_port`: Port number where the application will be exposed

### Optional Variables

```yaml
# Application deployment path
app_deploy_path: "/opt/web_app"

# Docker Compose configuration
docker_compose_project_name: "web_app"
docker_compose_file_path: "{{ app_deploy_path }}/docker-compose.yml"

# Application configuration
app_environment: "development"
docker_registry: ""  # Default to Docker Hub
docker_image_tag: "latest"

# Environment variables for the application
app_env_vars: {}

# Health check configuration
health_check_endpoint: "/health"
health_check_timeout: 30

# Wipe configuration
web_app_full_wipe: false  # Set to true to remove all application data
```

## Dependencies

This role depends on the `docker` role which should be installed and configured first.

## Example Playbook

```yaml
- hosts: web_servers
  vars:
    docker_image_name: "my-web-app"
    app_port: 8080
    app_env_vars:
      NODE_ENV: production
      API_KEY: "{{ vault_api_key }}"
  roles:
    - web_app
```

## Tags

- `setup`: Configure application environment
- `deploy`: Deploy the application
- `wipe`: Remove application (when web_app_full_wipe=true)
- `health-check`: Run application health checks

## Usage Examples

1. Deploy application:
   ```bash
   ansible-playbook playbook.yml -t deploy
   ```

2. Setup environment only:
   ```bash
   ansible-playbook playbook.yml -t setup
   ```

3. Wipe application:
   ```bash
   ansible-playbook playbook.yml -t wipe -e "web_app_full_wipe=true"
   ```

## License

MIT

## Author Information

Created by DevOps Core Course Team 