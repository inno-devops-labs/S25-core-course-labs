TASK [Gathering Facts] *********************************************************
ok: [vm]

TASK [docker : Install Docker] *************************************************
included: /Users/denisnesterov/Desktop/Innopolis/Third course second semester/Devops/Lab1/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm

TASK [docker : Install required system packages] *******************************
ok: [vm]

TASK [docker : Add Docker GPG apt Key] *****************************************
ok: [vm]

TASK [docker : Get Ubuntu release version] *************************************
ok: [vm]

TASK [docker : Add Docker Repository] ******************************************
ok: [vm]

TASK [docker : Install Docker] *************************************************
ok: [vm]

TASK [docker : Ensure Docker service is running] *******************************
ok: [vm]

TASK [docker : Ensure current user is added to docker group] *******************
ok: [vm]

TASK [docker : Install Docker Compose] *****************************************
included: /Users/denisnesterov/Desktop/Innopolis/Third course second semester/Devops/Lab1/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm

TASK [docker : Install Docker Compose.] ****************************************
ok: [vm]

TASK [web_app : Verify Docker is installed] ************************************
ok: [vm]

TASK [web_app : Display Docker version] ****************************************
ok: [vm] => {
    "msg": "Docker version 28.0.0, build f9ced58"
}

TASK [web_app : Pull the Docker image] *****************************************
ok: [vm]

TASK [web_app : Start the Docker container] ************************************
ok: [vm]

PLAY RECAP *********************************************************************
vm                         : ok=15   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

