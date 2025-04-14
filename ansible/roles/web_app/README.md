# Web Application Deployment Role

This Ansible role deploys Docker applications using Docker Compose, with support for health checks and automatic
restarts.

## Features

- Docker Compose-based deployment
- Health check support
- Configurable ports and environment variables
- Wipe functionality for clean reinstalls
- Automatic container restart on failure

## Requirements

- Ansible 2.9 or higher
- Docker
- Docker Compose
- Python docker module

## Role Variables

| Variable          | Description                                              | Default                                |
|-------------------|----------------------------------------------------------|----------------------------------------|
| docker_image      | Docker image to deploy                                   | dantetemplar/moscow-time-webapp:latest |
| app_port          | Application port to expose                               | 8000                                   |
| web_app_full_wipe | Enable full cleanup of previous deployment               | false                                  |
| app_name          | Application name used for directory and container naming | moscow_time_webapp                     |
| container_name    | Docker container name                                    | {{ app_name }}_container               |

## Dependencies

- docker role (for Docker installation and configuration)

## Example Playbook

```yaml
- hosts: servers
  become: yes
  roles:
    - role: web_app
      vars:
        docker_image: myapp:latest
        app_port: 8000
```

## Usage

### Basic Deployment

```bash
# Deploy application
ansible-playbook playbooks/dev/app_python/main.yaml

# Deploy with specific tags
ansible-playbook playbooks/dev/app_python/main.yaml --tags docker,deploy

# Wipe and redeploy
ansible-playbook playbooks/dev/app_python/main.yaml --tags wipe -e "web_app_full_wipe=true"
```

### Available Tags

- `setup`: Docker environment setup
- `docker`: Docker-specific operations
- `deploy`: Application deployment
- `wipe`: Cleanup operations
- `app`: All application-related tasks

## Directory Structure

```
web_app/
├── defaults/
│   └── main.yml           # Default variables
├── meta/
│   └── main.yml           # Role dependencies
├── tasks/
│   ├── main.yml           # Main tasks
│   └── 0-wipe.yml         # Cleanup tasks
└── templates/
    └── docker-compose.yml.j2  # Docker Compose template
```

## Healthchecks

The role configures healthchecks for deployed applications. The default configuration:

- Interval: 30s
- Timeout: 10s
- Retries: 3
- Test command: curl -f http://localhost:${PORT}/
