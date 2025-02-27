# Ansible config

## Checking Docker playbook
```bash
ansible-playbook playbooks/dev/main.yaml
```

## Output:
```bash
PLAY [Install Docker and Configure System] ************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
[WARNING]: Platform linux on host terraform-vm is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [terraform-vm]

TASK [Update apt cache] *******************************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Include Docker installation tasks] *****************************************************************************************************************
included: /Users/aleksejkurejkin/GolandProjects/devo/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Installing required system packages] ******************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Get Ubuntu release version] ************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker] ************************************************************************************************************************************
changed: [terraform-vm]

TASK [docker : Ensure Docker service is running] ******************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Ensure current user is added to docker group] ******************************************************************************************************
changed: [terraform-vm]

TASK [docker : Include Docker Compose installation tasks] *********************************************************************************************************
included: /Users/aleksejkurejkin/GolandProjects/devo/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Install Docker Compose] ****************************************************************************************************************************
changed: [terraform-vm]

TASK [Verify Docker installation] *********************************************************************************************************************************
ok: [terraform-vm]

TASK [Display Docker version] *************************************************************************************************************************************
ok: [terraform-vm] => {
    "docker_version.stdout": "Docker version 27.5.1, build 9f9e405"
}

PLAY RECAP ********************************************************************************************************************************************************
terraform-vm                 : ok=14   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


## Checking inventory
1)
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

## Output: 

```bash
{
    "_meta": {
        "hostvars": {
            "terraform-vm": {
                "ansible_host": "158.160.47.255",
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
            "terraform-vm"
        ]
    }
}
```

2)
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

## Output:
```bash
@all:
  |--@ungrouped:
  |  |--terraform-vm
```

# Lab 6

## Web app playbook
```bash
ansible-playbook playbooks/dev/main.yaml
```

## Terminal output:
```bash
PLAY [Install Docker and Configure System and Deploy] ******************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
[WARNING]: Platform linux on host terraform-vm is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [terraform-vm]

TASK [docker : Include Docker installation tasks] *****************************************************************************************************************
included: /Users/aleksejkurejkin/GolandProjects/devo/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Installing required system packages] ******************************************************************************************************************
changed: [terraform-vm]

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Get Ubuntu release version] ************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker] ************************************************************************************************************************************
changed: [terraform-vm]

TASK [docker : Ensure Docker service is running] ******************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Ensure current user is added to docker group] ******************************************************************************************************
ok: [terraform-vm]

TASK [docker : Include Docker Compose installation tasks] *********************************************************************************************************
included: /Users/aleksejkurejkin/GolandProjects/devo/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] ****************************************************************************************************************************
ok: [terraform-vm]

TASK [web_app : Run wipe tasks if enabled] ********************************************************************************************************************
skipping: [terraform-vm]

TASK [web_app : Ensure the application directory exists] *********************************************************************************************************************
changed: [terraform-vm]

TASK [web_app : Generate docker-compose configuration] *********************************************************************************************************************
changed: [terraform-vm]

TASK [web_app : Fetch latest Docker image] ********************************************************************************************************************************
changed: [terraform-vm]

TASK [web_app : Launch application with Docker Compose] ***********************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/web_app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid
potential confusion
changed: [terraform-vm]

PLAY RECAP ********************************************************************************************************************************************************
terraform-vm                 : ok=15   changed=6    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```


## Full wipe running
```bash
ansible-playbook playbooks/dev/main.yaml -e "web_app_full_wipe=true"
```

## Terminal output: 
```bash
PLAY [Install Docker and Configure System and Deploy] ******************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
[WARNING]: Platform linux on host terraform-vm is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [terraform-vm]

TASK [docker : Include Docker installation tasks] *****************************************************************************************************************
included: /Users/aleksejkurejkin/GolandProjects/devo/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Installing required system packages] ******************************************************************************************************************
changed: [terraform-vm]

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Get Ubuntu release version] ************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker] ************************************************************************************************************************************
changed: [terraform-vm]

TASK [docker : Ensure Docker service is running] ******************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Ensure current user is added to docker group] ******************************************************************************************************
ok: [terraform-vm]

TASK [docker : Include Docker Compose installation tasks] *********************************************************************************************************
included: /Users/aleksejkurejkin/GolandProjects/devo/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] ****************************************************************************************************************************
ok: [terraform-vm]

TASK [web_app : Run wipe tasks if enabled] ********************************************************************************************************************
included: /Users/aleksejkurejkin/GolandProjects/devo/S25-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for terraform-vm

TASK [web_app : Stop and remove containers] ***********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/web_app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid
potential confusion
changed: [terraform-vm]

TASK [web_app : Remove application directory] *********************************************************************************************************************
changed: [terraform-vm]

TASK [web_app : Ensure the application directory exists] *********************************************************************************************************************
changed: [terraform-vm]

TASK [web_app : Generate docker-compose configuration] *********************************************************************************************************************
changed: [terraform-vm]

TASK [web_app : Fetch latest Docker image] ********************************************************************************************************************************
ok: [terraform-vm]

TASK [web_app : Launch application with Docker Compose] ***********************************************************************************************************
changed: [terraform-vm]

PLAY RECAP ********************************************************************************************************************************************************
terraform-vm                 : ok=18   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
