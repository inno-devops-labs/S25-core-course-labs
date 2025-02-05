# Docker best practices

This document outlines the practices I used in my `Dockerfile`.

## What I did:

1.  Using a base image with a specific version of Python.
2.  Specifying the working directory.
3.  Installing dependencies without cache using `--no-cache-dir`.
4.  Running the application as a non-root user to enhance security.
5.  Copying files with explicit ownership.
6.  Not storing secret keys in the Dockerfile.
7.  Explicitly exposing the port for the web application.


## Differences between Dockerfile and distroless.Dockerfile:
1. In distroless, there is no need for explicit creation of a nonroot user and running the file under their name; using the :nonroot argument suffices.
2. The distroless image contains only the minimal necessary components and lacks shells for running the Golang binary, which reduces the number of attack vectors (CVEs) compared to even lightweight Alpine, which still has some extra functionality in certain cases (apk, shell).
3. In my case, the distroless container has a larger size compared to the standard Dockerfile. Distroless uses a different build format than Alpine. In our case, this leads to a larger size, but with larger projects, distroless will show a smaller container size.
4. Distroless complicates debugging since there is no possibility to run a shell.