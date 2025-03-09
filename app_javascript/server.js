const express = require('express');
const path = require('path');
const fs = require('fs');
const winston = require('winston');
const client = require('prom-client');

const app = express();
const port = 3000;

const collectDefaultMetrics = client.collectDefaultMetrics;
collectDefaultMetrics({ timeout: 5000 });

const httpRequestsTotal = new client.Counter({
  name: 'app_javascript_requests_total',
  help: 'Total requests to the application'
});

// Set up Winston logger
const logDir = path.join(__dirname, 'logs');
const dataDir = path.join(__dirname, 'data');
const visitsFile = path.join(dataDir, 'visits.txt');

if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

function loadVisits() {
  if (!fs.existsSync(visitsFile)) {
    return 0;
  }
  return parseInt(fs.readFileSync(visitsFile, 'utf8') || '0', 10);
}

function saveVisits(count) {
  fs.writeFileSync(visitsFile, count.toString());
}

let visitCount = loadVisits();

const logger = winston.createLogger({
  transports: [
    new winston.transports.File({
      filename: path.join(logDir, 'app.log'),
      level: 'info'
    })
  ]
});

// Serve static files (HTML, CSS, JS) from the 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to count visits
app.use((req, res, next) => {
  visitCount++;
  saveVisits(visitCount);
  next();
});

app.get('/', (req, res) => {
  logger.info('Home page requested');
  httpRequestsTotal.inc();
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/visits', (req, res) => {
  res.send(`Total visits: ${visitCount}`);
});

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', client.register.contentType);
  res.end(await client.register.metrics());
});

// Start the server only if this module is run directly
if (require.main === module) {
  logger.info(`Server is running at http://localhost:${port}`);
  app.listen(port);
}

// Export the app for testing
module.exports = app;