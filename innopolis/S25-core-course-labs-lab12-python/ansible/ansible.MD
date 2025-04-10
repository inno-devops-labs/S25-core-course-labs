
TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *************************************************************
task path: /Users/almazgaazov/.ansible/roles/geerlingguy.docker/tasks/main.yml:76
META: triggered running handlers for yandex_vm

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************
task path: /Users/almazgaazov/.ansible/roles/geerlingguy.docker/tasks/main.yml:79
skipping: [yandex_vm] => {
    "changed": false,
    "false_condition": "docker_install_compose | bool",
    "skip_reason": "Conditional result was False"
}

TASK [geerlingguy.docker : Get docker group info using getent.] ***************************************************************************************
task path: /Users/almazgaazov/.ansible/roles/geerlingguy.docker/tasks/main.yml:82
skipping: [yandex_vm] => {
    "changed": false,
    "false_condition": "docker_users | length > 0",
    "skip_reason": "Conditional result was False"
}

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ******************************************************************
task path: /Users/almazgaazov/.ansible/roles/geerlingguy.docker/tasks/main.yml:89
skipping: [yandex_vm] => {
    "changed": false,
    "skipped_reason": "No items in the list"
}

TASK [geerlingguy.docker : include_tasks] *************************************************************************************************************
task path: /Users/almazgaazov/.ansible/roles/geerlingguy.docker/tasks/main.yml:97
skipping: [yandex_vm] => {
    "changed": false,
    "false_condition": "at_least_one_user_to_modify is defined",
    "skip_reason": "Conditional result was False"
}

PLAY RECAP ********************************************************************************************************************************************
yandex_vm                  : ok=14   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   