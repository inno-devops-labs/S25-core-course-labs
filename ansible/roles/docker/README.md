# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_version`: Specifies the version of Docker to install (default: `latest`).
- `docker_compose_version`: Specifies the version of Docker Compose to install (default: `1.29.2`).
- `ansible_user`: The user to be added to the Docker group (default: `ubuntu`).
- `docker_packages`: A list of Docker packages to install (default: `docker-ce`, `docker-ce-cli`, `containerd.io`).
- `required_packages`: A list of required dependencies for Docker installation (default: `apt-transport-https`, `ca-certificates`, `curl`, `software-properties-common`).
- `docker_gpg_key`: The URL of the Docker GPG key (default: `https://download.docker.com/linux/ubuntu/gpg`).
- `docker_repo`: The Docker repository to use (default: `deb https://download.docker.com/linux/ubuntu jammy stable`).
- `docker_compose_url`: The URL to download Docker Compose (default: `https://github.com/docker/compose/releases/download/{{ docker_compose_version }}/docker-compose-linux-x86_64`).
- `docker_compose_dest`: The installation path for Docker Compose (default: `/usr/local/bin/docker-compose`).
- `docker_daemon_config`: Configuration settings for the Docker daemon (default: `{"no-new-privileges": true, "userns-remap": "default"}`).

## Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: docker
      become: true
```
