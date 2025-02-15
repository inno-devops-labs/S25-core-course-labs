
TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [docker : include_tasks] **************************************************
included: /home/utkanos/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install prerequisites] ******************************************
ok: [localhost]

TASK [docker : Add Docker GPG key] *********************************************
ok: [localhost]

TASK [docker : Add Docker repository] ******************************************
changed: [localhost]

TASK [docker : Install Docker] *************************************************
ok: [localhost]

TASK [docker : Ensure Docker service is enabled and running] *******************
changed: [localhost]

TASK [docker : Add users to the Docker group] **********************************
skipping: [localhost]

TASK [docker : Verify Docker installation] *************************************
skipping: [localhost]

TASK [docker : Display Docker version] *****************************************
ok: [localhost] => {
    "msg": ""
}

TASK [docker : include_tasks] **************************************************
included: /home/utkanos/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] ****************************************
changed: [localhost]

TASK [docker : Verify Docker Compose installation] *****************************
skipping: [localhost]

TASK [docker : Display Docker Compose version] *********************************
ok: [localhost] => {
    "msg": ""
}

PLAY RECAP *********************************************************************
localhost                  : ok=11   changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   

