# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Supported Operating Systems:
  - Arch Linux

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `v2.24.5`).

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: docker
```

## Usage

1. Include the role in your playbook.
2. Optionally override the default variables.
3. Run your playbook with the following command:
   ```bash
   ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
   ```
