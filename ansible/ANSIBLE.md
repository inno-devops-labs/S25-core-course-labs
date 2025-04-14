# Ansible

## Best practices

- Use `ansible-lint` to enforce coding standards and detect potential issues.
- Mostly use the `ansible.builtin` namespace for better compatibility.
- Always specify the state parameter explicitly to avoid unintended behavior.
- Always provide name attributes for all tasks.
- Use `fact caching` (configured in ansible.cfg) to improve performance.

## Local Ansible usage

- To run ansible fully autonomly, I used Docker container with ssh-server.
You can find `Dockerfile` and `docker-compose.yml` at `ansible/misc`.
This setup requires running with root priveledged to install Docker-inside-Docker.

To run container use

```bash
sudo docker-compose up --build -d
```

## Lab 5, Task 1: Initial setup + deploy docker with `geerlingguy.docker` role

- Install role using `ansible-galaxy`

```bash
ansible-galaxy install geerlingguy.docker
```

- Create playbook: see `playbooks/dev/geerlingguy_docker.yaml`

- Check playbook syntax

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/geerlingguy_docker.yaml --syntax-check

playbook: playbooks/dev/geerlingguy_docker.yaml
```

- Run a playbook

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/geerlingguy_docker.yaml

... [trimmed lines]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Add Docker repository.] ******************************************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Install Docker packages.] ****************************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ****************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **********************************************************************************************
ok: [test_host]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ***************************************************************************************************************************
changed: [test_host]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************************************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ********************************************************************************************
skipping: [test_host]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************
skipping: [test_host]

PLAY RECAP **********************************************************************************************************************************************************************
test_host                  : ok=15   changed=6    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   

```

## Lab 5, Task 2: Custom Docker Role

### Deployment output

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/main.yaml --syntax-check

playbook: playbooks/dev/main.yaml
```

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/main.yaml --diff

PLAY [all] **********************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [test_host]

TASK [docker : Include tasks to install Docker] *********************************************************************************************************************************
included: /home/raleksan/projects/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for test_host

TASK [docker : Update apt package index] ****************************************************************************************************************************************
ok: [test_host]

TASK [docker : Install required system packages] ********************************************************************************************************************************
ok: [test_host] => (item=apt-transport-https)
ok: [test_host] => (item=ca-certificates)
ok: [test_host] => (item=curl)
ok: [test_host] => (item=gnupg-agent)
ok: [test_host] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ***********************************************************************************************************************************
ok: [test_host]

TASK [docker : Add Docker's official apt repository] ****************************************************************************************************************************
ok: [test_host]

TASK [docker : Install Docker and dependencies] *********************************************************************************************************************************
ok: [test_host] => (item=docker-ce)
ok: [test_host] => (item=docker-ce-cli)
ok: [test_host] => (item=containerd.io)

TASK [docker : Include tasks to install Docker Compose] *************************************************************************************************************************
included: /home/raleksan/projects/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for test_host

TASK [docker : Download Docker Compose] *****************************************************************************************************************************************
ok: [test_host]

TASK [docker : Include tasks to configure Docker] *******************************************************************************************************************************
included: /home/raleksan/projects/S25-core-course-labs/ansible/roles/docker/tasks/configure_docker.yml for test_host

TASK [docker : Add user to docker group] ****************************************************************************************************************************************
ok: [test_host]

TASK [docker : Configure Docker daemon security] ********************************************************************************************************************************
ok: [test_host]

TASK [docker : Detect init system] **********************************************************************************************************************************************
ok: [test_host]

TASK [docker : Enable Docker service (Systemd only)] ****************************************************************************************************************************
skipping: [test_host]

TASK [docker : Restart Docker (Systemd only)] ***********************************************************************************************************************************
skipping: [test_host]

TASK [docker : Restart Docker (Service)] ****************************************************************************************************************************************
changed: [test_host]

PLAY RECAP **********************************************************************************************************************************************************************
test_host                  : ok=14   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

```

### Inventory details

- `ansible-inventory -i inventory/local.yml --list`

```bash
~ ansible-inventory -i inventory/local.yml --list | tail -n 50
                },
                "ansible_user_shell": {
                    "__ansible_unsafe": "/bin/bash"
                },
                "ansible_user_uid": 0,
                "ansible_userspace_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_userspace_bits": {
                    "__ansible_unsafe": "64"
                },
                "ansible_virtualization_role": {
                    "__ansible_unsafe": "guest"
                },
                "ansible_virtualization_tech_guest": [
                    {
                        "__ansible_unsafe": "container"
                    },
                    {
                        "__ansible_unsafe": "docker"
                    }
                ],
                "ansible_virtualization_tech_host": [
                    {
                        "__ansible_unsafe": "kvm"
                    }
                ],
                "ansible_virtualization_type": {
                    "__ansible_unsafe": "docker"
                },
                "gather_subset": [
                    {
                        "__ansible_unsafe": "all"
                    }
                ],
                "module_setup": true
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
            "test_host"
        ]
    }
}
```

- `ansible-inventory -i inventory/local.yml --graph`

```bash
~ ansible-inventory -i inventory/local.yml --graph 
@all:
  |--@ungrouped:
  |  |--test_host
```

## Lab 5, Bonus task

### Dynamic inventory

Not possible for me without cloud service.  `(ㆆ _ ㆆ)`

### Secure Docker Configuration

I configured `daemon.json` in `tasks/configure_docker.yml`:

```json
{
    "no-new-privileges": true,
    "userns-remap": "default",
    "restart": "always",
}
```

This ensures that Docker containers run without root privileges.

## Lab 6, deploy `app_pyhton` application

```bash
~ ansible-playbook -i inventory/local.yml playbooks/dev/app_python.yaml

... [trimmed lines]

TASK [docker : Configure Docker daemon security] ********************************************************************************************************************************
ok: [test_host]

TASK [docker : Detect init system] **********************************************************************************************************************************************
ok: [test_host]

TASK [docker : Enable Docker service (Systemd only)] ****************************************************************************************************************************
skipping: [test_host]

TASK [docker : Restart Docker (Systemd only)] ***********************************************************************************************************************************
skipping: [test_host]

TASK [docker : Restart Docker (Service)] ****************************************************************************************************************************************
changed: [test_host]

TASK [web_app : Check if Docker is installed] ***********************************************************************************************************************************
ok: [test_host]

TASK [web_app : Fail if Docker is not installed] ********************************************************************************************************************************
skipping: [test_host]

TASK [web_app : Create app directory] *******************************************************************************************************************************************
changed: [test_host]

TASK [web_app : Copy Docker Compose template] ***********************************************************************************************************************************
changed: [test_host]

TASK [web_app : Ensure docker service is active] ********************************************************************************************************************************
changed: [test_host]

TASK [web_app : Create and start the application services] **********************************************************************************************************************
changed: [test_host]

TASK [web_app : Check if web app directory exists] ******************************************************************************************************************************
skipping: [test_host]

TASK [web_app : Stop and remove the web app container] **************************************************************************************************************************
skipping: [test_host]

TASK [web_app : Remove app sources] *********************************************************************************************************************************************
skipping: [test_host]

PLAY RECAP **********************************************************************************************************************************************************************
test_host                  : ok=19   changed=5    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0   

```

## Lab 6, deploy `app_rust_distroless` application with tag `deploy`

```bash
ansible-playbook -i inventory/local.yml playbooks/dev/app_rust.yaml -t deploy

PLAY [Deploy app_rust] **********************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [test_host]

TASK [web_app : Create app directory] *******************************************************************************************************************************************
ok: [test_host]

TASK [web_app : Copy Docker Compose template] ***********************************************************************************************************************************
ok: [test_host]

TASK [web_app : Ensure docker service is active] ********************************************************************************************************************************
changed: [test_host]

TASK [web_app : Create and start the application services] **********************************************************************************************************************
ok: [test_host]

PLAY RECAP **********************************************************************************************************************************************************************
test_host                  : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Lab 6, running docker containers list

```bash
~ docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED             STATUS         PORTS                                         NAMES
af644b5a4628   raleksan/app_python:v0.1            "gunicorn --bind 0.0…"   2 minutes ago       Up 2 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp     app_python-web-1
0f733bfda9f8   raleksan/app_rust_distroless:v0.1   "./app"                  2 minutes ago       Up 2 minutes   0.0.0.0:8001->8000/tcp, [::]:8001->8000/tcp   app_rust_distroless-web-1
```

## Lab 6, Get HTML responce on host

- For `app_python`

```bash
~ curl localhost:8000
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moscow Time</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to bottom, #1e3c72, #2a5298);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }
        .container {
            max-width: 600px;
            width: 100%;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .time {
            font-size: 5rem;
            font-weight: bold;
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <p id="time" class="time">10:03:53 08.02.2025</p>
        <h1>Moscow Time</h1>
    </div>
</body>
</html>
```

- For `app_rust`

```bash
~ curl localhost:8001
<h1>Current time in Moscow: 2025-02-08 10:03:37</h1>
```

## Lab 6, Bonus Task: CD Improvement

I used my `web_app` role for both `app_python` and `app_rust` application:

```bash
.
`--ansible
    `-- playbooks
        `-- dev
            |-- app_python.yaml
            |
            `-- app_rust.yaml
```
