## 🚀 Quick Start

### Prerequisites

- Node.js 18+
- NPM/Yarn

### Installation

1. Install dependencies
```bash
npm install
```

2. Run 
```bash
npm start
```

3. Visit browser on `http://localhost:3001`


<br>

## 🐳 Docker 

### Local build
```bash
docker build -t moscow-time .
docker run -p 3001:3001 moscow-time
```

or

### Pull image from dockerhub
```bash
docker pull timurzheksimbaev/node-moscow-time:latest
docker run -p 3001:3001 timurzheksimbaev/node-moscow-time:latest
```

<br>

## 📤 Workflow
1. Tests job initiates: Node setup, npm install, ESLint check, Jest testing with coverage upload, Snyk scan. 
2. Docker job follows with Buildx caching, login and image push.