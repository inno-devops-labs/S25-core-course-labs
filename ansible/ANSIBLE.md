# Deployment output

## To deploy playbook
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --ask-become-pass
```

## Last 50 lines of run

```

TASK [Gathering Facts] *********************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python
interpreter at /usr/bin/python3.10, but future installation of another Python
interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [docker : Include Docker installation tasks] ******************************
included: /home/fory/devops-labs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Clean apt cache] ************************************************
ok: [localhost]

TASK [docker : Update apt cache] ***********************************************
ok: [localhost]

TASK [docker : Install required packages] **************************************
ok: [localhost]

TASK [docker : Create Docker GPG directory] ************************************
ok: [localhost]

TASK [docker : Download Docker GPG key] ****************************************
ok: [localhost]

TASK [docker : Add Docker repository] ******************************************
ok: [localhost]

TASK [docker : Install Docker packages] ****************************************
ok: [localhost]

TASK [docker : Ensure Docker service is enabled and started] *******************
ok: [localhost]

TASK [docker : Add users to docker group] **************************************
skipping: [localhost]

TASK [docker : Add current user to docker group] *******************************
ok: [localhost]

TASK [docker : Include Docker Compose installation tasks] **********************
included: /home/fory/devops-labs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] ****************************************
ok: [localhost]

TASK [web_app : Pull Docker image] *********************************************
changed: [localhost]

TASK [web_app : Create and start Moscow Time container] ************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=15   changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  

```



