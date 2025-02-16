# Docker Role

This Ansible role installs and configures Docker and Docker Compose, ensuring Docker starts on boot and allowing users to run Docker without `sudo`.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 or later

## Role Variables

| Variable                  | Description                                      | Default       |
|---------------------------|--------------------------------------------------|--------------|
| `docker_version`          | The version of Docker to install                | `latest`     |
| `docker_compose_version`  | The version of Docker Compose to install        | `latest`     |
| `docker_user`             | User to be added to the Docker group            | `{{ ansible_user }}` |
      

## Tasks Overview

This role performs the following actions:

1. Installs Docker and Docker Compose.
2. Enables and starts the Docker service on boot.
3. Adds the specified user to the `docker` group to allow running Docker commands without `sudo`.

## Handlers

- **Restart Docker**: Triggers when `daemon.json` is modified.

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: docker

