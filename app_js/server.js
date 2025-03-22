const express = require('express');
const path = require('path');
const app = express();
const timeRoutes = require('./app/routes/timeRoutes');
const { prometheusMiddleware, metricsHandler } = require('./app/middlewares/monitoring');

app.set('views', path.join(__dirname, 'app/views'));
app.set('view engine', 'html');
app.engine('html', require('ejs').renderFile);

// Use Prometheus Middleware
app.use(prometheusMiddleware);

// Routes
app.use('/time', timeRoutes);

// Metrics endpoint for Prometheus
app.get('/metrics', metricsHandler);

// Start server
const PORT = 3005;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
