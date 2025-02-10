# Best Practices Ansible

To ensure maintainability, scalability, and security when working with Ansible, follow these best practices:

* Keep tasks and configurations reusable by using Ansible roles for different components (e.g., common, webserver, db).
* Store variables in the appropriate folders (e.g., group_vars/, host_vars/).
* Use clear inventory files that distinguish environments (e.g., production, staging).
* Keep playbooks simple, focused, and concise. Each playbook should ideally only perform one function (e.g., setup, deploy).
* Ensure your playbooks can run multiple times without causing issues.
* Use variables for values that might change (e.g., server names, IP addresses).


# Deploy Docker with Ansible

1. Deployment Output

    ```shell
    ansible-playbook -i inventory/default_yandex.yml playbooks/dev/main.yaml -K
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
    changed: [docker]
    
    TASK [../../roles/docker : Add GPG-key Docker] **********************************************************************************************************************************************************
    changed: [docker]
    
    TASK [../../roles/docker : Add repo Docker] *************************************************************************************************************************************************************
    changed: [docker]
    
    TASK [../../roles/docker : Install Docker] **************************************************************************************************************************************************************
    changed: [docker]
    
    TASK [../../roles/docker : Verify Docker install] *******************************************************************************************************************************************************
    ok: [docker]
    
    TASK [../../roles/docker : Add the current user to docker group] ****************************************************************************************************************************************
    changed: [docker]
    
    TASK [../../roles/docker : Install Docker Compose] ******************************************************************************************************************************************************
    changed: [docker]
    
    TASK [../../roles/docker : Verify version Docker Compose] ***********************************************************************************************************************************************
    ok: [docker]
    
    TASK [../../roles/docker : Output version Docker Compose] ***********************************************************************************************************************************************
    ok: [docker] => {
        "compose_version.stdout": "docker-compose version 1.29.2, build 5becea4c"
    }
    
    TASK [../../roles/docker : Ensure daemon.json directory exists] *****************************************************************************************************************************************
    ok: [docker]
    
    TASK [../../roles/docker : Configure Docker security settings - Disable root access] ********************************************************************************************************************
    changed: [docker]
    
    TASK [../../roles/docker : Validate daemon.json syntax] *************************************************************************************************************************************************
    ok: [docker]
    
    TASK [../../roles/docker : Fail if daemon.json is invalid] **********************************************************************************************************************************************
    skipping: [docker]
    
    RUNNING HANDLER [../../roles/docker : Restart Docker] ***************************************************************************************************************************************************
    changed: [docker]
    
    PLAY RECAP **********************************************************************************************************************************************************************************************
    docker                     : ok=15   changed=8    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
    ```

2. Inventory Details

    ```shell
    ansible-inventory -i inventory/default_yandex.yml --list
    ```
    
    ```
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

    ```shell
    ansible-inventory -i inventory/default_yandex.yml --graph
    ```
    
    ```text
    @all:
      |--@ungrouped:
      |--@virtual_machines:
      |  |--docker
    ```

