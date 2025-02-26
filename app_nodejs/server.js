const express = require('express');
const moment = require('moment-timezone');
const promClient = require('prom-client');

const app = express();
const port = 3000;

// 1. Create a Registry to register metrics
const register = new promClient.Registry();

// 2. Collect default metrics (CPU, memory, etc.)
promClient.collectDefaultMetrics({ register });

// 3. Define a custom counter for HTTP requests
const httpRequestsCounter = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests received',
  labelNames: ['method', 'endpoint', 'statusCode']
});

// Register the custom metric
register.registerMetric(httpRequestsCounter);

// 4. Middleware to update the counter after each request finishes
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

// 5. Your existing route for the homepage
app.get('/', (req, res) => {
  const currentTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
  res.render('index', { currentTime });
});

// 6. Expose the /metrics endpoint
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

// 7. 404 handling
app.use((req, res) => {
  res.status(404).render('error', { message: 'Page not found' });
});

// 8. Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
