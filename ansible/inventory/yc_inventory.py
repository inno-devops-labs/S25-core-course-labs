#!/usr/bin/env python3
import json
import subprocess

# Specified cloud ID and folder ID
CLOUD_ID = "b1gqusmi8utuinc6cd8e"
FOLDER_ID = "b1gkfrhnhk61qtbtp02m"
def get_instances():
    """Fetch instances from Yandex Cloud."""
    command = [
        "yc", "compute", "instance", "list",
        "--cloud-id", CLOUD_ID,
        "--folder-id", FOLDER_ID,
        "--format=json"
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("Error fetching instances:", result.stderr)
        return []

    return json.loads(result.stdout)

def generate_inventory():
    """Generate Ansible dynamic inventory JSON."""
    instances = get_instances()
    inventory = {
        "_meta": {"hostvars": {}},
        "all": {"hosts": []}
    }

    for instance in instances:
        if "network_interfaces" in instance and instance["network_interfaces"]:
            ip = instance["network_interfaces"][0]["primary_v4_address"]["one_to_one_nat"]["address"]

            if ip:
                inventory["all"]["hosts"].append(ip)
                inventory["_meta"]["hostvars"][ip] = {
                    "ansible_host": ip,
                    "ansible_user": "yc-user",
                    "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                    "instance_name": instance["name"]
                }

    return json.dumps(inventory, indent=4)

if __name__ == "__main__":
    print(generate_inventory())
