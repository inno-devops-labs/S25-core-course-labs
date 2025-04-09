const express = require('express');
const moment = require('moment-timezone');
const promClient = require('prom-client');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

const visitsFilePath = process.env.VISITS_FILE_PATH || path.join(__dirname, 'data', 'visits.txt');

function getVisitsCount() {
  if (fs.existsSync(visitsFilePath)) {
    const data = fs.readFileSync(visitsFilePath, 'utf8');
    return parseInt(data, 10) || 0;
  }
  return 0;
}

function incrementVisitsCount() {
  let count = getVisitsCount();
  count++;
  fs.writeFileSync(visitsFilePath, count.toString(), 'utf8');
  return count;
}
// ----------------------------------------------------

// 2. Create a Registry to register metrics
const register = new promClient.Registry();

// 3. Collect default metrics (CPU, memory, etc.)
promClient.collectDefaultMetrics({ register });

// 4. Define a custom counter for HTTP requests
const httpRequestsCounter = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests received',
  labelNames: ['method', 'endpoint', 'statusCode']
});

// Register the custom metric
register.registerMetric(httpRequestsCounter);

// 5. Middleware to update the counter after each request finishes
app.use((req, res, next) => {
  res.on('finish', () => {
    httpRequestsCounter.inc({
      method: req.method,
      endpoint: req.path,
      statusCode: res.statusCode
    });
  });
  next();
});

// Use EJS as the view engine
app.set('view engine', 'ejs');

// 6. Existing route for the homepage (Moscow time)
app.get('/', (req, res) => {
  const currentTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
  res.render('index', { currentTime });
});

// ----------------------------------------------------
// 7. New /visits endpoint to increment & return the counter
// ----------------------------------------------------
app.get('/visits', (req, res) => {
  const newCount = incrementVisitsCount();
  res.send(`Visits Count: ${newCount}`);
});

// 8. Expose the /metrics endpoint for Prometheus
app.get('/metrics', async (req, res) => {
  try {
    // Gather all metrics from the registry
    const metrics = await register.metrics();
    res.setHeader('Content-Type', register.contentType);
    res.send(metrics);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

// 9. 404 handling
app.use((req, res) => {
  res.status(404).render('error', { message: 'Page not found' });
});

// 10. Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
