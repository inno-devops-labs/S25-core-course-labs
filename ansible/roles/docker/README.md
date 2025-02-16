# Docker Role

## Description
This is ansible role that installs Docker and Docker-Compose on target hosts

## Requirements
- Ansible >= 2.10
- Target hosts are running Ubuntu 22.04

## Dependencies

- `apt`
- `python3`

## How to Use

Example of playbook:

```yaml
- name: Install Docker on cloud
  hosts: all
  become: true
  roles:
    - docker
```

### YML Files in Docker Folder

- defaults/main.yml
- handlers/main.yml
- tasks/install_pip.yml
- tasks/install_docker.yml
- tasks/install_compose.yml
- tasks/main.yml