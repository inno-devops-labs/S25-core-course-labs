# Docker Role

This Ansible role installs and configures Docker and Docker Compose on Ubuntu systems.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (Focal Fossa)
- Python 3.x

## Role Variables

Available variables are listed below, along with default values:

```yaml
docker_compose_version: "v2.24.5"  # Version of Docker Compose to install
```

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
```

## Usage

1. Include the role in your playbook:
```yaml
- name: Install Docker
  hosts: your_servers
  roles:
    - docker
```

2. Run the playbook:
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```

3. Verify installation:
```bash
ansible all -i inventory/default_aws_ec2.yml -m shell -a "docker --version"
```

## Role Tasks

The role performs the following main tasks:

1. Installs required system packages
2. Adds Docker repository and GPG key
3. Installs Docker CE and related packages
4. Ensures Docker service is running and enabled
5. Adds the current user to the docker group
6. Installs Docker Compose

## License

MIT