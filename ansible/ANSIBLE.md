PLAY [Install and Configure Docker] ********************************************

TASK [Gathering Facts] ********************************************************* ok: [yandex_instance]

TASK [docker : include_tasks] ************************************************** included: /home/Matvey/DevOps/ansible/roles/docker/tasks/install_docker.yml for yandex_instance

TASK [docker : Install required dependencies] ********************************** ok: [yandex_instance]

TASK [docker : Add Docker GPG key] ********************************************* ok: [yandex_instance]

TASK [docker : Add Docker repository] ****************************************** ok: [yandex_instance]

TASK [docker : Install Docker engine] ****************************************** ok: [yandex_instance]

TASK [docker : include_tasks] ************************************************** included: /home/Matvey/DevOps/ansible/roles/docker/tasks/install_compose.yml for yandex_instance

TASK [docker : Download Docker Compose] **************************************** fatal: [yandex_instance]: FAILED! => {"changed": false, "dest": "/usr/local/bin/docker-compose", "elapsed": 10, "gid": 0, "group": "root", "mode": "0754", "msg": "Request failed: ", "owner": "root", "size": 73529752, "state": "file", "uid": 0, "url": "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64"}

PLAY RECAP ********************************************************************* yandex_instance : ok=7 changed=0 unreachable=0 failed=1 skipped=0 rescued=0 ignored=0

{ "_meta": { "hostvars": { "yandex_instance": { "ansible_host": "158.160.92.149", "ansible_ssh_private_key_file": "~/keys/VMkey", "ansible_user": "matvey" } } }, "all": { "children": [ "ungrouped" ] }, "ungrouped": { "hosts": [ "yandex_instance" ] } }

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
ok: [yandex_instance]

TASK [docker : Ensure Docker service starts on boot] ***************************
ok: [yandex_instance]

TASK [docker : Add current user to Docker group] *******************************
ok: [yandex_instance]

TASK [web_app : Pull the Docker Image from Docker Hub] *************************
changed: [yandex_instance]

TASK [web_app : Stop and Remove Existing Container (if running)] ***************
changed: [yandex_instance]

TASK [web_app : Run the Docker Container] **************************************
changed: [yandex_instance]

TASK [web_app : Verify Running Containers] *************************************
changed: [yandex_instance]

TASK [web_app : Show Running Containers] ***************************************
ok: [yandex_instance] => {
    "running_containers.stdout": "CONTAINER ID   IMAGE                         COMMAND           CREATED        STATUS        PORTS                                       NAMES\n29be825e1bcc   matveyplat/flask-app:latest   \"python app.py\"   1 second ago   Up 1 second   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   web_app"
}

PLAY RECAP *********************************************************************
yandex_instance            : ok=15   changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

