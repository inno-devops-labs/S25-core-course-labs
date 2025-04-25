# Ansible Playbook Execution:

```bash
tjann@fedora:~/DevOps-Course/ansible$ ansible-playbook playbooks/dev/main.yaml

PLAY [Deploy Python Container] *****************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change
the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm]

TASK [web_app : Include wipe tasks] ************************************************************************************************************************************************
included: /home/tjann/DevOps-Course/ansible/roles/web_app/tasks/0-wipe.yml for yandex_vm

TASK [web_app : Stop and remove containers] ****************************************************************************************************************************************
[WARNING]: Cannot parse event from non-JSON line: b'WARNING: Error parsing config file (/root/.docker/config.json): Invalid auth configuration file'. Please report this at
https://github.com/ansible-collections/community.docker/issues/new?assignees=&labels=&projects=&template=bug_report.md
[WARNING]: Docker compose: unknown None: /opt/python-app/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
ok: [yandex_vm]

TASK [web_app : Remove application directory] **************************************************************************************************************************************
changed: [yandex_vm]

TASK [web_app : Remove Docker image] ***********************************************************************************************************************************************
changed: [yandex_vm]

TASK [web_app : Create application directory] **************************************************************************************************************************************
changed: [yandex_vm]

TASK [web_app : Template docker-compose.yml] ***************************************************************************************************************************************
changed: [yandex_vm]

TASK [web_app : Create Docker config directory] ************************************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Configure Docker credentials] **************************************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Wait for Docker daemon] ********************************************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Pull application image] ********************************************************************************************************************************************
changed: [yandex_vm]

TASK [web_app : Create deployment directory for web_app] ***************************************************************************************************************************
changed: [yandex_vm]

TASK [web_app : Start the application container using Docker Compose] **************************************************************************************************************
changed: [yandex_vm]

PLAY RECAP *************************************************************************************************************************************************************************
yandex_vm                  : ok=13   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

Afterwards, the user can request the port via VM's terminal:

```bash
tjann@fhmm5i5qjoo0bl0si2gd:~$ curl localhost:5005
<!DOCTYPE html>
<h1>Moscow Time: 23:12:00 Moscow</h1>
<h2>Your Timezone: 20:12:00 </h2>
```

