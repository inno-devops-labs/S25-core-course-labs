# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Tasks

- Installs Docker dependencies
- Configures Docker repository
- Installs Docker Engine
- Sets up Docker Compose
- Configures daemon security settings
- Adds user to docker group

## Role Variables

- `docker_version`: Docker version to install (default: `5:27.5.1-1~ubuntu.22.04~jammy`)
- `ansible_user`: User to add to the Docker group (default: `ubuntu`)

## Example Playbook

```yaml
- name: Docker playbook
  hosts: all
  roles:
    - docker
```
