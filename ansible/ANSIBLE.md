# Ansible Deployment Documentation

This document provides an overview of the Ansible setup, playbooks, roles, and deployment process used to configure Docker on a cloud VM.

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
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_vm_1

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
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_vm_1

TASK [docker : Download Docker Compose] *********************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/manager.yml for yandex_vm_1

TASK [docker : Ensure Docker service is enabled and started on boot] ****************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add current user to docker group] ************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/secure.yml for yandex_vm_1

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
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_vm_1

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
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_vm_1

TASK [docker : Download Docker Compose] *********************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/manager.yml for yandex_vm_1

TASK [docker : Ensure Docker service is enabled and started on boot] ****************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : Add current user to docker group] ************************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/secure.yml for yandex_vm_1

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
      ansible_user: nickky
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
                "ansible_user": "nickky"
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


### Bonus Task: Dynamic Inventory and Secure Docker Configuration

#### **Dynamic Inventory Setup**
Dynamic inventory allows Ansible to automatically fetch the list of target hosts from a cloud provider Yandex Cloud instead of using a static inventory file. This is particularly useful for dynamic cloud environments where hosts are frequently added or removed.

- **Implementation**:
  - Dynamic inventory script version (`yacloud_compute.py` for Yandex Cloud).
    ```commandline
    plugin: yacloud_compute
    yacloud_token_file: "inventory/token"
    yacloud_clouds:
        - "cloud-n1col0s228"
    yacloud_folders:
        - "default"
      ```
  - Update the script in `ansible.cfg`:
    ```ini
    [defaults]
    inventory_plugins = inventory/plugins/
    enable_plugins = yacloud_compute
    ```
  - Let's check the dynamic inventory:
    ```bash
    ansible-inventory -i ./inventory/yacloud_compute.py --list
    ```
    ```commandline
    {
    "_meta": {
        "hostvars": {
            "compute-vm-2-2-20-ssd-1739715686355": {
                "ansible_host": "158.160.58.35"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "compute-vm-2-2-20-ssd-1739715686355"
        ]
    }
    }

    ```

    As for the plugin ```yacloud_compute.py``` there is 
    ```
    # GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

    from __future__ import (absolute_import, division, print_function)
    
    __metaclass__ = type
    
    DOCUMENTATION = '''
        name: yacloud_compute
        plugin_type: inventory
        short_description: Yandex.Cloud compute inventory source
        requirements:
            - yandexcloud
        extends_documentation_fragment:
            - inventory_cache
            - constructed
        description:
            - Get inventory hosts from Yandex Cloud
            - Uses a YAML configuration file that ends with C(yacloud_compute.(yml|yaml)).
        options:
            plugin:
                description: Token that ensures this is a source file for the plugin.
                required: True
                choices: ['yacloud_compute']
            yacloud_token:
                description: Oauth token for yacloud connection
            yacloud_token_file:
                description: File with oauth token for yacloud connection
            yacloud_clouds:
                description: Names of clouds to get hosts from
                type: list
                default: []
            yacloud_folders:
                description: Names of folders to get hosts from
                type: list
                default: []
            yacloud_group_label:
                description: VM's label used for group assignment
                type: string
                default: ""
    
    '''
    
    EXAMPLES = '''
    '''
    
    from ansible.errors import AnsibleError
    from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
    from ansible.utils.display import Display
    from ansible.module_utils._text import to_native
    
    try:
        import yandexcloud
        from yandex.cloud.compute.v1.instance_service_pb2_grpc import InstanceServiceStub
        from yandex.cloud.compute.v1.instance_service_pb2 import ListInstancesRequest
        from google.protobuf.json_format import MessageToDict
        from yandex.cloud.resourcemanager.v1.cloud_service_pb2 import ListCloudsRequest
        from yandex.cloud.resourcemanager.v1.cloud_service_pb2_grpc import CloudServiceStub
        from yandex.cloud.resourcemanager.v1.folder_service_pb2 import ListFoldersRequest
        from yandex.cloud.resourcemanager.v1.folder_service_pb2_grpc import FolderServiceStub
    except ImportError:
        raise AnsibleError('The yacloud dynamic inventory plugin requires yandexcloud')
    
    display = Display()
    
    
    class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
        NAME = 'yacloud_compute'
    
        def verify_file(self, path):
            if super(InventoryModule, self).verify_file(path):
                if path.endswith(('yacloud_compute.yml', 'yacloud_compute.yaml')):
                    return True
            display.debug(
                "yacloud_compute inventory filename must end with 'yacloud_compute.yml' or 'yacloud_compute.yaml'")
            return False
    
        def _get_ip_for_instance(self, instance):
            interfaces = instance["networkInterfaces"]
            for interface in interfaces:
                address = interface["primaryV4Address"]
                if address:
                    if address.get("oneToOneNat"):
                        return address["oneToOneNat"]["address"]
                    else:
                        return address["address"]
            return None
    
        def _get_clouds(self):
            all_clouds = MessageToDict(self.cloud_service.List(ListCloudsRequest()))["clouds"]
            if self.get_option('yacloud_clouds'):
                all_clouds[:] = [x for x in all_clouds if x["name"] in self.get_option('yacloud_clouds')]
            self.clouds = all_clouds
    
        def _get_folders(self):
            all_folders = []
            for cloud in self.clouds:
                all_folders += MessageToDict(self.folder_service.List(ListFoldersRequest(cloud_id=cloud["id"])))["folders"]
    
            if self.get_option('yacloud_folders'):
                all_folders[:] = [x for x in all_folders if x["name"] in self.get_option('yacloud_folders')]
    
            self.folders = all_folders
    
        def _get_all_hosts(self):
            self.hosts = []
            for folder in self.folders:
                hosts = self.instance_service.List(ListInstancesRequest(folder_id=folder["id"]))
                dict_ = MessageToDict(hosts)
    
                if dict_:
                    self.hosts += dict_["instances"]
    
        def _init_client(self):
            file = self.get_option('yacloud_token_file')
            token_var = self._vars.get("yacloud_token")
    
            if file is not None:
                token = open(file).read().strip()
            elif token_var is not None:
                token = token_var
            else:
                token = self.get_option('yacloud_token')
            if not token:
                raise AnsibleError(
                    "token it empty. provide either "
                    "`yacloud_token_file` or `yacloud_token`")
            sdk = yandexcloud.SDK(token=token)
    
            self.instance_service = sdk.client(InstanceServiceStub)
            self.folder_service = sdk.client(FolderServiceStub)
            self.cloud_service = sdk.client(CloudServiceStub)
    
        def _process_hosts(self):
            group_label = str(self.get_option('yacloud_group_label'))
    
            for instance in self.hosts:
                if group_label and group_label in instance["labels"]:
                    group = instance["labels"][group_label]
                else:
                    group = "yacloud"
    
                self.inventory.add_group(group=group)
                if instance["status"] == "RUNNING":
                    ip = self._get_ip_for_instance(instance)
                    if ip:
                        self.inventory.add_host(instance["name"], group=group)
                        self.inventory.set_variable(instance["name"], 'ansible_host', to_native(ip))
    
        def parse(self, inventory, loader, path, cache=True):
            super(InventoryModule, self).parse(inventory, loader, path)
    
            self._read_config_data(path)
            self._init_client()
    
            self._get_clouds()
            self._get_folders()
    
            self._get_all_hosts()
            self._process_hosts()
    ```
    There should also be a token in an inventory/token file
  
    #### **Let's also run a playbook, but for now with -u flag and after the username**
    ```commandline
    ansible-playbook playbooks/dev/main.yaml -u nickky
    ```
    ```commandline
    PLAY [Deploy Docker on Yandex Cloud VM] *********************************************************************************************************************************************************************

    TASK [Gathering Facts] **************************************************************************************************************************************************************************************
    [WARNING]: Platform linux on host compute-vm-2-2-20-ssd-1739715686355 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change
    the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
    included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for compute-vm-2-2-20-ssd-1739715686355
    
    TASK [docker : Update apt cache] ****************************************************************************************************************************************************************************
    changed: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : Install dependencies for Docker (Ubuntu)] ****************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : Add Docker GPG key for Ubuntu] ***************************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : Add Docker repository for Ubuntu] ************************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : Install Docker CE] ***************************************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
    included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for compute-vm-2-2-20-ssd-1739715686355
    
    TASK [docker : Download Docker Compose] *********************************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
    included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/manager.yml for compute-vm-2-2-20-ssd-1739715686355
    
    TASK [docker : Ensure Docker service is enabled and started on boot] ****************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : Add current user to docker group] ************************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : include_tasks] *******************************************************************************************************************************************************************************
    included: /home/nikolai/Documents/DevOpsLabs/S25-core-course-labs/ansible/roles/docker/tasks/secure.yml for compute-vm-2-2-20-ssd-1739715686355
    
    TASK [docker : Copy secure Docker daemon configuration] *****************************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    TASK [docker : Validate Docker daemon configuration JSON syntax] ********************************************************************************************************************************************
    ok: [compute-vm-2-2-20-ssd-1739715686355]
    
    PLAY RECAP **************************************************************************************************************************************************************************************************
    compute-vm-2-2-20-ssd-1739715686355 : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

    ```
---

### Secure Docker Configuration

To enhance Docker security, the following tasks are added to the Ansible playbook. These tasks ensure that the Docker daemon is configured securely and that the configuration is validated for correctness.

#### **Tasks for Secure Docker Configuration**

1. **Copy Secure Docker Daemon Configuration**  
   This task copies a secure configuration to the Docker daemon's configuration file (`daemon.json`). It ensures that the file is owned by `root` and has the correct permissions.

   ```yaml
   - name: Copy secure Docker daemon configuration
     copy:
       content: |
         {
             "userns-remap": "default"
         }
       dest: /etc/docker/daemon.json
       owner: root
       group: root
       mode: '0644'
     notify: restart docker
   ```
   
2. **Validate Docker Daemon Configuration JSON Syntax**
This task validates the JSON syntax of the daemon.json file to ensure it is correctly formatted.

```commandline
- name: Validate Docker daemon configuration JSON syntax
  command: python3 -m json.tool /etc/docker/daemon.json
  changed_when: false
```

### Key features

- **Security**: The `userns-remap` setting improves security by remapping user namespaces, reducing the risk of privilege escalation.
- **Validation**: Ensures the `daemon.json` file is syntactically correct, preventing Docker from failing due to configuration errors.
- **Idempotency**: The tasks are designed to be idempotent, meaning they can be run multiple times without causing unintended changes.