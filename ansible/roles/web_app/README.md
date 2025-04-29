# Docker Role

Deploys app_python with docker-compose

## Requirements

- Ubuntu latest
- Ansible 2.18.2

## Example Playbook

```yaml
- name: example-playbook
  hosts: all
  become: yes
  roles:
    - docker
    - web_app
  vars:
    ansible_user: ubuntu
    app_directory: app_python
    app_image: atkond/flask-app
    app_port: 5000
    web_app_full_wipe: true
```
