# Overview

This service lets you monitor some data about linux kernel code repository, like

- Number of commits
- Time since the first release

To run it locally, you may run

```bash
go run ./
```

With docker, you may try simple build:

```bash
docker build \
   --tag $(whoami)/app_go:v1.1 \
   --build-arg UID=10001 \
   --build-arg GID=10001 .
docker run app_go
```

or distroless build:

```bash
docker build -f distroless.dockerfile -t go_serv_dless .
docker run go_serv_dless
```

it also shows number of visits by `/visit` endpoint!

## Unit testing

The following functionality was covered with unit-tests:

- Correct time calculation
- Extraction of commit numbers
