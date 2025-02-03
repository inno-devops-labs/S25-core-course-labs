
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
docker build -t go_serv .
docker run go_serv
```

or distroless build:

```bash
docker build -f distroless.dockerfile -t go_serv_dless .
docker run go_serv_dless
```

# Unit testing

The following functionality was covered with unit-tests:

- Correct time calculation
- Extraction of commit numbers
