# Ansible Deployment for Docker and Web App

This repository contains Ansible playbooks and roles for deploying Docker and a sample web application on a cloud VM.

## Setup

1. Install Ansible: `sudo apt install ansible`
2. Configure SSH keys for the cloud VM.
3. Run the playbook: `ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml`

## Roles

- **docker**: Installs Docker and Docker Compose.
- **web_app**: Deploys a web application using Docker Compose.

## One problem in starting:

The structure which was provided in the lab task, gives an error( 

ERROR! the role 'docker' was not found in /home/m/IdeaProjects/S25-core-course-labs/ansible/playbooks/dev/roles:/home/m/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/home/m/IdeaProjects/S25-core-course-labs/ansible/playbooks/dev

The error appears to be in '/home/m/IdeaProjects/S25-core-course-labs/ansible/playbooks/dev/main.yaml': line 6, column 7, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

    - geerlingguy.docker
    - docker
      ^ here


So I moved the roles folder into the /playbooks/dev/ and this helped

```bash
ansible-playbook ansible/playbooks/dev/main.yaml --diff
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [all] *********************************************************************
skipping: no hosts matched

PLAY RECAP *********************************************************************


```


```bash
ausage: ansible-playbook [-h] [--version] [-v] [--private-key PRIVATE_KEY_FILE] [-u REMOTE_USER] [-c CONNECTION] [-T TIMEOUT] [--ssh-common-args SSH_COMMON_ARGS] [--sftp-extra-args SFTP_EXTRA_ARGS]
                        [--scp-extra-args SCP_EXTRA_ARGS] [--ssh-extra-args SSH_EXTRA_ARGS] [-k | --connection-password-file CONNECTION_PASSWORD_FILE] [--force-handlers] [--flush-cache] [-b]
                        [--become-method BECOME_METHOD] [--become-user BECOME_USER] [-K | --become-password-file BECOME_PASSWORD_FILE] [-t TAGS] [--skip-tags SKIP_TAGS] [-C] [-D] [-i INVENTORY] [--list-hosts]
                        [-l SUBSET] [-e EXTRA_VARS] [--vault-id VAULT_IDS] [-J | --vault-password-file VAULT_PASSWORD_FILES] [-f FORKS] [-M MODULE_PATH] [--syntax-check] [--list-tasks] [--list-tags] [--step]
                        [--start-at-task START_AT_TASK]
                        playbook [playbook ...]
ansible-playbook: error: ambiguous option: --list could match --list-hosts, --list-tasks, --list-tags
 
usage: ansible-playbook [-h] [--version] [-v] [--private-key PRIVATE_KEY_FILE] [-u REMOTE_USER] [-c CONNECTION] [-T TIMEOUT] [--ssh-common-args SSH_COMMON_ARGS] [--sftp-extra-args SFTP_EXTRA_ARGS]
                        [--scp-extra-args SCP_EXTRA_ARGS] [--ssh-extra-args SSH_EXTRA_ARGS] [-k | --connection-password-file CONNECTION_PASSWORD_FILE] [--force-handlers] [--flush-cache] [-b]
                        [--become-method BECOME_METHOD] [--become-user BECOME_USER] [-K | --become-password-file BECOME_PASSWORD_FILE] [-t TAGS] [--skip-tags SKIP_TAGS] [-C] [-D] [-i INVENTORY] [--list-hosts]
                        [-l SUBSET] [-e EXTRA_VARS] [--vault-id VAULT_IDS] [-J | --vault-password-file VAULT_PASSWORD_FILES] [-f FORKS] [-M MODULE_PATH] [--syntax-check] [--list-tasks] [--list-tags] [--step]
                        [--start-at-task START_AT_TASK]
                        playbook [playbook ...]

Runs Ansible playbooks, executing the defined tasks on the targeted hosts.

positional arguments:
  playbook              Playbook(s)

options:
  --become-password-file BECOME_PASSWORD_FILE, --become-pass-file BECOME_PASSWORD_FILE
                        Become password file
  --connection-password-file CONNECTION_PASSWORD_FILE, --conn-pass-file CONNECTION_PASSWORD_FILE
                        Connection password file
  --flush-cache         clear the fact cache for every host in inventory
  --force-handlers      run handlers even if a task fails
  --list-hosts          outputs a list of matching hosts; does not execute anything else
  --list-tags           list all available tags
  --list-tasks          list all tasks that would be executed
  --skip-tags SKIP_TAGS
                        only run plays and tasks whose tags do not match these values. This argument may be specified multiple times.
  --start-at-task START_AT_TASK
                        start the playbook at the task matching this name
  --step                one-step-at-a-time: confirm each task before running
  --syntax-check        perform a syntax check on the playbook, but do not execute it
  --vault-id VAULT_IDS  the vault identity to use. This argument may be specified multiple times.
  --vault-password-file VAULT_PASSWORD_FILES, --vault-pass-file VAULT_PASSWORD_FILES
                        vault password file
  --version             show program's version number, config file location, configured module search path, module location, executable location and exit
  -C, --check           don't make any changes; instead, try to predict some of the changes that may occur
  -D, --diff            when changing (small) files and templates, show the differences in those files; works great with --check
  -J, --ask-vault-password, --ask-vault-pass
                        ask for vault password
  -K, --ask-become-pass
                        ask for privilege escalation password
  -M MODULE_PATH, --module-path MODULE_PATH
                        prepend colon-separated path(s) to module library (default={{ ANSIBLE_HOME ~ "/plugins/modules:/usr/share/ansible/plugins/modules" }}). This argument may be specified multiple times.
  -e EXTRA_VARS, --extra-vars EXTRA_VARS
                        set additional variables as key=value or YAML/JSON, if filename prepend with @. This argument may be specified multiple times.
  -f FORKS, --forks FORKS
                        specify number of parallel processes to use (default=5)
  -h, --help            show this help message and exit
  -i INVENTORY, --inventory INVENTORY, --inventory-file INVENTORY
                        specify inventory host path or comma separated host list. --inventory-file is deprecated. This argument may be specified multiple times.
  -k, --ask-pass        ask for connection password
  -l SUBSET, --limit SUBSET
                        further limit selected hosts to an additional pattern
  -t TAGS, --tags TAGS  only run plays and tasks tagged with these values. This argument may be specified multiple times.
  -v, --verbose         Causes Ansible to print more debug messages. Adding multiple -v will increase the verbosity, the builtin plugins currently evaluate up to -vvvvvv. A reasonable level to start is -vvv,
                        connection debugging might require -vvvv. This argument may be specified multiple times.

Connection Options:
  control as whom and how to connect to hosts

  --private-key PRIVATE_KEY_FILE, --key-file PRIVATE_KEY_FILE
                        use this file to authenticate the connection
  --scp-extra-args SCP_EXTRA_ARGS
                        specify extra arguments to pass to scp only (e.g. -l)
  --sftp-extra-args SFTP_EXTRA_ARGS
                        specify extra arguments to pass to sftp only (e.g. -f, -l)
  --ssh-common-args SSH_COMMON_ARGS
                        specify common arguments to pass to sftp/scp/ssh (e.g. ProxyCommand)
  --ssh-extra-args SSH_EXTRA_ARGS
                        specify extra arguments to pass to ssh only (e.g. -R)
  -T TIMEOUT, --timeout TIMEOUT
                        override the connection timeout in seconds (default depends on connection)
  -c CONNECTION, --connection CONNECTION
                        connection type to use (default=ssh)
  -u REMOTE_USER, --user REMOTE_USER
                        connect as this user (default=None)

Privilege Escalation Options:
  control how and which user you become as on target hosts

  --become-method BECOME_METHOD
                        privilege escalation method to use (default=sudo), use `ansible-doc -t become -l` to list valid choices.
  --become-user BECOME_USER
                        run operations as this user (default=root)
  -b, --become          run operations with become (does not imply password prompting)
```


```bash
usage: ansible-playbook [-h] [--version] [-v] [--private-key PRIVATE_KEY_FILE]
                        [-u REMOTE_USER] [-c CONNECTION] [-T TIMEOUT]
                        [--ssh-common-args SSH_COMMON_ARGS]
                        [--sftp-extra-args SFTP_EXTRA_ARGS]
                        [--scp-extra-args SCP_EXTRA_ARGS]
                        [--ssh-extra-args SSH_EXTRA_ARGS]
                        [-k | --connection-password-file CONNECTION_PASSWORD_FILE]
                        [--force-handlers] [--flush-cache] [-b]
                        [--become-method BECOME_METHOD]
                        [--become-user BECOME_USER]
                        [-K | --become-password-file BECOME_PASSWORD_FILE]
                        [-t TAGS] [--skip-tags SKIP_TAGS] [-C] [-D]
                        [-i INVENTORY] [--list-hosts] [-l SUBSET]
                        [-e EXTRA_VARS] [--vault-id VAULT_IDS]
                        [-J | --vault-password-file VAULT_PASSWORD_FILES]
                        [-f FORKS] [-M MODULE_PATH] [--syntax-check]
                        [--list-tasks] [--list-tags] [--step]
                        [--start-at-task START_AT_TASK]
                        playbook [playbook ...]
ansible-playbook: error: unrecognized arguments: --graph
 
usage: ansible-playbook [-h] [--version] [-v] [--private-key PRIVATE_KEY_FILE]
                        [-u REMOTE_USER] [-c CONNECTION] [-T TIMEOUT]
                        [--ssh-common-args SSH_COMMON_ARGS]
                        [--sftp-extra-args SFTP_EXTRA_ARGS]
                        [--scp-extra-args SCP_EXTRA_ARGS]
                        [--ssh-extra-args SSH_EXTRA_ARGS]
                        [-k | --connection-password-file CONNECTION_PASSWORD_FILE]
                        [--force-handlers] [--flush-cache] [-b]
                        [--become-method BECOME_METHOD]
                        [--become-user BECOME_USER]
                        [-K | --become-password-file BECOME_PASSWORD_FILE]
                        [-t TAGS] [--skip-tags SKIP_TAGS] [-C] [-D]
                        [-i INVENTORY] [--list-hosts] [-l SUBSET]
                        [-e EXTRA_VARS] [--vault-id VAULT_IDS]
                        [-J | --vault-password-file VAULT_PASSWORD_FILES]
                        [-f FORKS] [-M MODULE_PATH] [--syntax-check]
                        [--list-tasks] [--list-tags] [--step]
                        [--start-at-task START_AT_TASK]
                        playbook [playbook ...]

Runs Ansible playbooks, executing the defined tasks on the targeted hosts.

positional arguments:
  playbook              Playbook(s)

options:
  --become-password-file BECOME_PASSWORD_FILE, --become-pass-file BECOME_PASSWORD_FILE
                        Become password file
  --connection-password-file CONNECTION_PASSWORD_FILE, --conn-pass-file CONNECTION_PASSWORD_FILE
                        Connection password file
  --flush-cache         clear the fact cache for every host in inventory
  --force-handlers      run handlers even if a task fails
  --list-hosts          outputs a list of matching hosts; does not execute
                        anything else
  --list-tags           list all available tags
  --list-tasks          list all tasks that would be executed
  --skip-tags SKIP_TAGS
                        only run plays and tasks whose tags do not match these
                        values. This argument may be specified multiple times.
  --start-at-task START_AT_TASK
                        start the playbook at the task matching this name
  --step                one-step-at-a-time: confirm each task before running
  --syntax-check        perform a syntax check on the playbook, but do not
                        execute it
  --vault-id VAULT_IDS  the vault identity to use. This argument may be
                        specified multiple times.
  --vault-password-file VAULT_PASSWORD_FILES, --vault-pass-file VAULT_PASSWORD_FILES
                        vault password file
  --version             show program's version number, config file location,
                        configured module search path, module location,
                        executable location and exit
  -C, --check           don't make any changes; instead, try to predict some
                        of the changes that may occur
  -D, --diff            when changing (small) files and templates, show the
                        differences in those files; works great with --check
  -J, --ask-vault-password, --ask-vault-pass
                        ask for vault password
  -K, --ask-become-pass
                        ask for privilege escalation password
  -M MODULE_PATH, --module-path MODULE_PATH
                        prepend colon-separated path(s) to module library
                        (default={{ ANSIBLE_HOME ~
                        "/plugins/modules:/usr/share/ansible/plugins/modules"
                        }}). This argument may be specified multiple times.
  -e EXTRA_VARS, --extra-vars EXTRA_VARS
                        set additional variables as key=value or YAML/JSON, if
                        filename prepend with @. This argument may be
                        specified multiple times.
  -f FORKS, --forks FORKS
                        specify number of parallel processes to use
                        (default=5)
  -h, --help            show this help message and exit
  -i INVENTORY, --inventory INVENTORY, --inventory-file INVENTORY
                        specify inventory host path or comma separated host
                        list. --inventory-file is deprecated. This argument
                        may be specified multiple times.
  -k, --ask-pass        ask for connection password
  -l SUBSET, --limit SUBSET
                        further limit selected hosts to an additional pattern
  -t TAGS, --tags TAGS  only run plays and tasks tagged with these values.
                        This argument may be specified multiple times.
  -v, --verbose         Causes Ansible to print more debug messages. Adding
                        multiple -v will increase the verbosity, the builtin
                        plugins currently evaluate up to -vvvvvv. A reasonable
                        level to start is -vvv, connection debugging might
                        require -vvvv. This argument may be specified multiple
                        times.

Connection Options:
  control as whom and how to connect to hosts

  --private-key PRIVATE_KEY_FILE, --key-file PRIVATE_KEY_FILE
                        use this file to authenticate the connection
  --scp-extra-args SCP_EXTRA_ARGS
                        specify extra arguments to pass to scp only (e.g. -l)
  --sftp-extra-args SFTP_EXTRA_ARGS
                        specify extra arguments to pass to sftp only (e.g. -f,
                        -l)
  --ssh-common-args SSH_COMMON_ARGS
                        specify common arguments to pass to sftp/scp/ssh (e.g.
                        ProxyCommand)
  --ssh-extra-args SSH_EXTRA_ARGS
                        specify extra arguments to pass to ssh only (e.g. -R)
  -T TIMEOUT, --timeout TIMEOUT
                        override the connection timeout in seconds (default
                        depends on connection)
  -c CONNECTION, --connection CONNECTION
                        connection type to use (default=ssh)
  -u REMOTE_USER, --user REMOTE_USER
                        connect as this user (default=None)

Privilege Escalation Options:
  control how and which user you become as on target hosts

  --become-method BECOME_METHOD
                        privilege escalation method to use (default=sudo), use
                        `ansible-doc -t become -l` to list valid choices.
  --become-user BECOME_USER
                        run operations as this user (default=root)
  -b, --become          run operations with become (does not imply password
                        prompting)
```