# Best Practices Ansible

To ensure maintainability, scalability, and security when working with Ansible, follow these best practices:

* Keep tasks and configurations reusable by using Ansible roles for different components (e.g., common, webserver, db).
* Store variables in the appropriate folders (e.g., group_vars/, host_vars/).
* Use clear inventory files that distinguish environments (e.g., production, staging).
* Keep playbooks simple, focused, and concise. Each playbook should ideally only perform one function (e.g., setup, deploy).
* Ensure your playbooks can run multiple times without causing issues.
* Use variables for values that might change (e.g., server names, IP addresses).

# Deploy Docker with Ansible

## Inventory List Output

```bash
ansible-inventory --list
```

```text
{
    "_meta": {
        "hostvars": {
            "docker": {
                "ansible_host": "84.201.136.228",
                "ansible_ssh_private_key_file": "/home/askar/.ssh/id_rsa",
                "ansible_user": "askar"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "docker"
        ]
    }
}
```

##  Inventory Graph Output

```bash
ansible-inventory --graph
```


## Application Deployment Output

```bash
ansible-playbook playbooks/dev/main.yml
```

```text

PLAY [Deploy Docker] ************************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************
[WARNING]: Platform linux on host docker is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [docker]

TASK [../../roles/docker : Update apt] ******************************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Install dependencies] ********************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Add GPG-key Docker] **********************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Add repo Docker] *************************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Install Docker] **************************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Verify Docker install] *******************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Add the current user to docker group] ****************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Install Docker Compose] ******************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Verify version Docker Compose] ***********************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Output version Docker Compose] ***********************************************************************************************************************************************
ok: [docker] => {
    "compose_version.stdout": "docker-compose version 1.29.2, build 5becea4c"
}

TASK [../../roles/docker : Ensure daemon.json directory exists] *****************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Configure Docker security settings - Disable root access] ********************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Validate daemon.json syntax] *************************************************************************************************************************************************
ok: [docker]

TASK [../../roles/docker : Fail if daemon.json is invalid] **********************************************************************************************************************************************
skipping: [docker]

PLAY RECAP **********************************************************************************************************************************************************************************************
docker                     : ok=14   changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```

## Application Python Deployment Output

```bash
ansible-playbook playbooks/dev/app_python/main.yml
```

```text
TASK [web_app : Pull Docker image] **********************************************************************************************************************************************************************
ok: [docker]

TASK [web_app : Start the web app container] ************************************************************************************************************************************************************
changed: [docker]

TASK [web_app : Create directory for docker-compose file] ***********************************************************************************************************************************************
changed: [docker]

TASK [web_app : Deploy docker-compose file] *************************************************************************************************************************************************************
changed: [docker]

TASK [web_app : Remove existing web app container] ******************************************************************************************************************************************************
skipping: [docker]

TASK [web_app : Remove docker-compose file] *************************************************************************************************************************************************************
skipping: [docker]

PLAY RECAP **********************************************************************************************************************************************************************************************
docker                     : ok=18   changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   

```


## Application Nodes Deployment Output

```bash
ansible-playbook playbooks/dev/app_nodes/main.yml
```

```
TASK [web_app : Pull Docker image] **********************************************************************************************************************************************************************
ok: [docker]

TASK [web_app : Start the web app container] ************************************************************************************************************************************************************
changed: [docker]

TASK [web_app : Create directory for docker-compose file] ***********************************************************************************************************************************************
ok: [docker]

TASK [web_app : Deploy docker-compose file] *************************************************************************************************************************************************************
changed: [docker]

TASK [web_app : Remove existing web app container] ******************************************************************************************************************************************************
skipping: [docker]

TASK [web_app : Remove docker-compose file] *************************************************************************************************************************************************************
skipping: [docker]

PLAY RECAP **********************************************************************************************************************************************************************************************
docker                     : ok=18   changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   

```
## Application Python Deployment Output With Docker tag

```bash
ansible-playbook playbooks/dev/app_python/main.yml --tags docker
```

```text

PLAY [Deploy Python App] ********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************
[WARNING]: Platform linux on host docker is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [docker]

TASK [web_app : Pull Docker image] **********************************************************************************************************************************************************************
ok: [docker]

TASK [web_app : Start the web app container] ************************************************************************************************************************************************************
ok: [docker]

TASK [web_app : Deploy docker-compose file] *************************************************************************************************************************************************************
changed: [docker]

PLAY RECAP **********************************************************************************************************************************************************************************************
docker                     : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Application Python Deployment Output With Wipe tag

```bash
ansible-playbook playbooks/dev/app_python/main.yml --tags wipe
```

```text
PLAY [Deploy Python App] ********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************
[WARNING]: Platform linux on host docker is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [docker]

TASK [web_app : Remove existing web app container] ******************************************************************************************************************************************************
changed: [docker]

TASK [web_app : Remove docker-compose file] *************************************************************************************************************************************************************
changed: [docker]

PLAY RECAP **********************************************************************************************************************************************************************************************
docker                     : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
