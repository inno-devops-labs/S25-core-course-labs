# Ansible Docker role

## Description

This ansible role installs Docker on Ubuntu 22.04

## Requirements

* `apt` must be pre-installed on the host machine.
* Configure variables in defaults.main.yml:

```shell
# Service options.
docker_service_manage: true
docker_service_state: started
docker_service_enabled: true
docker_restart_handler_state: restarted

# Docker Compose Plugin options.
docker_install_compose_plugin: true
docker_compose_package: docker-compose-plugin
docker_compose_package_state: present
```

## Playbook

Include `docker` role in your playbook

```shell
- name: Deploy Docker
  become: true
  hosts: all
  roles:
    - docker
```
