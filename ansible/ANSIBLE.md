
# Ansible related work

## Best practices

- Ansible-lint workflow

## Logs

Last lines of docker playbook:

```bash
PLAY [Dev playbook] *************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************
[WARNING]: Platform linux on host terraform-vm is using the discovered Python interpreter at /usr/bin/python3.10,
but future installation of another Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [terraform-vm]

TASK [docker : Install Docker] **************************************************************************************
included: /home/max/vscdir/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Update apt package index] ****************************************************************************
changed: [terraform-vm]

TASK [docker : Install required system packages] ********************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 65 not upgraded.
changed: [terraform-vm] => (item=apt-transport-https)
ok: [terraform-vm] => (item=ca-certificates)
ok: [terraform-vm] => (item=curl)
The following NEW packages will be installed:
  gnupg-agent
0 upgraded, 1 newly installed, 0 to remove and 65 not upgraded.
changed: [terraform-vm] => (item=gnupg-agent)
ok: [terraform-vm] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ***********************************************************************
changed: [terraform-vm]

TASK [docker : Add Docker's official apt repository] ****************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu jammy stable

changed: [terraform-vm]

TASK [docker : Install Docker and dependencies] *********************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 65 not upgraded.
changed: [terraform-vm] => (item=docker-ce)
ok: [terraform-vm] => (item=docker-ce-cli)
ok: [terraform-vm] => (item=containerd.io)

TASK [docker : Install Docker Compose] ******************************************************************************
included: /home/max/vscdir/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] ******************************************************************************
The following additional packages will be installed:
  python3-docker python3-dockerpty python3-docopt python3-dotenv
  python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
0 upgraded, 7 newly installed, 0 to remove and 65 not upgraded.
changed: [terraform-vm]

PLAY RECAP **********************************************************************************************************
terraform-vm               : ok=9    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739647398.970132 1543735 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

And docker is really enabled on the remote server:

```bash
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2025-02-15 19:22:36 UTC; 4min 35s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 185662 (dockerd)
      Tasks: 8
     Memory: 21.1M
        CPU: 509ms
     CGroup: /system.slice/docker.service
             └─185662 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```

the ansible-inventory -i inventory/yacloud_compute.yml --list command output is quite big, and first ~100 lines will be listed here:

```bash
{
    "_meta": {
        "hostvars": {
            "terraform-vm": {
                "ansible_all_ipv4_addresses": [
                    {
                        "__ansible_unsafe": "192.168.20.29"
                    }
                ],
                "ansible_all_ipv6_addresses": [
                    {
                        "__ansible_unsafe": "fe80::d20d:17ff:fea8:34c1"
                    }
                ],
                "ansible_apparmor": {
                    "status": {
                        "__ansible_unsafe": "enabled"
                    }
                },
                "ansible_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_bios_date": {
                    "__ansible_unsafe": "04/01/2014"
                },
                "ansible_bios_vendor": {
                    "__ansible_unsafe": "SeaBIOS"
                },
                "ansible_bios_version": {
                    "__ansible_unsafe": "1.16.3-1"
                },
                "ansible_board_asset_tag": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_board_name": {
                    "__ansible_unsafe": "xeon-e5-2660"
                },
                "ansible_board_serial": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_board_vendor": {
                    "__ansible_unsafe": "Yandex"
                },
                "ansible_board_version": {
                    "__ansible_unsafe": "pc-q35-yc-2.12"
                },
                "ansible_chassis_asset_tag": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_chassis_serial": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_chassis_vendor": {
                    "__ansible_unsafe": "Yandex"
                },
                "ansible_chassis_version": {
                    "__ansible_unsafe": "xeon-e5-2660"
                },
                "ansible_cmdline": {
                    "BOOT_IMAGE": {
                        "__ansible_unsafe": "/boot/vmlinuz-5.15.0-92-generic"
                    },
                    "biosdevname": {
                        "__ansible_unsafe": "0"
                    },
                    "console": {
                        "__ansible_unsafe": "ttyS0"
                    },
                    "net.ifnames": {
                        "__ansible_unsafe": "0"
                    },
                    "ro": true,
                    "root": {
                        "__ansible_unsafe": "UUID=ed465c6e-049a-41c6-8e0b-c8da348a3577"
                    }
                },
                "ansible_date_time": {
                    "date": {
                        "__ansible_unsafe": "2025-02-15"
                    },
                    "day": {
                        "__ansible_unsafe": "15"
                    },
                    "epoch": {
                        "__ansible_unsafe": "1739647244"
                    },
                    "epoch_int": {
                        "__ansible_unsafe": "1739647244"
                    },
                    "hour": {
                        "__ansible_unsafe": "19"
                    },
                    "iso8601": {
                        "__ansible_unsafe": "2025-02-15T19:20:44Z"
                    },
                    "iso8601_basic": {
                        "__ansible_unsafe": "20250215T192044772294"
                    },
                    "iso8601_basic_short": {
                        "__ansible_unsafe": "20250215T192044"
                    },
                    "iso8601_micro": {
                        "__ansible_unsafe": "2025-02-15T19:20:44.772294Z"
                    },
                    "minute": {
                        "__ansible_unsafe": "20"
                    },
                    "month": {
                        "__ansible_unsafe": "02"
                    },
                    "second": {
                        "__ansible_unsafe": "44"
                    },
                    "time": {
                        "__ansible_unsafe": "19:20:44"
                    },
                    "tz": {
                        "__ansible_unsafe": "UTC"
                    },
                    "tz_dst": {
                        "__ansible_unsafe": "UTC"
                    },
                    "tz_offset": {
                        "__ansible_unsafe": "+0000"
                    },
                    "weekday": {
                        "__ansible_unsafe": "Saturday"
                    },
                    "weekday_number": {
                        "__ansible_unsafe": "6"
                    },
                    "weeknumber": {
                        "__ansible_unsafe": "06"
                    },
                    "year": {
                        "__ansible_unsafe": "2025"
                    }
                },
                "ansible_default_ipv4": {
                    "address": {
                        "__ansible_unsafe": "192.168.20.29"
                    },
                    "alias": {
                        "__ansible_unsafe": "eth0"
                    },
                    "broadcast": {
                        "__ansible_unsafe": ""
```

## App deployment

```bash
TASK [docker : Add Docker's official GPG key] ********************************************************************************************************
ok: [terraform-vm]

TASK [docker : Add Docker's official apt repository] *************************************************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker and dependencies] ******************************************************************************************************
ok: [terraform-vm] => (item=docker-ce)
ok: [terraform-vm] => (item=docker-ce-cli)
ok: [terraform-vm] => (item=containerd.io)

TASK [docker : Install Docker Compose] ***************************************************************************************************************
included: /home/max/vscdir/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] ***************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Add user to docker group] *************************************************************************************************************
ok: [terraform-vm]

TASK [docker : Copy secure daemon.json to /etc/docker/] **********************************************************************************************
ok: [terraform-vm]

TASK [web_app : Full wipe] ***************************************************************************************************************************
included: /home/max/vscdir/S25-core-course-labs/ansible/roles/web_app/tasks/wipe.yml for terraform-vm

TASK [web_app : Check if app directory exists] *******************************************************************************************************
ok: [terraform-vm]

TASK [web_app : Wipe images] *************************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/app_python/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove
it to avoid potential confusion
changed: [terraform-vm]

TASK [web_app : Remove app directory] ****************************************************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/opt/app_python/",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/opt/app_python/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [terraform-vm]

TASK [web_app : Deploy dockerized app] ***************************************************************************************************************
included: /home/max/vscdir/S25-core-course-labs/ansible/roles/web_app/tasks/deploy.yml for terraform-vm

TASK [web_app : Create app directory] ****************************************************************************************************************
--- before
+++ after
@@ -1,6 +1,6 @@
 {
-    "group": 0,
-    "owner": 0,
+    "group": 1001,
+    "owner": 1000,
     "path": "/opt/app_python/",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform-vm]

TASK [web_app : Copy Docker Compose template] ********************************************************************************************************
--- before
+++ after: /home/max/.ansible/tmp/ansible-local-1701359kbf5cbep/tmpo7o8c0yv/docker-compose.yml.j2
@@ -0,0 +1,7 @@
+version: "3.9"
+services:
+  web:
+    image: "docker.io/elonmaxx/app_python:latest"
+    ports:
+      - target: "8080"
+        published: "8080"

changed: [terraform-vm]

TASK [web_app : Ensure docker service is OK] *********************************************************************************************************
ok: [terraform-vm]

TASK [web_app : Create and start the services] *******************************************************************************************************
changed: [terraform-vm]

PLAY RECAP *******************************************************************************************************************************************
terraform-vm               : ok=20   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

We may see it has really been deployed and site works:

```bash
$ curl xxx.xx.xx.xx:8080

    <!DOCTYPE html>
    <html>
    <head>
        <title>Time in Europe/Moscow</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f4f4f9;
                color: #333;
            }
            .time {
                font-size: 2em;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Current Time in Europe/Moscow</h1>
        <div class="time">2025-02-16 13:25:26 UTC+03:00</div>
    </body>
    </html>
```
