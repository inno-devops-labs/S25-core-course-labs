# Ansible Setup

## Lab 5: Ansible and Docker Deployment

### Deployment Output (Last 50 Lines)

```txt
> ansible-playbook playbooks/dev/main.yml | tail -n 50

ok: [yandex_cloud_terraform1]

TASK [docker : include_tasks] **************************************************
included: /Users/nikitashlyakhtin/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_cloud_terraform1, yandex_cloud_terraform2

TASK [docker : Install Docker dependencies] ************************************
ok: [yandex_cloud_terraform1]
ok: [yandex_cloud_terraform2]

TASK [docker : Add Docker's official GPG key] **********************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : Set up the Docker repository] ***********************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : Install Docker CE] **********************************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : include_tasks] **************************************************
included: /Users/nikitashlyakhtin/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for yandex_cloud_terraform1, yandex_cloud_terraform2

TASK [docker : Download Docker Compose binary] *********************************
ok: [yandex_cloud_terraform1]
ok: [yandex_cloud_terraform2]

TASK [docker : Verify Docker Compose installation] *****************************
changed: [yandex_cloud_terraform1]
changed: [yandex_cloud_terraform2]

TASK [docker : include_tasks] **************************************************
included: /Users/nikitashlyakhtin/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/enable_docker_boot.yml for yandex_cloud_terraform1, yandex_cloud_terraform2

TASK [docker : Enable Docker service to start on boot] *************************
ok: [yandex_cloud_terraform1]
ok: [yandex_cloud_terraform2]

TASK [docker : include_tasks] **************************************************
included: /Users/nikitashlyakhtin/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/add_user_to_docker_group.yml for yandex_cloud_terraform1, yandex_cloud_terraform2

TASK [docker : Add the current user to the docker group] ***********************
ok: [yandex_cloud_terraform1]
ok: [yandex_cloud_terraform2]

PLAY RECAP *********************************************************************
yandex_cloud_terraform1    : ok=13   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
yandex_cloud_terraform2    : ok=13   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

### Inventory Details

#### Inventory List Output

```txt
> ansible-inventory --list

{
    "_meta": {
        "hostvars": {
            "yandex_cloud_terraform1": {
                "ansible_host": "158.160.53.154",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "/Users/nikitashlyakhtin/.ssh/id_ed25519",
                "ansible_user": "devops"
            },
            "yandex_cloud_terraform2": {
                "ansible_host": "89.169.158.134",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "/Users/nikitashlyakhtin/.ssh/id_ed25519",
                "ansible_user": "devops"
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
            "yandex_cloud_terraform1",
            "yandex_cloud_terraform2"
        ]
    }
}
```

Explanation:
The output shows all defined hosts with their connection variables.
The _meta section holds host-specific details (like IP address, SSH key, user, and Python interpreter).
In our project, we have two hosts (VMs) placed in the default ungrouped group.

#### Inventory Graph Output

```txt
> ansible-inventory --graph

@all:
  |--@ungrouped:
  |  |--yandex_cloud_terraform1
  |  |--yandex_cloud_terraform2
```

Explanation:
The graph represents the hierarchy of the inventory in our Ansible setup.
All hosts (2 VMs) are in the ungrouped subcategory under *all* category

## Lab 6: Ansible and Docker Deployment

### Task 1: Application Deployment Output (Last 50 Lines)

```txt
> ansible-playbook playbooks/dev/main.yml | tail -n 50

TASK [docker : Add Docker's official GPG key] ****************************************************************************************************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : Set up the Docker repository] *****************************************************************************************************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : Install Docker CE] ****************************************************************************************************************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : include_tasks] ********************************************************************************************************************************
included: /Users/nikitashlyakhtin/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for yandex_cloud_terraform1, yandex_cloud_terraform2

TASK [docker : Download Docker Compose binary] ***************************************************************************************************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : Verify Docker Compose installation] ***********************************************************************************************************
changed: [yandex_cloud_terraform1]
changed: [yandex_cloud_terraform2]

TASK [docker : include_tasks] ********************************************************************************************************************************
included: /Users/nikitashlyakhtin/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/enable_docker_boot.yml for yandex_cloud_terraform1, yandex_cloud_terraform2

TASK [docker : Enable Docker service to start on boot] *******************************************************************************************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [docker : include_tasks] ********************************************************************************************************************************
included: /Users/nikitashlyakhtin/Innopolis/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/add_user_to_docker_group.yml for yandex_cloud_terraform1, yandex_cloud_terraform2

TASK [docker : Add the current user to the docker group] *****************************************************************************************************
ok: [yandex_cloud_terraform2]
ok: [yandex_cloud_terraform1]

TASK [web_app : Pull the web app Docker image] ***************************************************************************************************************
changed: [yandex_cloud_terraform1]
changed: [yandex_cloud_terraform2]

TASK [web_app : Start the web app container] *****************************************************************************************************************
changed: [yandex_cloud_terraform1]
changed: [yandex_cloud_terraform2]

PLAY RECAP ***************************************************************************************************************************************************
yandex_cloud_terraform1    : ok=15   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
yandex_cloud_terraform2    : ok=15   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
