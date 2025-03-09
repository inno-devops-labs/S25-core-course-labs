# Web Application Role

The good ol role for deploying an application with docker compose

## Requirements

- Ubuntu 24.04
- Ansible 2.17+
- Docker + Docker Compose (`docker` role)

## Role Variables

- `docker_image`: Web application image to use from Docker Hub
- - default: `gendiro/moscow-time-app:latest`
- `docker_container`: Web application container name
- - default: `moscow-time-app`
- `docker_compose_filename`: Docker Compose file name to use
- - default: `docker-compose.yml`
- `web_app_dir`: Where to put Docker Compose file
- - default: `/webapp`
- `internal_port`: Web application internal port
- - default: `8000`
- `external_port`: External port to use
- - default: `8000`
- `web_app_full_wipe`: Whether to perform wipe
- - default: `true`

## Example Playbook

```yaml
- name: Deploy Moscow Time App (Python)
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        docker_image: "gendiro/moscow-time-app:latest"
        docker_container: "moscow-time-app"
        docker_compose_filename: "docker-compose.yml"

        web_app_dir: "/webapp"

        internal_port: 8000
        external_port: 8000

        web_app_full_wipe: true

```
