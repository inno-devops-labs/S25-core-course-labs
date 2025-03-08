# Best practices

## No root inside the container

```docker
RUN adduser -u 8444 user
```

We add new user, which does not have any admin rights:

```docker
USER user
```

## Choosing the suitable image

I decided to use python slim buster version with stable Debian base. Also, there is a specific version of python to minimize any unexpected compatibility issues of latest release with an application.

## Installation process

Using `\` in `RUN` and breaking long commands for multiple lines makes Dockerfile more readable and easier to maintain.

## Other

- Exposing specific port with `EXPOSE` to clearly indicate on which port container listens for connections
- Copied only specific files instead all by `.`
- Excluded any markdown and environment files from container by including them into `.dockerignore`
