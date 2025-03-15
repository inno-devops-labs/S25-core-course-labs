# Docker Role

This Ansible role installs and configures Docker and Docker Compose on a Ubuntu 22.04 server. It handles the installation of Docker dependencies, Docker itself, and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (other distributions may require adjustments)

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`). 
  This allows for flexible installation methods depending on your environment.

## Role Tasks

The role performs the following tasks:

### Install Docker Dependencies:

Installs necessary packages like apt-transport-https, ca-certificates, curl, gnupg, and lsb-release.

### Add Docker’s Official GPG Key and Repository:

Imports Docker’s GPG key to /etc/apt/keyrings/docker.asc and sets up the Docker repository with the signed-by option to prevent conflicts.

### Install Docker CE:

Installs Docker Community Edition (CE) from the Docker repository.

### Install Docker Compose:

Downloads the Docker Compose binary (AMD64 architecture, typical for Yandex Cloud VMs), sets the executable permission, and verifies the installation.

### Secure Docker Configuration:

Configures Docker to enhance security by disabling root access. It modifies the Docker configuration file /etc/docker/daemon.json with two settings:

- no-new-privileges: Prevents Docker containers from gaining new privileges, even if they are running as root.
- userns-remap: Remaps the root user inside containers to a non-privileged user on the host system, improving isolation.

## Example Playbook

```yaml
---
- name: Deploy Docker on Yandex Cloud VM
  hosts: all
  become: true
  roles:
    - docker
```
