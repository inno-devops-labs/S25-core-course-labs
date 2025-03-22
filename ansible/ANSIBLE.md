# Lab 5

## Outputs

- `ansible-playbook playbooks/dev/main.yaml --check`
```
PLAY [Deploy Docker on VM in Yandex Cloud] *************************************************************************

TASK [Gathering Facts] *********************************************************************************************
fatal: [yandex_cloud_devops_lab4_vm]: FAILED! => {"msg": "The field 'remote_addr' has an invalid value, which includes an undefined variable.. 'dynamic_ip' is undefined"}

PLAY RECAP *********************************************************************************************************
yandex_cloud_devops_lab4_vm : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
```

- `ansible-playbook playbooks/dev/main.yaml -e "dynamic_ip=89.169.159.227"`
```

PLAY [Deploy Docker on VM in Yandex Cloud] *************************************

TASK [Gathering Facts] *********************************************************
[WARNING]: Platform linux on host yandex_cloud_devops_lab4_vm is using the
discovered Python interpreter at /usr/bin/python3.12, but future installation
of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_cloud_devops_lab4_vm]

TASK [docker : include_tasks] **************************************************
included: /home/VM/User/Learning/Program/DOE/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_cloud_devops_lab4_vm

TASK [docker : Add GPG key] ****************************************************
ok: [yandex_cloud_devops_lab4_vm]

TASK [docker : Set up the Docker repository] ***********************************
ok: [yandex_cloud_devops_lab4_vm]

TASK [docker : Install Docker CE] **********************************************
ok: [yandex_cloud_devops_lab4_vm]

TASK [docker : include_tasks] **************************************************
included: /home/VM/User/Learning/Program/DOE/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_cloud_devops_lab4_vm

TASK [docker : Install docker-compose] *****************************************
ok: [yandex_cloud_devops_lab4_vm]

TASK [docker : include_tasks] **************************************************
included: /home/VM/User/Learning/Program/DOE/S25-core-course-labs/ansible/roles/docker/tasks/docker_enable.yml for yandex_cloud_devops_lab4_vm

TASK [docker : Enable Docker service to start on boot] *************************
ok: [yandex_cloud_devops_lab4_vm]

TASK [docker : include_tasks] **************************************************
included: /home/VM/User/Learning/Program/DOE/S25-core-course-labs/ansible/roles/docker/tasks/add_user_to_group.yml for yandex_cloud_devops_lab4_vm

TASK [docker : Add the current user to the docker group] ***********************
ok: [yandex_cloud_devops_lab4_vm]

PLAY RECAP *********************************************************************
yandex_cloud_devops_lab4_vm : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


```

- `ansible-inventory -i inventory/default_yandex_cloud.yml --list`
```
{
    "_meta": {
        "hostvars": {
            "yandex_cloud_devops_lab4_vm": {
                "ansible_host": "{{ dynamic_ip }}",
                "ansible_ssh_private_key_file": "/home/VM/.ssh/yandex_cloud_vm",
                "ansible_user": "user"
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
            "yandex_cloud_devops_lab4_vm"
        ]
    }
}
```

- `ansible-inventory -i inventory/default_yandex_cloud.yml --graph`
```
@all:
  |--@ungrouped:
  |  |--yandex_cloud_devops_lab4_vm
```

### Bonus task

- `ansible-playbook playbooks/dev/main.yaml -e "dynamic_ip=158.160.41.38"`
```
TASK [docker : Modify daemon to disable root access] ***************************************************************
changed: [yandex_cloud_devops_lab4_vm]

TASK [docker : Restart docker.service to apply changes] ************************************************************
changed: [yandex_cloud_devops_lab4_vm]

PLAY RECAP *********************************************************************************************************
yandex_cloud_devops_lab4_vm : ok=14   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

# Lab 6

## Outputs

- `ansible-playbook playbooks/dev/main.yaml`
```
(venv) [VM@LVM ansible]$ ansible-playbook playbooks/dev/main.yaml 

PLAY [Deploy Docker on VM in Yandex Cloud] *************************************************************************

TASK [Gathering Facts] *********************************************************************************************
[WARNING]: Platform linux on host devops_lab4_vm is using the discovered Python interpreter at /usr/bin/python3.12,
but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [devops_lab4_vm]

TASK [web_app : include_tasks] *************************************************************************************
included: /home/VM/User/Learning/Program/DOE/S25-core-course-labs/ansible/roles/web_app/tasks/pull_image.yml for devops_lab4_vm

TASK [web_app : Pull docker image from Docker Hub] *****************************************************************
ok: [devops_lab4_vm]

TASK [web_app : include_tasks] *************************************************************************************
included: /home/VM/User/Learning/Program/DOE/S25-core-course-labs/ansible/roles/web_app/tasks/start_container.yml for devops_lab4_vm

TASK [web_app : Start container] ***********************************************************************************
changed: [devops_lab4_vm]

PLAY RECAP *********************************************************************************************************
devops_lab4_vm             : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739903906.085356   13756 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.

```
