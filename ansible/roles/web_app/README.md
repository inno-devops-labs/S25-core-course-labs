# Web App Role

This role deploys the flask-app's Docker image using Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 or compatible

## Role Variables

- `docker_image`: The Docker image to deploy (default: "synavtora/flaskapp:latest").
- `app_port`: The port on which the application will be exposed (default: 5000).
- `web_app_full_wipe`: Bool variable to enable or disable the wipe logic (default: false).

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: web_app
