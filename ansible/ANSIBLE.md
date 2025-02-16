
PLAY [Install and Configure Docker] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_instance]

TASK [docker : include_tasks] **************************************************
included: /home/Matvey/DevOps/ansible/roles/docker/tasks/install_docker.yml for yandex_instance

TASK [docker : Install required dependencies] **********************************
ok: [yandex_instance]

TASK [docker : Add Docker GPG key] *********************************************
ok: [yandex_instance]

TASK [docker : Add Docker repository] ******************************************
ok: [yandex_instance]

TASK [docker : Install Docker engine] ******************************************
ok: [yandex_instance]

TASK [docker : include_tasks] **************************************************
included: /home/Matvey/DevOps/ansible/roles/docker/tasks/install_compose.yml for yandex_instance

TASK [docker : Download Docker Compose] ****************************************
fatal: [yandex_instance]: FAILED! => {"changed": false, "dest": "/usr/local/bin/docker-compose", "elapsed": 10, "gid": 0, "group": "root", "mode": "0754", "msg": "Request failed: <urlopen error timed out>", "owner": "root", "size": 73529752, "state": "file", "uid": 0, "url": "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64"}

PLAY RECAP *********************************************************************
yandex_instance            : ok=7    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

{
    "_meta": {
        "hostvars": {
            "yandex_instance": {
                "ansible_host": "158.160.92.149",
                "ansible_ssh_private_key_file": "~/keys/VMkey",
                "ansible_user": "matvey"
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
            "yandex_instance"
        ]
    }
}
