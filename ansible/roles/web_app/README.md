# Web App Ansible Role

## Description
This role deploys a web application using Docker Compose.

## Requirements
- Ansible 2.9+
- Docker installed

## Variables
- `docker_image`: The image to deploy.
- `app_port`: The port to expose the application.

## Usage
```yaml
- hosts: all
- roles:
    - role: web_app 
      become: true
```
```sh
ansible-playbook site.yml
```
### Fow wipe
```sh
ansible-playbook site.yml --tags wipe
```
