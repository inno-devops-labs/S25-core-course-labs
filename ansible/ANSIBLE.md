# Deployment output

## To deploy playbook
```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```

## Last 50 lines of run

```
PLAY [Install Docker] **********************************************************

TASK [Gathering Facts] *********************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python
interpreter at /usr/bin/python3.10, but future installation of another Python
interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [docker : Include Docker installation tasks] ******************************
included: /home/fory/devops-labs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Clean apt cache] ************************************************
ok: [localhost] => {"changed": false, "cmd": ["apt-get", "clean"], "delta": "0:00:00.020190", "end": "2025-02-16 20:48:15.364088", "msg": "", "rc": 0, "start": "2025-02-16 20:48:15.343898", "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}

TASK [docker : Update apt cache] ***********************************************
ok: [localhost] => {"attempts": 1, "cache_update_time": 1739727208, "cache_updated": false, "changed": false}

TASK [docker : Install required packages] **************************************
ok: [localhost] => {"attempts": 1, "cache_update_time": 1739727208, "cache_updated": false, "changed": false}

TASK [docker : Create Docker GPG directory] ************************************
ok: [localhost] => {"changed": false, "gid": 0, "group": "root", "mode": "0755", "owner": "root", "path": "/etc/apt/keyrings", "size": 4096, "state": "directory", "uid": 0}

TASK [docker : Download Docker GPG key] ****************************************
ok: [localhost] => {"changed": false, "checksum_dest": "f5b5bd1487cefc0c53c947e11ca202e86b33dbad", "checksum_src": "f5b5bd1487cefc0c53c947e11ca202e86b33dbad", "dest": "/etc/apt/keyrings/docker.gpg", "elapsed": 0, "gid": 0, "group": "root", "md5sum": "1afae06b34a13c1b3d9cb61a26285a15", "mode": "0644", "msg": "OK (3817 bytes)", "owner": "root", "size": 3817, "src": "/home/fory/.ansible/tmp/ansible-tmp-1739728097.312985-36199-203078826838821/tmpwu2k_ssm", "state": "file", "status_code": 200, "uid": 0, "url": "https://download.docker.com/linux/ubuntu/gpg"}

TASK [docker : Add Docker repository] ******************************************
ok: [localhost] => {"attempts": 1, "changed": false, "repo": "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable", "sources_added": [], "sources_removed": [], "state": "present"}

TASK [docker : Install Docker packages] ****************************************
ok: [localhost] => {"cache_update_time": 1739727208, "cache_updated": false, "changed": false}

TASK [docker : Ensure Docker service is enabled and started] *******************
ok: [localhost] => {"changed": false, "enabled": true, "name": "docker", "state": "started", "status": {"ActiveEnterTimestamp": "Sun 2025-02-16 20:40:14 MSK", "ActiveEnterTimestampMonotonic": "1013075382", "ActiveExitTimestamp": "n/a", "ActiveExitTimestampMonotonic": "0", "ActiveState": "active", "After": "sysinit.target time-set.target containerd.service firewalld.service network-online.target basic.target system.slice docker.socket systemd-journald.socket", "AllowIsolate": "no", "AssertResult": "yes", "AssertTimestamp": "Sun 2025-02-16 20:40:13 MSK", "AssertTimestampMonotonic": "1012670802", "Before": "shutdown.target multi-user.target", "BlockIOAccounting": "no", "BlockIOWeight": "[not set]", "CPUAccounting": "yes", "CPUAffinityFromNUMA": "no", "CPUQuotaPerSecUSec": "infinity", "CPUQuotaPeriodUSec": "infinity", "CPUSchedulingPolicy": "0", "CPUSchedulingPriority": "0", "CPUSchedulingResetOnFork": "no", "CPUShares": "[not set]", "CPUUsageNSec": "237403000", "CPUWeight": "[not set]", "CacheDirectoryMode": "0755", "CanFreeze": "yes", "CanIsolate": "no", "CanReload": "yes", "CanStart": "yes", "CanStop": "yes", "CapabilityBoundingSet": "cap_chown cap_dac_override cap_dac_read_search cap_fowner cap_fsetid cap_kill cap_setgid cap_setuid cap_setpcap cap_linux_immutable cap_net_bind_service cap_net_broadcast cap_net_admin cap_net_raw cap_ipc_lock cap_ipc_owner cap_sys_module cap_sys_rawio cap_sys_chroot cap_sys_ptrace cap_sys_pacct cap_sys_admin cap_sys_boot cap_sys_nice cap_sys_resource cap_sys_time cap_sys_tty_config cap_mknod cap_lease cap_audit_write cap_audit_control cap_setfcap cap_mac_override cap_mac_admin cap_syslog cap_wake_alarm cap_block_suspend cap_audit_read cap_perfmon cap_bpf cap_checkpoint_restore", "CleanResult": "success", "CollectMode": "inactive", "ConditionResult": "yes", "ConditionTimestamp": "Sun 2025-02-16 20:40:13 MSK", "ConditionTimestampMonotonic": "1012670801", "ConfigurationDirectoryMode": "0755", "Conflicts": "shutdown.target", "ControlGroup": "/system.slice/docker.service", "ControlPID": "0", "CoredumpFilter": "0x33", "DefaultDependencies": "yes", "DefaultMemoryLow": "0", "DefaultMemoryMin": "0", "Delegate": "yes", "DelegateControllers": "cpu cpuacct cpuset io blkio memory devices pids bpf-firewall bpf-devices bpf-foreign bpf-socket-bind", "Description": "Docker Application Container Engine", "DevicePolicy": "auto", "Documentation": "https://docs.docker.com", "DynamicUser": "no", "EffectiveCPUs": "0-15", "EffectiveMemoryNodes": "0", "ExecMainCode": "0", "ExecMainExitTimestamp": "n/a", "ExecMainExitTimestampMonotonic": "0", "ExecMainPID": "33930", "ExecMainStartTimestamp": "Sun 2025-02-16 20:40:13 MSK", "ExecMainStartTimestampMonotonic": "1012671621", "ExecMainStatus": "0", "ExecReload": "{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "ExecReloadEx": "{ path=/bin/kill ; argv[]=/bin/kill -s HUP $MAINPID ; flags= ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }", "ExecStart": "{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; ignore_errors=no ; start_time=[Sun 2025-02-16 20:40:13 MSK] ; stop_time=[n/a] ; pid=33930 ; code=(null) ; status=0/0 }", "ExecStartEx": "{ path=/usr/bin/dockerd ; argv[]=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock ; flags= ; start_time=[Sun 2025-02-16 20:40:13 MSK] ; stop_time=[n/a] ; pid=33930 ; code=(null) ; status=0/0 }", "FailureAction": "none", "FileDescriptorStoreMax": "0", "FinalKillSignal": "9", "FragmentPath": "/lib/systemd/system/docker.service", "FreezerState": "running", "GID": "[not set]", "GuessMainPID": "yes", "IOAccounting": "no", "IOReadBytes": "18446744073709551615", "IOReadOperations": "18446744073709551615", "IOSchedulingClass": "2", "IOSchedulingPriority": "4", "IOWeight": "[not set]", "IOWriteBytes": "18446744073709551615", "IOWriteOperations": "18446744073709551615", "IPAccounting": "no", "IPEgressBytes": "[no data]", "IPEgressPackets": "[no data]", "IPIngressBytes": "[no data]", "IPIngressPackets": "[no data]", "Id": "docker.service", "IgnoreOnIsolate": "no", "IgnoreSIGPIPE": "yes", "InactiveEnterTimestamp": "n/a", "InactiveEnterTimestampMonotonic": "0", "InactiveExitTimestamp": "Sun 2025-02-16 20:40:13 MSK", "InactiveExitTimestampMonotonic": "1012671753", "InvocationID": "a8e0e226e8734d39a981c10e9ad4c3b9", "JobRunningTimeoutUSec": "infinity", "JobTimeoutAction": "none", "JobTimeoutUSec": "infinity", "KeyringMode": "private", "KillMode": "process", "KillSignal": "15", "LimitAS": "infinity", "LimitASSoft": "infinity", "LimitCORE": "infinity", "LimitCORESoft": "infinity", "LimitCPU": "infinity", "LimitCPUSoft": "infinity", "LimitDATA": "infinity", "LimitDATASoft": "infinity", "LimitFSIZE": "infinity", "LimitFSIZESoft": "infinity", "LimitLOCKS": "infinity", "LimitLOCKSSoft": "infinity", "LimitMEMLOCK": "8388608", "LimitMEMLOCKSoft": "8388608", "LimitMSGQUEUE": "819200", "LimitMSGQUEUESoft": "819200", "LimitNICE": "0", "LimitNICESoft": "0", "LimitNOFILE": "524288", "LimitNOFILESoft": "1024", "LimitNPROC": "infinity", "LimitNPROCSoft": "infinity", "LimitRSS": "infinity", "LimitRSSSoft": "infinity", "LimitRTPRIO": "0", "LimitRTPRIOSoft": "0", "LimitRTTIME": "infinity", "LimitRTTIMESoft": "infinity", "LimitSIGPENDING": "54224", "LimitSIGPENDINGSoft": "54224", "LimitSTACK": "infinity", "LimitSTACKSoft": "8388608", "LoadState": "loaded", "LockPersonality": "no", "LogLevelMax": "-1", "LogRateLimitBurst": "0", "LogRateLimitIntervalUSec": "0", "LogsDirectoryMode": "0755", "MainPID": "33930", "ManagedOOMMemoryPressure": "auto", "ManagedOOMMemoryPressureLimit": "0", "ManagedOOMPreference": "none", "ManagedOOMSwap": "auto", "MemoryAccounting": "yes", "MemoryAvailable": "infinity", "MemoryCurrent": "23257088", "MemoryDenyWriteExecute": "no", "MemoryHigh": "infinity", "MemoryLimit": "infinity", "MemoryLow": "0", "MemoryMax": "infinity", "MemoryMin": "0", "MemorySwapMax": "infinity", "MountAPIVFS": "no", "NFileDescriptorStore": "0", "NRestarts": "0", "NUMAPolicy": "n/a", "Names": "docker.service", "NeedDaemonReload": "no", "Nice": "0", "NoNewPrivileges": "no", "NonBlocking": "no", "NotifyAccess": "main", "OOMPolicy": "continue", "OOMScoreAdjust": "-500", "OnFailureJobMode": "replace", "OnSuccessJobMode": "fail", "Perpetual": "no", "PrivateDevices": "no", "PrivateIPC": "no", "PrivateMounts": "no", "PrivateNetwork": "no", "PrivateTmp": "no", "PrivateUsers": "no", "ProcSubset": "all", "ProtectClock": "no", "ProtectControlGroups": "no", "ProtectHome": "no", "ProtectHostname": "no", "ProtectKernelLogs": "no", "ProtectKernelModules": "no", "ProtectKernelTunables": "no", "ProtectProc": "default", "ProtectSystem": "no", "RefuseManualStart": "no", "RefuseManualStop": "no", "ReloadResult": "success", "RemainAfterExit": "no", "RemoveIPC": "no", "Requires": "docker.socket sysinit.target system.slice", "Restart": "always", "RestartKillSignal": "15", "RestartUSec": "2s", "RestrictNamespaces": "no", "RestrictRealtime": "no", "RestrictSUIDSGID": "no", "Result": "success", "RootDirectoryStartOnly": "no", "RuntimeDirectoryMode": "0755", "RuntimeDirectoryPreserve": "no", "RuntimeMaxUSec": "infinity", "SameProcessGroup": "no", "SecureBits": "0", "SendSIGHUP": "no", "SendSIGKILL": "yes", "Slice": "system.slice", "StandardError": "inherit", "StandardInput": "null", "StandardOutput": "journal", "StartLimitAction": "none", "StartLimitBurst": "3", "StartLimitIntervalUSec": "1min", "StartupBlockIOWeight": "[not set]", "StartupCPUShares": "[not set]", "StartupCPUWeight": "[not set]", "StartupIOWeight": "[not set]", "StateChangeTimestamp": "Sun 2025-02-16 20:40:14 MSK", "StateChangeTimestampMonotonic": "1013075382", "StateDirectoryMode": "0755", "StatusErrno": "0", "StopWhenUnneeded": "no", "SubState": "running", "SuccessAction": "none", "SyslogFacility": "3", "SyslogLevel": "6", "SyslogLevelPrefix": "yes", "SyslogPriority": "30", "SystemCallErrorNumber": "2147483646", "TTYReset": "no", "TTYVHangup": "no", "TTYVTDisallocate": "no", "TasksAccounting": "yes", "TasksCurrent": "18", "TasksMax": "infinity", "TimeoutAbortUSec": "1min 30s", "TimeoutCleanUSec": "infinity", "TimeoutStartFailureMode": "terminate", "TimeoutStartUSec": "infinity", "TimeoutStopFailureMode": "terminate", "TimeoutStopUSec": "1min 30s", "TimerSlackNSec": "50000", "Transient": "no", "TriggeredBy": "docker.socket", "Type": "notify", "UID": "[not set]", "UMask": "0022", "UnitFilePreset": "enabled", "UnitFileState": "enabled", "UtmpMode": "init", "WantedBy": "multi-user.target", "Wants": "containerd.service network-online.target", "WatchdogSignal": "6", "WatchdogTimestamp": "n/a", "WatchdogTimestampMonotonic": "0", "WatchdogUSec": "0"}}

TASK [docker : Add users to docker group] **************************************
skipping: [localhost] => {"changed": false, "skipped_reason": "No items in the list"}

TASK [docker : Add current user to docker group] *******************************
ok: [localhost] => {"append": true, "changed": false, "comment": "root", "group": 0, "groups": "docker", "home": "/root", "move_home": false, "name": "root", "shell": "/bin/bash", "state": "present", "uid": 0}

TASK [docker : Include Docker Compose installation tasks] **********************
included: /home/fory/devops-labs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] ****************************************
ok: [localhost] => {"changed": false, "checksum_dest": "d9ab460c5ffdda02605821c083a902af28af528b", "checksum_src": "d9ab460c5ffdda02605821c083a902af28af528b", "dest": "/usr/local/bin/docker-compose", "elapsed": 86, "gid": 0, "group": "root", "md5sum": "aea273a344c430d1c89d23b21fa18f63", "mode": "0755", "msg": "OK (61389086 bytes)", "owner": "root", "size": 61389086, "src": "/home/fory/.ansible/tmp/ansible-tmp-1739728099.776645-36382-154981778255112/tmpdezftskv", "state": "file", "status_code": 200, "uid": 0, "url": "https://github.com/docker/compose/releases/download/v2.24.5/docker-compose-linux-x86_64"}

PLAY RECAP *********************************************************************
localhost                  : ok=13   changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```

# Inventory details

### `ansible-inventory -i inventory/default_aws_ec2.yml --list`

```
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
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
            "localhost"
        ]
    }
}
```

### `ansible-inventory -i inventory/default_aws_ec2.yml --graph`

```
@all:
  |--@ungrouped:
  |  |--localhost
```



