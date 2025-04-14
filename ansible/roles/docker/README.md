# Docker Role

This role installs and configures Docker and Docker Compose on Ubuntu systems.

## Requirements

- Ansible 2.9+
- Ubuntu 20.04 (Focal Fossa)
- SSH access to target machines
- Sudo privileges on target machines

## Role Variables

Available variables are listed below, along with default values:

```yaml
docker_compose_version: "1.29.2"  # Version of Docker Compose to install
```

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - docker
```

## Role Tasks

The role performs the following main tasks:

1. Installs required system packages
2. Installs Docker using the official installation script
3. Configures Docker to start on boot
4. Creates docker group and adds specified user to it
5. Installs Docker Compose