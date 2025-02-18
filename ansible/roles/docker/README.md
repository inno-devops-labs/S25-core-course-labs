# Docker Role

This role installs Docker on a remote machine.

## Requirements

- The remote machine should be accessible via SSH.
- Ansible version 2.x or higher is required.
- `sudo` privileges are required on the target machine. You will be prompted to enter the `BECOME` password (usually the password for `sudo`), so make sure you have access to it.


## Role Variables

This role can be customized using the following variables:

- `docker_version`: The version of Docker to install. (Default is the latest version available from the repository.)

Example in `defaults/main.yml`:
```yaml
docker_version: latest
```
### Dependencies
None.

## Example Playbook
This role can be used in a playbook to install Docker on the remote machines:

``` yaml
---
- name: Install Docker on localhost
  hosts: all
  become: yes
  roles:
    - docker
```

## Installation
To use this role, clone the repository and include it in your playbook like shown in the example above.

## Testing the Installation
After running the playbook, verify Docker is installed by executing the following command on the remote machine:

``` bash
docker --version
```
You should see the installed Docker version output, similar to:

```bash
Docker version 26.1.3, build 26.1.3-0ubuntu1~22.04.1
```
### Important Notes
During playbook execution, you will be prompted for the BECOME password (usually your sudo password). This is required to install Docker and perform privileged operations on the target machine.

If you see any issues related to sudo permissions, ensure your user has sudo privileges.

## Troubleshooting
If Docker isn't installed successfully, ensure that:

The target machine has a stable internet connection to download Docker.

You have the necessary sudo privileges on the target machine.

Check the playbook logs for any error messages related to permission or network issues.
