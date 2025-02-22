# Ansible config

# Docker

## Running docker playbook
```bash
ansible-playbook playbooks/dev/main.yaml
```

Output:
```bash
PLAY [Install Docker and Configure System] ************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm1 is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [yandex_vm1]

TASK [Update apt cache] *******************************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Include Docker installation tasks] *****************************************************************************************************************
included: /Users/timurzeksimbaev/Desktop/Inno3Year/2 semester/DevOps/ansible/roles/docker/tasks/install_docker.yml for yandex_vm1

TASK [docker : Install required system packages] ******************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Get Ubuntu release version] ************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Install Docker] ************************************************************************************************************************************
changed: [yandex_vm1]

TASK [docker : Ensure Docker service is running] ******************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Ensure current user is added to docker group] ******************************************************************************************************
changed: [yandex_vm1]

TASK [docker : Include Docker Compose installation tasks] *********************************************************************************************************
included: /Users/timurzeksimbaev/Desktop/Inno3Year/2 semester/DevOps/ansible/roles/docker/tasks/install_compose.yml for yandex_vm1

TASK [docker : Install Docker Compose] ****************************************************************************************************************************
changed: [yandex_vm1]

TASK [Verify Docker installation] *********************************************************************************************************************************
ok: [yandex_vm1]

TASK [Display Docker version] *************************************************************************************************************************************
ok: [yandex_vm1] => {
    "docker_version.stdout": "Docker version 27.5.1, build 9f9e405"
}

PLAY RECAP ********************************************************************************************************************************************************
yandex_vm1                 : ok=14   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


## Checking inventory
1. *List*
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

Output: 

```bash
{
    "_meta": {
        "hostvars": {
            "yandex_vm1": {
                "ansible_host": "89.169.167.22",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "nphne-dessscxu"
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
            "yandex_vm1"
        ]
    }
}
```

2. *Graph*
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

Output:
```bash
@all:
  |--@ungrouped:
  |  |--yandex_vm1
```

<br>
<br>
<br>
<br>

# Web app

## Running playbook

```bash
ansible-playbook playbooks/dev/app_python/main.yaml
```

Output:
```bash
PLAY [Deploy Python Web Application] ******************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm1 is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [yandex_vm1]

TASK [docker : Include Docker installation tasks] *****************************************************************************************************************
included: /Users/timurzeksimbaev/Desktop/Inno3Year/2 semester/DevOps/ansible/roles/docker/tasks/install_docker.yml for yandex_vm1

TASK [docker : Install required system packages] ******************************************************************************************************************
changed: [yandex_vm1]

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Get Ubuntu release version] ************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Install Docker] ************************************************************************************************************************************
changed: [yandex_vm1]

TASK [docker : Ensure Docker service is running] ******************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Ensure current user is added to docker group] ******************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Include Docker Compose installation tasks] *********************************************************************************************************
included: /Users/timurzeksimbaev/Desktop/Inno3Year/2 semester/DevOps/ansible/roles/docker/tasks/install_compose.yml for yandex_vm1

TASK [docker : Install Docker Compose] ****************************************************************************************************************************
ok: [yandex_vm1]

TASK [web_app : Include wipe tasks if enabled] ********************************************************************************************************************
skipping: [yandex_vm1]

TASK [web_app : Create application directory] *********************************************************************************************************************
changed: [yandex_vm1]

TASK [web_app : Template docker-compose file] *********************************************************************************************************************
changed: [yandex_vm1]

TASK [web_app : Pull Docker image] ********************************************************************************************************************************
changed: [yandex_vm1]

TASK [web_app : Start application using docker compose] ***********************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/python_app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid
potential confusion
changed: [yandex_vm1]

PLAY RECAP ********************************************************************************************************************************************************
yandex_vm1                 : ok=15   changed=6    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```


## Running playbook with full wipe

```bash
ansible-playbook playbooks/dev/app_python/main.yaml -e "web_app_full_wipe=true"
```
Output: 
```bash
PLAY [Deploy Python Web Application] ******************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm1 is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [yandex_vm1]

TASK [docker : Include Docker installation tasks] *****************************************************************************************************************
included: /Users/timurzeksimbaev/Desktop/Inno3Year/2 semester/DevOps/ansible/roles/docker/tasks/install_docker.yml for yandex_vm1

TASK [docker : Install required system packages] ******************************************************************************************************************
changed: [yandex_vm1]

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Get Ubuntu release version] ************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Install Docker] ************************************************************************************************************************************
changed: [yandex_vm1]

TASK [docker : Ensure Docker service is running] ******************************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Ensure current user is added to docker group] ******************************************************************************************************
ok: [yandex_vm1]

TASK [docker : Include Docker Compose installation tasks] *********************************************************************************************************
included: /Users/timurzeksimbaev/Desktop/Inno3Year/2 semester/DevOps/ansible/roles/docker/tasks/install_compose.yml for yandex_vm1

TASK [docker : Install Docker Compose] ****************************************************************************************************************************
ok: [yandex_vm1]

TASK [web_app : Include wipe tasks if enabled] ********************************************************************************************************************
included: /Users/timurzeksimbaev/Desktop/Inno3Year/2 semester/DevOps/ansible/roles/web_app/tasks/0-wipe.yml for yandex_vm1

TASK [web_app : Stop and remove containers] ***********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/python_app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid
potential confusion
changed: [yandex_vm1]

TASK [web_app : Remove application directory] *********************************************************************************************************************
changed: [yandex_vm1]

TASK [web_app : Create application directory] *********************************************************************************************************************
changed: [yandex_vm1]

TASK [web_app : Template docker-compose file] *********************************************************************************************************************
changed: [yandex_vm1]

TASK [web_app : Pull Docker image] ********************************************************************************************************************************
ok: [yandex_vm1]

TASK [web_app : Start application using docker compose] ***********************************************************************************************************
changed: [yandex_vm1]

PLAY RECAP ********************************************************************************************************************************************************
yandex_vm1                 : ok=18   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Running with specific tags
```bash
ansible-playbook playbooks/dev/app_python/main.yaml --tags "setup,deploy"
```

Output: 
```bash
PLAY [Deploy Python Web Application] ******************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm1 is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [yandex_vm1]

TASK [web_app : Create application directory] *********************************************************************************************************************
ok: [yandex_vm1]

TASK [web_app : Template docker-compose file] *********************************************************************************************************************
ok: [yandex_vm1]

TASK [web_app : Start application using docker compose] ***********************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/python_app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid
potential confusion
ok: [yandex_vm1]

PLAY RECAP ********************************************************************************************************************************************************
yandex_vm1                 : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```