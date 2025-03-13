# Docker Role

## Description

This Ansible role installs and configures Docker and Docker Compose on Ubuntu-based systems.

## Requirements

- Ubuntu 22.04+
- Ansible 2.9+
- sudo privileges

## Role Variables

| Variable                 | Default Value  | Description |
|--------------------------|---------------|-------------|
| `docker_version`         | `latest`      | Docker version to install |
| `docker_compose_version` | `1.29.2`      | Docker Compose version to install |
| `ansible_distribution_release` | `jammy` | Ubuntu distribution release name |
| `ansible_user`           | Current user  | The user to be added to the Docker group |

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: docker
```

## Running the Playbook

Move to ansible folder:

```sh
cd ansible
```

Execute the following command:

```sh
ansible-playbook -i inventory/localhost.yml playbooks/dev/main.yml --ask-become-pass --diff
```

--ask-become-pass is used to provide a password to sudo, after running the command write the password

For a dry run:

```sh
ansible-playbook -i inventory/localhost.yml playbooks/dev/main.yml --ask-become-pass --check
```

## Verifying the Installation

After running the playbook, check if Docker is installed:

```sh
docker --version
```

Check Docker Compose version:

```sh
docker-compose --version
```
