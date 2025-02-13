# Web App Role

This role deploys a Docker-based web application using Ansible.

## Requirements
- Ansible 2.9+
- Ubuntu 22.04+
- Docker & Docker Compose

## Role Variables
- `app_image`: The Docker image to deploy (default: `"nikachek/moscow-time-api:latest"`).
- `container_name`: The name of the Docker container.
- `host_port`: The external port for the application.

## Example Playbook
```yaml
- hosts: all
  roles:
    - web_app
```

