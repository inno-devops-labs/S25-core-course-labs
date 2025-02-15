# Ansible

## Best Practices

* 

## Execute Playbook

`ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml`

```
root@dmhd6219-laptop:~/S25-core-course-labs/ansible# ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ******************************************************************************

TASK [Gathering Facts] *******************************************************************************************
[WARNING]: Platform linux on host compute-vm-2-1-10-hdd-1739622264989 is using the discovered Python interpreter
at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that
path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more
information.
ok: [compute-vm-2-1-10-hdd-1739622264989]

TASK [docker : Update apt packages] ******************************************************************************
changed: [compute-vm-2-1-10-hdd-1739622264989]

TASK [docker : Install apt packages] *****************************************************************************
ok: [compute-vm-2-1-10-hdd-1739622264989]

TASK [docker : Add Docker's official GPG key] ********************************************************************
ok: [compute-vm-2-1-10-hdd-1739622264989]

TASK [docker : Add Docker's official apt repository] *************************************************************
ok: [compute-vm-2-1-10-hdd-1739622264989]

TASK [docker : Install Docker and Docker Compose] ****************************************************************
ok: [compute-vm-2-1-10-hdd-1739622264989] => (item=docker-ce)
ok: [compute-vm-2-1-10-hdd-1739622264989] => (item=docker-ce-cli)
ok: [compute-vm-2-1-10-hdd-1739622264989] => (item=containerd.io)
ok: [compute-vm-2-1-10-hdd-1739622264989] => (item=docker-buildx-plugin)
ok: [compute-vm-2-1-10-hdd-1739622264989] => (item=docker-compose-plugin)

TASK [docker : Add Docker group] *********************************************************************************
ok: [compute-vm-2-1-10-hdd-1739622264989]

TASK [docker : Add user to Docker group] *************************************************************************
ok: [compute-vm-2-1-10-hdd-1739622264989]

TASK [docker : Enable and start Docker services] *****************************************************************
ok: [compute-vm-2-1-10-hdd-1739622264989] => (item=docker.service)
ok: [compute-vm-2-1-10-hdd-1739622264989] => (item=containerd.service)

PLAY RECAP *******************************************************************************************************
compute-vm-2-1-10-hdd-1739622264989 : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739625458.621024   41796 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

## Inventory Details

`ansible-inventory -i inventory/yacloud_compute.yaml --list`

```
root@dmhd6219-laptop:~/S25-core-course-labs/ansible# ansible-inventory -i inventory/yacloud_compute.yaml --list
{
    "_meta": {
        "hostvars": {
            "compute-vm-2-1-10-hdd-1739622264989": {
                "ansible_all_ipv4_addresses": [
                    {
                        "__ansible_unsafe": "172.17.0.1"
                    },
                    {
                        "__ansible_unsafe": "10.130.0.9"
                    }
                ],
                "ansible_all_ipv6_addresses": [
                    {
                        "__ansible_unsafe": "fe80::d20d:74ff:fe20:7657"
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
                    "__ansible_unsafe": "xeon-gold-6338"
                },
                "ansible_board_serial": {
                    "__ansible_unsafe": "YC-fv47883mas44i5vnf51h"
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
                    "__ansible_unsafe": "xeon-gold-6338"
                },
                "ansible_chassis_vendor": {
                    "__ansible_unsafe": "Yandex"
                },
                "ansible_chassis_version": {
                    "__ansible_unsafe": "xeon-gold-6338"
                },
                "ansible_cmdline": {
                    "BOOT_IMAGE": {
                        "__ansible_unsafe": "/boot/vmlinuz-6.8.0-52-generic"
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
                        "__ansible_unsafe": "UUID=9ca38502-006d-4f2a-89e1-4c5147e69837"
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
                        "__ansible_unsafe": "1739625430"
                    },
                    "epoch_int": {
                        "__ansible_unsafe": "1739625430"
                    },
                    "hour": {
                        "__ansible_unsafe": "13"
                    },
                    "iso8601": {
                        "__ansible_unsafe": "2025-02-15T13:17:10Z"
                    },
                    "iso8601_basic": {
                        "__ansible_unsafe": "20250215T131710201885"
                    },
                    "iso8601_basic_short": {
                        "__ansible_unsafe": "20250215T131710"
                    },
                    "iso8601_micro": {
                        "__ansible_unsafe": "2025-02-15T13:17:10.201885Z"
                    },
                    "minute": {
                        "__ansible_unsafe": "17"
                    },
                    "month": {
                        "__ansible_unsafe": "02"
                    },
                    "second": {
                        "__ansible_unsafe": "10"
                    },
                    "time": {
                        "__ansible_unsafe": "13:17:10"
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
                        "__ansible_unsafe": "10.130.0.9"
                    },
                    "alias": {
                        "__ansible_unsafe": "eth0"
                    },
                    "broadcast": {
                        "__ansible_unsafe": ""
                    },
                    "gateway": {
                        "__ansible_unsafe": "10.130.0.1"
                    },
                    "interface": {
                        "__ansible_unsafe": "eth0"
                    },
                    "macaddress": {
                        "__ansible_unsafe": "d0:0d:74:20:76:57"
                    },
                    "mtu": 1500,
                    "netmask": {
                        "__ansible_unsafe": "255.255.255.0"
                    },
                    "network": {
                        "__ansible_unsafe": "10.130.0.0"
                    },
                    "prefix": {
                        "__ansible_unsafe": "24"
                    },
                    "type": {
                        "__ansible_unsafe": "ether"
                    }
                },
                "ansible_default_ipv6": {},
                "ansible_device_links": {
                    "ids": {
                        "vda": [
                            {
                                "__ansible_unsafe": "virtio-fv4kj9d7rdtvl61n0b8j"
                            }
                        ],
                        "vda1": [
                            {
                                "__ansible_unsafe": "virtio-fv4kj9d7rdtvl61n0b8j-part1"
                            }
                        ],
                        "vda2": [
                            {
                                "__ansible_unsafe": "virtio-fv4kj9d7rdtvl61n0b8j-part2"
                            }
                        ]
                    },
                    "labels": {},
                    "masters": {},
                    "uuids": {
                        "vda2": [
                            {
                                "__ansible_unsafe": "9ca38502-006d-4f2a-89e1-4c5147e69837"
                            }
                        ]
                    }
                },
                "ansible_devices": {
                    "loop0": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "4096"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop1": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "512"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop2": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "512"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop3": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "512"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop4": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "512"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop5": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "512"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop6": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "512"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop7": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "512"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "vda": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": "SCSI storage controller: Red Hat, Inc. Virtio block device"
                        },
                        "links": {
                            "ids": [
                                {
                                    "__ansible_unsafe": "virtio-fv4kj9d7rdtvl61n0b8j"
                                }
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {
                            "vda1": {
                                "holders": [],
                                "links": {
                                    "ids": [
                                        {
                                            "__ansible_unsafe": "virtio-fv4kj9d7rdtvl61n0b8j-part1"
                                        }
                                    ],
                                    "labels": [],
                                    "masters": [],
                                    "uuids": []
                                },
                                "sectors": {
                                    "__ansible_unsafe": "2048"
                                },
                                "sectorsize": 512,
                                "size": {
                                    "__ansible_unsafe": "1.00 MB"
                                },
                                "start": {
                                    "__ansible_unsafe": "2048"
                                },
                                "uuid": null
                            },
                            "vda2": {
                                "holders": [],
                                "links": {
                                    "ids": [
                                        {
                                            "__ansible_unsafe": "virtio-fv4kj9d7rdtvl61n0b8j-part2"
                                        }
                                    ],
                                    "labels": [],
                                    "masters": [],
                                    "uuids": [
                                        {
                                            "__ansible_unsafe": "9ca38502-006d-4f2a-89e1-4c5147e69837"
                                        }
                                    ]
                                },
                                "sectors": {
                                    "__ansible_unsafe": "20967391"
                                },
                                "sectorsize": 512,
                                "size": {
                                    "__ansible_unsafe": "10.00 GB"
                                },
                                "start": {
                                    "__ansible_unsafe": "4096"
                                },
                                "uuid": {
                                    "__ansible_unsafe": "9ca38502-006d-4f2a-89e1-4c5147e69837"
                                }
                            }
                        },
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "20971520"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "10.00 GB"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "4096"
                        },
                        "vendor": {
                            "__ansible_unsafe": "0x1af4"
                        },
                        "virtual": 1
                    }
                },
                "ansible_distribution": {
                    "__ansible_unsafe": "Ubuntu"
                },
                "ansible_distribution_file_parsed": true,
                "ansible_distribution_file_path": {
                    "__ansible_unsafe": "/etc/os-release"
                },
                "ansible_distribution_file_variety": {
                    "__ansible_unsafe": "Debian"
                },
                "ansible_distribution_major_version": {
                    "__ansible_unsafe": "24"
                },
                "ansible_distribution_release": {
                    "__ansible_unsafe": "noble"
                },
                "ansible_distribution_version": {
                    "__ansible_unsafe": "24.04"
                },
                "ansible_dns": {
                    "nameservers": [
                        {
                            "__ansible_unsafe": "127.0.0.53"
                        }
                    ],
                    "options": {
                        "edns0": true,
                        "trust-ad": true
                    },
                    "search": [
                        {
                            "__ansible_unsafe": "ru-central1.internal"
                        },
                        {
                            "__ansible_unsafe": "auto.internal"
                        }
                    ]
                },
                "ansible_docker0": {
                    "active": false,
                    "device": {
                        "__ansible_unsafe": "docker0"
                    },
                    "features": {
                        "esp_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "esp_tx_csum_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "fcoe_mtu": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "generic_receive_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "generic_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "highdma": {
                            "__ansible_unsafe": "on"
                        },
                        "hsr_dup_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_ins_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_rm_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hw_tc_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "l2_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "large_receive_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "loopback": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "macsec_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "netns_local": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "ntuple_filters": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "receive_hashing": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_all": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_checksumming": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_fcs": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_hw": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_list": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_gro_forwarding": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_tunnel_port_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_hw_parse": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tcp_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "tls_hw_record": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_rx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_tx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_fcoe_crc": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ip_generic": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_checksum_ipv4": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ipv6": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_sctp": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksumming": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_esp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_fcoe_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_gre_csum_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_gre_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_gso_list": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_gso_partial": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_gso_robust": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_ipxip4_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_ipxip6_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_lockless": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_nocache_copy": {
                            "__ansible_unsafe": "off"
                        },
                        "tx_scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_scatter_gather_fraglist": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_sctp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp6_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_ecn_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_mangleid_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tunnel_remcsum_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_udp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_udp_tnl_csum_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_udp_tnl_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_vlan_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_vlan_stag_hw_insert": {
                            "__ansible_unsafe": "on"
                        },
                        "vlan_challenged": {
                            "__ansible_unsafe": "off [fixed]"
                        }
                    },
                    "hw_timestamp_filters": [],
                    "id": {
                        "__ansible_unsafe": "8000.0242c543a43e"
                    },
                    "interfaces": [],
                    "ipv4": {
                        "address": {
                            "__ansible_unsafe": "172.17.0.1"
                        },
                        "broadcast": {
                            "__ansible_unsafe": "172.17.255.255"
                        },
                        "netmask": {
                            "__ansible_unsafe": "255.255.0.0"
                        },
                        "network": {
                            "__ansible_unsafe": "172.17.0.0"
                        },
                        "prefix": {
                            "__ansible_unsafe": "16"
                        }
                    },
                    "macaddress": {
                        "__ansible_unsafe": "02:42:c5:43:a4:3e"
                    },
                    "mtu": 1500,
                    "promisc": false,
                    "speed": -1,
                    "stp": false,
                    "timestamping": [],
                    "type": {
                        "__ansible_unsafe": "bridge"
                    }
                },
                "ansible_domain": {
                    "__ansible_unsafe": "ru-central1.internal"
                },
                "ansible_effective_group_id": 0,
                "ansible_effective_user_id": 0,
                "ansible_env": {
                    "HOME": {
                        "__ansible_unsafe": "/root"
                    },
                    "LANG": {
                        "__ansible_unsafe": "en_US.UTF-8"
                    },
                    "LOGNAME": {
                        "__ansible_unsafe": "root"
                    },
                    "MAIL": {
                        "__ansible_unsafe": "/var/mail/root"
                    },
                    "PATH": {
                        "__ansible_unsafe": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
                    },
                    "PWD": {
                        "__ansible_unsafe": "/home/ubuntu"
                    },
                    "SHELL": {
                        "__ansible_unsafe": "/bin/bash"
                    },
                    "SUDO_COMMAND": {
                        "__ansible_unsafe": "/bin/sh -c echo BECOME-SUCCESS-veaaxrqcxwwsdyhqfuefnlzhlpcaasqa ; /usr/bin/python3.12 /home/ubuntu/.ansible/tmp/ansible-tmp-1739625427.5317507-41858-12173445878197/AnsiballZ_setup.py"
                    },
                    "SUDO_GID": {
                        "__ansible_unsafe": "1001"
                    },
                    "SUDO_UID": {
                        "__ansible_unsafe": "1000"
                    },
                    "SUDO_USER": {
                        "__ansible_unsafe": "ubuntu"
                    },
                    "TERM": {
                        "__ansible_unsafe": "xterm-256color"
                    },
                    "USER": {
                        "__ansible_unsafe": "root"
                    }
                },
                "ansible_eth0": {
                    "active": true,
                    "device": {
                        "__ansible_unsafe": "eth0"
                    },
                    "features": {
                        "esp_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "esp_tx_csum_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "fcoe_mtu": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "generic_receive_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "generic_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "highdma": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "hsr_dup_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_ins_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_rm_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hw_tc_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "l2_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "large_receive_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "loopback": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "macsec_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "netns_local": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "ntuple_filters": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "receive_hashing": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_all": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_checksumming": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "rx_fcs": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_hw": {
                            "__ansible_unsafe": "on"
                        },
                        "rx_gro_list": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_gro_forwarding": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_tunnel_port_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_filter": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "rx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_hw_parse": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tcp_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "tls_hw_record": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_rx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_tx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_fcoe_crc": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ip_generic": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_checksum_ipv4": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ipv6": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_sctp": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksumming": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_esp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_fcoe_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_list": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_partial": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_robust": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_ipxip4_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_ipxip6_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_lockless": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_nocache_copy": {
                            "__ansible_unsafe": "off"
                        },
                        "tx_scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_scatter_gather_fraglist": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_sctp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_tcp6_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_ecn_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_mangleid_segmentation": {
                            "__ansible_unsafe": "off"
                        },
                        "tx_tcp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tunnel_remcsum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_tnl_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_tnl_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_stag_hw_insert": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "vlan_challenged": {
                            "__ansible_unsafe": "off [fixed]"
                        }
                    },
                    "hw_timestamp_filters": [],
                    "ipv4": {
                        "address": {
                            "__ansible_unsafe": "10.130.0.9"
                        },
                        "broadcast": {
                            "__ansible_unsafe": ""
                        },
                        "netmask": {
                            "__ansible_unsafe": "255.255.255.0"
                        },
                        "network": {
                            "__ansible_unsafe": "10.130.0.0"
                        },
                        "prefix": {
                            "__ansible_unsafe": "24"
                        }
                    },
                    "ipv6": [
                        {
                            "address": {
                                "__ansible_unsafe": "fe80::d20d:74ff:fe20:7657"
                            },
                            "prefix": {
                                "__ansible_unsafe": "64"
                            },
                            "scope": {
                                "__ansible_unsafe": "link"
                            }
                        }
                    ],
                    "macaddress": {
                        "__ansible_unsafe": "d0:0d:74:20:76:57"
                    },
                    "mtu": 1500,
                    "pciid": {
                        "__ansible_unsafe": "virtio1"
                    },
                    "promisc": false,
                    "speed": -1,
                    "timestamping": [],
                    "type": {
                        "__ansible_unsafe": "ether"
                    }
                },
                "ansible_fibre_channel_wwn": [],
                "ansible_fips": false,
                "ansible_form_factor": {
                    "__ansible_unsafe": "Other"
                },
                "ansible_fqdn": {
                    "__ansible_unsafe": "compute-vm-2-1-10-hdd-1739622264989.ru-central1.internal"
                },
                "ansible_host": "158.160.147.38",
                "ansible_hostname": {
                    "__ansible_unsafe": "compute-vm-2-1-10-hdd-1739622264989"
                },
                "ansible_hostnqn": {
                    "__ansible_unsafe": ""
                },
                "ansible_interfaces": [
                    {
                        "__ansible_unsafe": "docker0"
                    },
                    {
                        "__ansible_unsafe": "lo"
                    },
                    {
                        "__ansible_unsafe": "eth0"
                    }
                ],
                "ansible_is_chroot": false,
                "ansible_iscsi_iqn": {
                    "__ansible_unsafe": "iqn.2004-10.com.ubuntu:01:688cf580e02f"
                },
                "ansible_kernel": {
                    "__ansible_unsafe": "6.8.0-52-generic"
                },
                "ansible_kernel_version": {
                    "__ansible_unsafe": "#53-Ubuntu SMP PREEMPT_DYNAMIC Sat Jan 11 00:06:25 UTC 2025"
                },
                "ansible_lo": {
                    "active": true,
                    "device": {
                        "__ansible_unsafe": "lo"
                    },
                    "features": {
                        "esp_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "esp_tx_csum_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "fcoe_mtu": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "generic_receive_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "generic_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "highdma": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "hsr_dup_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_ins_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_rm_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hw_tc_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "l2_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "large_receive_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "loopback": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "macsec_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "netns_local": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "ntuple_filters": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "receive_hashing": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_all": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_checksumming": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "rx_fcs": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_hw": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_list": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_gro_forwarding": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_tunnel_port_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_hw_parse": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tcp_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "tls_hw_record": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_rx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_tx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_fcoe_crc": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ip_generic": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_checksum_ipv4": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ipv6": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_sctp": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_checksumming": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_esp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_fcoe_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_list": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_gso_partial": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_robust": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_ipxip4_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_ipxip6_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_lockless": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_nocache_copy": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_scatter_gather": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_scatter_gather_fraglist": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_sctp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp6_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_ecn_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_mangleid_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tunnel_remcsum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_udp_tnl_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_tnl_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_stag_hw_insert": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "vlan_challenged": {
                            "__ansible_unsafe": "on [fixed]"
                        }
                    },
                    "hw_timestamp_filters": [],
                    "ipv4": {
                        "address": {
                            "__ansible_unsafe": "127.0.0.1"
                        },
                        "broadcast": {
                            "__ansible_unsafe": ""
                        },
                        "netmask": {
                            "__ansible_unsafe": "255.0.0.0"
                        },
                        "network": {
                            "__ansible_unsafe": "127.0.0.0"
                        },
                        "prefix": {
                            "__ansible_unsafe": "8"
                        }
                    },
                    "ipv6": [
                        {
                            "address": {
                                "__ansible_unsafe": "::1"
                            },
                            "prefix": {
                                "__ansible_unsafe": "128"
                            },
                            "scope": {
                                "__ansible_unsafe": "host"
                            }
                        }
                    ],
                    "mtu": 65536,
                    "promisc": false,
                    "timestamping": [],
                    "type": {
                        "__ansible_unsafe": "loopback"
                    }
                },
                "ansible_loadavg": {
                    "15m": 0.0,
                    "1m": 0.0,
                    "5m": 0.0
                },
                "ansible_local": {},
                "ansible_locally_reachable_ips": {
                    "ipv4": [
                        {
                            "__ansible_unsafe": "10.130.0.9"
                        },
                        {
                            "__ansible_unsafe": "127.0.0.0/8"
                        },
                        {
                            "__ansible_unsafe": "127.0.0.1"
                        },
                        {
                            "__ansible_unsafe": "172.17.0.1"
                        }
                    ],
                    "ipv6": [
                        {
                            "__ansible_unsafe": "::1"
                        },
                        {
                            "__ansible_unsafe": "fe80::d20d:74ff:fe20:7657"
                        }
                    ]
                },
                "ansible_lsb": {
                    "codename": {
                        "__ansible_unsafe": "noble"
                    },
                    "description": {
                        "__ansible_unsafe": "Ubuntu 24.04.1 LTS"
                    },
                    "id": {
                        "__ansible_unsafe": "Ubuntu"
                    },
                    "major_release": {
                        "__ansible_unsafe": "24"
                    },
                    "release": {
                        "__ansible_unsafe": "24.04"
                    }
                },
                "ansible_lvm": {
                    "lvs": {},
                    "pvs": {},
                    "vgs": {}
                },
                "ansible_machine": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_machine_id": {
                    "__ansible_unsafe": "23000007fc874207657084917f779431"
                },
                "ansible_memfree_mb": 194,
                "ansible_memory_mb": {
                    "nocache": {
                        "free": 710,
                        "used": 250
                    },
                    "real": {
                        "free": 194,
                        "total": 960,
                        "used": 766
                    },
                    "swap": {
                        "cached": 0,
                        "free": 0,
                        "total": 0,
                        "used": 0
                    }
                },
                "ansible_memtotal_mb": 960,
                "ansible_mounts": [
                    {
                        "block_available": 1523659,
                        "block_size": 4096,
                        "block_total": 2557650,
                        "block_used": 1033991,
                        "device": {
                            "__ansible_unsafe": "/dev/vda2"
                        },
                        "dump": 0,
                        "fstype": {
                            "__ansible_unsafe": "ext4"
                        },
                        "inode_available": 519384,
                        "inode_total": 655360,
                        "inode_used": 135976,
                        "mount": {
                            "__ansible_unsafe": "/"
                        },
                        "options": {
                            "__ansible_unsafe": "rw,relatime"
                        },
                        "passno": 0,
                        "size_available": 6240907264,
                        "size_total": 10476134400,
                        "uuid": {
                            "__ansible_unsafe": "9ca38502-006d-4f2a-89e1-4c5147e69837"
                        }
                    }
                ],
                "ansible_nodename": {
                    "__ansible_unsafe": "compute-vm-2-1-10-hdd-1739622264989"
                },
                "ansible_os_family": {
                    "__ansible_unsafe": "Debian"
                },
                "ansible_pkg_mgr": {
                    "__ansible_unsafe": "apt"
                },
                "ansible_proc_cmdline": {
                    "BOOT_IMAGE": {
                        "__ansible_unsafe": "/boot/vmlinuz-6.8.0-52-generic"
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
                        "__ansible_unsafe": "UUID=9ca38502-006d-4f2a-89e1-4c5147e69837"
                    }
                },
                "ansible_processor": [
                    {
                        "__ansible_unsafe": "0"
                    },
                    {
                        "__ansible_unsafe": "GenuineIntel"
                    },
                    {
                        "__ansible_unsafe": "Intel Xeon Processor (Icelake)"
                    },
                    {
                        "__ansible_unsafe": "1"
                    },
                    {
                        "__ansible_unsafe": "GenuineIntel"
                    },
                    {
                        "__ansible_unsafe": "Intel Xeon Processor (Icelake)"
                    }
                ],
                "ansible_processor_cores": 1,
                "ansible_processor_count": 1,
                "ansible_processor_nproc": 2,
                "ansible_processor_threads_per_core": 2,
                "ansible_processor_vcpus": 2,
                "ansible_product_name": {
                    "__ansible_unsafe": "xeon-gold-6338"
                },
                "ansible_product_serial": {
                    "__ansible_unsafe": "YC-fv47883mas44i5vnf51h"
                },
                "ansible_product_uuid": {
                    "__ansible_unsafe": "23000007-fc87-4207-6570-84917f779431"
                },
                "ansible_product_version": {
                    "__ansible_unsafe": "pc-q35-yc-2.12"
                },
                "ansible_python": {
                    "executable": {
                        "__ansible_unsafe": "/usr/bin/python3.12"
                    },
                    "has_sslcontext": true,
                    "type": {
                        "__ansible_unsafe": "cpython"
                    },
                    "version": {
                        "major": 3,
                        "micro": 3,
                        "minor": 12,
                        "releaselevel": {
                            "__ansible_unsafe": "final"
                        },
                        "serial": 0
                    },
                    "version_info": [
                        3,
                        12,
                        3,
                        {
                            "__ansible_unsafe": "final"
                        },
                        0
                    ]
                },
                "ansible_python_version": {
                    "__ansible_unsafe": "3.12.3"
                },
                "ansible_real_group_id": 0,
                "ansible_real_user_id": 0,
                "ansible_selinux": {
                    "status": {
                        "__ansible_unsafe": "disabled"
                    }
                },
                "ansible_selinux_python_present": true,
                "ansible_service_mgr": {
                    "__ansible_unsafe": "systemd"
                },
                "ansible_ssh_host_key_ecdsa_public": {
                    "__ansible_unsafe": "[ДАННЫЕ УДАЛЕНЫ]"
                },
                "ansible_ssh_host_key_ecdsa_public_keytype": {
                    "__ansible_unsafe": "ecdsa-sha2-nistp256"
                },
                "ansible_ssh_host_key_ed25519_public": {
                    "__ansible_unsafe": "[ДАННЫЕ УДАЛЕНЫ]"
                },
                "ansible_ssh_host_key_ed25519_public_keytype": {
                    "__ansible_unsafe": "ssh-ed25519"
                },
                "ansible_ssh_host_key_rsa_public": {
                    "__ansible_unsafe": "[ДАННЫЕ УДАЛЕНЫ]"
                },
                "ansible_ssh_host_key_rsa_public_keytype": {
                    "__ansible_unsafe": "ssh-rsa"
                },
                "ansible_swapfree_mb": 0,
                "ansible_swaptotal_mb": 0,
                "ansible_system": {
                    "__ansible_unsafe": "Linux"
                },
                "ansible_system_capabilities": [],
                "ansible_system_capabilities_enforced": {
                    "__ansible_unsafe": "False"
                },
                "ansible_system_vendor": {
                    "__ansible_unsafe": "Yandex"
                },
                "ansible_uptime_seconds": 3049,
                "ansible_user_dir": {
                    "__ansible_unsafe": "/root"
                },
                "ansible_user_gecos": {
                    "__ansible_unsafe": "root"
                },
                "ansible_user_gid": 0,
                "ansible_user_id": {
                    "__ansible_unsafe": "root"
                },
                "ansible_user_shell": {
                    "__ansible_unsafe": "/bin/bash"
                },
                "ansible_user_uid": 0,
                "ansible_userspace_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_userspace_bits": {
                    "__ansible_unsafe": "64"
                },
                "ansible_virtualization_role": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_virtualization_tech_guest": [],
                "ansible_virtualization_tech_host": [],
                "ansible_virtualization_type": {
                    "__ansible_unsafe": "NA"
                },
                "discovered_interpreter_python": {
                    "__ansible_unsafe": "/usr/bin/python3.12"
                },
                "gather_subset": [
                    {
                        "__ansible_unsafe": "all"
                    }
                ],
                "module_setup": true
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "compute-vm-2-1-10-hdd-1739622264989"
        ]
    }
}
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739625526.827411   43153 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```