# WebApp Role

This role installs `unileonid/time-app-py` Docker image and starts it. It depends on `docker` role and some of its variables.

## Requirements

- Ansible 2.16+
- Ubuntu 24.04 (stable) (by default)

## Role Variables

- `time_app_version`: (default: `latest`)
- `time_app_docker_container_name`: (default: `unileonid_time_app_py`)
- `time_app_external_port`: (default: `8080`)
- `time_app_wipe_container`: (default: `false`)
- `time_app_docker_compose_path`: (default: `/home/{{ docker_user }}/docker-compose.yml`)


## Example Playbook

```yaml
- hosts: all
  roles:
  - role: web_app
```
