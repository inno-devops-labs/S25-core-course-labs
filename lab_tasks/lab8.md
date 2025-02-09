# Lab 8: Monitoring with Prometheus

## Overview

In this lab, you will become acquainted with Prometheus, set it up, and configure applications to collect metrics.

## Task 1: Prometheus Setup

**6 Points:**

1. Learn About Prometheus:
   - Begin by reading about Prometheus and its fundamental concepts:
     - [Prometheus Overview](https://prometheus.io/docs/introduction/overview/)
     - [Prometheus Naming Best Practices](https://prometheus.io/docs/practices/naming/)

2. Integration with Docker Compose:
   - Expand your existing `docker-compose.yml` file from the previous lab to include Prometheus.

3. Prometheus Configuration:
   - Configure Prometheus to collect metrics from both Loki and Prometheus containers.

4. Verify Prometheus Targets:
   - Access `http://localhost:9090/targets` to ensure that Prometheus is correctly scraping metrics.
   - Capture screenshots that confirm the successful setup and place them in a file named `METRICS.md` within the monitoring folder.

## Task 2: Dashboard and Configuration Enhancements

**4 Points:**

1. Grafana Dashboards:
   - Set up dashboards in Grafana for both Loki and Prometheus.
   - You can use examples as references:
     - [Example Dashboard for Loki](https://grafana.com/grafana/dashboards/13407)
     - [Example Dashboard for Prometheus](https://grafana.com/grafana/dashboards/3662)
   - Capture screenshots displaying your successful dashboard configurations and include them in `METRICS.md`.

2. Service Configuration Updates:
   - Enhance the configuration of all services in the `docker-compose.yml` file:
     - Add log rotation mechanisms.
     - Specify memory limits for containers.
   - Ensure these changes are documented within your `METRICS.md` file.

3. Metrics Gathering:
   - Extend Prometheus to gather metrics from all services defined in the `docker-compose.yml` file.

## Bonus Task: Metrics and Health Checks

**To Earn 2.5 Additional Points:**

1. Application Metrics:
   - Integrate metrics into your applications. You can refer to Python examples like:
     - [Monitoring a Synchronous Python Web Application](https://dzone.com/articles/monitoring-your-synchronous-python-web-application)
     - [Metrics Monitoring in Python](https://opensource.com/article/18/4/metrics-monitoring-and-python)

2. Obtain Application Metrics:
   - Configure your applications to export metrics.

3. METRICS.md Update:
   - Document your progress with the bonus tasks, including screenshots, in the `METRICS.md` file.

4. Health Checks:
   - Further enhance the `docker-compose.yml` file's service configurations by adding health checks for the containers.

### Guidelines

- Maintain a well-structured and comprehensible `METRICS.md` document.
- Adhere to file and folder naming conventions.
- Utilize code blocks and Markdown formatting where appropriate.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Ensure thorough documentation of your work, and guarantee that Prometheus correctly collects metrics. Take advantage of the bonus tasks to deepen your understanding and enhance the completeness of your setup.
