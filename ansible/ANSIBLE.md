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
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags docker

# Run only Docker image management
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags docker-image

# Run only container management
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags container

# Run full deployment
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --tags deploy
```

### Role Dependencies

The web_app role has been configured with the following dependencies:

- `docker`: Required for Docker engine and Docker Compose functionality

These dependencies are automatically handled through the role's meta/main.yml configuration.

### Task Organization

Tasks within roles are organized using logical blocks for better maintainability and clarity:

- Docker Image Management Block
  - Pull Docker image
  - Tags: docker-image, deploy

- Container Management Block
  - Create and start container
  - Configure container settings
  - Tags: container, deploy

This block-based organization allows for:
- Better error handling
- Logical grouping of related tasks
- Easier maintenance and debugging
- Selective execution using tags

## Best Practices

1. Always use roles for modular and reusable configurations
2. Keep sensitive information in encrypted files using ansible-vault
3. Use tags for selective execution of tasks
4. Maintain proper documentation for roles and playbooks
5. Follow idempotency principles in all tasks



$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Deploy Docker and Web Application] ***************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Check if Docker is already installed] ***************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Install required system packages] *******************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add Docker GPG apt Key] *****************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add Docker Repository] ******************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Install Docker] *************************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Create docker group if it doesn't exist] ************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Set correct permissions for Docker socket] **********************************************************************************************************************************
skipping: [my_vm]

TASK [docker : Configure Docker daemon directory] ******************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Enable Docker service on boot] **********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Ensure Docker daemon configuration directory exists] ************************************************************************************************************************
ok: [my_vm]

TASK [docker : Configure Docker daemon options] ********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Ensure Docker service is started and enabled] *******************************************************************************************************************************
ok: [my_vm]

TASK [docker : Ensure Docker users are added to Docker group] ******************************************************************************************************************************
ok: [my_vm] => (item=ubuntu)

TASK [docker : Install Docker Compose] *****************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Create Docker Compose symlink] **********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Check Docker service status] ************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Verify Docker service is running and enabled] *******************************************************************************************************************************
ok: [my_vm] => {
    "changed": false,
    "msg": "Docker service is properly configured and running"
}




TASK [docker : Verify Docker Compose installation] *****************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Display Docker Compose version] *********************************************************************************************************************************************
ok: [my_vm] => {
    "compose_version.stdout": "Docker Compose version v2.23.3"
}

TASK [docker : Verify user group membership] ***********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add to the Docker group] ****************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Disable root access] ********************************************************************************************************************************************************
--- before: /etc/docker/daemon.json
+++ after: /etc/docker/daemon.json
@@ -1,8 +1,3 @@
 {
-    "log-driver": "json-file",
-    "log-opts": {
-        "max-file": "3",
-        "max-size": "100m"
-    },
-    "storage-driver": "overlay2"
-}
\ No newline at end of file
+  "userns-remap": "default"
+}

changed: [my_vm]

TASK [docker : Activate Docker services] ***************************************************************************************************************************************************
ok: [my_vm]

RUNNING HANDLER [docker : restart docker] **************************************************************************************************************************************************
changed: [my_vm]

PLAY RECAP *********************************************************************************************************************************************************************************
my_vm                      : ok=24   changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0


$ ansible-playbook playbooks/dev/main.yaml --check

PLAY [Deploy Docker and Web Application] ***************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Check if Docker is already installed] ***************************************************************************************************************************************
skipping: [my_vm]

TASK [docker : Install required system packages] *******************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add Docker GPG apt Key] *****************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Add Docker Repository] ******************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Install Docker] *************************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Create docker group if it doesn't exist] ************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Set correct permissions for Docker socket] **********************************************************************************************************************************
skipping: [my_vm]

TASK [docker : Configure Docker daemon directory] ******************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Enable Docker service on boot] **********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Ensure Docker daemon configuration directory exists] ************************************************************************************************************************
ok: [my_vm]

TASK [docker : Configure Docker daemon options] ********************************************************************************************************************************************
changed: [my_vm]

TASK [docker : Ensure Docker service is started and enabled] *******************************************************************************************************************************
ok: [my_vm]

TASK [docker : Ensure Docker users are added to Docker group] ******************************************************************************************************************************
ok: [my_vm] => (item=ubuntu)

TASK [docker : Install Docker Compose] *****************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Create Docker Compose symlink] **********************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Check Docker service status] ************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Verify Docker service is running and enabled] *******************************************************************************************************************************
ok: [my_vm] => {
    "changed": false,
    "msg": "Docker service is properly configured and running"
}



TASK [docker : Verify Docker Compose installation] *****************************************************************************************************************************************
skipping: [my_vm]

TASK [docker : Display Docker Compose version] *********************************************************************************************************************************************
ok: [my_vm] => {
    "compose_version.stdout": ""
}

TASK [docker : Verify user group membership] ***********************************************************************************************************************************************
skipping: [my_vm]

TASK [docker : Add to the Docker group] ****************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Disable root access] ********************************************************************************************************************************************************
ok: [my_vm]

TASK [docker : Activate Docker services] ***************************************************************************************************************************************************
ok: [my_vm]

RUNNING HANDLER [docker : restart docker] **************************************************************************************************************************************************
changed: [my_vm]

PLAY RECAP *********************************************************************************************************************************************************************************
my_vm                      : ok=21   changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0

$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "my_vm": {
                "ansible_host": "89.169.156.69",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "my_vm"
        ]
    }
}

$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--my_vm
