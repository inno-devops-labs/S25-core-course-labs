
# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17+ 
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `latest`).

## Playbook for local deployment

```yaml
    - name: Deploy Docker using Ansible
    hosts: all
    become: true
    roles:
        - docker
```

## Playbook for yandex deployment

Required: 
- install the plugin yacloud_compute.py (https://github.com/rodion-goritskov/yacloud_compute)

```yaml
    all:
        hosts:
            compute-lab5-1: # vm machine name in yandex cloud 
            ansible_host: 84.201.151.82 # ip your VM
            ansible_user: ivangeliev # your yandex profile name 
            yacloud_token_file: ./inventory/authorized_key.json # path to the downloaded from yandex cloud json key for VM access
            plugin: yacloud_compute # plugin path 
```
