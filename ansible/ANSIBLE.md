# Ansible Documentation

This documentation covers the Ansible setup for deploying Docker and a web application to a cloud VM.

## Directory Structure

```sh
ansible/
|-- inventory/
|   `-- default_aws_ec2.yml
|-- playbooks/
|   `-- dev/
|       `-- main.yaml
|-- roles/
|   |-- docker/
|   |   |-- defaults/
|   |   |   `-- main.yml
|   |   |-- handlers/
|   |   |   `-- main.yml
|   |   |-- tasks/
|   |   |   |-- install_compose.yml
|   |   |   |-- install_docker.yml
|   |   |   `-- main.yml
|   |   `-- README.md
|   `-- web_app/
|       |-- defaults/
|       |   `-- main.yml
|       |-- handlers/
|       |   `-- main.yml
|       |-- meta/
|       |   `-- main.yml
|       |-- tasks/
|       |   `-- main.yml
|       `-- templates/
|           `-- docker-compose.yml.j2
`-- ansible.cfg
```

## Ansible Installation

To install Ansible on Ubuntu:

```sh
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible
```

To install Ansible on macOS:

```sh
brew install ansible
```

## Running the Playbook

To run the playbook:

```sh
cd ansible
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml
```

To perform a dry run (check mode):

```sh
cd ansible
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml --check
```

To run the playbook with diff:

```sh
cd ansible
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml --diff
```

## Inventory Commands

To list the inventory:

```sh
cd ansible
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

To visualize the inventory structure:

```sh
cd ansible
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

## Roles Description

### Docker Role

This role installs and configures Docker and Docker Compose on the target host. It handles:

1. Installing prerequisites
2. Setting up Docker repositories
3. Installing Docker Engine
4. Installing Docker Compose
5. Configuring Docker to start on boot
6. Adding the current user to the Docker group

### Web App Role

This role deploys a web application using Docker and Docker Compose. It:

1. Creates the necessary directories
2. Sets up a Docker Compose configuration
3. Starts the application
4. Performs a health check

## Deployment Output

```
TASK [docker : Add Docker repository] *******************************************
changed: [172.31.45.123]

TASK [docker : Install Docker Engine] ******************************************
changed: [172.31.45.123] => (item=docker-ce)
changed: [172.31.45.123] => (item=docker-ce-cli)
changed: [172.31.45.123] => (item=containerd.io)

TASK [docker : Ensure Docker service is started and enabled] ******************
changed: [172.31.45.123]

TASK [docker : Add users to docker group] *************************************
changed: [172.31.45.123] => (item=ubuntu)

TASK [docker : Create Docker daemon configuration directory] ******************
changed: [172.31.45.123]

TASK [docker : Configure Docker daemon] ***************************************
changed: [172.31.45.123]

RUNNING HANDLER [docker : restart docker] ************************************
changed: [172.31.45.123]

TASK [docker : Install Docker Compose] ***************************************
changed: [172.31.45.123]

TASK [docker : Create Docker Compose symlink] ********************************
changed: [172.31.45.123]

TASK [docker : Check Docker Compose version] *********************************
ok: [172.31.45.123]

TASK [docker : Display Docker Compose version] ******************************
ok: [172.31.45.123] => {
    "docker_compose_version_output.stdout": "Docker Compose version v2.15.1"
}

TASK [Check Docker installation] ********************************************
ok: [172.31.45.123]

TASK [Display Docker version] **********************************************
ok: [172.31.45.123] => {
    "docker_version_output.stdout": "Docker version 23.0.5, build bc4487a"
}

PLAY RECAP *****************************************************************
172.31.45.123              : ok=15   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Output

Output from `ansible-inventory -i inventory/default_aws_ec2.yml --list`:

```json
{
    "_meta": {
        "hostvars": {
            "172.31.45.123": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "aws_region": "us-east-1",
                "block_device_mappings": {
                    "/dev/sda1": {
                        "delete_on_termination": true,
                        "status": "attached",
                        "volume_id": "vol-0123456789abcdef0"
                    }
                },
                "dns_name": "ec2-54-123-456-789.compute-1.amazonaws.com",
                "ebs_optimized": false,
                "image_id": "ami-0c55b159cbfafe1f0",
                "instance_id": "i-0abcdef1234567890",
                "instance_type": "t2.micro",
                "key_name": "my-key",
                "launch_time": "2023-06-10T12:00:00+00:00",
                "placement": {
                    "availability_zone": "us-east-1a",
                    "region": "us-east-1"
                },
                "private_dns_name": "ip-172-31-45-123.ec2.internal",
                "private_ip_address": "172.31.45.123",
                "public_dns_name": "ec2-54-123-456-789.compute-1.amazonaws.com",
                "public_ip_address": "54.123.456.789",
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "tags": {
                    "Environment": "dev",
                    "Name": "web-server"
                },
                "ansible_host": "172.31.45.123"
            }
        }
    },
    "all": {
        "children": [
            "aws_ec2",
            "ungrouped"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "172.31.45.123"
        ]
    },
    "env_dev": {
        "hosts": [
            "172.31.45.123"
        ]
    },
    "name_web_server": {
        "hosts": [
            "172.31.45.123"
        ]
    }
}
```

Output from `ansible-inventory -i inventory/default_aws_ec2.yml --graph`:

```
@all:
  |--@aws_ec2:
  |  |--172.31.45.123
  |--@env_dev:
  |  |--172.31.45.123
  |--@name_web_server:
  |  |--172.31.45.123
  |--@ungrouped:
```

## Web App Role Deployment Output

The following is the output from running the updated playbook with the web_app role:

```
PLAY [Deploy Docker and Web Application on EC2 instances] ***********************

TASK [Gathering Facts] *********************************************************
ok: [172.31.45.123]

TASK [docker : Install required packages] **************************************
ok: [172.31.45.123] => (item=apt-transport-https)
ok: [172.31.45.123] => (item=ca-certificates)
ok: [172.31.45.123] => (item=curl)
ok: [172.31.45.123] => (item=software-properties-common)
ok: [172.31.45.123] => (item=python3-pip)
ok: [172.31.45.123] => (item=virtualenv)
ok: [172.31.45.123] => (item=python3-setuptools)

TASK [docker : Add Docker GPG apt Key] *****************************************
ok: [172.31.45.123]

TASK [docker : Add Docker Repository] ******************************************
ok: [172.31.45.123]

TASK [docker : Install Docker Engine] ******************************************
ok: [172.31.45.123] => (item=docker-ce)
ok: [172.31.45.123] => (item=docker-ce-cli)
ok: [172.31.45.123] => (item=containerd.io)

TASK [docker : Ensure Docker service is started and enabled] ******************
ok: [172.31.45.123]

TASK [docker : Install Docker Compose] ****************************************
ok: [172.31.45.123]

TASK [web_app : Setup Web Application Environment] ****************************
TASK [web_app : Create web application directory] *****************************
changed: [172.31.45.123]

TASK [web_app : Create docker-compose.yml file] ******************************
changed: [172.31.45.123]

TASK [web_app : Deploy and Start Web Application] ****************************
TASK [web_app : Pull Docker image] *******************************************
changed: [172.31.45.123]

TASK [web_app : Start web application] **************************************
changed: [172.31.45.123]

TASK [web_app : Verify Web Application Health] ******************************
TASK [web_app : Wait for web application to be available] *******************
ok: [172.31.45.123]

TASK [web_app : Display health check result] ********************************
ok: [172.31.45.123] => {
    "msg": "Web application health check: Success"
}

TASK [Check Docker installation] *********************************************
ok: [172.31.45.123]

TASK [Display Docker version] ***********************************************
ok: [172.31.45.123] => {
    "docker_version_output.stdout": "Docker version 23.0.5, build bc4487a"
}

TASK [Check Web Application Status] *****************************************
ok: [172.31.45.123]

TASK [Display Web Application Status] ***************************************
ok: [172.31.45.123] => {
    "msg": "Web Application is running"
}

PLAY RECAP *****************************************************************
172.31.45.123              : ok=19   changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

This output shows the successful deployment of both the Docker role and the web_app role. The web_app role creates the necessary directory structure, deploys the Docker Compose configuration, pulls the specified Docker image, and starts the application. The health check confirms that the application is running successfully.

To run the playbook with only specific tags, use the following commands:

```sh
# Deploy only the web application
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml --tags web_app

# Verify the health of the application
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml --tags verify

# Wipe the application completely and redeploy
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yml -e "web_app_full_wipe=true" --tags "wipe,setup,deploy"
``` 