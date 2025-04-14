# Role Name

The `docker` role allows you to deploy Docker on the server.
It installs Docker and Docker Compose with necessary dependencies included.
Also it configures Docker security settings (disable root access).

## Requirements

- Ansible 2.18.2+
- Python 3.12+
- Ubuntu 24.04

## Role Variables

None.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
      become: true
```
