```yml
PLAY [Setup Docker] *********************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
[WARNING]: Platform linux on host yandex_cloud is using the discovered Python interpreter at /usr/bin/python3.12, but future
installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_cloud]

TASK [geerlingguy.docker : Load OS-specific vars.] **************************************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
included: /Users/pupolina/Documents/Innopolis/DevOps_labs/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_cloud

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] **************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ****************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ***********************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **************************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure directory exists for /etc/apt/keyrings] ***************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Add Docker apt key.] *****************************************************************************************
changed: [yandex_cloud]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ******************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *********************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Add Docker repository.] **************************************************************************************
changed: [yandex_cloud]

TASK [geerlingguy.docker : Install Docker packages.] ************************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Install docker-compose plugin.] ******************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ******************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***********************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Configure Docker daemon options.] ****************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***************************************************************
ok: [yandex_cloud]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***********************************************

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Get docker group info using getent.] *************************************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ****************************************************
skipping: [yandex_cloud]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [yandex_cloud]

PLAY RECAP ******************************************************************************************************************************
yandex_cloud               : ok=14   changed=2    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   
```

```bash
ansible all -m ping

[WARNING]: Platform linux on host yandex_cloud is using the discovered Python interpreter at /usr/bin/python3.12, but future
installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
yandex_cloud | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.12"
    },
    "changed": false,
    "ping": "pong"
}
```