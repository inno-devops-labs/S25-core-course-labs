# Metrics report

## Screenshots

Please see an [issue on my GitHub repository](https://github.com/FallenChromium/S25-core-course-labs/issues/12) for screenshots (I really don't want ot commit pictures to the repo).

All services are monitored by Prometheus using cAdvisor, a container metrics collector for Docker.

## Log rotation

```diff
+    logging:
+      options:
+        max-size: 10m
```

## Resource constraints

```diff
+    deploy:
+      resources:
+        limits:
+          memory: 256M
```

## Bonus task

Since I am using FastAPI, I can use the [`prometheus-fastapi-instrumentator`](https://pypi.org/project/prometheus-fastapi-instrumentator/) library to instrument the application which does export the basic http_* metrics.

I've tried to use a [Metrics dashboard for FastAPI](https://github.com/Kludex/fastapi-prometheus-grafana/tree/master/grafana/provisioning) to make it look beautiful, but most of the queries were not working. A screenshot of a query that works is provided in the issue.
