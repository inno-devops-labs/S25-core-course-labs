# Overview

# **Best Practices Implemented in Ansible Playbook**

## **1️ Rigorous Syntax Validation & Dry-Run Testing**  
Before deployment, the playbook undergoes **strict syntax validation** using the `--syntax-check` flag. This ensures error-free execution.  
Additionally, a **dry-run simulation** (`--check` flag) is performed to preview changes **without modifying the system**, providing confidence in the expected behavior.

---

## **2Efficient Service Management with Handlers**  
Handlers are implemented to **restart services only when necessary**, particularly for **Docker**.  
This approach:
- **Minimizes downtime**
- **Optimizes resource usage**
- **Ensures smooth playbook execution without unnecessary restarts**  

---

## **3️ Improved Readability & Maintainability**  
Each task includes a **clear and descriptive name**, making the playbook:  
 **Easier to read and understand**  
 **More maintainable for future modifications**  
 **Simpler to debug**, as errors and progress can be quickly identified  

---

## **4️ Secure Docker Configuration**  
The playbook enhances security by **restricting root access** to Docker.  
This is achieved by:  
 **Modifying the `daemon.json` file** with Ansible’s `copy` module.  
 **Ensuring a more secure and controlled Docker environment.**  

---

## **5️ Robust Pre-Deployment Validation**  
To prevent issues in production, the playbook undergoes **comprehensive pre-deployment checks**, including:  
 **Syntax validation** (`--syntax-check`)  
 **Dry-run execution** (`--check`)  
 **Configuration testing** before applying changes  

This proactive approach **reduces deployment risks and ensures reliability**.

---

### ** Summary of Best Practices**  
 **Validates playbook syntax & performs dry-run simulations**  
 **Uses handlers to restart services only when necessary**  
 **Improves readability with clear task names**  
 **Enhances Docker security by disabling root access**  
 **Implements pre-deployment validation to ensure a stable setup**  

---
## Outputs

```shell


```shell
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-playbook playbooks/dev/main.yaml --diff --check

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/home/suleimankrimeddin/.ssh/lab/id_ed25519': 
ok: [host1]

TASK [docker : Update apt] *****************************************************
changed: [host1]

TASK [docker : Python3 and pip3 installation] **********************************
changed: [host1]

TASK [docker : Install docker] *************************************************
changed: [host1]

TASK [docker : Install docker compose] *****************************************
changed: [host1]

PLAY RECAP *********************************************************************
host1                      : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


```shell
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-inventory -i inventory/default_lab.yml --list
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_host": "89.150.34.19",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "hosts": [
            "host1"
        ]
    }
}
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-inventory -i inventory/default_lab.yml --graph
@all
 |--host1