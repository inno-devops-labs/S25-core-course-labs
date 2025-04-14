# Ansible Documentation

## Overview

This project uses Ansible to automate the deployment of Docker and Docker Compose on a cloud VM (Yandex Cloud Console). The role for Docker installation is custom-built and includes all necessary tasks for installation, configuration, and management of Docker services.

## Ansible structure

The structure differs from the specified one. Namely, the `roles` folder has been moved to the `dev` folder. In the process, I encountered an error (The error description is attached below.) that I couldn't fix, so I did everything as required in the error description. Otherwise, the `ansible` structure is no different.

### Error description

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
ERROR! the role 'docker' was not found in /home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev/roles:/home/egor/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev

The error appears to be in '/home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev/main.yaml': line 6, column 7, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

#    - geerlingguy.docker
    - docker
```

### Structure

```
ansible
|-- inventory
|   `-- default_aws_ec2.yml
|-- playbooks
|   `-- dev
|       |-- main.yaml
|       |-- roles
|           |-- docker
|           |   |-- defaults
|           |   |   `-- main.yml
|           |   |-- handlers
|           |   |   `-- main.yml
|           |   |-- tasks
|           |   |   |-- install_compose.yml
|           |   |   |-- install_docker.yml
|           |   |   `-- main.yml
|           |   `-- README.md
|           `-- web_app
|               |-- defaults
|               |   `-- main.yml
|               |-- handlers
|               |   `-- main.yml
|               |-- meta
|               |   `-- main.yml
|               |-- tasks
|               |   `-- main.yml
|               `-- templates
|                   `-- docker-compose.yml.j2
|-- ansible.cfg
|-- ANSIBLE.md
```

## Inventory structure

The inventory is structured to support EC2 instances in AWS and uses SSH for remote communication. The `default_aws_ec2.yml` inventory file contains the details for connecting to the cloud VM.

```yaml
all:
  hosts:
    your-ec2-instance:
      ansible_host: 158.160.162.136
      ansible_user: vakzlak
      ansible_ssh_private_key_file: /home/egor/.ssh/id_rsa
```

## Playbook for `geerlingguy.docker` role (`ansible-galaxy`) and output

### Playbook:

```yaml
- name: Deploy docker on Cloud VM
  hosts: all
  become: true
  roles:
    - geerlingguy.docker
#    - docker
```

### Output:

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Deploy docker on Cloud VM] *********************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Load OS-specific vars.] ***************************************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************
included: /home/egor/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for your-ec2-instance

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] ***************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] *****************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ***************************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ****************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Add Docker apt key.] ******************************************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *******************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] **********************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Add Docker repository.] ***************************************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Install Docker packages.] *************************************************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Install docker-compose plugin.] *******************************************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *******************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ************************************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Configure Docker daemon options.] *****************************************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ****************************************************************************************
ok: [your-ec2-instance]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ************************************************************************

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Get docker group info using getent.] **************************************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *****************************************************************************
skipping: [your-ec2-instance]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************
skipping: [your-ec2-instance]

PLAY RECAP *******************************************************************************************************************************************************
your-ec2-instance          : ok=14   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   

```

## Playbook for `docker` role and output

### Playbook:

```yaml
- name: Deploy docker on Cloud VM
  hosts: all
  become: true
  roles:
#    - geerlingguy.docker
    - docker
```

### Output:

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Deploy docker on Cloud VM] ******************************************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : include_tasks] *********************************************************************************************************************************************************************************************
included: /home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev/roles/docker/tasks/install_docker.yml for your-ec2-instance

TASK [docker : Remove old docker sources list] ****************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Remove old docker GPG key] *********************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Update apt cache] ******************************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Install docker] ********************************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Add docker repository] *************************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Update apt cache] ******************************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Verify Docker installation] ********************************************************************************************************************************************************************************
changed: [your-ec2-instance]

TASK [docker : Show Docker version] ***************************************************************************************************************************************************************************************
ok: [your-ec2-instance] => {
    "docker_version.stdout": "Docker version 27.5.1, build 9f9e405"
}

TASK [docker : include_tasks] *********************************************************************************************************************************************************************************************
included: /home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev/roles/docker/tasks/install_compose.yml for your-ec2-instance

TASK [docker : Download Docker Compose] ***********************************************************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Verify Docker Compose installation] ************************************************************************************************************************************************************************
changed: [your-ec2-instance]

TASK [docker : Show Docker Compose version] *******************************************************************************************************************************************************************************
ok: [your-ec2-instance] => {
    "compose_version.stdout": "docker-compose version 1.29.2, build 5becea4c"
}

PLAY RECAP ****************************************************************************************************************************************************************************************************************
your-ec2-instance          : ok=14   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --check

PLAY [Deploy docker on Cloud VM] *********************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : include_tasks] ************************************************************************************************************************************
included: /home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev/roles/docker/tasks/install_docker.yml for your-ec2-instance

TASK [docker : Remove old docker sources list] *******************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Remove old docker GPG key] ************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Update apt cache] *********************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Install docker] ***********************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Add docker repository] ****************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Update apt cache] *********************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Verify Docker installation] ***********************************************************************************************************************
skipping: [your-ec2-instance]

TASK [docker : Show Docker version] ******************************************************************************************************************************
ok: [your-ec2-instance] => {
    "docker_version.stdout": ""
}

TASK [docker : include_tasks] ************************************************************************************************************************************
included: /home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev/roles/docker/tasks/install_compose.yml for your-ec2-instance

TASK [docker : Download Docker Compose] **************************************************************************************************************************
ok: [your-ec2-instance]

TASK [docker : Verify Docker Compose installation] ***************************************************************************************************************
skipping: [your-ec2-instance]

TASK [docker : Show Docker Compose version] **********************************************************************************************************************
ok: [your-ec2-instance] => {
    "compose_version.stdout": ""
}

PLAY RECAP *******************************************************************************************************************************************************
your-ec2-instance          : ok=12   changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
```

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "your-ec2-instance": {
                "ansible_host": "158.160.162.136",
                "ansible_ssh_private_key_file": "/home/egor/.ssh/id_rsa",
                "ansible_user": "vakzlak"
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
            "your-ec2-instance"
        ]
    }
}
```

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--your-ec2-instance
```

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ docker-compose --version
Docker Compose version v2.20.3
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ docker --version
Docker version 27.2.0, build 3ab4256
```

## Playbook for `web_app` role and output

### Playbook:

```yaml
- name: Deploy docker on Cloud VM
  hosts: all
  become: true
  vars:
    web_app_full_wipe: true
  roles:
#    - geerlingguy.docker
#    - docker
    - web_app
```

### Output:

```
(venv) egor@egor-100-HP:~/PycharmProjects/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml

PLAY [Deploy docker on Cloud VM] *********************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
ok: [your-ec2-instance]

TASK [web_app : Include wipe tasks] ******************************************************************************************************************************
included: /home/egor/PycharmProjects/S25-core-course-labs/ansible/playbooks/dev/roles/web_app/tasks/0-wipe.yml for your-ec2-instance

TASK [web_app : Stop and remove Docker containers] ***************************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Remove Docker images] ****************************************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Remove application directory] ********************************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Remove Docker Compose binary] ********************************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Ensure appgroup exists] **************************************************************************************************************************
ok: [your-ec2-instance]

TASK [web_app : Ensure appuser exists] ***************************************************************************************************************************
ok: [your-ec2-instance]

TASK [web_app : Ensure application directory exists] *************************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Copy application files to the server (excluding venv)] *******************************************************************************************
[DEPRECATION WARNING]: The connection's stdin object is deprecated. Call display.prompt_until(msg) instead. This feature will be removed in version 2.19. 
Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
changed: [your-ec2-instance]

TASK [web_app : Ensure Docker Compose file is present] ***********************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Ensure Docker Python SDK is installed] ***********************************************************************************************************
ok: [your-ec2-instance]

TASK [web_app : Download Docker Compose binary] ******************************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Ensure Docker Compose is executable] *************************************************************************************************************
ok: [your-ec2-instance]

TASK [web_app : Ensure Docker containers are running] ************************************************************************************************************
changed: [your-ec2-instance]

TASK [web_app : Ensure Docker containers are started] ************************************************************************************************************
changed: [your-ec2-instance]

PLAY RECAP *******************************************************************************************************************************************************
your-ec2-instance          : ok=16   changed=10   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    
```