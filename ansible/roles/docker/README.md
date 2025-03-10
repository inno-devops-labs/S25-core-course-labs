# Docker Role

This role installs and configures **Docker** and **Docker Compose** on a target machine using Ansible.

## Requirements

- Ansible **2.9+**
- Target OS: **Ubuntu 22.04** (may work with other Debian-based distributions)

## Role Variables

| Variable                 | Default  | Description                               |
| ------------------------ | -------- | ----------------------------------------- |
| `docker_version`         | `latest` | The version of Docker to install.         |
| `docker_compose_version` | `1.29.2` | The version of Docker Compose to install. |

## Tasks Performed by This Role

- Installs **Docker CE** and **Docker Compose**.
- Enables Docker service to **start on boot**.
- Adds the **current user to the `docker` group** (to avoid using `sudo`).

## Example Playbook Usage

To use this role, include it in your playbook:

```
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker
```

## Usage Instructions

1. Ensure **Ansible** is installed.
2. Add this role to your **playbook**.
3. Override any variables (if necessary) by passing `-extra-vars` in the CLI or using `group_vars`.
4. Run the playbook:

   ```
   ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
   ```
