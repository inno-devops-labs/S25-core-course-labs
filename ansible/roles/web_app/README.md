# Docker Role

This role deploys application on virtual machine. It has three tags:

`setup` - for whole setup of application (default)

`deploy` - create application directory and up docker compose

`wipe` - remove containers and application directory

## Requirements

- Ansible 2.17.7
- Ubuntu 24.04

## Role Variables

`internal_port`: port for application

`docker_image`: which image to use in docker compose

`web_app_full_wipe`: flag for enabling or disabling wiping process

`web_app_dir`: application directory

## Example Playbook

```yaml
- name: Deploy python app
  hosts: all
  become: true
  roles:
    - web_app
  vars:
    - web_app_full_wipe: true
```
