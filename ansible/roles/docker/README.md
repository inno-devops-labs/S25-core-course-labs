# Web App Role

This role installs and configures a web application.

## Requirements

- Ansible 2.17+
- Ubuntu 22.04+

## Role Variables

- `docker_image`: The Docker image to use (default: "darrpyy/devops").
- `docker_container`: The name of the Docker container (default: "py-app").
- `docker_compose_file_name`: The name of the Docker Compose file (default: "docker-compose.yml").
- `internal_port`: The internal port of the application (default: "5000").
- `external_port`: The external port of the application (default: "80").
- `app_dir`: The directory of the application (default: "/app").
- `app_wipe`: Whether to wipe the application (default: "true").

## Example Playbook

```yaml
- name: Deployment python application
  roles:
    - name: web app
      vars:
        docker_image: "darrpyy/devops"
        docker_container: "py-app"
        docker_compose_file_name: "docker-compose.yml"

        internal_port: 5000
        external_port: 8001

        app_dir: "/app"
        app_wipe: true
```
## Dependencies
This role depends on the `docker` role.