# Ansible

## Best Practices

1. **Pre-Execution Validation**
   - **Simulated Execution**: Before applying changes to the target environment, the playbook was executed in dry-run mode using the `--check` flag. This allowed us to simulate the changes and verify their correctness without making any actual modifications.
   - **Syntax Validation**: To ensure the playbook was error-free, we performed a syntax check using the `--syntax-check` option. This step helped identify and resolve potential issues early in the process, ensuring smooth execution during deployment.
2. **Efficient Use of Handlers**
   - Handlers were implemented to manage service restarts intelligently. For example, services like Docker were only restarted when specific tasks triggered a change. This approach minimized unnecessary service interruptions and ensured optimal resource utilization.
3. **Enhanced Security Configuration**
   - A dedicated task was included to harden Docker's security settings. Specifically:
     - **Root Access Restriction**: The `daemon.json` file was modified using the `copy` module to disable root access for Docker. This configuration significantly enhanced the security posture of the Docker environment by reducing the risk of unauthorized access.
4. **Modular Role Design**
   - The playbook leveraged modular roles to organize tasks logically. This design approach improved maintainability and reusability, allowing individual components (e.g., Docker installation and configuration) to be updated or reused independently.
5. **Inventory Management**
   - A static inventory file was used to define host-specific variables, such as SSH keys and user credentials. This ensured that the playbook could be executed consistently across different environments while maintaining flexibility for customization.
6. **Version Control for Dependencies**
   - Specific versions of tools like Docker and Docker Compose were explicitly defined in the playbook. This practice ensured consistency across deployments and avoided compatibility issues caused by unexpected updates.

```txt
(venv) ➜  ansible git:(Lab-5) ✗ ansible-playbook -i inventory/default_yandex_cloud.yml playbooks/dev/main.yaml
```
```txt
PLAY [Deploy Docker and Configure Security] ******************************************************

TASK [Gathering Facts] ***************************************************************************
[WARNING]: Platform linux on host yandex_instance_1 is using the discovered Python interpreter at
/usr/bin/python3.10, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_instance_1]

TASK [docker : Install Docker dependencies] ******************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker GPG key] ***************************************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker repository] ************************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker] *******************************************************************
ok: [yandex_instance_1]

TASK [docker : Ensure Docker service is running and enabled on boot] *****************************
ok: [yandex_instance_1]

TASK [docker : Download Docker Compose binary] ***************************************************
ok: [yandex_instance_1]

TASK [docker : Verify Docker Compose installation] ***********************************************
ok: [yandex_instance_1]

TASK [docker : Display installed Docker Compose version] *****************************************
ok: [yandex_instance_1] => {
    "msg": "Docker Compose installed successfully: Docker Compose version v2.33.0"
}

TASK [docker : Configure Docker daemon.json for security] ****************************************
ok: [yandex_instance_1]

TASK [docker : Add users to the docker group] ****************************************************
ok: [yandex_instance_1] => (item=yc-user)

PLAY RECAP ***************************************************************************************
yandex_instance_1          : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

```txt
(venv) ➜  ansible git:(Lab-5) ✗ ansible-inventory -i inventory/default_yandex_cloud.yml --list 
```
```txt
{
    "_meta": {
        "hostvars": {
            "yandex_instance_1": {
                "ansible_host": "51.250.15.50",
                "ansible_ssh_private_key_file": "~/.ssh/yacloud",
                "ansible_user": "yc-user"
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

```txt
(venv) ➜  ansible git:(Lab-5) ✗ ansible-inventory -i inventory/default_yandex_cloud.yml --graph
```
```txt
@all:
  |--@ungrouped:
  |  |--yandex_instance_1
```