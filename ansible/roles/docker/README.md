# Docker Role

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

Configure variables in [defaults/main.yml](defaults/main.yml):

* docker_compose_version: "1.29.2"
    This property sets the version of Docker Compose to be installed. Docker Compose is used for managing multi-container Docker applications. By setting this property to "1.29.2", you are ensuring that the specified version of Docker Compose is installed. If no specific version is required, you can adjust this to the latest version.

## Playbook

Include `docker` role in your playbook

```shell
- name: Deploy Docker
  become: true
  hosts: all
  roles:
    - docker
```

## Tasks

[main.yml](tasks/main.yml)

The main playbook file that imports tasks from separate YAML files.

* install_docker.yml - Installs Docker and its dependencies.
* install_compose.yml - Installs Docker Compose.
* security_docker.yml - Applies security settings to Docker.

[install_docker.yml](tasks/install_docker.yml)

This file is responsible for installing Docker and configuring it.

Tasks Breakdown
* Update package cache (apt update).
* Install dependencies (required for Docker installation).
* Add Docker’s official GPG key (for package verification).
* Add Docker repository (for downloading the latest stable version).
* Install Docker.
* Enable and start Docker service.
* Add the current user to the docker group (to allow non-root users to run Docker commands).

[install_compose.yml](tasks/install_compose.yml)
This file installs Docker Compose.

Tasks Breakdown
* Download Docker Compose binary from the official GitHub releases.
* Verify that Docker Compose is installed correctly.
* Output the installed version for debugging.


[security_docker.yml](tasks/security_docker.yml)

This file applies security settings to Docker.

Tasks Breakdown
* Ensure /etc/docker/ directory exists.
* Apply security configurations in daemon.json:
* userns-remap: "default" → Prevents running containers as root.
* no-new-privileges: true → Blocks privilege escalation inside containers.
* live-restore: true → Keeps containers running even if Docker service restarts.
* Validate JSON syntax using jq.
* Fail if the JSON file is invalid, preventing Docker misconfiguration.