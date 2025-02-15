# Web App Role

This Ansible role deploys a web application using Docker and Docker Compose.

## Requirements
- Ansible 2.9+
- Docker installed on the target machine

## Variables

- `app_directory`: Directory where the application is stored.
- `app_image`: Docker image to be used.
- `app_port`: Port for the application.

## Example Playbook

```yaml
- name: Deploy Web Application
  hosts: all
  become: yes
  roles:
    - web_app
