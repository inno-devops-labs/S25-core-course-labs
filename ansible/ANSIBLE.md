# Ansible Deployment Documentation

This document describes the Ansible setup for deploying Docker and Docker Compose to a remote Ubuntu 22.04+ server using the official Docker repository.

## Directory Structure

```
ansible/
├── inventory/
│   └── default_aws_ec2.yml    # Inventory file for target servers
├── playbooks/
│   └── dev/
│       └── main.yaml          # Main playbook for Docker deployment
├── roles/
│   └── docker/               # Docker role
│       ├── defaults/
│       ├── handlers/
│       ├── tasks/
│       └── README.md
└── ansible.cfg               # Ansible configuration file
```

## Prerequisites

1. Ansible installed on the control node
2. SSH access to target servers
3. Python 3.x on target servers

## Inventory Example

`ansible/inventory/default_aws_ec2.yml`:
```yaml
all:
  children:
    webservers:
      hosts:
        web1:
          ansible_host: "176.108.253.168"
          ansible_user: "user1"
          ansible_ssh_private_key_file: "~/.ssh/id_rsa"
      vars:
        ansible_python_interpreter: /usr/bin/python3
```

## Usage

1. Verify inventory:
   ```bash
   ansible-inventory -i inventory/default_aws_ec2.yml --list
   ansible-inventory -i inventory/default_aws_ec2.yml --graph
   ```
   
   Output:
   ```json
   {
       "_meta": {
           "hostvars": {
               "web1": {
                   "ansible_host": "176.108.253.168",
                   "ansible_python_interpreter": "/usr/bin/python3",
                   "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                   "ansible_user": "user1"
               }
           }
       },
       "all": {
           "children": [
               "ungrouped",
               "webservers"
           ]
       },
       "webservers": {
           "hosts": [
               "web1"
           ]
       }
   }
   ```
   ```
   @all:
     |--@ungrouped:
     |--@webservers:
     |  |--web1
   ```

2. Run the playbook:
   ```bash
   # Dry run
   ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --check --diff

   # Actual deployment
   ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --diff
   ```

    dry-run output:
   ```
   PLAY [Deploy Docker and Docker Compose] ****************************************

   TASK [Gathering Facts] *********************************************************
   ok: [web1]

   TASK [Update apt cache] ********************************************************
   ok: [web1]

   TASK [docker : Remove old Docker versions if they exist] ***********************
   ok: [web1]

   TASK [docker : Install required system packages] *******************************
   ok: [web1]

   TASK [docker : Add Docker GPG apt Key] *****************************************
   changed: [web1]

   TASK [docker : Add Docker repository] ******************************************
   changed: [web1]

   TASK [docker : Install Docker Engine] ******************************************
   ok: [web1]

   TASK [docker : Ensure Docker service is running] *******************************
   ok: [web1]

TASK [Verify Docker installation] **********************************************
skipping: [web1]

TASK [Display Docker version] **************************************************
ok: [web1] => 
  docker_version_check.stdout_lines: []

TASK [Verify Docker Compose installation] **************************************
skipping: [web1]

TASK [Display Docker Compose version] ******************************************
ok: [web1] => 
  docker_compose_version_check.stdout_lines: []

PLAY RECAP *********************************************************************
web1                       : ok=10   changed=2    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
   ```

## Troubleshooting

- Ensure the SSH key has correct permissions (chmod 600)
- Verify the user has sudo privileges
- Check if the user is in the docker group
- If Docker service fails to start, check system logs: `journalctl -u docker`

## Security Considerations

- The playbook uses sudo for privilege escalation
- Docker daemon is configured with secure defaults
- System packages are updated before installation

## Maintenance

- Update the Docker version in `roles/docker/defaults/main.yml` if needed
- Review and update security configurations
- Monitor Docker logs and system resources
