# Custom `web_app` Ansible role

This role will install a web application Docker image on the host

## Requires

- Docker role

## Usage

```
- name: Example web_app usage
  hosts: all
  become: true
  roles:
    - role: web_app
      image: alexstrnik/python-app:latest
      ports:
        - 8080:5000
```
