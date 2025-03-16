# Docker Role

This role runs an applicationn using either docker or docker-compose

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_image`: The image to run (default: `tedor49/python_msk_time:latest`)
- `dockerhub_username`: DockerHub username (gets from HUB_USER env variable by default)
- `dockerhub_password`: DockerHub password (gets from HUB_PASS env variable by default)
- `deploy_type`: Runs the image with either just docker (`docker`) or docker-compose(`compose`) (default: `docker`)
- `web_app_full_wipe`: when true, all images and deployments will be wiped (default: false)

## Example Playbook

```yaml
- hosts: all

  roles:
    - roles/docker	
    - roles/web_app
```
