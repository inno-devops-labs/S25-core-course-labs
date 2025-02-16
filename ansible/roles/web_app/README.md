# Web Application Role

This Ansible role deploys web applications using Docker Compose. It provides a flexible way to deploy containerized applications with proper configuration and environment variables.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (target system)
- Docker and Docker Compose (installed via dependency on docker role)
- Community Docker collection (`ansible-galaxy collection install community.docker`)

## Role Variables

Available variables are listed below, along with default values:

```yaml
# Application deployment path
app_deploy_path: "/opt/web_app"

# Docker Compose configuration
docker_compose_project_name: "web_app"
docker_compose_file_path: "{{ app_deploy_path }}/docker-compose.yml"

# Application configuration
app_environment: "development"
app_port: 8080

# Docker image configuration
docker_registry: ""  # Default to Docker Hub
docker_image_name: ""
docker_image_tag: "latest"

# Environment variables for the application
app_env_vars: {}

# Health check configuration
health_check_endpoint: "/health"
health_check_timeout: 30
```

## Dependencies

- `docker` role (automatically installed)

## Example Playbook

```yaml
- hosts: web_servers
  vars:
    docker_image_name: "nginx"
    app_port: 80
    app_env_vars:
      NGINX_HOST: "example.com"
      NGINX_PORT: "80"
  roles:
    - role: web_app
```

## Usage

1. Set the required variables in your playbook or inventory
2. Include the role in your playbook
3. Run your playbook

Example command:
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```

## Templates

### Docker Compose Template

The role includes a default Docker Compose template that supports:
- Custom image registry
- Environment variables
- Health checks
- Network configuration
- Port mapping

You can override this template by placing your own version in your playbook's templates directory.

### Environment Variables Template

A template for generating `.env` files is included, which will be used if `app_env_vars` is defined.

## Handlers

The role provides two handlers:
- `restart web app`: Restarts the application using Docker Compose
- `rebuild web app`: Rebuilds and restarts the application

## License

MIT

## Author Information

Created for DevOps Core Course Labs 