# Ansible Web App role

## Description

This Ansible role deploys application Docker images on Ubuntu 22.04. It includes optional logic for wiping the application, which can be enabled in the playbook.

## Requirements

* This role depends on `docker` role, so `apt` must be pre-installed on the host machine.
* Configure variables in defaults.main.yml:

```shell
web_app_name: "web_app"
web_app_wipe: true
web_app_deploy: true
web_app_path: /app
web_app_port: 80
web_container_port: 8080
web_app_image: busybox
```

## Usage

Example of using `web_app` role for python-app deployment

```shell
- name: python_app
  hosts: all
  become: true
  become_method: 'sudo'
  roles:
    - name: web_app
      tags: [web_app-python]
      vars:
        web_app_name: app_python
        web_app_path: /app_python
        web_app_port: 8080
        web_container_port: 8080
        web_app_image: docker.io/maksalena/server-app:latest
```
