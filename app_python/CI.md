## CI

For optimizing CI I used the next best practices:
    - Caching 
        - For python requirements
        - For Dockerfile
    - Vulnerability checking
    - Atomic execution for commands (in one `run:` section)
    