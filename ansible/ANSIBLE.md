# Ansible

This lab is made with the usage of Yandex Cloud virtual machine.

## Best Practices Applied:
1. Use of `--check` and `--diff` flags. Also, there is an opportunity to check syntax.
2. Usage of `handlers` for Docker.

## Check Ansible inventory:
```
ansible-inventory -i inventory/yacloud_compute.yml --list
{
    "_meta": {
        "hostvars": {
            "dev": {
                "ansible_host": "51.250.106.195"
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
            "dev"
        ]
    }
}
```

## Check that everything is applicable to remote VM:
```
ansible-playbook playbooks/dev/main.yml --diff [Also, can specify the private key if it is missed]
PLAY [Dev] *************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
[WARNING]: Platform linux on host dev is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [dev]

TASK [docker : Install Docker] *****************************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for dev

TASK [docker : Update apt package index] *******************************************************************************************************************************
changed: [dev]

TASK [docker : Install dependencies] ***********************************************************************************************************************************
ok: [dev] => (item=apt-transport-https)
ok: [dev] => (item=ca-certificates)
ok: [dev] => (item=curl)
ok: [dev] => (item=gnupg-agent)
ok: [dev] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************
ok: [dev]

TASK [docker : Add Docker apt repository] ******************************************************************************************************************************
ok: [dev]

TASK [docker : Update apt package index after adding repository] *******************************************************************************************************
changed: [dev]

TASK [docker : Install Docker with dependencies] ***********************************************************************************************************************
ok: [dev]

TASK [docker : Secure Docker configuration] ****************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for dev

TASK [docker : Add user to Docker group] *******************************************************************************************************************************
ok: [dev]

TASK [docker : Disable root access] ************************************************************************************************************************************
ok: [dev]

TASK [docker : Install Docker Compose] *********************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for dev

TASK [docker : Install Docker Compose] *********************************************************************************************************************************
The following additional packages will be installed:
  python3-docker python3-dockerpty python3-docopt python3-dotenv
  python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
0 upgraded, 7 newly installed, 0 to remove and 7 not upgraded.
changed: [dev]

PLAY RECAP *************************************************************************************************************************************************************
dev                        : ok=13   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Lab 6 Output
### Command to run the process for Python web-app: `ansible-playbook playbooks/dev/app_python/main.yml`
```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs/ansible$ ansible-playbook playbooks/dev/app_python/main.yml --private-key ~/.ssh/gitlab_new -u nikita

PLAY [Deploy Python app] ***********************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
[WARNING]: Platform linux on host dev is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [dev]

TASK [docker : Install Docker] *****************************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for dev

TASK [docker : Update apt package index] *******************************************************************************************************************************
changed: [dev]

TASK [docker : Install dependencies] ***********************************************************************************************************************************
ok: [dev] => (item=apt-transport-https)
ok: [dev] => (item=ca-certificates)
ok: [dev] => (item=curl)
ok: [dev] => (item=gnupg-agent)
ok: [dev] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************
ok: [dev]

TASK [docker : Add Docker apt repository] ******************************************************************************************************************************
ok: [dev]

TASK [docker : Update apt package index after adding repository] *******************************************************************************************************
changed: [dev]

TASK [docker : Install Docker with dependencies] ***********************************************************************************************************************
ok: [dev]

TASK [docker : Secure Docker configuration] ****************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for dev

TASK [docker : Add user to Docker group] *******************************************************************************************************************************
ok: [dev]

TASK [docker : Disable root access] ************************************************************************************************************************************
ok: [dev]

TASK [docker : Install Docker Compose] *********************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for dev

TASK [docker : Install Docker Compose] *********************************************************************************************************************************
changed: [dev]

TASK [web_app : Deploy App] ********************************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/web_app/tasks/deploy.yml for dev

TASK [web_app : Pull Docker image] *************************************************************************************************************************************
changed: [dev]

TASK [web_app : Start container] ***************************************************************************************************************************************
changed: [dev]

TASK [web_app : Create directory for docker-compose file] **************************************************************************************************************changed: [dev]

TASK [web_app : Deploy docker-compose file] ****************************************************************************************************************************changed: [dev]

TASK [web_app : Remove container] **************************************************************************************************************************************skipping: [dev]

TASK [web_app : Remove docker-compose file] ****************************************************************************************************************************skipping: [dev]

PLAY RECAP *************************************************************************************************************************************************************
dev                        : ok=18   changed=7    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

### Command to run the process for NodeJS web-app: `ansible-playbook playbooks/dev/app_nodejs/main.yml`
```
nikita@LAPTOP-DOBKKTS4:~/S25-core-course-labs/ansible$ ansible-playbook playbooks/dev/app_nodejs/main.yml --private-key ~/.ssh/gitlab_new -u nikita

PLAY [Deploy Python app] ***********************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************
[WARNING]: Platform linux on host dev is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [dev]

TASK [docker : Install Docker] *****************************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for dev

TASK [docker : Update apt package index] *******************************************************************************************************************************
changed: [dev]

TASK [docker : Install dependencies] ***********************************************************************************************************************************
ok: [dev] => (item=apt-transport-https)
ok: [dev] => (item=ca-certificates)
ok: [dev] => (item=curl)
ok: [dev] => (item=gnupg-agent)
ok: [dev] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************
ok: [dev]

TASK [docker : Add Docker apt repository] ******************************************************************************************************************************
ok: [dev]

TASK [docker : Update apt package index after adding repository] *******************************************************************************************************
ok: [dev]

TASK [docker : Install Docker with dependencies] ***********************************************************************************************************************
ok: [dev]

TASK [docker : Secure Docker configuration] ****************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for dev

TASK [docker : Add user to Docker group] *******************************************************************************************************************************
ok: [dev]

TASK [docker : Disable root access] ************************************************************************************************************************************
ok: [dev]

TASK [docker : Install Docker Compose] *********************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for dev

TASK [docker : Install Docker Compose] *********************************************************************************************************************************
changed: [dev]

TASK [web_app : Deploy App] ********************************************************************************************************************************************
included: /home/nikita/S25-core-course-labs/ansible/roles/web_app/tasks/deploy.yml for dev

TASK [web_app : Pull Docker image] *************************************************************************************************************************************
changed: [dev]

TASK [web_app : Start container] ***************************************************************************************************************************************
changed: [dev]

TASK [web_app : Create directory for docker-compose file] **************************************************************************************************************changed: [dev]

TASK [web_app : Deploy docker-compose file] ****************************************************************************************************************************changed: [dev]

TASK [web_app : Remove container] **************************************************************************************************************************************skipping: [dev]

TASK [web_app : Remove docker-compose file] ****************************************************************************************************************************skipping: [dev]

PLAY RECAP *************************************************************************************************************************************************************
dev                        : ok=18   changed=6    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```