# Web Application Role

This Ansible role deploys a web application using Docker Compose.

## Requirements

- Docker
- Docker Compose
- Ansible 2.9+

## Role Dependencies

- docker role

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| docker_image | "your-docker-image:latest" | Docker image to deploy |
| app_port | 8080 | Application port to expose |
| web_app_full_wipe | false | Enable/disable full wipe of the application |
| docker_compose_dir | "/opt/web_app" | Directory for docker-compose files |
| docker_compose_file | "docker-compose.yml" | Name of docker-compose file |

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: web_app
      vars:
        docker_image: "droznik/moscow-time"
        app_port: 8080
```

## Tags

- `wipe`: Remove containers and application files
- `setup`: Configure application environment
- `deploy`: Deploy or update the application

## Usage

Regular deployment:
```bash
ansible-playbook playbook.yml --tags deploy
```

Wipe and redeploy:
```bash
ansible-playbook playbook.yml --tags wipe,deploy -e "web_app_full_wipe=true"
``` 