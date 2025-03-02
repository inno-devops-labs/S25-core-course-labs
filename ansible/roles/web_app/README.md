# Web Application Role

This role deploys a Python web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04
- Docker (installed via docker role dependency)

## Role Variables

- `docker_image`: Docker image to deploy (default: "mazzz3r/app_python:latest")
- `app_container_name`: Container name (default: "python_app")
- `app_port`: Internal container port (default: 5000)
- `app_external_port`: External port mapping (default: 5000)
- `app_directory`: Application directory (default: "/opt/python_app")
- `web_app_full_wipe`: Enable wipe functionality (default: false)

## Dependencies

- docker role

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: web_app
```

## Usage

Regular deployment:
```bash
ansible-playbook playbook.yml --tags app
```

Wipe and redeploy:
```bash
ansible-playbook playbook.yml --tags wipe,app -e "web_app_full_wipe=true"
``` 