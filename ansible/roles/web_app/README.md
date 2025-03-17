# Web Application Deployment Role

This Ansible role is designed to deploy and manage a web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9 or later  
- Ubuntu 22.04  
- Docker (installed as a dependency via the docker role)  
- Docker Compose  

## Role Variables

- `app_directory`: The location where the web application will be deployed (default: `/opt/web_app`).
- `docker_image`: The Docker image to be used for deployment (must be specified).
- `app_port`: The port on which the application will be accessible (default: `8080`).
- `web_app_full_wipe`: Determines if the application should be fully removed during cleanup (default: `false`).

## Dependencies

- `docker` role

## Example Playbook

```yaml
- hosts: all
  vars:
    docker_image: user/webapp:latest
    app_port: 8080
  roles:
    - role: web_app
```

## Tags
- `setup` – Initial setup tasks
- `docker` – Docker tasks
- `deploy` – Application deployment tasks
- `wipe` – Full wipe process (only runs when web_app_full_wipe=true)

## Usage

`Standard Deployment`:
```bash
ansible-playbook playbooks/dev/main.yaml
```

`Deployment with full wipe`:
```bash
ansible-playbook playbooks/dev/main.yaml -e "web_app_full_wipe=true"
```

`Running Specific Tags`:
```bash
ansible-playbook playbooks/dev/main.yaml --tags "setup,deploy"
```
