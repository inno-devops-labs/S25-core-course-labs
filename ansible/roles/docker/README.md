# Docker Role

This role installs and configures Docker and Docker Compose on Debian systems.

## Requirements

- Ansible 2.12+
- Debian 9+

## Role Variables

- `docker_users`: The users to add to the Docker group (default: the current Ansible remote user).
- `docker_on_boot`: Whether to enable systemctl service to start Docker on boot (default: `true`).

## Example Playbook

```yaml
- hosts: all
    roles:
    - role: docker
      become: true
```
