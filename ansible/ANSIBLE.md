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
    └── web_app/      # Web application deployment role
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

### Web Application Role

The Web Application role handles the deployment of Docker containers for web applications. This role handles:

- Pulling Docker images
- Creating and starting containers with proper configuration
- Setting resource limits and environment variables

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

## Web Application Deployment

### Role Variables

The following variables can be configured in `roles/web_app/defaults/main.yml`:
- `docker_image_name`: Name of your Docker image
- `docker_image_tag`: Tag of the Docker image
- `docker_container_name`: Name for the deployed container
- `container_ports`: Port mappings
- `container_env`: Environment variables
- `restart_policy`: Container restart policy
- `memory_limit`: Container memory limit
- `cpu_limit`: Container CPU limit

### Deployment

To deploy the web application, run:

```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags web_app
```

The deployment output will be updated here after the first successful deployment.
