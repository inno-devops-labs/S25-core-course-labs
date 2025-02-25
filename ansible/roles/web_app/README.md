# Web App Role

This role installs and configures a web application.

## Requirements

- Ansible 2.17+
- Ubuntu 22.04+

## Role Variables

- `docker_image`: The Docker image to use (default: "azamatbayramov/s25-devops-py-dl:latest").
- `docker_container`: The name of the Docker container (default: "py-app").
- `docker_compose_file_name`: The name of the Docker Compose file (default: "docker-compose.yml").
- `internal_port`: The internal port of the application (default: "8001").
- `external_port`: The external port of the application (default: "80").
- `app_dir`: The directory of the application (default: "/app").
- `app_wipe`: Whether to wipe the application (default: "true").

## Example Playbook

```yaml
- name: Deploy Go App
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        docker_image: "azamatbayramov/s25-devops-go-dl:latest"
        docker_container: "go-app"
        docker_compose_file_name: "docker-compose.yml"

        internal_port: 8002
        external_port: 8002

        app_dir: "/app"
        app_wipe: true
```

## Dependencies

This role depends on the `docker` role.
