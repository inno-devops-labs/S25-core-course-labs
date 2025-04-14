# Ansible

## Lab6

``` PLAY [Deploy python app via Docker] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [my_yandex_vm]

TASK [docker : Install Docker & compose] ***************************************
included: /home/kamil/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for my_yandex_vm

TASK [docker : Install prerequisites] ******************************************
ok: [my_yandex_vm]

TASK [docker : Add Docker’s official GPG key] **********************************
ok: [my_yandex_vm]

TASK [docker : Add Docker’s repository] ****************************************
ok: [my_yandex_vm]

TASK [docker : Update package cache] *******************************************
ok: [my_yandex_vm]

TASK [docker : Install Docker] *************************************************
ok: [my_yandex_vm]

TASK [docker : Ensure Docker is running] ***************************************
ok: [my_yandex_vm]

TASK [docker : Security configurations] ****************************************
included: /home/kamil/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/security.yml for my_yandex_vm

TASK [docker : Add to the Docker group] ****************************************
ok: [my_yandex_vm]

TASK [docker : Disable root access] ********************************************
ok: [my_yandex_vm]

TASK [docker : Activate Docker services] ***************************************
ok: [my_yandex_vm]

TASK [web_app : Pull Docker image] *********************************************
ok: [my_yandex_vm]

TASK [web_app : Run the container] *********************************************
ok: [my_yandex_vm]

PLAY RECAP *********************************************************************
my_yandex_vm               : ok=14   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Lab5
``` ansible-playbook  <path_to_playbook> --diff --check```
```PLAY [install Docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [my_yandex_vm]

TASK [docker : Install Docker & compose] ***************************************
included: /home/kamil/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for my_yandex_vm

TASK [docker : Install prerequisites] ******************************************
ok: [my_yandex_vm]

TASK [docker : Add Docker’s official GPG key] **********************************
ok: [my_yandex_vm]

TASK [docker : Add Docker’s repository] ****************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=x86_64] https://download.docker.com/linux/ubuntu focal stable

changed: [my_yandex_vm]

TASK [docker : Update package cache] *******************************************
changed: [my_yandex_vm]

TASK [docker : Install Docker] *************************************************
ok: [my_yandex_vm]

TASK [docker : Ensure Docker is running] ***************************************
ok: [my_yandex_vm]

TASK [docker : Security configurations] ****************************************
included: /home/kamil/PycharmProjects/S25-core-course-labs/ansible/roles/docker/tasks/security.yml for my_yandex_vm

TASK [docker : Add to the Docker group] ****************************************
changed: [my_yandex_vm]

TASK [docker : Activate Docker services] ***************************************
ok: [my_yandex_vm]

PLAY RECAP *********************************************************************
my_yandex_vm               : ok=11   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```ansible-inventory -i <name_of_your_inventory_file>.yaml --list```

```{
    "_meta": {
        "hostvars": {
            "my_yandex_vm": {
                "ansible_host": "158.160.36.148",
                "ansible_ssh_private_key_file": "~/.ssh/yandex",
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
            "my_yandex_vm"
        ]
    }
}
```

```ansible-inventory -i <name_of_your_inventory_file>.yaml --graph```
```@all:
  |--@ungrouped:
  |  |--my_yandex_vm
```

