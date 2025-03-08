# Docker Role

This role deploys the app using docker.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_image`: Name of docker image
- `docker_container`: Docker container name
- `internal_port`
- `external_port`
- `web_app_full_wipe`: for viping previous app (true)
- `web_app_dir`: /webapp by default

## Playbook

```yaml
- name: Deploy Python app
  hosts: all
  become: yes
  roles:
    - web_app
    vars:
      docker_image: "nickolaus899/python-msk-time:latest"
      docker_container: python-msk-time

      internal_port: 5000
      external_port: 8080
      web_app_full_wipe: true  
```

## Tasks

* `0-wipe.yml`
* `deploy.yml`