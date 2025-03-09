# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
```

## Features

- Installs Docker CE and required dependencies
- Installs Docker Compose
- Configures Docker to start on boot
- Adds the current user to the docker group
- Handles service restart when needed

## Usage

1. Include the role in your playbook
2. Optionally override the default variables
3. Run your playbook

Example command:
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```

## License

MIT

## Author Information

Created for DevOps Core Course Labs 