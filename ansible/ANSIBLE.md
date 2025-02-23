# Ansible Deployment Documentation

---

## Repository Structure

The repository is organized as follows:

```commandline
ansible/
├── inventory/
│   ├── plugins/
│   │   └── yacloud_compute.py
│   ├── token/
│   ├── yacloud_compute.yaml
│   ├── yandex_cloud_inventory.yaml
├── playbooks/
│   └── dev/
│       └── main.yaml
├── roles/
│   ├── docker/
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   ├── tasks/
│   │   │   ├── install_compose.yml
│   │   │   ├── install_docker.yml
│   │   │   ├── main.yml
│   │   │   ├── manager.yml
│   │   │   └── secure.yml
│   │   └── README.md
│   └── web_app/
├── ansible.cfg
└── ANSIBLE.md
```

## Playbook Execution

The playbook `main.yaml` located in `ansible/playbooks/dev/` was used to deploy Docker. The playbook leverages the custom Docker role.

```main.yml
- name: Deploy Docker on Yandex Cloud VM
  hosts: all
  become: yes
  roles:
    - docker
```

To execute the playbook in a dry run mode:

```bash
ansible-playbook ansible/playbooks/dev/main.yaml --check --diff
```

Output:
```commandline

PLAY [Deploy Docker on Yandex Cloud VM] *********************************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm_1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that
path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_vm_1

TASK [docker : Update apt cache] ****************************************************************************************************************************************************************************
changed: [yandex_vm_1]

TASK [docker : Install dependencies for Docker (Ubuntu)] ****************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add Docker GPG key for Ubuntu] ***************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add Docker repository for Ubuntu] ************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Install Docker CE] ***************************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_vm_1

TASK [docker : Download Docker Compose] *********************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/manager.yml for yandex_vm_1

TASK [docker : Ensure Docker service is enabled and started on boot] ****************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add current user to docker group] ************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/secure.yml for yandex_vm_1

TASK [docker : Copy secure Docker daemon configuration] *****************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Validate Docker daemon configuration JSON syntax] ********************************************************************************************************************************************
skipping: [yandex_vm_1]

PLAY RECAP **************************************************************************************************************************************************************************************************
yandex_vm_1                : ok=14   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  
```

And for the usual deployments, we use ```ansible-playbook playbooks/dev/main.yaml``` command:
Output:
```commandline
PLAY [Deploy Docker on Yandex Cloud VM] *********************************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm_1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that
path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_vm_1

TASK [docker : Update apt cache] ****************************************************************************************************************************************************************************
changed: [yandex_vm_1]

TASK [docker : Install dependencies for Docker (Ubuntu)] ****************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add Docker GPG key for Ubuntu] ***************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add Docker repository for Ubuntu] ************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Install Docker CE] ***************************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_vm_1

TASK [docker : Download Docker Compose] *********************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/manager.yml for yandex_vm_1

TASK [docker : Ensure Docker service is enabled and started on boot] ****************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add current user to docker group] ************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /Users/demanzverev/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/secure.yml for yandex_vm_1

TASK [docker : Copy secure Docker daemon configuration] *****************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Validate Docker daemon configuration JSON syntax] ********************************************************************************************************************************************
ok: [yandex_vm_1]

PLAY RECAP **************************************************************************************************************************************************************************************************
yandex_vm_1                : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory Details

The inventory file `yandex_cloud_inventory.yaml` was used to define the target hosts. Below is the output of the inventory commands:

The file looks like that:
```commandline
all:
  hosts:
    yandex_vm_1:
      ansible_host: 158.160.58.35
      ansible_user: demakoder
      ansible_ssh_private_key_file: ~/.ssh/id_rsa.pub
```

1. **List inventory**:

   ```bash
   ansible-inventory -i ansible-inventory -i inventory/yandex_cloud_inventory.yaml --list
   ```

Output:
```
   {
    "_meta": {
        "hostvars": {
            "yandex_vm_1": {
                "ansible_host": "158.160.58.35",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa.pub",
                "ansible_user": "demakoder"
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
            "yandex_vm_1"
        ]
    }
}
 ```
2. **Visual inventory structure**:

```bash
   ansible-inventory -i ansible-inventory -i inventory/yandex_cloud_inventory.yaml --graph
```

Output:
```commandline
@all:
  |--@ungrouped:
  |  |--yandex_vm_1
```

### Key Features

1. **Orchestrates Task Execution**
    - Coordinates the execution of other tasks in a specific order to ensure proper configuration.

2. **Installs and Configures Software**
    - Ensures required software (e.g., Docker, Docker Compose) is installed and configured correctly.

3. **Applies Security Settings**
    - Configures security settings, such as disabling root access or modifying `daemon.json`.

4. **Ensures Idempotency**
    - Designed to be idempotent, meaning it can be run multiple times without causing unintended changes.

5. **Supports Modularity**
    - Calls other task files (e.g., `install_docker.yml`, `install_compose.yml`) for modular and reusable code.
6. **Logs and Reports Changes**
    - Provides feedback on changes made during execution, ensuring transparency.
