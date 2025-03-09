const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const client = require('prom-client');

// Set up Prometheus metrics registry and collect default metrics
const register = new client.Registry();
client.collectDefaultMetrics({ register });

// Create a custom gauge metric for current Moscow time (in seconds)
const currentTimeGauge = new client.Gauge({
  name: 'current_moscow_time',
  help: 'Current time in Moscow as a Unix timestamp',
});
register.registerMetric(currentTimeGauge);

// File path for persisting the visit counter
const VISITS_FILE = 'visits';

// Helper function to format the date in 'YYYY-MM-DD HH:MM:SS' format
function formatDate(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');
  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

// Functions to read and update visit counter
function getVisits() {
  try {
    if (fs.existsSync(VISITS_FILE)) {
      const data = fs.readFileSync(VISITS_FILE, 'utf8');
      return parseInt(data, 10) || 0;
    }
    return 0;
  } catch (err) {
    return 0;
  }
}

function updateVisits() {
  const count = getVisits() + 1;
  fs.writeFileSync(VISITS_FILE, count.toString(), 'utf8');
  return count;
}

// Main route: shows current time in Moscow
app.get('/', (req, res) => {
  // Get current time in Moscow using the built-in Intl API
  const options = { timeZone: 'Europe/Moscow', hour12: false };
  const moscowTimeString = new Date().toLocaleString('en-US', options);
  const moscowTime = new Date(moscowTimeString);
  // Update Prometheus gauge (convert to seconds)
  currentTimeGauge.set(moscowTime.getTime() / 1000);
  // Format the time for display
  const formattedTime = formatDate(moscowTime);
  // Update visit counter
  updateVisits();
  res.send(`
    <h1>Welcome to my Node.js Web App!</h1>
    <h1>Current Time in Moscow: ${formattedTime} MSK</h1>
  `);
});

// displays the current visit count
app.get('/visits', (req, res) => {
  const count = getVisits();
  res.send(`<h2>Number of visits: ${count}</h2>`);
});

// Expose metrics endpoint for Prometheus
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

// Start server on port 3000 (or process.env.PORT if defined)
const PORT = process.env.PORT || 3000;
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Node.js app is running at http://localhost:${PORT}`);
  });
}

module.exports = app;
