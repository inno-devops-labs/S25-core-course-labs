# Docker Role


This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.10+
- Ubuntu 22.04
- 'sudo' privileges on the target machine

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).

## Example Playbook

```yaml
- name: install Docker
  hosts: all
  roles:
    - role: docker
```

## Configured Tasks

1. Dependencies installation
2. Docker repository adding
3. Docker installation
4. Docker compose installation
5. Enabling Docker autolaunching (systemctl enable docker)
6. User adding to the 'docker' group
7. Install completion check


## Playbook Instance

```yaml
- hosts: all

  roles:
    - roles/docker	
```