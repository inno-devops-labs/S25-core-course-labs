# Ansible Documentation

This directory contains Ansible playbooks and roles for deploying Docker and the web application.

## Inventory

The inventory file `ansible/inventory/default_aws_ec2.yml` contains the details of the target hosts.

To list the inventory, run:

```sh
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
```

To visualize the inventory structure, run:

```bash
Copy
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
```

## Playbooks
- `ansible/playbooks/dev/main.yaml`: Playbook to deploy Docker and the web application.

## Roles
- `ansible/roles/docker`: Custom role to install and configure Docker and Docker Compose.
