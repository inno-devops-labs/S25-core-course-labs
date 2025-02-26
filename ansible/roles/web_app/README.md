# Web App Role
This role allows to extract the image of Docker application Moscow Time on Python, run container for it. It also generates a Docker Compose configuration. Using the Wipe tasks (tag wipe and web_app_full_wipe=true) you can remove the created container and docker-compose.

## Requirements for the hosts
* Ubuntu 22.04
* Docker and Docker Compose (easy to set up with the usage of role `docker`)
* Python 3+
* 
## Role Variables
* `web_app_docker_image` is the name of webapp image used
* `web_app_docker_image_tag` is the tag of the webapp image
* `web_app_container_name` is the resulting name of the running container
* `web_app_container_port` the port that is being listened from the container by app
* `web_app_port the port` opened on VM
* `web_app_full_wipe` (default is `false`) enables removal of generated container as well as Docker Compose file.

## Usage
```
- hosts: all
- roles:
    - role: web_app 
      become: true
```
