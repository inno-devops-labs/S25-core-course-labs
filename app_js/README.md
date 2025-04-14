# Moscow Time Web Application

Simple Node.js web application for bonus Lab 1 task that displays the current time in Moscow. It is built using the Express.js framework and EJS for rendering the HTML page.

## Requirements

- Node.js 22+
- Dependencies listed in `package.json`

## Docker

### How to build?

```bash
docker build -t app_js:alpine .
```

### How to pull

```bash
docker pull raydenoir/app_js:alpine
```

### How to Run

```bash
docker run -p 127.0.0.1:<desired_port>:3000 -d --name app_js-alpine app_js:alpine
```

## Docker Distroless Image Version

### How to build?

```bash
docker build -f distroless.Dockerfile -t app_js:distroless .
```

### How to pull

```bash
docker pull raydenoir/app_js:distroless
```

### How to Run

```bash
docker run -p 127.0.0.1:<desired_port>:3000 -d --name app_js-distroless app_js:distroless
```

## Manual Setup

1. Clone the repository

2. Make sure you're in the JavaScript application directory

   ```bash
   cd ./app_js
   ```

3. Install dependencies

   ```bash
   npm install
   ```

## Running the Application

```bash
npm start
```

## Using the Application

Go to <http://127.0.0.1:3000/time> (in case it runs locally)
