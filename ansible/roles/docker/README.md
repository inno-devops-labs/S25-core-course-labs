# Docker Role

 This role installs and configures Docker and Docker Compose.

## Requirements

- Ubuntu latest
- Ansible 2.18.2

## Example Playbook

```yaml
- name: example-playbook
  hosts: all
  become: yes
  roles:
    - role: docker
```
