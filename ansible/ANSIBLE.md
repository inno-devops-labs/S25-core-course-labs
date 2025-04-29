# Ansible

## Best Practices

1. Tasks have explanatory names

## Deployment

### `ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml`

![alt text](image.png)

### `ansible-inventory -i inventory --list`

![alt text](image-1.png)

## app_python deployment

### `ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/app_python/main.yaml`

![alt text](image-2.png)