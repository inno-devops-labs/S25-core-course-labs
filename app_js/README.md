# Vue.js Real-Time Clock

## Overview
Displays a real-time digital clock with smooth transitions and gradient background

## Features
- Auto-updating time display
- Responsive design
- Animated background
- Clean UI with shadow effects

## Installation
```bash
npm install
npm run dev
```

## Run
```bash
npm run-script dev 
```
## Docker run

Build and run both docker images.

```bash
docker build -t yourusername/app_js .
docker run -p 80:80 yourusername/app_js

docker build -f distroless.Dockerfile -t yourusername/app_js:distroless .
docker run -p 80:80 yourusername/app_js:distroless
```