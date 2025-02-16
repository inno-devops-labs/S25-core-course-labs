# Docker Role

Installs and configures Docker with Docker Compose plugin

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
```
