# New York Time Web App

## Overview
This is a simple JavaScript web application using **Node.js & Express.js** that displays the **current time in New York**. The time updates each time the page is refreshed.

## Installation Guide

### Prerequisites
- Node.js installed

### Steps to Run Locally
1. Clone this repository:
   ```bash
    https://github.com/SuleimanKarimEddin/S25-core-course-labs/tree/master
    cd S25-core-course-labs
    git checkout lab1
    cd app_js
    npm install
    npm run start
    

## Framework Choice: Express.js
I chose **Express.js** for this project because:
- It is lightweight and easy to set up.
- It provides a simple way to create web servers in Node.js.
- It has a large ecosystem with useful middleware options.

## Best Practices Followed
1. **Code Readability:** Used meaningful variable names and formatting.
2. **Modular Approach:** Separated server logic into a dedicated file.
3. **Timezone Handling:** Used `moment-timezone` to ensure accurate New York time.
4. **Error Handling:** Basic error handling is included in Express.

## Testing and Code Quality
- The app was tested locally to ensure the displayed time updates upon refresh.
- Used `nodemon` during development for automatic reloading.
