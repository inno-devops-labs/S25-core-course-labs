# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.16+
- Ubuntu 24.04 (stable) (by default)

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_distro`: Distro Docker to install (default: `ubuntu oracular stable`).
- `docker_user`: User to grant Docker group (default: `root`).

## Example Playbook

```yaml
- hosts: all
  roles:
  - role: docker
```
