# Web App Role

   This role deploys a Docker container for the web application.

## Requirements

- Ansible 2.9+
- The `docker` role must be available as this role depends on it.
- Ubuntu 22.04

## Role Variables

- `docker_image`: The Docker image to deploy.
- `container_name`: Name of the container.
- `host_port`: Port on the host for direct container mapping.
- `container_port`: Container's internal port.
- `app_port`: Port used in the docker-compose file.
- `restart_policy`: Restart policy for the container.
- `web_app_full_wipe`: Set to `true` to enable wipe logic (removes container and deployment files).

## Dependencies

This role depends on the `docker` role which is defined in the meta file.

## Example Playbook

```yaml
  - name: Deploy application with Docker container
  hosts: all
  become: true
  roles:
    - docker
    - web_app
```
