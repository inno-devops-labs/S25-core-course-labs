# Web Application Role

Deploys a web application using Docker Compose.

## Requirements

- Docker Compose installed (via `docker` role)

## Role Variables

- `docker_image`: "your-registry/your-image:tag"
- `app_port`: 8000
- `web_app_full_wipe`: false

## Usage

**Tags** are used to split the two use cases.

1. Run full deployment:

```bash
ansible-playbook playbooks/dev/main.yml --tags deploy --check
```

2. Run wipe tasks:

Additional variable will prevent accidental wipes during manipulations.

```bash
ansible-playbook playbooks/dev/main.yml --tags wipe -e "web_app_full_wipe=true"
```

# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Example Playbook

```yaml
- hosts: all
  roles:
  - role: web_app
```
