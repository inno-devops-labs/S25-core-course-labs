# Ansible Configuration and Documentation

## Project Structure

```
ansible/
├── ansible.cfg         # Ansible configuration file
├── inventory/         # Inventory directory
│   └── default_aws_ec2.yml  # AWS EC2 dynamic inventory
├── playbooks/         # Playbook directory
│   └── dev/
│       └── main.yaml  # Main deployment playbook
└── roles/            # Roles directory
    ├── docker/       # Docker installation and configuration role
```

## Configuration

The project uses a standard Ansible configuration located in `ansible.cfg`:

- Inventory directory: `inventory/`
- Playbooks directory: `playbooks/`
- Roles path: `roles/`
- Remote user: `whatislav`

## Inventory

The project uses AWS EC2 dynamic inventory (`default_aws_ec2.yml`) to automatically discover and manage instances.

## Roles

### Docker Role

The Docker role handles the installation and configuration of Docker and Docker Compose on target hosts. It includes:

- Installation of Docker Engine
- Installation of Docker Compose
- Security configurations
- System configurations for Docker
- Docker service management

## Playbooks

### Main Deployment Playbook

Location: `playbooks/dev/main.yaml`

This playbook orchestrates the full deployment process:
- Installs and configures Docker
- Deploys the web application
- Applies necessary configurations

## Usage

### Prerequisites

1. Ansible installed on the control node
2. AWS credentials configured (for EC2 dynamic inventory)
3. SSH access to target hosts

### Running Playbooks

To run the main deployment playbook:

```bash
ansible-playbook playbooks/dev/main.yaml
```

### Tags

Different tags can be used to run specific parts of the playbooks:

```bash
# Run only Docker installation
ansible-playbook playbooks/dev/main.yaml --tags docker
```

## Best Practices

1. Always use roles for modular and reusable configurations
2. Keep sensitive information in encrypted files using ansible-vault
3. Use tags for selective execution of tasks
4. Maintain proper documentation for roles and playbooks
5. Follow idempotency principles in all tasks
