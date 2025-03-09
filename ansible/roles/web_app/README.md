# Web Application Role

Deploys a web app using Docker Compose.

## Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `docker_image` | `myapp:latest` | Docker image name |
| `app_port` | `8080` | Host port mapping |
| `web_app_wipe` | `false` | Enable destructive cleanup |

## Usage
```yaml
- hosts: all
  roles:
    - role: web_app
  vars:
    docker_image: "custom_image:v1"
    app_port: 3000
   ```

# Deployment Commands

## Deploy with Wipe
```bash
ansible-playbook playbooks/dev/main.yaml -e "web_app_wipe=true" --tags webapp,wipe

```
## Output 
```text
TASK [docker : Install Docker dependencies] *************************************
ok: [host_01] => (item=apt-transport-https)
ok: [host_01] => (item=ca-certificates)
ok: [host_01] => (item=curl)
ok: [host_01] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] **********************************************
changed: [host_01]

TASK [docker : Add Docker repository] *******************************************
changed: [host_01]

TASK [docker : Install Docker] **************************************************
changed: [host_01] => {"changed": true, "version": "24.0.7"}

TASK [docker : Ensure Docker is enabled and started] ****************************
changed: [host_01]

TASK [docker : Add user to docker group] ****************************************
changed: [host_01] => {"name": "ubuntu", "groups": "docker"}

TASK [docker : Install Docker Compose] ******************************************
changed: [host_01] => {"dest": "/usr/local/bin/docker-compose", "url": "https://github.com/docker/compose/releases/download/v2.26.0/docker-compose-Linux-x86_64"}

TASK [web_app : Create app directory] *******************************************
changed: [host_01] => {"path": "/opt/web_app", "state": "directory"}

TASK [web_app : Deploy Docker Compose template] *********************************
--- before: /opt/web_app/docker-compose.yml (content)
+++ after: /opt/web_app/docker-compose.yml (content)
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  web:
+    image: "myapp:latest"
+    ports:
+      - "8080:80"
+    restart: always
+
changed: [host_01]

TASK [web_app : Start containers] ***********************************************
changed: [host_01] => {"changed": true, "output": "Creating network 'web_app_default'...\nCreating web_app_web_1..."}

RUNNING HANDLER [docker : restart docker] ***************************************
changed: [host_01]

PLAY RECAP **********************************************************************
host_01  : ok=12  changed=9   unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

#### 9. **Execute Playbook**
```bash
# Dry-run with tags
ansible-playbook playbooks/dev/main.yaml --tags webapp --check

# Full deployment
ansible-playbook playbooks/dev/main.yaml --tags webapp

# Wipe containers
ansible-playbook playbooks/dev/main.yaml -e "web_app_wipe=true" --tags wipe