# Lab 16: IPFS and Fleek Submission

## Task 1: IPFS Gateway Setup

For this lab, I setup IPFS gateway with Docker and do experiment with distribute file system. Here is how I did everything:

### Step 1: Check Docker Install

First, I check if Docker is install on my system:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ docker --version
Docker version 28.0.1, build 068a01e
```

### Step 2: Get IPFS Docker Image

I pull IPFS Docker image from repository:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ docker pull ipfs/go-ipfs
Using default tag: latest
latest: Pulling from ipfs/go-ipfs
aef0d3bb86ca: Pull complete 
dcc0f7fb2bac: Pull complete 
fe065ccc210b: Pull complete 
79504cd4c722: Pull complete 
45342749d773: Pull complete 
90ea3e36f565: Pull complete 
4e4808fd7f09: Pull complete 
5508b02f6e76: Pull complete 
8cadd41fbbcb: Pull complete 
4f4fb700ef54: Pull complete 
1a3664255ee9: Pull complete 
48437c09a56d: Pull complete 
c7d729ca6d80: Pull complete 
Digest: sha256:23ac0100897d3c8ed1968850a140e6946a9e8fdf29bfd0b32522ff18a4e8690a
Status: Downloaded newer image for ipfs/go-ipfs:latest
docker.io/ipfs/go-ipfs:latest
```

### Step 3: Make Directory for IPFS Files

I create directory to store my files for IPFS sharing:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ mkdir -p ipfs_files
```

### Step 4: Run IPFS Container

I launch IPFS container with this command, make ports mapped and volumes:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ docker run -d --name ipfs_host -v $(pwd)/ipfs_files:/export -v ipfs_data:/data/ipfs -p 8080:8080 -p 4001:4001 -p 5001:5001 ipfs/go-ipfs
c9d885c68af98241e368421982bb516a6356fed5694ab8096f50f0dc0c268e7e
```

Command use these ports:
- 8080: for HTTP gateway access
- 4001: for p2p swarm communications
- 5001: for API to control IPFS

Also I mount two volumes:
- directory ipfs_files as /export in container
- volume ipfs_data for save IPFS datas

### Step 5: Check Container Run

I verify container running OK:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED         STATUS         PORTS                                                                          NAMES
c9d885c68af9   ipfs/go-ipfs                          "/sbin/tini -- /usr/…"   8 seconds ago   Up 7 seconds (healthy)   0.0.0.0:4001->4001/tcp, [::]:4001->4001/tcp, 0.0.0.0:5001->5001/tcp, [::]:5001->5001/tcp, 4001/udp, 0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp, 8081/tcp   ipfs_host
```

### Step 6: Create Test File to Upload

I make simple text file for upload to IPFS:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ echo "This is a test file for IPFS upload" > ipfs_files/test_file.txt
```

### Step 7: Add File to IPFS

I add file to IPFS with command:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ docker exec ipfs_host ipfs add /export/test_file.txt
 36 B / 36 B  100.00%added QmTs2j9tAfoC8qGY1imskcuR6L8eR9PULNR13cqN2XKKY3 test_file.txt
```

This give me hash `QmTs2j9tAfoC8qGY1imskcuR6L8eR9PULNR13cqN2XKKY3`, which is unique identificator for my file in IPFS network.

### Step 8: Check Connected Peers

I was surprise how many peers connect to my IPFS node so fast:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ docker exec ipfs_host ipfs swarm peers | wc -l
170
```

My node connect to 170 peers. This show how distribute nature of IPFS working.

### Step 9: Check Bandwidth Usage

Also I check bandwidth statistic of IPFS node:

```
dpttk@codenv:~/uni/devops/S25-core-course-labs$ docker exec ipfs_host ipfs stats bw
Bandwidth
TotalIn: 5.9 MB
TotalOut: 3.4 MB
RateIn: 7.9 kB/s
RateOut: 21 kB/s
```

### Access File from IPFS Gateways

With hash of file, I can get my file from any public IPFS gateway using URLs:

- https://ipfs.io/ipfs/QmTs2j9tAfoC8qGY1imskcuR6L8eR9PULNR13cqN2XKKY3
- https://cloudflare-ipfs.com/ipfs/QmTs2j9tAfoC8qGY1imskcuR6L8eR9PULNR13cqN2XKKY3
- https://ipfs.infura.io/ipfs/QmTs2j9tAfoC8qGY1imskcuR6L8eR9PULNR13cqN2XKKY3

### Reflexions

Setup IPFS with Docker was pretty easy, actually. Most interesting thing is how fast my node connect to global IPFS network and start exchange data. Interesting that after upload file to IPFS, you can get it from any gateway just with content hash.
