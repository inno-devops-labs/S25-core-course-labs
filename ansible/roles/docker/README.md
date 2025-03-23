```markdown
# Docker Role

Installs Docker and Docker Compose on Ubuntu systems.

## Requirements
- Ansible 2.9+
- Ubuntu 22.04/20.04

## Variables
 - `docker_version` : latest
 - `docker_compose_version`: v2.32.4

## Example Playbook
```yaml
- name: Install Docker and Docker Compose
  hosts: all
  become: yes
  roles:
    - role: ../../roles/docker
```