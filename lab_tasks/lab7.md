# Lab 7: Monitoring and Logging

## Overview

In this lab, you will become familiar with a logging stack that includes Promtail, Loki, and Grafana. Your goal is to create a Docker Compose configuration and configuration files to set up this logging stack.

## Task 1: Logging Stack Setup

**6 Points:**

1. Study the Logging Stack:
   - Begin by researching the components of the logging stack:
     - [Grafana Webinar: Loki Getting Started](https://grafana.com/go/webinar/loki-getting-started/)
     - [Loki Overview](https://grafana.com/docs/loki/latest/overview/)
     - [Loki GitHub Repository](https://github.com/grafana/loki)

2. Create a Monitoring Folder:
   - Start by creating a new folder named `monitoring` in your project directory.

3. Docker Compose Configuration:
   - Inside the `monitoring` folder, prepare a `docker-compose.yml` file that defines the entire logging stack along with your application.
   - To assist you in this task, refer to these resources for sample Docker Compose configurations:
     - [Example Docker Compose Configuration from Loki Repository](https://github.com/grafana/loki/blob/main/production/docker-compose.yaml)
     - [Promtail Configuration Example](https://github.com/black-rosary/loki-nginx/blob/master/promtail/promtail.yml) (Adapt it as needed)

4. Testing:
   - Verify that the configured logging stack and your application work as expected.

## Task 2: Documentation and Reporting

**4 Points:**

1. Logging Stack Report:
   - Create a new file named `LOGGING.md` to document how the logging stack you've set up functions.
   - Provide detailed explanations of each component's role within the stack.

2. Screenshots:
   - Capture screenshots that demonstrate the successful operation of your logging stack.
   - Include these screenshots in your `LOGGING.md` report for reference.

## Bonus Task: Additional Configuration

**2.5 Points:**

1. Integrating Your Extra App:
   - Extend the `docker-compose.yml` configuration to include your additional application.

2. Configure Stack for Comprehensive Logging:
   - Modify the logging stack's configuration to collect logs from all containers defined in the `docker-compose.yml`.
   - Include screenshots in your `LOGGING.md` report to demonstrate your success.

### Guidelines

- Ensure that your documentation in `LOGGING.md` is well-structured and comprehensible.
- Follow proper naming conventions for files and folders.
- Use code blocks and Markdown formatting where appropriate.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Thoroughly document your work, and ensure the logging stack functions correctly. Utilize the bonus points opportunity to enhance your understanding and the completeness of your setup.
