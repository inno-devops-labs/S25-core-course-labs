# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17.8
- Ubuntu any version

## Example Playbook

```yaml
- name: Playbook
  hosts: all
  become: yes
  roles:
    - docker
    # - geerlingguy.docker
```
