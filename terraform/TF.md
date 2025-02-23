```sh
terraform state list
docker_container.nginx
docker_image.nginx
```
```sh
terraform state show docker_container.nginx
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "14ecbf23852f"
    id                                          = "14ecbf23852f39f7bef43a73bfa6ecb4dcb17f50c170d4e7e0f2dd27a759f0e8"
    image                                       = "sha256:1d668e06f1e534ab338404ba891c37d618dd53c9073dcdd4ebde82aa7643f83f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "default"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
```sh
[0m[1mdocker_image.nginx: Refreshing state... [id=sha256:1d668e06f1e534ab338404ba891c37d618dd53c9073dcdd4ebde82aa7643f83fnginx:latest][0m
[0m[1mdocker_container.nginx: Refreshing state... [id=14ecbf23852f39f7bef43a73bfa6ecb4dcb17f50c170d4e7e0f2dd27a759f0e8][0m

[0m[1m[32mNo changes.[0m[1m Your infrastructure matches the configuration.[0m

[0mTerraform has compared your real infrastructure against your configuration
and found no differences, so no changes are needed.
[0m[1m[32m
Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
[0m
```

```sh
terraform output
container_name = "custom_nginx"
```

```sh
$ yc iam service-account create --name galyusha              
done (2s)
id: ajekq9h3db50unm57ajs
folder_id: b1g0u5p8fg45gkiq8600
created_at: "2025-02-06T15:42:02.343887607Z"
name: galyusha
```

```sh
yc resource-manager folder list
+----------------------+---------+--------+--------+
|          ID          |  NAME   | LABELS | STATUS |
+----------------------+---------+--------+--------+
| b1g0u5p8fg45gkiq8600 | default |        | ACTIVE |
+----------------------+---------+--------+--------+
```
### Created an authorized key
```sh
yc iam key create   --service-account-id ajekq9h3db50unm57ajs   --folder-name default --output key.json
id: ajej9lugbbltpkd2m820
service_account_id: ajekq9h3db50unm57ajs
created_at: "2025-02-06T19:05:29.569036713Z"
key_algorithm: RSA_2048
```
### Create a CLI profile to run operations on behalf of the service account. Name the profile:
```sh
yc config profile create cli_profile   
Profile 'cli_profile' created and activated
```
### Get organization ID
```sh
yc organization-manager organization list
+----------------------+--------------------------+--------------------------+--------+
|          ID          |           NAME           |          TITLE           | LABELS |
+----------------------+--------------------------+--------------------------+--------+
| bpfmmlad51noq63i40un | organization-belyash-394 | organization-belyash-394 |        |
+----------------------+--------------------------+--------------------------+--------+
```
### Set profile configuration
```sh
yc config set service-account-key key.json
yc config set cloud-id <cloud_ID>
yc config set folder-id <folder_ID>
```

### Add the credentials to the environment variables:
```sh
export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id)
```

