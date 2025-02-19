# Docker Role

This role installs and configures Docker and Docker Compose on both Ubuntu and macOS systems.

## Requirements

- Ansible 2.9+
- Target system (one of):
  - Ubuntu 22.04 with Python 3.x
  - macOS with Homebrew installed
- For local development:
  - ANSIBLE_SUDO_PASS environment variable set

## Role Variables

The role uses the following variables (defined in `defaults/main.yml`):

```yaml
# Docker version configuration
docker_package: "docker-ce"
docker_compose_version: "v2.24.5"

# Users to be added to docker group (Linux only)
docker_users: ["{{ ansible_user_id }}"]

# Docker daemon configuration (Linux only)
docker_daemon_options:
  log-driver: "json-file"
  log-opts:
    max-size: "100m"
  storage-driver: "overlay2"
```

## Platform-Specific Behavior

### Ubuntu
- Installs Docker CE from official Docker repository
- Configures Docker daemon using daemon.json
- Adds specified users to docker group
- Enables and starts Docker service
- Installs Docker Compose from GitHub releases

### macOS
- Installs Docker Desktop using Homebrew
- Installs Docker Compose using Homebrew
- No daemon configuration needed (handled by Docker Desktop)

## Dependencies

- For macOS: Homebrew must be installed
- For Ubuntu: No external dependencies

## Example Playbook

```yaml
# For Ubuntu systems
- hosts: webservers
  roles:
    - role: docker
      vars:
        docker_users: ["ubuntu"]

# For local macOS development
- hosts: localhost
  roles:
    - role: docker
```

## Testing

You can test the role using:
```bash
# Set sudo password for local testing
export ANSIBLE_SUDO_PASS='your_sudo_password'

# Dry run
ANSIBLE_BECOME_PASS=$ANSIBLE_SUDO_PASS ansible-playbook playbooks/dev/main.yaml --check --diff

# Actual run
ANSIBLE_BECOME_PASS=$ANSIBLE_SUDO_PASS ansible-playbook playbooks/dev/main.yaml
```

## License

MIT

## Author Information

Created for S25-core-course-labs 