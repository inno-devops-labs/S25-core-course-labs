# Ansible Deployment Documentation

## Overview
This documentation covers the Ansible deployment process for the Moscow Time Web Applications.

## Role Structure

The `web_app` role has been created with the following structure:
```
web_app/
├── defaults/
│   └── main.yml           # Default variables
├── meta/
│   └── main.yml          # Role dependencies (docker)
├── tasks/
│   ├── main.yml          # Main tasks
│   └── 0-wipe.yml        # Cleanup tasks
└── templates/
    └── docker-compose.yml.j2  # Docker Compose template
```

## Deployment Process

The deployment is organized into several stages with proper tagging:
- `setup`: Docker environment setup
- `docker`: Docker-specific operations
- `deploy`: Application deployment
- `wipe`: Cleanup operations
- `app`: All application-related tasks

### Running the Deployment

Basic deployment:
```bash
ansible-playbook playbooks/dev/app_python/main.yaml
```

Selective execution with tags:
```bash
ansible-playbook playbooks/dev/app_python/main.yaml --tags docker,deploy
```

Wipe and redeploy:
```bash
ansible-playbook playbooks/dev/app_python/main.yaml --tags wipe -e "web_app_full_wipe=true"
```

## Latest Deployment Output

<details>
<summary>Click to expand</summary>

```
(venv) dante@dante-pc:~/PycharmProjects/fork-S25-core-course-labs/ansible$ ansible-playbook playbooks/dev/app_python/main.yaml

PLAY [Deploy Moscow Time Web Application] ********************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************************
[WARNING]: Platform linux on host ec2-instance is using the discovered Python interpreter at /usr/bin/python3.11, but future installation of another Python interpreter could change
the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [ec2-instance]

TASK [docker : Remove old versions] **************************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/remove_old_versions.yml for ec2-instance

TASK [docker : Remove conflicting packages] ******************************************************************************************************************************************
changed: [ec2-instance]

TASK [docker : Add repo] *************************************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/add_repo.yml for ec2-instance

TASK [docker : Update apt] ***********************************************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Install prerequisites for key addition] *******************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Add Docker apt repository key.] ***************************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Add Docker's official apt repository] *********************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Install Docker] *******************************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ec2-instance

TASK [docker : Install Docker and dependencies] **************************************************************************************************************************************
changed: [ec2-instance]

TASK [docker : Add user(s) to Docker group] ******************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/add_to_group.yml for ec2-instance

TASK [docker : Add user to docker group] *********************************************************************************************************************************************
ok: [ec2-instance] => (item=dante)

TASK [docker : Start docker on startup] **********************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/enable_on_boot.yml for ec2-instance

TASK [docker : Enable Docker service on boot] ****************************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Configure Docker security settings] ***********************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for ec2-instance

TASK [docker : Create docker config directory] ***************************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Configure Docker daemon security settings] ****************************************************************************************************************************
ok: [ec2-instance]

TASK [web_app : Include wipe tasks] **************************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for ec2-instance

TASK [web_app : Check if wipe is enabled] ********************************************************************************************************************************************
skipping: [ec2-instance]

TASK [web_app : Stop and remove containers] ******************************************************************************************************************************************
skipping: [ec2-instance]

TASK [web_app : Remove docker-compose file] ******************************************************************************************************************************************
skipping: [ec2-instance]

TASK [web_app : Clean up Docker system] **********************************************************************************************************************************************
skipping: [ec2-instance]

TASK [web_app : Install required packages] *******************************************************************************************************************************************
changed: [ec2-instance]

TASK [web_app : Ensure Docker service is running] ************************************************************************************************************************************
ok: [ec2-instance]

TASK [web_app : Create application directory] ****************************************************************************************************************************************
ok: [ec2-instance]

TASK [web_app : Template docker-compose file] ****************************************************************************************************************************************
ok: [ec2-instance]

TASK [web_app : Pull Docker image] ***************************************************************************************************************************************************
ok: [ec2-instance]

TASK [web_app : Deploy with docker-compose] ******************************************************************************************************************************************
changed: [ec2-instance]

PLAY RECAP ***************************************************************************************************************************************************************************
ec2-instance               : ok=24   changed=4    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
```

</details>

## Applications

The deployment process supports multiple applications:

1. Python Moscow Time App (Port 8000):
   - Image: dantetemplar/moscow-time-webapp:latest
   - Status: Running and healthy
   - Endpoint: /

2. Node.js Moscow Time App (Port 8001):
   - Image: dantetemplar/nodejs-time-webapp:latest
   - Status: Running
   - Endpoint: /

Both applications provide Moscow time in JSON format and are deployed using the same Ansible role with different configurations.