# Web App Role

This Ansible role deploys a containerized web application using Docker and Docker Compose

## Requirements

- Ansible 2.9+
- Ubuntu 20.04+
- Docker (installed via dependency)
- Docker Compose V2

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| docker_image | your-docker-image:latest | Docker image to be deployed |
| app_port | 8000 | Port to expose the application |
| web_app_full_wipe | false | Enable complete cleanup of the application |

## Dependencies

- docker role (automatically installed)

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - web_app
  vars:
    docker_image: "dexnight/moscow-time-app:latest"
    app_port: 8000
```

## Tags

- `setup`: Initial setup tasks
- `docker`: Docker-related operations (pulling images, starting containers)
- `wipe`: Cleanup tasks (only executed when web_app_full_wipe=true)

## Usage

### Normal Deployment
```bash
ansible-playbook playbook.yml
```

### Deploy Only Docker-Related Tasks
```bash
ansible-playbook playbook.yml --tags docker
```

### Clean Up Application
```bash
ansible-playbook playbook.yml --tags wipe -e "web_app_full_wipe=true"
```