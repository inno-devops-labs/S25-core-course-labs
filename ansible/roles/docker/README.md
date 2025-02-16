# Docker Role

This role installs and configures Docker and Docker Compose on Ubuntu systems.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (Jammy Jellyfish)
- Python 3.10+

## Role Variables

- `docker_compose_version`: Docker Compose version to install (default: `v2.20.0`)

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: docker
      vars:
        docker_compose_version: "v2.20.0"