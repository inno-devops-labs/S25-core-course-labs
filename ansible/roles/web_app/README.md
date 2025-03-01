# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `latest`).

## Example Playbook

```yaml
- name: Install and Configure Docker
  hosts: all
  become: yes 
  roles:
    - web_app
```

## Tags
- `wipe` - stop and remove a container with image
- `app` - run the app inside container
- `docker-compose` - generate a docker-compose file from template
- `setup` - install docker 
- `docker` - pull image