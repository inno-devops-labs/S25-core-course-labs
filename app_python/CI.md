# CI Overview

1. Each task is isolated and executed sequentially, simplifying the debugging process by clearly indicating what’s failing and where.

2. Important data is secured using GitHub repository secrets.

3. GitHub Actions are employed (such as checkout, setup-python, etc.).

4. Job execution is organized using the "needs" directive. This makes the sequence of jobs clear.
