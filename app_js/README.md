# The JS application to calculate distance between two cities

*Enter names of any two cities and get know the distance between them*

### Run server
```
node server.js
```

### Installing dependencies
You can install it using

```
npm install
```

or with a command:
```
cat requirements.txt | xargs npm install
```

### Project structure
```
app_js/
│
├── server.js
├── public/
│   └── index.html
|   └── script.js
|   └── styles.js
├── package.json
├── package-lock.json
├── .env
... other files
```

# Docker

### Building
```
docker build -t js-cities-dist .
```
#### For Distroless
```
docker build -t js-distroless -f distroless.Dockerfile .
```

### Run
```
docker run -p 3000:3000 js-cities-dist
```
#### For Distroless
```
docker run -p 3000:3000 js-distroless &
```
Run in distroless image in background.


### Pull
```
docker pull nickolaus899/js-cities-dist:latest
```
#### For Distroless
```
docker pull nickolaus899/js-distroless:latest
```

# CI/CD
GitHub Actions were added to the project. I use `js.yml` for automated
actions. 

### Workflow:
1. **Dependencies:**: install from `package.json`
2. **Linter:**: check code quality using `standard`
3. **Tests:**: run unit tests with `jest`
4. **Docker:**: build and push a Docker image to DockerHub

### Workflow Budge
[![Node.js CI with Docker](https://github.com/Nickolaus-899/S25-core-course-labs/actions/workflows/js.yml/badge.svg)](https://github.com/Nickolaus-899/S25-core-course-labs/actions/workflows/js.yml)
