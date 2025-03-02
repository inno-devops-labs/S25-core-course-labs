# Ansible Configuration Documentation

This document provides information about the Ansible configuration used in this project for deploying Docker to AWS EC2 instances.

## Prerequisites

1. Install Ansible and required dependencies:
```bash
pip install ansible boto3
```

2. Configure AWS credentials in `~/.aws/credentials` or as environment variables:
```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

## Configuration Details

### Ansible Configuration (`ansible.cfg`)
```ini
[defaults]
inventory = inventory/default_aws_ec2.yml
roles_path = roles
host_key_checking = False
remote_user = ubuntu
private_key_file = ~/.ssh/id_rsa

[privilege_escalation]
become = True
become_method = sudo
become_user = root
become_ask_pass = False
```

### Dynamic Inventory Configuration
The project uses AWS EC2 dynamic inventory (`default_aws_ec2.yml`):
```yaml
plugin: aws_ec2
regions:
  - us-west-2  # Adjust this to your AWS region
filters:
  instance-state-name: running
  tag:Environment: dev
keyed_groups:
  - key: tags.Environment
    prefix: env
  - key: tags.Role
    prefix: role
compose:
  ansible_host: public_ip_address
```

## Usage

### Verify Inventory
```bash
# List all hosts
ansible-inventory -i inventory/default_aws_ec2.yml --list

# Show inventory graph
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

### Running Playbooks

1. Perform a dry run (check mode):
```bash
ansible-playbook playbooks/dev/main.yaml --check
```

2. Run the playbook with diff mode to see changes:
```bash
ansible-playbook playbooks/dev/main.yaml --diff
```

3. Run the playbook normally:
```bash
ansible-playbook playbooks/dev/main.yaml
```

## Roles

### Docker Role
The Docker role installs and configures Docker and Docker Compose on Ubuntu systems. See [Docker Role README](roles/docker/README.md) for detailed documentation.

Key features:
- Installs Docker CE and Docker Compose
- Configures Docker to start on boot
- Adds the specified user to the Docker group
- Handles service restart when needed

## Deployment Output
```bash
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Deploy Docker to EC2 instances] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [ec2-instance]

TASK [docker : Install required system packages] ********************************
changed: [ec2-instance]

TASK [docker : Add Docker GPG key] *********************************************
changed: [ec2-instance]

TASK [docker : Add Docker repository] ******************************************
changed: [ec2-instance]

TASK [docker : Install Docker] ************************************************
changed: [ec2-instance]

TASK [docker : Ensure Docker service is enabled and started] *******************
changed: [ec2-instance]

TASK [docker : Add user to docker group] **************************************
changed: [ec2-instance]

TASK [docker : Install Docker Compose] ****************************************
changed: [ec2-instance]

PLAY RECAP *******************************************************************
ec2-instance              : ok=8    changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Output
```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@aws_ec2:
  |  |--@env_dev:
  |  |  |--ec2-instance
  |--@ungrouped:
```

## Web Application Deployment Output
```bash
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Deploy Docker and Web Application to EC2 instances] ***********************

TASK [Gathering Facts] *********************************************************
ok: [ec2-instance]

TASK [web_app : Include wipe tasks] ********************************************
skipped: [ec2-instance]

TASK [web_app : Setup application environment] *********************************
ok: [ec2-instance] => (item=Create application directory)
changed: [ec2-instance] => (item=Copy Docker Compose template)
changed: [ec2-instance] => (item=Create .env file)

TASK [web_app : Deploy application] *******************************************
changed: [ec2-instance] => (item=Pull Docker images)
changed: [ec2-instance] => (item=Deploy application with Docker Compose)

TASK [web_app : Health check] ************************************************
ok: [ec2-instance]

PLAY RECAP *******************************************************************
ec2-instance              : ok=5    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## Troubleshooting

1. If the playbook fails with AWS connectivity issues:
   - Verify AWS credentials are properly configured
   - Check if the specified region matches your EC2 instances
   - Ensure the instances have the correct tags

2. If Docker installation fails:
   - Check system requirements are met
   - Verify internet connectivity on target instances
   - Ensure proper sudo privileges

3. If Docker Compose installation fails:
   - Check if the specified version exists
   - Verify download URL is accessible
   - Check available disk space

## Security Considerations

1. AWS credentials are stored securely
2. SSH keys are used for authentication
3. Sudo privileges are configured properly
4. Docker group membership is managed securely 
