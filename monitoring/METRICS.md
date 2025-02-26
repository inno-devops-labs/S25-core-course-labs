Docker Compose:

![Docker Compose ps](images/image-5.png)

Prometheus Targets:

![Prometheus Targets](images/image-6.png)

Loki Metrics:

![Loki Metrics](images/image-7.png)

Prometheus Metrics:

![Prometheus Metrics](images/image-8.png)

Applied Changes:

```docker
logging:
      driver: "json-file" # logs should be stored in JSON.
      options:
        max-size: "10m" # Limits the maximum size of a single log file to 10 megabytes.
        max-file: "3" # Keeps a maximum of 3 log files before rotating.
    deploy:
      resources:
        limits:
          memory: 128M # Restricts the container to use a maximum of 128 megabytes of RAM.
```

Finally, I integrated Prometheus Client with /metrics endpoint in both Python and JS applications and added them as Prometheus Targets (along with other components)

![Prometheus Targets Bonus](images/image-9.png)

Components Healthcheck:

![Healthcheks](images/image-10.png)