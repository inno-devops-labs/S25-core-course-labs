# Docker Role

  This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_image`: `anyarylova/app_python`
- `docker_container`: `app_python`
- `app_port`: `8080`

## Example Playbook

```yaml
  - name: Deploy Web App
    hosts: local
    become: yes
    roles:
      - web_app
```

## Dependencies

- Docker
