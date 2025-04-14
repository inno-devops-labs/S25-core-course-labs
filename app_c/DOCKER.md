# Docker best practices

I have implemented the following Docker best practices:

- Choosing the right base image:

  I have decided to use python:alpine3.21 since it
  has no vulnerabilities and is very small

- Exclude with .dockerignore

  I have excluded all unnecessary files using .dockerignore,
 this includes .md files, __pycahce__, and .gitignore

- Create ephemeral containers

  The only thing needed to run the container is forwarding
 a port, and nothing else. As the application is stateless
 itself, the container can be rebooted without the user
 even noticing anything

- Don't install unnecessary packages

  There are no system packages installed at all, only python
 packages that are required to run the server.

- Leverage build cache

  I have sorted the instructions in the following order:
 first, I install python dependencies, since these are
 the least likely, to change, second, I copy the page files and
 the server code, since those are the most likely to change,
 third, I change the user since it is a fast task and needs to be
 done after everything, and I run the server in the end.

- Pin base image versions

  I have pinned the version of alpine that I use.

- Dockerfile instructions

  Only necessary files are copied

  User is changed from root

  Working directory is specified using full path

## Difference between distro and distroless

Surprisingly, the distroless image was larger that the normal
one:

![Image sizes](https://github.com/user-attachments/assets/ade5a061-8cdf-4605-bb21-09db23fa1296)

In this case, I think it is because there were some problems
with the build and previous image was included somehow, even
though that is not supposed to happen.

The main thing about distroless images is that they do not
contain an operating system. That means that they generally
require less space, have less attack vectors, and are more
specialized.

 
