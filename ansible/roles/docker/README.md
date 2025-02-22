# Docker Role

The following role installs Docker with Docker Compose. Additionally, it adds user to docker group, ensures that Docker will start on boot and removes extra priviledges (root access) from the containers to ensure safety.

## Requirements

- **Ansible** 2.9+
- **Supported OS**: Ubuntu 22.04+

## Role Variables

- `compose_version`: The required version of Docker Сompose to be installed.The version of Docker Compose to install (default: `1.29.2`)

- `ansible_user`: Username in VM.

## Example Playbook

The playbook for role

```yaml
  - name: Install Docker
    hosts: all
    become: true
    roles:
      - docker
```