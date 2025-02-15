# Web App Role

The role deploys web app using Docker Compose on the virtual machine.

## Requirements

- Ansible 2.17+
- Ubuntu 24.04
- `docker` role

## Role Variables

- `docker_image`: Web app image from Docker Hub (default: `bugay/python-msk-time-app-distroless:1.0`)
- `docker_container`: Web app container name (default: `python-web-app`)
- `docker_compose_filename`: Docker Compose file name (default: `docker-compose.yml`)
- `web_app_dir`: Webb app root directory (default: `/webapp`)
- `internal_port`: Web app internal port (default: `5000`)
- `external_port`: Web app external port (default: `5000`)
- `web_app_full_wipe`: Flag for wipe (default: `true`)

## Example Playbook

```yaml
- name: Deploy python web app
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        docker_image: "bugay/python-msk-time-app-distroless:1.0"
        docker_container: "python-web-app"
        docker_compose_filename: "docker-compose.yml"

        web_app_dir: "/webapp"

        internal_port: 5000
        external_port: 5000

        web_app_full_wipe: true
```
