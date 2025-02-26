const client = require('prom-client');

// Create a Registry to register metrics
const register = new client.Registry();
client.collectDefaultMetrics({ register });

// Create custom metrics
const httpRequestCounter = new client.Counter({
    name: 'http_requests_total',
    help: 'Total number of HTTP requests',
    labelNames: ['method', 'route', 'status_code'],
});

const httpRequestDuration = new client.Histogram({
    name: 'http_request_duration_seconds',
    help: 'HTTP request latency in seconds',
    labelNames: ['method', 'route'],
    buckets: [0.1, 0.5, 1, 3, 5], // Buckets for response time
});

register.registerMetric(httpRequestCounter);
register.registerMetric(httpRequestDuration);

// Middleware to track metrics
const prometheusMiddleware = (req, res, next) => {
    const start = process.hrtime();

    res.on('finish', () => {
        const duration = process.hrtime(start);
        const responseTimeInSeconds = duration[0] + duration[1] / 1e9;

        httpRequestCounter.labels(req.method, req.path, res.statusCode).inc();
        httpRequestDuration.labels(req.method, req.path).observe(responseTimeInSeconds);
    });

    next();
};

// Expose metrics endpoint
const metricsHandler = async (req, res) => {
    res.set('Content-Type', register.contentType);
    res.end(await register.metrics());
};

module.exports = { prometheusMiddleware, metricsHandler };
