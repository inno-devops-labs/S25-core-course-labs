# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `2.15.1`).
- `docker_packages`: List of prerequisite packages for Docker installation.
- `docker_users`: List of users to add to the Docker group (default: current ansible user).
- `docker_daemon_config`: Configuration for the Docker daemon.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
      docker_version: "latest"
      docker_compose_version: "2.15.1"
      docker_users:
        - ubuntu
```

## License

MIT

## Author Information

Created for the S25 DevOps Core Course Labs. 