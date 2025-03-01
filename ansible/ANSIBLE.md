# Output
TASK [geerlingguy.docker : Add Docker repository.] *****************************
ok: [62.84.120.225]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [62.84.120.225]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
ok: [62.84.120.225]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [62.84.120.225]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
ok: [62.84.120.225]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [62.84.120.225]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [62.84.120.225]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [62.84.120.225]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [62.84.120.225]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [62.84.120.225]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [62.84.120.225]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [62.84.120.225]

TASK [web_app : Ensure Docker is running] **************************************
ok: [62.84.120.225]

TASK [web_app : Pull the Docker image] *****************************************
ok: [62.84.120.225]

TASK [web_app : Start the Docker container] ************************************
changed: [62.84.120.225]

PLAY RECAP *********************************************************************
62.84.120.225              : ok=17   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   