Deploy web app
=========

Role for deployment devops web_app

Requirements
------------

- docker.community - tasks to operate docker

Role Variables
--------------

- `docker_image: "wensiet/devops-py-app"` - docker image name
- `docker_tag: "latest"` - tag that will be used for deployment
- `internal_port: 8000` - internal application port
- `external_port: 8000` - port that will be expose by docker compose

Dependencies
------------

- ./roles/docker - role to install docker

Example Playbook
----------------

```ansible
- name: Deploy web app
  hosts: all
  become: true
  roles:
    - web_app
```

