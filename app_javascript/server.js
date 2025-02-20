const express = require('express');
const path = require('path');
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

// Optional: a route to send a custom message if needed
app.get('/', (req, res) => {
  logger.info('Home page requested');
  httpRequestsTotal.inc();
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
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
