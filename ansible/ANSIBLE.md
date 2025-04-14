# Ansible

## Inventory

This inventory file for Ansible specifies a single host entry, "host1", with the IP address 130.193.35.32, and assigns the "devops" user for executing Ansible tasks.

## Playbook

This playbook runs tasks on all hosts, using a docker role with elevated privileges and specifying the SSH private key file with ansible_ssh_private_key_file.

## Role: docker

1. default/main.yml - sets up Docker and Docker Compose configurations.
2. handlers/main.yml - defines a handler to restart Docker via the service module.
3. tasks/install_compose.yml - installs Docker Compose with pip.
4. tasks/install_docker.yml - installs Docker on Debian using apt.
5. tasks/main.yml - updates the apt cache, installs Python3 and pip3, and runs tasks for installing Docker and Docker Compose.

## Ansible configuration (ansible.cfg)

Sets default parameters, specifying directories for playbooks, inventory, and roles while defining default user and SSH key settings to simplify playbook configuration.

## `ansible-playbook ansible/playbooks/dev/main.yml --diff`

```sh
PLAY [all] *******************************************************************

TASK [Gathering Facts] *************************************************************
ok: [host1]

TASK [docker : Apt update] *********************************************************
changed: [host1]

TASK [docker : Installation of python3 and pip3] ***********************************
ok: [host1]

TASK [docker : Install docker] *****************************************************
ok: [host1]

TASK [docker : Install docker compose] *********************************************
ok: [host1]

PLAY RECAP *************************************************************************
host1                      : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## `ansible-inventory -i ansible/inventory/yandex_cloud.yml --list`

```markdown
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_host": "130.193.35.32",
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
            "host1"
        ]
    }
}


```

## `ansible-inventory -i ansible/inventory/yandex_cloud.yml --graph`

```markdown
@all:
  |--@ungrouped:
  |  |--host1


```

## `ansible-playbook playbooks/dev/main.yaml`

```markfown

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [host1]

TASK [docker : Apt update] *****************************************************
changed: [host1]

TASK [docker : Installation of python3 and pip3] *******************************
ok: [host1]

TASK [docker : Install docker] *************************************************
ok: [host1]

TASK [docker : Install docker compose] *****************************************
ok: [host1]

TASK [web_app : Ensure Docker Installed] ***************************************
ok: [host1]

TASK [web_app : Apt Update Cache] **********************************************
changed: [host1]

TASK [web_app : Install Docker‑Image] ******************************************
ok: [host1]

TASK [web_app : Launch App Container] ******************************************
ok: [host1]

PLAY RECAP *********************************************************************
host1                      : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Executing playbook to deploy the role (last 50 lines) `ansible-playbook playbooks/dev/main.yaml`

```markdown
TASK [Gathering Facts] *********************************************************
ok: [host1]

TASK [Run Docker Role] *********************************************************
included: docker for host1

TASK [docker : Apt update] *****************************************************
changed: [host1]

TASK [docker : Installation of python3 and pip3] *******************************
ok: [host1]

TASK [docker : Install docker] *************************************************
ok: [host1]

TASK [docker : Install docker compose] *****************************************
ok: [host1]

TASK [Run web_app Role] ********************************************************
included: web_app for host1

TASK [docker : Apt update] *****************************************************
changed: [host1]

TASK [docker : Installation of python3 and pip3] *******************************
ok: [host1]

TASK [docker : Install docker] *************************************************
ok: [host1]

TASK [docker : Install docker compose] *****************************************
ok: [host1]

TASK [web_app : Ensure Docker Installed] ***************************************
ok: [host1]

TASK [web_app : Apt Update Cache] **********************************************
changed: [host1]

TASK [web_app : Install Docker‑Image] ******************************************
ok: [host1]

TASK [web_app : Launch App Container] ******************************************
ok: [host1]

TASK [web_app : Deploy Docker-Compose] *****************************************
ok: [host1]

PLAY RECAP *********************************************************************
host1                      : ok=16   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

