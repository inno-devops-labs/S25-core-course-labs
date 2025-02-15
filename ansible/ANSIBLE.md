# Ansible Documentation

This document describes the Ansible configuration and usage for the project.

## Overview

This Ansible setup is designed to:
1. Install and configure Docker on target systems
2. Support both local development (macOS) and production (Ubuntu) environments
3. Provide a foundation for web application deployment

## Directory Structure

```
ansible/
├── ANSIBLE.md               # Main documentation
├── ansible.cfg             # Ansible configuration
├── inventory/
│   └── default_aws_ec2.yml # Inventory file for hosts
├── playbooks/
│   └── dev/
│       └── main.yaml      # Main playbook for deployment
└── roles/
    ├── docker/            # Docker installation role
    │   ├── README.md     # Role documentation
    │   ├── defaults/
    │   │   └── main.yml  # Default variables
    │   ├── handlers/
    │   │   └── main.yml  # Handlers for service restart
    │   └── tasks/
    │       ├── install_compose.yml  # Docker Compose installation
    │       ├── install_docker.yml   # Docker installation
    │       └── main.yml            # Main task file
    └── web_app/           # Web application deployment role (to be implemented)
        ├── defaults/
        │   └── main.yml
        ├── handlers/
        │   └── main.yml
        ├── meta/
        │   └── main.yml
        ├── tasks/
        │   └── main.yml
        └── templates/
            └── docker-compose.yml.j2
```

## Configuration

The `ansible.cfg` file contains the following settings:
```ini
[defaults]
inventory = ./inventory/default_aws_ec2.yml
remote_user = ubuntu
host_key_checking = False
private_key_file = ~/.ssh/id_rsa
roles_path = ./roles
localhost_warning = False

[privilege_escalation]
become = true
become_method = sudo
become_user = root
become_ask_pass = false
```

## Inventory Structure

The inventory is configured in `inventory/default_aws_ec2.yml` with the following structure:

```yaml
---
all:
  children:
    local:
      hosts:
        localhost:
          ansible_connection: local
          ansible_python_interpreter: /opt/homebrew/bin/python3
          ansible_become_password: "{{ lookup('env', 'ANSIBLE_SUDO_PASS') }}"
```

Current inventory visualization:
```
# Inventory Graph
@all:
  |--@ungrouped:
  |--@local:
  |  |--localhost

# Inventory List
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_become_password": "{{ lookup('env', 'ANSIBLE_SUDO_PASS') }}",
                "ansible_connection": "local",
                "ansible_python_interpreter": "/opt/homebrew/bin/python3"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "local"
        ]
    },
    "local": {
        "hosts": [
            "localhost"
        ]
    }
}
```

## Roles

### Docker Role

The Docker role installs and configures Docker and Docker Compose. Key features:
- Cross-platform support (Ubuntu and macOS)
- Docker daemon configuration (Linux)
- User permission management
- Docker Compose installation
- Service management

For detailed information, see [Docker Role README](roles/docker/README.md)

## Usage

### Prerequisites
1. Ansible 2.9+ installed
2. For macOS local development:
   - Homebrew installed
   - ANSIBLE_SUDO_PASS environment variable set:
     ```bash
     export ANSIBLE_SUDO_PASS='your_sudo_password'
     ```
3. For Ubuntu deployment:
   - SSH key configured
   - Target host accessible

### Running Playbooks

```bash
# Set sudo password for local development
export ANSIBLE_SUDO_PASS='your_sudo_password'

# Validate inventory
ansible-inventory -i inventory/default_aws_ec2.yml --graph
ansible-inventory -i inventory/default_aws_ec2.yml --list

# Test connectivity (with sudo password)
ANSIBLE_BECOME_PASS=$ANSIBLE_SUDO_PASS ansible all -m ping

# Dry run with diff
ANSIBLE_BECOME_PASS=$ANSIBLE_SUDO_PASS ansible-playbook playbooks/dev/main.yaml --check --diff

# Actual deployment
ANSIBLE_BECOME_PASS=$ANSIBLE_SUDO_PASS ansible-playbook playbooks/dev/main.yaml
```

### Deployment to EC2

To deploy to EC2:
1. Update inventory file with EC2 instance details:
```yaml
all:
  children:
    webservers:
      hosts:
        ec2_instance:
          ansible_host: YOUR_EC2_IP
          ansible_user: ubuntu
          ansible_ssh_private_key_file: ~/.ssh/your-key.pem
```
2. Ensure SSH key permissions are correct (`chmod 600`)
3. Test connectivity and deploy

## Troubleshooting

Common issues and solutions:
1. Sudo password issues:
   - Set ANSIBLE_SUDO_PASS environment variable
   - Use ANSIBLE_BECOME_PASS for command execution
   - Check become_ask_pass setting
2. SSH connection issues:
   - Verify SSH key permissions
   - Check host connectivity
   - Ensure proper security group rules
3. Docker installation issues:
   - Check system requirements
   - Verify internet connectivity
   - Check available disk space 

## Example Playbook Execution

Here's an example of running the playbook in check mode:

```
PLAY [Deploy Docker and Web Application] ****************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [localhost]

TASK [docker : Include Docker installation tasks] *******************************************************
included: /Users/nikitadrozdov/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Check if running on macOS] ***************************************************************
ok: [localhost]

TASK [docker : Check if Docker Desktop is installed] ****************************************************
ok: [localhost]

TASK [docker : Install Docker Desktop using Homebrew] ***************************************************
skipping: [localhost]

TASK [docker : Install required system packages] ********************************************************
skipping: [localhost]

TASK [docker : Add Docker GPG apt Key] ******************************************************************
skipping: [localhost]

TASK [docker : Add Docker Repository] *******************************************************************
skipping: [localhost]

TASK [docker : Install Docker] **************************************************************************
skipping: [localhost]

TASK [docker : Ensure Docker service is enabled and started] ********************************************
skipping: [localhost]

TASK [docker : Add users to docker group] ***************************************************************
skipping: [localhost] => (item=root) 
skipping: [localhost]

TASK [docker : Include Docker Compose installation tasks] ***********************************************
included: /Users/nikitadrozdov/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Check if running on macOS] ***************************************************************
ok: [localhost]

TASK [docker : Install Docker Compose] ******************************************************************
skipping: [localhost]

TASK [docker : Create docker config directory] **********************************************************
skipping: [localhost]

TASK [docker : Configure Docker daemon] *****************************************************************
skipping: [localhost]

TASK [docker : Check if Docker Compose is installed] ****************************************************
skipping: [localhost]

TASK [docker : Install Docker Compose using Homebrew] ***************************************************
skipping: [localhost]

PLAY RECAP **********************************************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
```

This output shows:
1. Successful fact gathering
2. Proper detection of macOS environment
3. Skipping of Ubuntu-specific tasks
4. No changes needed (Docker already installed)
5. All tasks executed without errors 

## Latest Deployment Output

```bash
PLAY [Deploy Docker and Web Application] ***********************************************

TASK [Gathering Facts] *****************************************************************
ok: [localhost]

TASK [web_app : Create application directory] ******************************************
ok: [localhost]

TASK [web_app : Deploy docker-compose file] ********************************************
changed: [localhost]

TASK [web_app : Pull and start application] ********************************************
changed: [localhost]

PLAY RECAP *****************************************************************************
localhost                  : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

The deployment was successful with:
- 4 tasks completed successfully
- 2 tasks resulted in changes
- No failures or errors
- Application successfully deployed and running on port 8080

## Accessing the Application

The web application is accessible at:
- URL: http://localhost:8080
- Image: droznik/moscow-time
- Container name: web_app-app-1

## Running Deployments

To deploy the application:
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags deploy
```

To wipe and redeploy:
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags wipe,deploy -e "web_app_full_wipe=true"
``` 