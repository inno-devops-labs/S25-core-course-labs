# Web App Role

This role deploys the web application's Docker image using Docker Compose.

## Requirements

- Ansible 2.9 or higher
- Ubuntu 22.04 or compatible
- Python 3.8 with pip3

## Role Variables
- `docker_image`: Name of the Docker image
- `app_port`: The port (5000) the application will be exposed
- `web_app_full_wipe`: Flag for the wipe logic (default: false)

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: web_app