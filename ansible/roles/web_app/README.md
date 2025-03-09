# Web_App Role

This role sets up and deploys a web application using Docker container.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `image_name`: docker image for the application (default: `jodak628286/python_app`)
- `image_tag`: tag of the Docker image (default: `latest`)
- `container_name`: name of the Docker container (default: `python-app`)
- `app_dir`: directory where application files will be stored (default: `/opt/{{ container_name }}`)
- `restart_policy`: service restart policy (default: `always`)
- `web_app_full_wipe`: enable complete removal of application (default: `false`)

## Dependencies

The role depends on the Docker role, which must be installed first. The dependency is automatically handled through:

```yaml
dependencies:
  - role: docker
```

## Example Playbook

Basic usage:

```yaml
hosts: all
become: true
roles:
  - docker
  - web_app
```

## Role Tasks

The role performs 2 main tasks:

1. Application Deployment:

- Creates application directory
- Configures Docker Compose template
- Starts services using Docker Compose

2. Application Cleanup (when web_app_full_wipe is true):

- Stops running container
- Removes Docker image
- Cleans up application files (including docker artefacts)

## Tags

Available tags for task execution:

- `app`: All application-related tasks
- `deploy`: Deployment tasks
- `compose`: Docker Compose tasks
- `start`: Container start
- `wipe`: Cleanup operations

## Usage

**To deploy the application:**

```bash
ansible-playbook -i inventory/hosts.yml playbooks/dev/main.yaml --tags "deploy"
```

Example output:

```bash
 ___________________________
< PLAY [Deploy Application] >
 ---------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

 ________________________
< TASK [Gathering Facts] >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

Enter passphrase for key '/home/artyom/.ssh/id_ed25519': 
ok: [server]
 _________________________________________
< TASK [web_app : Create application dir] >
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

ok: [server]
 ____________________________________________________________
/ TASK [web_app : Add Docker Compose template to application \
\ dir]                                                       /
 ------------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

ok: [server]
 ______________________________________________________
< TASK [web_app : Start services using Docker Compose] >
 ------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 ____________
< PLAY RECAP >
 ------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

server                     : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

Validating result:

```bash
`--> curl 89.169.132.160
<!DOCTYPE html>
<html>
    <head>
        <title>Current Time In Moscow</title>
    </head>
    <body>
        <h2>Current time (Europe/Moscow): 2025-03-02 16:42:17 MSK</h2>
    </body>
```

**To remove the application:**

```bash
ansible-playbook -i inventory/hosts.yml playbooks/dev/main.yaml --tags "wipe" -e "web_app_full_wipe=true"
```

Example output:

```bash
 ___________________________
< PLAY [Deploy Application] >
 ---------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

 ________________________
< TASK [Gathering Facts] >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

ok: [server]
 _______________________________________________
< TASK [web_app : Remove application container] >
 -----------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 ______________________________________
< TASK [web_app : Remove Docker image] >
 --------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 _______________________________________________
< TASK [web_app : Remove all application files] >
 -----------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server] => (item=/opt/python-app)
ok: [server] => (item=/var/lib/docker/containers/python-app)
 ____________
< PLAY RECAP >
 ------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

server                     : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

Validating result:

```bash
`--> curl 89.169.132.160
curl: (7) Failed to connect to 89.169.132.160 port 80 after 8 ms: Could not connect to server
```
