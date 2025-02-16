# Docker Role

This role deploy specific format of docker-compose.yml (for course web app) to host machine

## Requirements:

- Deployed `Docker role` on host

## How to use:

Just use the role, no extra actions required

```
- name: <Name of task>
  hosts: <Specified hosts or "all">
  become: true
  roles:
    - role: web_app
      image: <Name of image>:<tag>
      ports:
        - <port ext 1>:<port int 1>
        ...
        - <port ext n>:<port int n>
```
