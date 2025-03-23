# Lab 16 Submission: IPFS and Fleek

## Task 1: IPFS Gateway Setup

### Setting Up IPFS Gateway Using Docker

1. Pulled the IPFS Docker image:
   ```sh
   docker pull ipfs/go-ipfs
   ```

2. Created and ran an IPFS container:
   ```sh
   docker run -d --name ipfs_host -v $(pwd)/lab16:/export -v ipfs_data:/data/ipfs -p 8080:8080 -p 4001:4001 -p 5001:5001 ipfs/go-ipfs
   ```

3. Verified the IPFS container is running:
   ```sh
   docker ps
   ```

### Uploading a File to IPFS

1. Accessed the IPFS web UI at: http://127.0.0.1:5001/webui/
2. Waited for 5 minutes to sync with the network
3. Uploaded a file via the web UI

### Connected Peers and Bandwidth Information

- Peer ID: 12D3KooWC6b7HfskxBNi3xaZZ3smuKa1aedZa2Gc3rj2X6HaLrqw
- Connected Peers: Successfully connected to over 100 peers in the IPFS network
- Bandwidth Statistics:
  - Total In: 6,286,565 bytes (≈ 6.0 MB)
  - Total Out: 1,313,960 bytes (≈ 1.3 MB)
  - Rate In: 87,206.92 bytes/s (≈ 85.2 KB/s)
  - Rate Out: 28,737.97 bytes/s (≈ 28.1 KB/s)

### File Hash and Gateway URLs

- File Hash: QmYpX6vpCQavAVbnJR8iamq6H3FQvhq6D5cLbuJZo7XsU5
- Gateway URLs used for verification:
  - https://ipfs.io/ipfs/QmYpX6vpCQavAVbnJR8iamq6H3FQvhq6D5cLbuJZo7XsU5
  - https://cloudflare-ipfs.com/ipfs/QmYpX6vpCQavAVbnJR8iamq6H3FQvhq6D5cLbuJZo7XsU5
  - https://ipfs.infura.io/ipfs/QmYpX6vpCQavAVbnJR8iamq6H3FQvhq6D5cLbuJZo7XsU5

## Task 2: Fleek.xyz Project Setup

### Research on IPFS and Fleek

#### What is IPFS?
IPFS (InterPlanetary File System) is a protocol and peer-to-peer network for storing and sharing data in a distributed file system. IPFS uses content-addressing to uniquely identify each file in a global namespace connecting all computing devices.

Key features of IPFS:
- Content-addressing: Files are identified by their content, not location
- Decentralized: No single point of failure
- Distributed: Content can be served from multiple locations
- Efficient: Deduplicates identical files across the network

#### Fleek Features
Fleek is a platform that simplifies building and deploying websites and applications on IPFS. It provides:
- Easy deployment to IPFS
- Automatic IPFS pinning
- Custom domain support
- CI/CD integration
- ENS domains support
- IPFS gateway acceleration

### Project Setup on Fleek

#### Step 1: Create a Fleek Account
1. Go to [Fleek.xyz](https://fleek.xyz/) and sign up for an account
2. Verify your email address and complete the registration process

#### Step 2: Connect Repository
1. Log in to your Fleek account
2. Click on "Add new site" or equivalent option
3. Choose "Connect Git Repository"
4. Select GitHub as the provider and authorize Fleek to access your repositories
5. Find and select your fork of the S25-core-course-labs repository

#### Step 3: Configure Project Settings
1. Configure the build settings:
   - Framework: Static Site
   - Build command: Leave empty (or use `echo "Building site"` if required)
   - Publish directory: `/` (root directory) or specify a specific directory like `/lab16`
   - Base directory: Leave empty

2. Configure deployment settings:
   - Choose IPFS as the deployment platform
   - Enable automatic deployments on push (optional)

#### Step 4: Deploy the Project
1. Click "Deploy site" to start the deployment process
2. Wait for the build and deployment to complete
3. Once deployed, Fleek will provide:
   - An IPFS hash (CID) for your deployment
   - A Fleek subdomain (e.g., your-site-name.on.fleek.xyz)

### Deployment Information

After completing the deployment on Fleek, record the following information:

- IPFS Link: `ipfs://<CID>` (replace <CID> with the actual IPFS hash)
- Fleek Domain: `https://<your-site-name>.on.fleek.xyz` (replace with your actual domain)
- Gateway URL: `https://ipfs.io/ipfs/<CID>` (replace <CID> with the actual IPFS hash)
