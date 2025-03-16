# Web App Role

- Deploys your application container using Docker Compose.
    - Renders a Docker Compose file from a Jinja2 template.
    - Pulls the specified Docker image.
    - Starts the container using Docker Compose.
    - Includes wipe logic to remove previous deployments if enabled.
- Bonus CD Improvement:
  Two extra playbooks are provided:
    - `app_python/main.yaml` for the Python application.
    - `app_go/main.yaml` for the Go application.

## Playbook Usage

### Deploy the Python Application

```bash
  ansible-playbook playbooks/dev/app_python/main.yaml --tags web_app
```
Output:
```
mishagladyshev@Mishas-MacBook-Air ansible % ansible-playbook playbooks/dev/app_python/main.yml --tags web_app     

PLAY [Deploy Python Application using Docker Compose] ***************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************
[WARNING]: Platform linux on host vm-1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-1]
[WARNING]: Platform linux on host vm-2 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-2]

TASK [web_app : Create deployment directory for web_app] ************************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

TASK [web_app : Render Docker Compose template for the application] *************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

TASK [web_app : Pull Docker image for the application] **************************************************************************************************************************************************
ok: [vm-1]
ok: [vm-2]

TASK [web_app : Start the application container using Docker Compose] ***********************************************************************************************************************************
changed: [vm-2]
changed: [vm-1]

PLAY RECAP **********************************************************************************************************************************************************************************************
vm-1                       : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vm-2                       : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    
```

![Python](assets/app_python.png "Python application (Moscow Time)"))

### Deploy the Go Application
```bash
ansible-playbook playbooks/dev/app_golang/main.yaml --tags web_app
```
Output:
```
mishagladyshev@Mishas-MacBook-Air ansible % ansible-playbook playbooks/dev/app_go/main.yml --tags web_app

PLAY [Deploy Go Application using Docker Compose] *******************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************************
[WARNING]: Platform linux on host vm-1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-1]
[WARNING]: Platform linux on host vm-2 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that path.
See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [vm-2]

TASK [web_app : Create deployment directory for web_app] ************************************************************************************************************************************************
changed: [vm-1]
changed: [vm-2]

TASK [web_app : Render Docker Compose template for the application] *************************************************************************************************************************************
changed: [vm-1]
changed: [vm-2]

TASK [web_app : Pull Docker image for the application] **************************************************************************************************************************************************
changed: [vm-1]
changed: [vm-2]

TASK [web_app : Start the application container using Docker Compose] ***********************************************************************************************************************************
changed: [vm-2]
changed: [vm-1]

PLAY RECAP **********************************************************************************************************************************************************************************************
vm-1                       : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vm-2                       : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

![Go](assets/app_go.png "Golang application (Fork Counter)")

## Best Practices
- Block-based tasks.
- By role dependency mechanic, we can be sure that docker is installed before deployment.
- Tags are used to allow selective execution.
