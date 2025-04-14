# Web App Role

This role deploys your application's Docker image using Docker Compose. It is designed to integrate into a Continuous Deployment (CD) process, allowing you to easily update and roll out your application container.

## Requirements

- Ansible 2.18
- Ubuntu 22.04

## Role Variables

- **`app_port`**: The port mapping for your application (default: `8080`).
- **`web_app_full_wipe`**: Boolean flag to enable wipe logic (default: `false`).

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: web_app
