Role Name
=========

This role deploys a Python web application using Docker containers

Requirements
------------
- Ansible 2.9+
- `community.docker` collection

Role Variables
--------------

| Variable | Default | Description |
|----------|---------|-------------|
| `web_app_image` | `emiliogain/my-python-app` | Docker image name |
| `web_app_image_tag` | `latest` | Image version tag |
| `web_app_container_name` | `python-app` | Container name |
| `web_app_ports` | `["8080:5000"]` | Port mappings |
| `web_app_restart_policy` | `unless-stopped` | Container restart policy |
| `app_install_dir` | `/opt/python-app` | Installation directory |
| `web_app_full_wipe` | `false` | Destroy all resources when true |


Dependencies
------------

- `docker` role (installs Docker engine)

Example Playbook
----------------

```yaml
- name: Install and Configure Docker, Run the Web App
  hosts: all
  become: true
  roles:
    - web_app
```

Wipe deployment:
```yaml
- name: Install and Configure Docker, Run the Web App
  hosts: all
  become: true
  roles:
    - role: web_app
  vars:
    web_app_full_wipe: true
  tags: wipe
```



License
-------

MIT-0


