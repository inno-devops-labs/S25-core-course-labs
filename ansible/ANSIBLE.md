# Docker installation via ansible

1) I applied terraform config to deploy my vms
2) I created a playbook 
```yaml
- name: Deploy Docker using the Docker role
  hosts: all
  become: yes

  roles:
    - docker
```
3) I created a custom role for docker inside **/role/docker**
4) I created inventory file fom my vms
```yaml
all:
  hosts:
    vm-1:
      ansible_host: 158.160.90.175
      ansible_user: misha
      ansible_ssh_private_key_file: ~/.ssh/id_rsa
    vm-2:
      ansible_host: 158.160.89.38
      ansible_user: misha
      ansible_ssh_private_key_file: ~/.ssh/id_rsa
```
5) **ansible-inventory -i inventory/default_yc_compute.yml --list**
```
{
    "_meta": {
        "hostvars": {
            "vm-1": {
                "ansible_host": "158.160.90.175",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "misha"
            },
            "vm-2": {
                "ansible_host": "158.160.89.38",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "misha"
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
            "vm-1",
            "vm-2"
        ]
    }
}

```

5) **ansible-inventory -i inventory/default_yc_compute.yml --graph**
```
@all:
  |--@ungrouped:
  |  |--vm-1
  |  |--vm-2
```

6) I created **ansible.cfg**
```
[defaults]
inventory = inventory/default_yc_compute.yml
playbook_dir = playbooks/
roles_path = roles/
host_key_checking = False
retry_files_enabled = False
inventory_plugins = inventory/plugins/
```

7) I applied my playbook
```bash
ansible-playbook playbooks/dev/main.yml  
```

```
PLAY [Deploy Docker using the Docker role] **************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************
[WARNING]: Platform linux on host vm-1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-1]
[WARNING]: Platform linux on host vm-2 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-2]

TASK [docker : include_tasks] ***************************************************************************************************************************************************************************
included: /Users/mishagladyshev/studying/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm-1, vm-2

TASK [docker : Update apt cache] ************************************************************************************************************************************************************************
changed: [vm-2]
changed: [vm-1]

TASK [docker : Install dependencies for Docker (Ubuntu)] ************************************************************************************************************************************************
ok: [vm-2]
ok: [vm-1]

TASK [docker : Add Docker GPG key for Ubuntu] ***********************************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

TASK [docker : Add Docker repository for Ubuntu] ********************************************************************************************************************************************************
ok: [vm-2]
ok: [vm-1]

TASK [docker : Install Docker CE] ***********************************************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

TASK [docker : include_tasks] ***************************************************************************************************************************************************************************
included: /Users/mishagladyshev/studying/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm-1, vm-2

TASK [docker : Download Docker Compose] *****************************************************************************************************************************************************************
ok: [vm-2]
ok: [vm-1]

TASK [docker : include_tasks] ***************************************************************************************************************************************************************************
included: /Users/mishagladyshev/studying/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/configure.yml for vm-1, vm-2

TASK [docker : Ensure Docker service is enabled and started on boot] ************************************************************************************************************************************
ok: [vm-2]
ok: [vm-1]

TASK [docker : Add current user to docker group] ********************************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

TASK [docker : include_tasks] ***************************************************************************************************************************************************************************
included: /Users/mishagladyshev/studying/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/secure.yml for vm-1, vm-2

TASK [docker : Copy secure Docker daemon configuration] *************************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

TASK [docker : Validate Docker daemon configuration JSON syntax] ****************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

PLAY RECAP **********************************************************************************************************************************************************************************************
vm-1                       : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vm-2                       : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

8) Then I verified that docker was correctly installed using **docker ps**


# Bonus task

1) I installed **yacloud_config** plugin from source repo
2) I created new inventory file and connect my token to it
```yaml
plugin: yacloud_compute
yacloud_token_file: "./inventory/token"
yacloud_clouds:
  - "cloud-mishagladyschev"
yacloud_folders:
  - "default"
```
3) I changed my config
```
[defaults]
inventory = inventory/yacloud_compute.yaml
playbook_dir = playbooks/
roles_path = roles/
host_key_checking = False
retry_files_enabled = False
inventory_plugins = inventory/plugins/
enable_plugins = yacloud_compute
```
4) I added **secure.yml** to my docker role to make secure daemon
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

- name: Validate Docker daemon configuration JSON syntax
  command: python3 -m json.tool /etc/docker/daemon.json
  changed_when: false
```
5) I checked and my playbook successfully executes

# Web app deployment

Output of
```bash
    ansible-playbook playbooks/dev/main.yml --tags web_app
```

```
PLAY [Deploy Docker using the Docker role] **************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************
[WARNING]: Platform linux on host vm-1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-1]
[WARNING]: Platform linux on host vm-2 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-2]

TASK [web_app : Create deployment directory for web_app] ************************************************************************************************************************************************
changed: [vm-2]
changed: [vm-1]

TASK [web_app : Render Docker Compose template for the application] *************************************************************************************************************************************
changed: [vm-2]
changed: [vm-1]

TASK [web_app : Pull Docker image for the application] **************************************************************************************************************************************************
changed: [vm-1]
changed: [vm-2]

TASK [web_app : Start the application container using Docker Compose] ***********************************************************************************************************************************
changed: [vm-1]
changed: [vm-2]

PLAY RECAP **********************************************************************************************************************************************************************************************
vm-1                       : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vm-2                       : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```