# Web App role

This role install docker, docker compose and deploys the application

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `app_image`: Image name for deployments
- `image_tag`: Spicific image tag
- `container_name`: Name of the container to run the app
- `app_ports`: Ports between host and container
- `restart_policy`: Restart policy for constainer
- `web_app_full_wipe`: Wipe the data or not (true/false)
- `app_install_dir`: Directory to install the application

## Example Playbook

```yaml
- name: Deploy application
  hosts: all
  become: true
  roles:
    - web_app
```
