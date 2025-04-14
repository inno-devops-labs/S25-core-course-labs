const express = require('express');
const moment = require('moment-timezone');
const promClient = require('prom-client');

const app = express();
const PORT = process.env.PORT || 3000;

// Create a Prometheus registry
const register = new promClient.Registry();
promClient.collectDefaultMetrics({ register });

// Define a counter metric
const requestCounter = new promClient.Counter({
    name: 'node_app_requests_total',
    help: 'Total number of requests received',
    registers: [register],
});

app.get('/', (req, res) => {
    requestCounter.inc(); // Increment counter each time endpoint is accessed
    const moscowTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
    res.send(`<h1>Current Time in Moscow: ${moscowTime}</h1>`);
});

// Expose `/metrics`
app.get('/metrics', async (req, res) => {
    res.setHeader('Content-Type', register.contentType);
    res.end(await register.metrics());
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
