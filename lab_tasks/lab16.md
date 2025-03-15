# Lab 16: IPFS and Fleek

In this lab, you will explore essential DevOps tools and set up a project on the Fleek service. Follow the tasks below to complete the lab assignment.

## Task 1: Set Up an IPFS Gateway Using Docker

Objective: Understand and implement an IPFS gateway using Docker, upload a file, and verify it via an IPFS cluster.

1. Set Up IPFS Gateway:
   - Install Docker on your machine if it's not already installed.
     - [Docker Installation Guide](https://docs.docker.com/get-docker/)

   - Pull the IPFS Docker image and run an IPFS container:

     ```sh
     docker pull ipfs/go-ipfs
     docker run -d --name ipfs_host -v /path/to/folder/with/file:/export -v ipfs_data:/data/ipfs -p 8080:8080 -p 4001:4001 -p 5001:5001 ipfs/go-ipfs
     ```

   - Verify the IPFS container is running:

     ```sh
     docker ps
     ```

2. Upload a File to IPFS:
   - Open a browser and access the IPFS web UI:

     ```sh
     http://127.0.0.1:5001/webui/
     ```

   - Explore the web UI and wait for 5 minutes to sync up with the network.
   - Upload any file via the web UI.
   - Use the obtained hash to access the file via any public IPFS gateway. Here are a few options:
     - [IPFS.io Gateway](https://ipfs.io/ipfs/)
     - [Cloudflare IPFS Gateway](https://cloudflare-ipfs.com/ipfs/)
     - [Infura IPFS Gateway](https://ipfs.infura.io/ipfs/)

   - Append your file hash to any of the gateway URLs to verify your file is accessible. Note that it may fail due to network overload, so don't worry if you can't reach it.

3. Documentation:
   - Create a `submission2.md` file.
   - Share information about connected peers and bandwidth in your report.
   - Provide the hash and the URLs used to verify the file on the IPFS gateways.

## Task 2: Set Up Project on Fleek.xyz

Objective: Set up a project on the Fleek service and share the IPFS link.

1. Research:
   - Understand what IPFS is and its purpose.
   - Explore Fleek's features.

2. Set Up:
   - Sign up for a Fleek account if you haven't already.
   - Use your fork of the Labs repository as your project source. Optionally, set up your own website (notify us in advance).
   - Configure the project settings on Fleek.
   - Deploy the Labs repository to Fleek, ensuring it is uploaded to IPFS.

3. Documentation:
   - Share the IPFS link and domain of the deployed project in the `submission2.md` file.

## Additional Resources

- [IPFS Documentation](https://docs.ipfs.io/)
- [Fleek Documentation](https://docs.fleek.xyz/)

### Guidelines

- Use proper Markdown formatting for documentation files.
- Organize files with appropriate naming conventions.
- Create a Pull Request to the main branch of the repository with your completed lab assignment.

> Note: Actively explore and document your findings to gain hands-on experience with IPFS and Fleek.
