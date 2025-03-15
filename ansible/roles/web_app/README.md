# Web App Role

This Ansible role deploys and manages a web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04
- Docker (installed via docker role dependency)
- Docker Compose

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| app_directory | /opt/web_app | Directory where the application will be deployed |
| docker_image | - | Docker image to deploy (must be specified) |
| app_port | 3000 | Port to expose the application |
| web_app_full_wipe | false | Whether to completely remove the application when running wipe tasks |

## Dependencies

- docker role

## Example Playbook

```yaml
- hosts: all
  vars:
    docker_image: your-username/your-app:latest
    app_port: 3000
  roles:
    - role: web_app
```

## Tags

- `setup`: Initial setup tasks
- `docker`: Docker-related tasks
- `deploy`: Application deployment tasks
- `wipe`: Cleanup tasks (only run when web_app_full_wipe is true)

## Usage

### Regular Deployment
```bash
ansible-playbook playbooks/dev/app_python/main.yaml
```

### Deployment with Wipe
```bash
ansible-playbook playbooks/dev/app_python/main.yaml -e "web_app_full_wipe=true"
```

### Running Specific Tags
```bash
ansible-playbook playbooks/dev/app_python/main.yaml --tags "setup,deploy"
```