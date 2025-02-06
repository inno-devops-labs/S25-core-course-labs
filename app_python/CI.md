# Best practices for CI actions

## Multistage pipeline

All processes are separeted, runs continiosly and independently from each other. This helps to find out wich part is broken (if it is), enables parallelism for better performance.

## Caching

Cache installed dependecies for further usage in actions.

## Docker

Automated building docker image for Docker Hub.

## Check for vulnerabilities

Check if code satisfied to modern security standarts.

## Linters

Check if code satisfied to modern codestyle of Python.
