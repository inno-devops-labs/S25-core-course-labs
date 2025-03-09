# Docker Role

This role installs and configures Docker and Docker Compose on Ubuntu systems.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 or later
- SSH access to the target machine
- Sudo privileges on the target machine

## Role Variables

No variables are currently defined in this role. The role uses default values for all configurations.

## Dependencies

None

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: docker
```

## Features

- Installs Docker CE from the official Docker repository
- Installs Docker Compose v2.24.5
- Configures Docker to start on boot
- Adds the current user to the docker group
- Installs required Python packages for Docker management
- Creates necessary directories for Docker Compose
