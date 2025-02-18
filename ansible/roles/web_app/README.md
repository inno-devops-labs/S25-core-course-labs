# Docker Role

This role deploys web application given a docker image.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Dependencies

Depends on the `docker` role.

## Tasks

- Everything that the `docker` role does
- Deploys given docker images using docker compose

## Role Variables

- `docker_image`: Docker image to deploy
- `app_port`: Port to expose the web application on
- `web_app_full_wipe`: Whether to wipe the web application before deploying

## Example Playbook

```yaml
- name: Python app playbook
  hosts: all
  vars:
    docker_image: "nai1ka/time-service-cicd:latest"
    app_port: 8000 
    web_app_full_wipe: false
  roles:
    - web_app
```
