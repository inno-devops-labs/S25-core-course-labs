# Ansible

## Best practice

1. Playbook validation.     
- `--syntax-check` flag to validate syntax
- `--check` flag to simulate changes without applying them
2. Use of handlers
3. Secure docker configuration

## Docker Deployment output

```aiignore
 ansible-playbook playbooks/dev/main.yml --diff

PLAY [Setup Docker on Yandex Cloud VM] *********************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
included: /home/dasha/devops/devops_labs/ansible/roles/docker/tasks/install_docker.yml for yandex_instance_1

TASK [docker : Update apt package index] *******************************************************************************************************************************************
changed: [yandex_instance_1]

TASK [docker : Install required system packages] ***********************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker repository] **********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Start Docker service] ***********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Secure Docker Configuration] ****************************************************************************************************************************************
included: /home/dasha/devops/devops_labs/ansible/roles/docker/tasks/secure_configuration.yml for yandex_instance_1

TASK [docker : Add user to Docker group] *******************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Disable root access] ************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker Compose] *********************************************************************************************************************************************
included: /home/dasha/devops/devops_labs/ansible/roles/docker/tasks/install_compose.yml for yandex_instance_1

TASK [docker : Install Docker Compose] *********************************************************************************************************************************************
ok: [yandex_instance_1]

PLAY RECAP *************************************************************************************************************************************************************************
yandex_instance_1          : ok=13   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

## Docker Inventory details

```aiignore
 ansible-inventory -i inventory/yacloud.yml --graph
@all:
  |--@ungrouped:
  |  |--yandex_instance_1
  
 ```
```aiignore
root@LAPTOP-382BEF3K:/home/dasha/devops/devops_labs/ansible# ansible-inventory -i inventory/yacloud.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_instance_1": {
                "ansible_host": "89.169.148.84",
                "ansible_ssh_private_key_file": "/home/dasha/.ssh/id_ed25519",
                "ansible_user": "dasha"
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
            "yandex_instance_1"
        ]
    }
}

```


## Webapp deployment output

```aiignore
ansible-playbook playbooks/dev/app_python/main.yml 
[WARNING]: Found variable using reserved name: port

PLAY [Deploy Python app] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
included: /home/dasha/devops/devops_labs/ansible/roles/docker/tasks/install_docker.yml for yandex_instance_1

TASK [docker : Update apt package index] *******************************************************************************************************************************************
changed: [yandex_instance_1]

TASK [docker : Install required system packages] ***********************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker repository] **********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Start Docker service] ***********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Secure Docker Configuration] ****************************************************************************************************************************************
included: /home/dasha/devops/devops_labs/ansible/roles/docker/tasks/secure_configuration.yml for yandex_instance_1

TASK [docker : Add user to Docker group] *******************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Disable root access] ************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker Compose] *********************************************************************************************************************************************
included: /home/dasha/devops/devops_labs/ansible/roles/docker/tasks/install_compose.yml for yandex_instance_1

TASK [docker : Install Docker Compose] *********************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Deploy App] ********************************************************************************************************************************************************
included: /home/dasha/devops/devops_labs/ansible/roles/web_app/tasks/deploy.yml for yandex_instance_1

TASK [web_app : Pull Docker image] *************************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Deploy docker container] *******************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Create directory for docker-compose file] **************************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Deploy docker-compose file] ****************************************************************************************************************************************
ok: [yandex_instance_1]

TASK [web_app : Remove container] **************************************************************************************************************************************************
skipping: [yandex_instance_1]

TASK [web_app : Remove docker-compose file] ****************************************************************************************************************************************
skipping: [yandex_instance_1]

PLAY RECAP *************************************************************************************************************************************************************************
yandex_instance_1          : ok=18   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0


```

## App

![img](/attachments/img_3.png)