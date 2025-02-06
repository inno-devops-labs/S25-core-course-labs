## Terraform

Commands outputs:
    - `terraform show`
        ```
        $ terraform show
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
            hostname                                    = "b94d8e21c785"
            id                                          = "b94d8e21c78561f1c50678076eb05d2d767e6022ee54f5689c57d84441dfb88b"
            image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
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
            network_mode                                = "bridge"
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

        # docker_image.nginx:
        resource "docker_image" "nginx" {
            id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
            image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
            keep_locally = false
            name         = "nginx:latest"
            repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
        }
        ```
    - `terraform state list`
        ```
        $ terraform state list
        docker_container.nginx
        docker_image.nginx
        ```
    - `terraform state show docker_container.nginx`
        ```
        $ terraform state show docker_container.nginx
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
            hostname                                    = "a600411b43fa"
            id                                          = "a600411b43faf367befb2a05e4a176e44f8dbf7064c2c593b0a73c0f08e84ea1"
            image                                       = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
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
            network_mode                                = "bridge"
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
    - `terraform state show docker_image.nginx`
        ```
        $ terraform state show docker_image.nginx
        # docker_image.nginx:
        resource "docker_image" "nginx" {
            id           = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8enginx:latest"
            image_id     = "sha256:97662d24417b316f60607afbca9f226a2ba58f09d642f27b8e197a89859ddc8e"
            keep_locally = false
            name         = "nginx:latest"
            repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
        }
        ```
        