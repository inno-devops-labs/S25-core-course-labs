# Docker deployment

## Output of  `ansible-playbook playbooks/dev/main.yaml --diff`, last 50 lines

```bash
(venv) ➜  ansible git:(lab-4) ✗ ansible-playbook playbooks/dev/main.yaml --diff | tail -n 50
[WARNING]: Platform linux on host witty_amalthea is using the discovered Python
interpreter at /usr/bin/python3.10, but future installation of another Python
interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.

PLAY [Install docker on VM] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [witty_amalthea]

TASK [docker : include_tasks] **************************************************
included: /Users/wensiet/PycharmProjects/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for witty_amalthea

TASK [docker : Update apt packages] ********************************************
changed: [witty_amalthea]

TASK [docker : Install prequisites] ********************************************
ok: [witty_amalthea]

TASK [docker : Make keyrings] **************************************************
changed: [witty_amalthea]

TASK [docker : Add GPG] ********************************************************
ok: [witty_amalthea]

TASK [docker : Add repository] *************************************************
ok: [witty_amalthea]

TASK [docker : Install Docker packages] ****************************************
ok: [witty_amalthea]

TASK [docker : Check if Docker service is enabled] *****************************
ok: [witty_amalthea]

TASK [docker : Add current user to docker group] *******************************
ok: [witty_amalthea]

TASK [docker : include_tasks] **************************************************
included: /Users/wensiet/PycharmProjects/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for witty_amalthea

TASK [docker : Install Docker packages] ****************************************
ok: [witty_amalthea]

TASK [docker : Check if Docker service is enabled] *****************************
ok: [witty_amalthea]

PLAY RECAP *********************************************************************
witty_amalthea             : ok=13   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Command `ansible-inventory --list`

```bash
(venv) ➜  ansible git:(lab-4) ✗ ansible-inventory --list
{
    "_meta": {
        "hostvars": {
            "witty_amalthea": {
                "ansible_host": "212.60.20.87",
                "ansible_user": "root"
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
            "witty_amalthea"
        ]
    }
}
```

## Command `ansible-inventor --graph`

```bash
(venv) ➜  ansible git:(lab-4) ✗ ansible-inventory --graph
@all:
  |--@ungrouped:
  |  |--witty_amalthea
```

## Explanation

Inventory commands displays that I have a server with name `witty_amalthea`, with some IP
and default root user. It is not grouped.
