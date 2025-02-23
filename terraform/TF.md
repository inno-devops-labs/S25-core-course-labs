# Terraform Lab Documentation

## terraform apply

Plan: 2 to add, 0 to change, 0 to destroy.       

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Creation complete after 24s [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 4s [id=08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.


## terraform state list

docker_container.nginx
docker_image.nginx


## terraform state show docker_container.nginx

# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      =
 null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     =
 null
    cpu_shares                                  = 0
    domainname                                  =
 null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "08b0fe62afbf"
    id                                          = "08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036"
    image                                       = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
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
    pid_mode                                    =
 null
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
    user                                        =
 null
    userns_mode                                 =
 null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 =
 null

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}


## terraform state show docker_image.nginx    

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx" 
    image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"      
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}


# after changes 

## terraform apply

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036]

Plan: 1 to add, 0 to change, 1 to destroy.     

docker_container.nginx: Destroying... [id=08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=be509c8f045e47fd0d7f72ecd47191bbf2b0cc62826b3a47056468d33106042a]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.


## terraform destroy

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=be509c8f045e47fd0d7f72ecd47191bbf2b0cc62826b3a47056468d33106042a]

Plan: 0 to add, 0 to change, 2 to destroy.     

docker_container.nginx: Destroying... [id=be509c8f045e47fd0d7f72ecd47191bbf2b0cc62826b3a47056468d33106042a]
docker_container.nginx: Destruction complete after 1s
docker_image.nginx: Destroying... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_image.nginx: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.


## terraform apply                 
       
Plan: 2 to add, 0 to change, 0 to destroy.     

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Creation complete after 16s [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 4s [id=fb6b896e9bae07eddb1b973c9d144aa12220c8d9694475b3ab20c5438d2168dd]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.


## terraform apply -var "container_name=YetAnotherName"

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=fb6b896e9bae07eddb1b973c9d144aa12220c8d9694475b3ab20c5438d2168dd]

Plan: 1 to add, 0 to change, 1 to destroy.     

docker_container.nginx: Destroying... [id=fb6b896e9bae07eddb1b973c9d144aa12220c8d9694475b3ab20c5438d2168dd]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=506e5a0e63d32a6d8761971fa4879c923276f3199c378a9bf4e75458941c9f00]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.


## terraform apply 

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=506e5a0e63d32a6d8761971fa4879c923276f3199c378a9bf4e75458941c9f00]    

Plan: 1 to add, 0 to change, 1 to destroy.

docker_container.nginx: Destroying... [id=506e5a0e63d32a6d8761971fa4879c923276f3199c378a9bf4e75458941c9f00]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=dbe28f5310cad7e2d773c1b5285d864adafd5ce00a5eac694d2b0ba00907185e]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.


## terraform apply

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=dbe28f5310cad7e2d773c1b5285d864adafd5ce00a5eac694d2b0ba00907185e]    

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + container_id = (known after apply) 
  + image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx"

docker_container.nginx: Destroying... [id=dbe28f5310cad7e2d773c1b5285d864adafd5ce00a5eac694d2b0ba00907185e]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx"


## terraform output

container_id = "c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx"


## terraform destroy

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801]    

Plan: 0 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  - container_id = "c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801" -> null
  - image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx" -> null

docker_container.nginx: Destroying... [id=c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801]
docker_container.nginx: Destruction complete after 1s
docker_image.nginx: Destroying... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]  
docker_image.nginx: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.
