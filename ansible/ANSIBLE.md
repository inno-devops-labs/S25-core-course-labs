# Ansible and Docker Deployment docs


## Executing Playbook
To execute the playbook for deploying docker, run:
```bash
ansible-playbook -i inventory/hosts.yml playbooks/dev/main.yaml -K
```

```bash
BECOME password: 
[DEPRECATION WARNING]: community.general.yaml has been deprecated. The plugin has been superseded by the the option `result_format=yaml` in callback plugin ansible.builtin.default from ansible-core 2.13 onwards. This feature will be 
removed from community.general in version 13.0.0. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
 _______________________
< PLAY [Install Docker] >
 -----------------------
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

The authenticity of host '89.169.132.160 (89.169.132.160)' can't be established.
ED25519 key fingerprint is SHA256:xvHZPTE50EhukxvDfpV4Am8OHUhb5uabYXvCztUi0+4.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Enter passphrase for key '/home/artyom/.ssh/id_ed25519': 
ok: [server]
 _______________________________________
< TASK [docker : Install Docker Engine] >
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

included: /home/artyom/projects/S25-DevOps-labs/ansible/roles/docker/tasks/install_docker.yml for server
 ___________________________________________
< TASK [docker : Install required packages] >
 -------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 ____________________________________________________
< TASK [docker : Create /etc/apt/keyrings directory] >
 ----------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

ok: [server]
 __________________________________________
< TASK [docker : Download Docker GPG keys] >
 ------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 ____________________________________________________
< TASK [docker : Add +r perm for installed GPG keys] >
 ----------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 ______________________________________________________
< TASK [docker : Check if docker repo file is present] >
 ------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

ok: [server]
 ______________________________________________________
< TASK [docker : Add docker repository to Apt sources] >
 ------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 _________________________________________
< TASK [docker : Install docker packages] >
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 ______________________________________________
< TASK [docker : Add user to the Docker group] >
 ----------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [server]
 ________________________________________
< TASK [docker : Install Docker Compose] >
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

included: /home/artyom/projects/S25-DevOps-labs/ansible/roles/docker/tasks/install_compose.yml for server
 ________________________________________
< TASK [docker : Install Docker compose] >
 ----------------------------------------
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

server                     : ok=12   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory details

- Output of `ansible-inventory -i inventory/hosts.yml --list`

```bash
{
    "_meta": {
        "hostvars": {
            "server": {
                "ansible_host": "89.169.132.160",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "ubuntu"
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
            "server"
        ]
    }
}
```

- Output of `ansible-inventory -i inventory/hosts.yml --graph`

```bash
@all:
  |--@ungrouped:
  |  |--server
```
