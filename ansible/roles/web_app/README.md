# Ansible Web Application Role

This Ansible role manages the deployment of Docker containers for web applications using Docker Compose.

## Requirements

- Docker Engine (installed via dependency on docker role)
- Docker Compose
- Python docker and docker-compose modules
- Ansible 2.9 or higher

## Role Variables

### Default Variables

```yaml
# Docker image configuration
docker_image_name: "whatislav/moscow-time-app"
docker_image_tag: "latest"
docker_container_name: "web-app"

# Container configuration
container_ports:
  - "80:80"
container_env:
  NODE_ENV: "production"

# Container restart policy
restart_policy: "unless-stopped"

# Container resource limits
memory_limit: "512m"
cpu_limit: "0.5"

# Wipe configuration
web_app_full_wipe: false  # Set to true to enable wiping
```

## Dependencies

- `docker` role (automatically included via meta/main.yml)

## Example Playbook

```yaml
- hosts: web_servers
  roles:
    - role: web_app
      tags: ['web_app']
```

## Usage

### Standard Deployment

```bash
# Full deployment
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags deploy

# Only pull Docker image
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags docker-image

# Only manage container
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags container
```

### Wipe Deployment

To remove the application and all related files:

```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags wipe -e "web_app_full_wipe=true"
```

## Directory Structure

```
.
├── defaults/
│   └── main.yml          # Default variables
├── meta/
│   └── main.yml          # Role metadata and dependencies
├── tasks/
│   ├── 0-wipe.yml        # Wipe tasks
│   └── main.yml          # Main tasks
└── templates/
    └── docker-compose.yml.j2  # Docker Compose template
```

## Tags

- `deploy`: Full deployment
- `docker-image`: Docker image management
- `container`: Container management
- `config`: Configuration tasks
- `wipe`: Wipe tasks (must be explicitly called)