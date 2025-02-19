# Logging Stack Report

## Overview

## Architecture

### Components

- `loki` - log storage, aggregation and querying system
- `promtail` - flexible log collector that can parse logs from files and other inputs and send them (for example to loki)
- `grafana` - visualization tool that can integrate with loki to show and filter logs (or use them in dashboards)

### Interconnections

- promtail uses loki http api to push logs
- grafana uses loki http api to query logs
- promtail uses /var/log and /var/lib/docker/containers/ bind mounts to parse logs

## Observations

- Apparently, there's a [docker driver](https://grafana.com/docs/loki/latest/send-data/docker-driver/) for loki, but the arm64 support landed just a month ago and some sources say it's not production ready yet. Changing the daemon.json config sounds... a bit invasive and not suitable for all cases. Skip.
- There are several ways to differentiate logs from different containers. 
  - Many guides recommend mounting `docker.sock` into `promtail` to use docker service discovery to enrich logs from docker. It's a security hazard. I thought it's not needed since /var/log/docker/ contains all the logs, but apparently docker doesn't put the container and project names inside the logs.
  - One [guide on Habr](https://habr.com/ru/articles/784410/) suggests using `labels-regex` in the logging options to add container and project names to the logs, but this is done using `daemon.json`, which I wanted to avoid. 
    - I figured I can do it on a container level by using `logging > options` field in the docker-compose.yaml and to specify only the labels I need and not use an all-allowing regex.
    - Learned about [Docker loggin driver tag settings](https://docs.docker.com/engine/logging/log_tags/) along the way. Good info, but not very useful for this lab, though you can [use it](https://gist.github.com/ruanbekker/c6fa9bc6882e6f324b4319c5e3622460?permalink_comment_id=4162236) to parse Prom labels from the Docker tag pattern because Docker tag is a label (duh, not confused yet?) that is outputted by the Docker logging driver by default.
    - Switching to a journald driver was also an option because it enables container id and container names by default, but I still didn't practice in setting up systemd log rotation etc., so I'll stick with the json-file driver.
- [vector](https://vector.dev/) is a tool that can send Docker logs to loki and it looks good, but ideally it should be set up as an executable on the host (and I have a `colima` Docker vm on macOS, deleting vector after the lab sounds fine but it's a painful-to-reproduce config)
- Loki and grafana spawn tons of logs about themselves in the default configs. In a production setup this should be changed.

**Decision**: I'll use `promtail` without the `docker.sock` mount.

## Results

### Screenshots

<img width="1400" alt="Image" src="https://github.com/user-attachments/assets/71893ae0-70a7-4e07-8da3-dd54bc1b13d8" />

It's a screenshot from a Grafana query to Loki that filters both my main and bonus application logs. It has additional labels added by `promtail` to the logs. Check [the issue in my repo](https://github.com/FallenChromium/S25-core-course-labs/issues/10) if for some reason the image is not rendered.