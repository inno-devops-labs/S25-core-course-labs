# Docker Role

This role installs and configures Docker CE and Docker Compose on Ubuntu-based systems.

## Requirements

- Ansible 2.9+
- Ubuntu-based system (tested on Pop!_OS)
- Root/sudo access

## Role Variables

### Default Variables

```yaml
# Docker version configuration
docker_version: "latest"
docker_compose_version: "v2.24.5"

# Docker daemon configuration
docker_daemon_options: {}

# User configuration
docker_users: []  # List of additional users to add to docker group

# System configuration
docker_apt_repository: "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable"
```

### Required Packages
The role automatically installs these dependencies:
- ca-certificates
- curl
- gnupg

## Features

- Installs Docker CE from official Docker repository
- Installs Docker Compose v2
- Configures Docker daemon
- Adds specified users to the docker group
- Automatically adds the ansible user to the docker group

## Example Playbook

```yaml
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker
```

## Usage

1. Ensure your inventory file is configured (default uses localhost)
2. Run the playbook:
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --ask-become-pass
```

## Notes

- The role uses Ubuntu's Docker repository even on Pop!_OS for better compatibility (there is no Docker repository for Pop!_OS)
- Docker Compose is installed from GitHub releases
- The role includes retry logic for package installation to handle system locks (since the system is locked when the package is being installed and it prevents the playbook from continuing)