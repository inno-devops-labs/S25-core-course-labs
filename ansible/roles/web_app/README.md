# Web App Role

This role enables pulling Docker image of Web App, setting a container
from it, starting it. It also generates a Docker Compose config.
Using Wipe tasks (tag `wipe` and `web_app_full_wipe=true`) one
can delete created container and docker-compose file.

## Requirements for the hosts

- Ubuntu 22.04 Jammy
- Docker and Docker Compose (`docker` role inherited and can be used to set it up)
- Python 3+

## Role Variables

- `web_app_docker_image` is the name of webapp image used
- `web_app_docker_image_tag` is the tag of the webapp image
- `web_app_container_name` is the resulting name of the running container
- `web_app_container_port` the port that is being listened from the container by app 
- `web_app_port` the port opened on VM
- `web_app_full_wipe` (default is `false`) enables removal of generated container as well as Docker Compose file.

## Usage

```yaml
- hosts: all
- roles:
    - role: web_app 
      become: true
```
