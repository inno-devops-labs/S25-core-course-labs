# Terraform Lab Documentation

### terraform init

Initializing the backend...
Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "~> 3.0.1"...
- Installing kreuzwerker/docker v3.0.2...
- Installed kreuzwerker/docker v3.0.2 (self-signed, key ID BD080C4571C6104C)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!     

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.


### terraform apply

Terraform used the selected providers to
generate the following execution plan. Resource  
actions are indicated with the following
symbols:
  + create

Terraform will perform the following actions:    

  # docker_container.nginx will be created       
  + resource "docker_container" "nginx" {        
      + attach                                   
   = false
      + bridge                                   
   = (known after apply)
      + command                                  
   = (known after apply)
      + container_logs                           
   = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                               
   = (known after apply)
      + env                                      
   = (known after apply)
      + exit_code                                
   = (known after apply)
      + hostname                                 
   = (known after apply)
      + id                                       
   = (known after apply)
      + image                                    
   = (known after apply)
      + init                                     
   = (known after apply)
      + ipc_mode                                 
   = (known after apply)
      + log_driver                               
   = (known after apply)
      + logs                                     
   = false
      + must_run                                 
   = true
      + name                                     
   = "tutorial"
      + network_data                             
   = (known after apply)
      + read_only                                
   = false
      + remove_volumes                           
   = true
      + restart                                  
   = "no"
      + rm                                       
   = false
      + runtime                                  
   = (known after apply)
      + security_opts                            
   = (known after apply)
      + shm_size                                 
   = (known after apply)
      + start                                    
   = true
      + stdin_open                               
   = false
      + stop_signal                              
   = (known after apply)
      + stop_timeout                             
   = (known after apply)
      + tty                                      
   = false
      + wait                                     
   = false
      + wait_timeout                             
   = 60

      + healthcheck (known after apply)

      + labels (known after apply)

      + ports {
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)       
      + image_id     = (known after apply)       
      + keep_locally = false
      + name         = "nginx"
      + repo_digest  = (known after apply)       
    }

Plan: 2 to add, 0 to change, 0 to destroy.       

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.        

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Creation complete after 24s [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 4s [id=08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.


### terraform state list

docker_container.nginx
docker_image.nginx


### terraform state show docker_container.nginx

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


### terraform state show docker_image.nginx    

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx" 
    image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"      
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34"
}


## after changes 

### terraform apply

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036]

Terraform used the selected providers to       
generate the following execution plan.
Resource actions are indicated with the        
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:  

  # docker_container.nginx must be replaced    
-/+ resource "docker_container" "nginx" {      
      + bridge                                 
     = (known after apply)
      ~ command                                
     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                         
     = (known after apply)
      - cpu_shares                             
     = 0 -> null
      - dns                                    
     = [] -> null
      - dns_opts                               
     = [] -> null
      - dns_search                             
     = [] -> null
      ~ entrypoint                             
     = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                    
     = [] -> (known after apply)
      + exit_code                              
     = (known after apply)
      - group_add                              
     = [] -> null
      ~ hostname                               
     = "08b0fe62afbf" -> "learn-terraform-docker" # forces replacement
      ~ id                                     
     = "08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036" -> (known after apply)
      ~ init                                   
     = false -> (known after apply)
      ~ ipc_mode                               
     = "private" -> (known after apply)        
      ~ log_driver                             
     = "json-file" -> (known after apply)      
      - log_opts                               
     = {} -> null
      - max_retry_count                        
     = 0 -> null
      - memory                                 
     = 0 -> null
      - memory_swap                            
     = 0 -> null
        name                                   
     = "tutorial"
      ~ network_data                           
     = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0  
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16 
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                           
     = "bridge" -> null # forces replacement   
      - privileged                             
     = false -> null
      - publish_all_ports                      
     = false -> null
      ~ runtime                                
     = "runc" -> (known after apply)
      ~ security_opts                          
     = [] -> (known after apply)
      ~ shm_size                               
     = 64 -> (known after apply)
      ~ stop_signal                            
     = "SIGQUIT" -> (known after apply)        
      ~ stop_timeout                           
     = 0 -> (known after apply)
      - storage_opts                           
     = {} -> null
      - sysctls                                
     = {} -> null
      - tmpfs                                  
     = {} -> null
        # (20 unchanged attributes hidden)     

      ~ healthcheck (known after apply)        

      ~ labels (known after apply)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)  
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.     

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.      

  Enter a value: yes

docker_container.nginx: Destroying... [id=08b0fe62afbf914b70fc225de487be660eb28a06412560c37be5511294544036]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=be509c8f045e47fd0d7f72ecd47191bbf2b0cc62826b3a47056468d33106042a]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.


### terraform destroy

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=be509c8f045e47fd0d7f72ecd47191bbf2b0cc62826b3a47056468d33106042a]

Terraform used the selected providers to       
generate the following execution plan.
Resource actions are indicated with the        
following symbols:
  - destroy

Terraform will perform the following actions:  

  # docker_container.nginx will be destroyed   
  - resource "docker_container" "nginx" {      
      - attach                                 
     = false -> null
      - command                                
     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> null
      - container_read_refresh_timeout_milliseconds = 15000 -> null
      - cpu_shares                             
     = 0 -> null
      - dns                                    
     = [] -> null
      - dns_opts                               
     = [] -> null
      - dns_search                             
     = [] -> null
      - entrypoint                             
     = [
          - "/docker-entrypoint.sh",
        ] -> null
      - env                                    
     = [] -> null
      - group_add                              
     = [] -> null
      - hostname                               
     = "learn-terraform-docker" -> null        
      - id                                     
     = "be509c8f045e47fd0d7f72ecd47191bbf2b0cc62826b3a47056468d33106042a" -> null
      - image                                  
     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34" -> null      
      - init                                   
     = false -> null
      - ipc_mode                               
     = "private" -> null
      - log_driver                             
     = "json-file" -> null
      - log_opts                               
     = {} -> null
      - logs                                   
     = false -> null
      - max_retry_count                        
     = 0 -> null
      - memory                                 
     = 0 -> null
      - memory_swap                            
     = 0 -> null
      - must_run                               
     = true -> null
      - name                                   
     = "tutorial" -> null
      - network_data                           
     = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0  
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16 
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> null
      - network_mode                           
     = "bridge" -> null
      - privileged                             
     = false -> null
      - publish_all_ports                      
     = false -> null
      - read_only                              
     = false -> null
      - remove_volumes                         
     = true -> null
      - restart                                
     = "no" -> null
      - rm                                     
     = false -> null
      - runtime                                
     = "runc" -> null
      - security_opts                          
     = [] -> null
      - shm_size                               
     = 64 -> null
      - start                                  
     = true -> null
      - stdin_open                             
     = false -> null
      - stop_signal                            
     = "SIGQUIT" -> null
      - stop_timeout                           
     = 0 -> null
      - storage_opts                           
     = {} -> null
      - sysctls                                
     = {} -> null
      - tmpfs                                  
     = {} -> null
      - tty                                    
     = false -> null
      - wait                                   
     = false -> null
      - wait_timeout                           
     = 60 -> null
        # (7 unchanged attributes hidden)      

      - ports {
          - external = 8080 -> null
          - internal = 80 -> null
          - ip       = "0.0.0.0" -> null       
          - protocol = "tcp" -> null
        }
    }

  # docker_image.nginx will be destroyed       
  - resource "docker_image" "nginx" {
      - id           = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx" -> null
      - image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34" -> null
      - keep_locally = false -> null
      - name         = "nginx" -> null
      - repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34" -> null
    }

Plan: 0 to add, 0 to change, 2 to destroy.     

Do you really want to destroy all resources?   
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

docker_container.nginx: Destroying... [id=be509c8f045e47fd0d7f72ecd47191bbf2b0cc62826b3a47056468d33106042a]
docker_container.nginx: Destruction complete after 1s
docker_image.nginx: Destroying... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_image.nginx: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.


### terraform apply                 
       
Terraform used the selected providers to       
generate the following execution plan.
Resource actions are indicated with the        
following symbols:
  + create

Terraform will perform the following actions:  

  # docker_container.nginx will be created     
  + resource "docker_container" "nginx" {      
      + attach                                 
     = false
      + bridge                                 
     = (known after apply)
      + command                                
     = (known after apply)
      + container_logs                         
     = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                             
     = (known after apply)
      + env                                    
     = (known after apply)
      + exit_code                              
     = (known after apply)
      + hostname                               
     = (known after apply)
      + id                                     
     = (known after apply)
      + image                                  
     = (known after apply)
      + init                                   
     = (known after apply)
      + ipc_mode                               
     = (known after apply)
      + log_driver                             
     = (known after apply)
      + logs                                   
     = false
      + must_run                               
     = true
      + name                                   
     = "ExampleNginxContainer"
      + network_data                           
     = (known after apply)
      + read_only                              
     = false
      + remove_volumes                         
     = true
      + restart                                
     = "no"
      + rm                                     
     = false
      + runtime                                
     = (known after apply)
      + security_opts                          
     = (known after apply)
      + shm_size                               
     = (known after apply)
      + start                                  
     = true
      + stdin_open                             
     = false
      + stop_signal                            
     = (known after apply)
      + stop_timeout                           
     = (known after apply)
      + tty                                    
     = false
      + wait                                   
     = false
      + wait_timeout                           
     = 60

      + healthcheck (known after apply)        

      + labels (known after apply)

      + ports {
          + external = 8080
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)     
      + image_id     = (known after apply)     
      + keep_locally = false
      + name         = "nginx"
      + repo_digest  = (known after apply)     
    }

Plan: 2 to add, 0 to change, 0 to destroy.     

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.      

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Creation complete after 16s [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 4s [id=fb6b896e9bae07eddb1b973c9d144aa12220c8d9694475b3ab20c5438d2168dd]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.


### terraform apply -var "container_name=YetAnotherName"

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=fb6b896e9bae07eddb1b973c9d144aa12220c8d9694475b3ab20c5438d2168dd]

Terraform used the selected providers to       
generate the following execution plan.
Resource actions are indicated with the        
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:  

  # docker_container.nginx must be replaced    
-/+ resource "docker_container" "nginx" {      
      + bridge                                 
     = (known after apply)
      ~ command                                
     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                         
     = (known after apply)
      - cpu_shares                             
     = 0 -> null
      - dns                                    
     = [] -> null
      - dns_opts                               
     = [] -> null
      - dns_search                             
     = [] -> null
      ~ entrypoint                             
     = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                    
     = [] -> (known after apply)
      + exit_code                              
     = (known after apply)
      - group_add                              
     = [] -> null
      ~ hostname                               
     = "fb6b896e9bae" -> (known after apply)   
      ~ id                                     
     = "fb6b896e9bae07eddb1b973c9d144aa12220c8d9694475b3ab20c5438d2168dd" -> (known after apply)
      ~ init                                   
     = false -> (known after apply)
      ~ ipc_mode                               
     = "private" -> (known after apply)        
      ~ log_driver                             
     = "json-file" -> (known after apply)      
      - log_opts                               
     = {} -> null
      - max_retry_count                        
     = 0 -> null
      - memory                                 
     = 0 -> null
      - memory_swap                            
     = 0 -> null
      ~ name                                   
     = "ExampleNginxContainer" -> "YetAnotherName" # forces replacement
      ~ network_data                           
     = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0  
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16 
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                           
     = "bridge" -> null # forces replacement   
      - privileged                             
     = false -> null
      - publish_all_ports                      
     = false -> null
      ~ runtime                                
     = "runc" -> (known after apply)
      ~ security_opts                          
     = [] -> (known after apply)
      ~ shm_size                               
     = 64 -> (known after apply)
      ~ stop_signal                            
     = "SIGQUIT" -> (known after apply)        
      ~ stop_timeout                           
     = 0 -> (known after apply)
      - storage_opts                           
     = {} -> null
      - sysctls                                
     = {} -> null
      - tmpfs                                  
     = {} -> null
        # (20 unchanged attributes hidden)     

      ~ healthcheck (known after apply)        

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.     

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.      

  Enter a value: yes

docker_container.nginx: Destroying... [id=fb6b896e9bae07eddb1b973c9d144aa12220c8d9694475b3ab20c5438d2168dd]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=506e5a0e63d32a6d8761971fa4879c923276f3199c378a9bf4e75458941c9f00]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.


### terraform init

Initializing the backend...
Initializing provider plugins...
- Reusing previous version of kreuzwerker/docker from the dependency lock file
- Using previously-installed kreuzwerker/docker v3.0.2

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see 
any changes that are required for your infrastructure. All Terraform commands 
should now work.

If you ever set or change modules or backend configuration for Terraform,     
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.


### terraform apply 

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=506e5a0e63d32a6d8761971fa4879c923276f3199c378a9bf4e75458941c9f00]    

Terraform used the selected providers  
to generate the following execution    
plan. Resource actions are indicated   
with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                         
             = (known after apply)     
      ~ command                        
             = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)       
      + container_logs                 
             = (known after apply)     
      - cpu_shares                     
             = 0 -> null
      - dns                            
             = [] -> null
      - dns_opts                       
             = [] -> null
      - dns_search                     
             = [] -> null
      ~ entrypoint                     
             = [
          - "/docker-entrypoint.sh",   
        ] -> (known after apply)       
      ~ env                            
             = [] -> (known after apply)
      + exit_code                      
             = (known after apply)     
      - group_add                      
             = [] -> null
      ~ hostname                       
             = "506e5a0e63d3" -> (known after apply)
      ~ id                             
             = "506e5a0e63d32a6d8761971fa4879c923276f3199c378a9bf4e75458941c9f00" -> (known after apply)
      ~ init                           
             = false -> (known after apply)
      ~ ipc_mode                       
             = "private" -> (known after apply)
      ~ log_driver                     
             = "json-file" -> (known after apply)
      - log_opts                       
             = {} -> null
      - max_retry_count                
             = 0 -> null
      - memory                         
             = 0 -> null
      - memory_swap                    
             = 0 -> null
      ~ name                           
             = "YetAnotherName" -> "tutorial" # forces replacement
      ~ network_data                   
             = [
          - {
              - gateway                
   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address             
   = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address            
   = "02:42:ac:11:00:02"
              - network_name           
   = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)       
      - network_mode                   
             = "bridge" -> null # forces replacement
      - privileged                     
             = false -> null
      - publish_all_ports              
             = false -> null
      ~ runtime                        
             = "runc" -> (known after apply)
      ~ security_opts                  
             = [] -> (known after apply)
      ~ shm_size                       
             = 64 -> (known after apply)
      ~ stop_signal                    
             = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                   
             = 0 -> (known after apply)
      - storage_opts                   
             = {} -> null
      - sysctls                        
             = {} -> null
      - tmpfs                          
             = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)     

        # (1 unchanged block hidden)   
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?  
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=506e5a0e63d32a6d8761971fa4879c923276f3199c378a9bf4e75458941c9f00]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=dbe28f5310cad7e2d773c1b5285d864adafd5ce00a5eac694d2b0ba00907185e]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.


### terraform apply

docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=dbe28f5310cad7e2d773c1b5285d864adafd5ce00a5eac694d2b0ba00907185e]    

Terraform used the selected providers  
to generate the following execution    
plan. Resource actions are indicated   
with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                         
             = (known after apply)     
      ~ command                        
             = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)       
      + container_logs                 
             = (known after apply)     
      - cpu_shares                     
             = 0 -> null
      - dns                            
             = [] -> null
      - dns_opts                       
             = [] -> null
      - dns_search                     
             = [] -> null
      ~ entrypoint                     
             = [
          - "/docker-entrypoint.sh",   
        ] -> (known after apply)       
      ~ env                            
             = [] -> (known after apply)
      + exit_code                      
             = (known after apply)     
      - group_add                      
             = [] -> null
      ~ hostname                       
             = "dbe28f5310ca" -> (known after apply)
      ~ id                             
             = "dbe28f5310cad7e2d773c1b5285d864adafd5ce00a5eac694d2b0ba00907185e" -> (known after apply)
      ~ init                           
             = false -> (known after apply)
      ~ ipc_mode                       
             = "private" -> (known after apply)
      ~ log_driver                     
             = "json-file" -> (known after apply)
      - log_opts                       
             = {} -> null
      - max_retry_count                
             = 0 -> null
      - memory                         
             = 0 -> null
      - memory_swap                    
             = 0 -> null
        name                           
             = "tutorial"
      ~ network_data                   
             = [
          - {
              - gateway                
   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address             
   = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address            
   = "02:42:ac:11:00:02"
              - network_name           
   = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)       
      - network_mode                   
             = "bridge" -> null # forces replacement
      - privileged                     
             = false -> null
      - publish_all_ports              
             = false -> null
      ~ runtime                        
             = "runc" -> (known after apply)
      ~ security_opts                  
             = [] -> (known after apply)
      ~ shm_size                       
             = 64 -> (known after apply)
      ~ stop_signal                    
             = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                   
             = 0 -> (known after apply)
      - storage_opts                   
             = {} -> null
      - sysctls                        
             = {} -> null
      - tmpfs                          
             = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)     

        # (1 unchanged block hidden)   
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + container_id = (known after apply) 
  + image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx"

Do you want to perform these actions?  
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=dbe28f5310cad7e2d773c1b5285d864adafd5ce00a5eac694d2b0ba00907185e]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx"


### terraform output

container_id = "c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801"
image_id = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx"


### terraform destroy
docker_image.nginx: Refreshing state... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]
docker_container.nginx: Refreshing state... [id=c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801]    

Terraform used the selected providers  
to generate the following execution    
plan. Resource actions are indicated   
with the following symbols:
  - destroy

Terraform will perform the following actions:

  # docker_container.nginx will be destroyed
  - resource "docker_container" "nginx" {
      - attach                         
             = false -> null
      - command                        
             = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> null
      - container_read_refresh_timeout_milliseconds = 15000 -> null
      - cpu_shares                     
             = 0 -> null
      - dns                            
             = [] -> null
      - dns_opts                       
             = [] -> null
      - dns_search                     
             = [] -> null
      - entrypoint                     
             = [
          - "/docker-entrypoint.sh",   
        ] -> null
      - env                            
             = [] -> null
      - group_add                      
             = [] -> null
      - hostname                       
             = "c950f5befbaa" -> null  
      - id                             
             = "c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801" -> null
      - image                          
             = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34" -> null
      - init                           
             = false -> null
      - ipc_mode                       
             = "private" -> null       
      - log_driver                     
             = "json-file" -> null     
      - log_opts                       
             = {} -> null
      - logs                           
             = false -> null
      - max_retry_count                
             = 0 -> null
      - memory                         
             = 0 -> null
      - memory_swap                    
             = 0 -> null
      - must_run                       
             = true -> null
      - name                           
             = "tutorial" -> null      
      - network_data                   
             = [
          - {
              - gateway                
   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address             
   = "172.17.0.2"
              - ip_prefix_length          = 16
              - mac_address            
   = "02:42:ac:11:00:02"
              - network_name           
   = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> null
      - network_mode                   
             = "bridge" -> null        
      - privileged                     
             = false -> null
      - publish_all_ports              
             = false -> null
      - read_only                      
             = false -> null
      - remove_volumes                 
             = true -> null
      - restart                        
             = "no" -> null
      - rm                             
             = false -> null
      - runtime                        
             = "runc" -> null
      - security_opts                  
             = [] -> null
      - shm_size                       
             = 64 -> null
      - start                          
             = true -> null
      - stdin_open                     
             = false -> null
      - stop_signal                    
             = "SIGQUIT" -> null       
      - stop_timeout                   
             = 0 -> null
      - storage_opts                   
             = {} -> null
      - sysctls                        
             = {} -> null
      - tmpfs                          
             = {} -> null
      - tty                            
             = false -> null
      - wait                           
             = false -> null
      - wait_timeout                   
             = 60 -> null
        # (7 unchanged attributes hidden)

      - ports {
          - external = 8080 -> null    
          - internal = 80 -> null      
          - ip       = "0.0.0.0" -> null
          - protocol = "tcp" -> null   
        }
    }

  # docker_image.nginx will be destroyed
  - resource "docker_image" "nginx" {  
      - id           = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx" -> null        
      - image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34" -> null
      - keep_locally = false -> null   
      - name         = "nginx" -> null 
      - repo_digest  = "nginx@sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34" -> null       
    }

Plan: 0 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  - container_id = "c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801" -> null
  - image_id     = "sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx" -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.     
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

docker_container.nginx: Destroying... [id=c950f5befbaaa5dbb0eef7d6751dddd4eca9578cfc23a5437acc09d031d6b801]
docker_container.nginx: Destruction complete after 1s
docker_image.nginx: Destroying... [id=sha256:91734281c0ebfc6f1aea979cffeed5079cfe786228a71cc6f1f46a228cde6e34nginx]  
docker_image.nginx: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.
