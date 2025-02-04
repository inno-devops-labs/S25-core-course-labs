# CI

1. All tasks are separated and run one after the other, which makes it convenient to debug and see what is broken and where
2. Using github repository secrets to save important data
3. Using GitHub actions (checkout, setup-python, etc.)
4. Ordered execution of jobs using `needs`, for example SNYK needs tests and linter to be done
5. Caching
