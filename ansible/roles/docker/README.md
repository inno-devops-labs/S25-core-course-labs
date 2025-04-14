# Docker Role

This Ansible role automates the installation and configuration of Docker and Docker Compose on Ubuntu-based systems.

---

## Requirements

- **Ansible** 2.9 or later  
- **Ubuntu** 22.04 LTS  
- **Python** 3.x installed on the target machine  

---

## Role Variables

```yaml
docker_compose_version: "v2.24.5"  # Specifying the Docker Compose version to be installed
```

---

## Dependencies
This role has no external dependencies.

---

## Usage Example
1) Adding the Role to the Playbook
```yaml
- name: Setup Docker
  hosts: target_servers
  roles:
    - docker
```

2) Running the Playbook
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```

3) Verifying the Installation
```bash
ansible all -i inventory/default_aws_ec2.yml -m shell -a "docker --version"
```

---

## Role Execution Steps
This role performs the following setup operations:
1) Installing required system dependencies
2) Adding the official Docker repository and its GPG key
3) Installing Docker CE and necessary components
4) Ensuring the Docker service is enabled and running
5) Adding the executing user to the docker group for permission management
6) Installing Docker Compose for managing multi-container applications
