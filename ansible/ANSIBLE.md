# Ansible Docker Deployment

## Deployment output

```bash
PLAY [Deploy Web Application] ************************************************************

TASK [Gathering Facts] *******************************************************************
ok: [my_yandex_vm]

TASK [docker : Install required packages] ************************************************
ok: [my_yandex_vm]

TASK [docker : Create directory for APT keyrings (if missing)] ***************************
ok: [my_yandex_vm]

TASK [docker : Download and save Docker GPG key] *****************************************
ok: [my_yandex_vm]

TASK [docker : Add Docker repository] ****************************************************
ok: [my_yandex_vm]

TASK [docker : Update APT cache and install Docker] **************************************
ok: [my_yandex_vm]

TASK [docker : Start and enable Docker service] ******************************************
ok: [my_yandex_vm]

TASK [docker : Install Docker Compose] ***************************************************
ok: [my_yandex_vm]

TASK [docker : Verify Docker Compose installation] ***************************************
ok: [my_yandex_vm]

TASK [docker : Display installed Docker Compose version] *********************************
ok: [my_yandex_vm] => {
    "msg": "Installed Docker Compose version: Docker Compose version v2.33.0"
}

TASK [web_app : Pull the latest Docker image] ********************************************
changed: [my_yandex_vm]

TASK [web_app : Run the Docker container] ************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [my_yandex_vm]

PLAY RECAP *******************************************************************************
my_yandex_vm               : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory list output

```bash
{
    "_meta": {
        "hostvars": {
            "my_yandex_vm": {
                "ansible_host": "89.169.156.215",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/my-yandex-key.pub",
                "ansible_user": "nika"
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
            "my_yandex_vm"
        ]
    }
}
```

## Inventory graph output

```bash
@all:
  |--@ungrouped:
  |  |--my_yandex_vm
```

