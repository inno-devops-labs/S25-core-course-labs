# Web App Role

This role deploys the Moscow Time web application using Docker.

## Requirements

- Docker (installed via the docker role)
- Docker Compose v2

## Role Variables

### Default Variables

```yaml
# Wipe configuration
web_app_full_wipe: false  # Set to true to remove all application files

# Docker image configuration
web_app_image: "forygg/moscow-never-sleeps:latest"
web_app_container_name: "moscow-time-app"

# Application configuration
web_app_port: 5000
web_app_host_port: 80

# Container configuration
web_app_restart_policy: "unless-stopped"
```

## Dependencies

- docker role (automatically included via meta/main.yml)

## Tags

- `setup`: Configure the deployment environment
- `config`: Generate configuration files
- `deploy`: Deploy the application
- `docker`: Docker-specific operations
- `wipe`: Remove the application (must be explicitly called)

## Handlers

The role includes two handlers for managing the application state:

- `restart web app`: Simply restarts the container while preserving its configuration
- `recreate web app`: Completely removes and recreates the container (triggered by configuration changes)

These handlers are automatically triggered when:
- Docker image is updated
- Configuration files are modified
- Docker Compose template is changed

## Example Playbook

```yaml
- name: Deploy Moscow Time App
  hosts: all
  become: true
  roles:
    - web_app
```

## Usage

### Standard Deployment
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --ask-become-pass
```

### Deploy Only Docker-related Tasks
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags docker --ask-become-pass
```

### Remove Application
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags wipe -e "web_app_full_wipe=true" --ask-become-pass
``` 