
# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17+ 
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `latest`).

## Playbook for local deployment

```yaml
    - name: Deploy Docker using Ansible
    hosts: all
    become: true
    roles:
        - docker
```

## Playbook for yandex deployment

Required: 
- install the plugin yacloud_compute.py (https://github.com/rodion-goritskov/yacloud_compute)

```yaml
    all:
        hosts:
            compute-lab5-1: # vm machine name in yandex cloud 
            ansible_host: 84.201.151.82 # ip your VM
            ansible_user: ivangeliev # your yandex profile name 
            yacloud_token_file: ./inventory/authorized_key.json # path to the downloaded from yandex cloud json key for VM access
            plugin: yacloud_compute # plugin path 
```

# Customize the startup of the desired project 
There are two projects to choose from to run: 
1. python web app
2. golang web app

Before you run them, you can specify the necessary settings in the main.yaml file of both projects. To do this, you need to go to `playbooks/dev/app_python` or `playbooks/dev/app_golang`. 
```yaml
- name: Deploy Docker using Ansible
  hosts: all
  become: true
  roles:
    - web_app
  vars:
    docker_image: "lekski/python-web-app:latest"
    container_port: "80"
    container_name: "python_web_app"
```
vars block is the same for both projects. Here you can select the port on which web_app will run (default 80), the docker_image to be used, and the name of the container to be created. 

If necessary, you can also make changes to `roles/web_app/defaults/main.yaml: 
```yaml
---
    docker_compose_dest: "/home/web_app/docker-compose.yml"
    docker_compose_dir: "/home/web_app"
    app_wipe: false
    exposed_port: "8000"
```
- docker_compose_dest and docker_compose_dir are used as paths where docker-compose is located and where it will be created, you can change them if you wish. 
- app_wipe is used to stop and delete a running docker container without having to specify the wipe tag, but I prefer to specify the wipe tag rather than change the value here. 
- exposed_port is the port on which the application in the docker container is started. Both of the projects shown here run on port 8000. 
  
This is the end of the configuration and the project can be started: 
```bash 
ansible-playbook -i ansible/inventory/yandex_inventory.yaml ansible/playbooks/dev/{{web_app name}}/main.yaml --tags docker -K
``` 
To stop and remove the docker container: 
```bash 
ansible-playbook -i ansible/inventory/yandex_inventory.yaml ansible/playbooks/dev/app_python/main.yaml --tags wipe -K
```
