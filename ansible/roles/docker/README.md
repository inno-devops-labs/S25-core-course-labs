# Docker Role

Installs Docker and Docker Compose on Ubuntu 22.04.

## Requirements
- Ansible 2.9+
- Ubuntu 22.04

## Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `docker_version` | `5:24.0.7-1~ubuntu.22.04~jammy` | Docker package version |
| `docker_compose_version` | `v2.26.0` | Docker Compose version |

## Example Playbook
```yaml
- hosts: all
  roles:
    - role: docker