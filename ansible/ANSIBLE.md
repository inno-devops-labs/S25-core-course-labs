# Ansible Documentation

## Project Structure
```ansible/
├── inventory/
│   └── default_aws_ec2.yml
├── roles/
│   └── docker/
├── playbooks/
│   └── dev/
│       └── main.yaml
└── ansible.cfg
```

## Inventory

### Inventory Structure
```bash
$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--localhost
```

### Detailed Inventory Output
```bash
$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
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
            "localhost"
        ]
    }
}
```

## Deployment Output

```bash
$ ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K

PLAY RECAP ******************************************************************************
localhost : ok=37 changed=0 unreachable=0 failed=0 skipped=22 rescued=0 ignored=0
```

## Installation Verification

### Component Versions
```bash
$ docker --version
Docker version 27.5.1, build 9f9e405

$ docker-compose --version
Docker Compose version v2.32.1
```

### Service Status
```bash
$ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running)
```

### Docker Group Check
```bash
$ groups | grep docker
m7 ... docker ...
```

## Common Commands

### Running Playbooks
```bash
# Standard run
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml

# Run with sudo privileges
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K

# Syntax check
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml --syntax-check

# Dry run
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml --check -K

# Show differences
ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml --diff -K
```

## Roles

### Web App Role

Role for deploying an application using Docker Compose.

#### Variables

- `app_name`: Application name (default: python-app)
- `app_image`: Docker image for the application
- `app_port`: Application port (default: 8000)
- `deploy_user`: User for deployment
- `deploy_directory`: Directory for deployment

#### Dependencies

- Docker role

#### Example Usage

```yaml
- hosts: all
  vars:
    github_username: "your-username"
    github_token: "your-token"
  roles:
    - web_app
```

## Deployment Output

```bash
PLAY [Deploy Application] ***********************************************************

TASK [Gathering Facts] *************************************************************
ok: [localhost]

TASK [web_app : Create application directory] **************************************
changed: [localhost]

TASK [web_app : Template docker-compose.yml] **************************************
changed: [localhost]

TASK [web_app : Login to GitHub Container Registry] *******************************
ok: [localhost]

TASK [web_app : Pull application image] ******************************************
changed: [localhost]

TASK [web_app : Start application] ***********************************************
changed: [localhost]

PLAY RECAP **********************************************************************
localhost : ok=6 changed=4 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```