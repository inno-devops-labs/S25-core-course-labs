# Web App Role

This role deploys a Docker-based web application.

## Requirements
- Docker installed on the target machine.
- Ansible 2.9 or higher.

## Role Variables
- `docker_image`: The Docker image to deploy.
- `app_port`: The port to expose the application on.
- `web_app_full_wipe`: Whether to wipe the Docker environment (default: `false`).

## Example Playbook

```yaml
   - name: Deploy Docker
     hosts: all
     become: true
     roles:
       - webapp
