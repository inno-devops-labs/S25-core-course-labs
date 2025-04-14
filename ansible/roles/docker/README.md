# Docker Role

This Ansible role installs and configures Docker and Docker Compose on Ubuntu servers. It provides a robust and secure Docker installation with proper user permissions and system configurations.

## Requirements

- Ubuntu 20.04 (Focal) or newer
- Ansible 2.9 or newer
- Python 3.x
- Sudo privileges on target hosts

## Role Variables

Available variables are listed below, along with default values:

```yaml
# Docker package and service configuration
docker_package: "docker-ce"
docker_package_state: present

# Docker Compose configuration
docker_compose_version: "2.23.3"
docker_compose_path: "/usr/local/bin/docker-compose"

# Docker daemon options
docker_daemon_options:
  storage-driver: "overlay2"
  log-driver: "json-file"
  log-opts:
    max-size: "100m"
    max-file: "3"

# Users to be added to docker group
docker_users:
  - "{{ ansible_user }}"

# Docker apt repository configuration
docker_apt_release_channel: stable
docker_apt_arch: amd64
docker_apt_repository: "deb [arch={{ docker_apt_arch }}] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} {{ docker_apt_release_channel }}"
docker_apt_gpg_key: "https://download.docker.com/linux/ubuntu/gpg"

# System packages required for Docker
docker_required_packages:
  - apt-transport-https
  - ca-certificates
  - curl
  - software-properties-common
  - python3-pip
  - virtualenv
  - python3-setuptools
```

## Role Features

1. **Docker Installation**:
   - Installs latest Docker CE version
   - Configures Docker repository
   - Sets up Docker daemon options
   - Enables Docker service

2. **Docker Compose Installation**:
   - Installs specified Docker Compose version
   - Creates appropriate symlinks
   - Verifies installation

3. **Security Configuration**:
   - Creates docker group
   - Manages user permissions
   - Sets appropriate file permissions
   - Configures Docker daemon security options

## Dependencies

None. This role is self-contained and does not depend on other Ansible roles.

## Example Playbooks

1. **Basic Usage**:
```yaml
- hosts: servers
  roles:
    - role: docker
```

2. **Custom Configuration**:
```yaml
- hosts: servers
  roles:
    - role: docker
      vars:
        docker_users:
          - ubuntu
          - admin
        docker_compose_version: "2.23.3"
        docker_daemon_options:
          storage-driver: "overlay2"
          log-driver: "json-file"
          log-opts:
            max-size: "100m"
            max-file: "3"
```

3. **Production Setup**:
```yaml
- hosts: production_servers
  roles:
    - role: docker
      vars:
        docker_daemon_options:
          storage-driver: "overlay2"
          log-driver: "json-file"
          log-opts:
            max-size: "500m"
            max-file: "5"
          metrics-addr: "0.0.0.0:9323"
          experimental: true
```

## Usage

1. **Include Role in Requirements**:
```yaml
# requirements.yml
- src: https://github.com/yourusername/ansible-role-docker
  name: docker
  version: main
```

2. **Install Role**:
```bash
ansible-galaxy install -r requirements.yml
```

3. **Use in Playbook**:
```yaml
- hosts: servers
  roles:
    - docker
```

## Troubleshooting

1. **Docker Service Issues**:
   - Check service status: `systemctl status docker`
   - Review logs: `journalctl -u docker`

2. **Permission Problems**:
   - Verify user is in docker group: `groups username`
   - Check Docker socket permissions: `ls -l /var/run/docker.sock`

3. **Installation Failures**:
   - Verify system requirements
   - Check network connectivity
   - Review apt repository configuration