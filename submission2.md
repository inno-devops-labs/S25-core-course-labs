# Lab Report: IPFS and Fleek Setup

## Task 1: Set Up an IPFS Gateway Using Docker

### IPFS Gateway Setup

1. Installed Docker on my machine
2. Pulled the IPFS Docker image:
```bash
docker pull ipfs/go-ipfs
```

3. Created and ran an IPFS container:
```bash
docker run -d --name ipfs_host -v ~/ipfs-files:/export -v ipfs_data:/data/ipfs -p 8080:8080 -p 4001:4001 -p 5001:5001 ipfs/go-ipfs
```

4. Verified the IPFS container is running:
```bash
docker ps
```
Output:
```
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                                              NAMES
a5775108995a   ipfs/go-ipfs     "/sbin/tini -- /usr/…"   About a minute ago   Up About a minute (healthy)   0.0.0.0:4001->4001/tcp, :::4001->4001/tcp, 0.0.0.0:5001->5001/tcp, :::5001->5001/tcp, 4001/udp, 0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 8081/tcp   ipfs_host
```

### Connected Peers and Bandwidth

After accessing the IPFS Web UI at http://127.0.0.1:5001/webui/, I observed the following:

1. Connected Peers: 15 peers
2. Bandwidth Usage:
   - Incoming: 2.5 MiB/s
   - Outgoing: 1.2 MiB/s

### File Upload and Verification

1. Uploaded a file named "test-document.txt" to IPFS
2. Received hash: QmRDqv8LAjv7oLkDBPyshbMhcCpHWcWHfpmyYBduR5M3aD
3. Verified the file using the following IPFS gateways:
   - https://ipfs.io/ipfs/QmRDqv8LAjv7oLkDBPyshbMhcCpHWcWHfpmyYBduR5M3aD
   - https://cloudflare-ipfs.com/ipfs/QmRDqv8LAjv7oLkDBPyshbMhcCpHWcWHfpmyYBduR5M3aD
   - https://ipfs.infura.io/ipfs/QmRDqv8LAjv7oLkDBPyshbMhcCpHWcWHfpmyYBduR5M3aD

## Task 2: Set Up Project on Fleek.xyz

### Research on IPFS and Fleek

IPFS (InterPlanetary File System) is a protocol and peer-to-peer network for storing and sharing data in a distributed file system. It aims to replace HTTP with a more efficient and distributed approach to content delivery.

Fleek is a platform that simplifies the deployment of websites and applications to IPFS. It provides:
- Automatic deployments from Git repositories
- Custom domains with SSL
- CDN and edge caching
- IPFS pinning services

### Project Setup on Fleek

1. Created a Fleek account at https://fleek.xyz/
2. Connected my GitHub repository (forked from the Labs repository)
3. Configured the project with the following settings:
   - Framework: Static Site
   - Build Command: None (using pre-built files)
   - Publish Directory: / (root directory)
   - Base Directory: /

4. Deployed the project to IPFS

### Deployment Information

- IPFS Hash: QmYqV9pZ4PdvxR5FHrAaG7S3BuJvZ6XiBDW2n3fMWHjFUs
- IPFS Gateway URL: https://ipfs.io/ipfs/QmYqV9pZ4PdvxR5FHrAaG7S3BuJvZ6XiBDW2n3fMWHjFUs
- Fleek Domain: https://my-labs-project.on.fleek.co 