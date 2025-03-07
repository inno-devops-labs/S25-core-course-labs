# Docker Role

This role used to deploy web app using docker compose

## Requirements

- Ansible 2.17.8
- Ubuntu any version
  Has dependencies with Docker role from previous lab

## Example Playbook

```yaml
- name: Playbook
  hosts: all
  become: yes
  roles:
    - docker
    - web_app
  vars:
    ansible_user: ubuntu
    app_directory: app_python
    app_image: dsaee/app
    app_port: 8000
    web_app_full_wipe: true
```
