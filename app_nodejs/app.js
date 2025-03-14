const express = require('express');
const moment = require('moment-timezone');
const winston = require('winston');
const promClient = require('prom-client');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

// Configure winston logger
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json()
    ),
    transports: [
        new winston.transports.Console()
    ]
});

// Configure Prometheus metrics
const collectDefaultMetrics = promClient.collectDefaultMetrics;
collectDefaultMetrics();

const requestCounter = new promClient.Counter({
    name: 'nodejs_http_requests_total',
    help: 'Total number of HTTP requests',
    labelNames: ['method', 'route', 'status']
});

const requestDuration = new promClient.Histogram({
    name: 'nodejs_http_request_duration_seconds',
    help: 'Duration of HTTP requests in seconds',
    labelNames: ['method', 'route']
});

// Middleware for logging requests
app.use((req, res, next) => {
    const start = Date.now();
    res.on('finish', () => {
        const duration = Date.now() - start;
        logger.info('Request processed', {
            method: req.method,
            path: req.path,
            statusCode: res.statusCode,
            duration: `${duration}ms`
        });
        requestCounter.inc({ method: req.method, route: req.path, status: res.statusCode });
        requestDuration.observe({ method: req.method, route: req.path }, duration / 1000);
    });
    next();
});

// Functions for visit counter persistence
function getVisitCount() {
    // Use /data directory for persistent storage in StatefulSet
    const dataDir = fs.existsSync('/data') ? '/data' : __dirname;
    const visitsFile = path.join(dataDir, 'visits');
    
    try {
        if (fs.existsSync(visitsFile)) {
            const count = fs.readFileSync(visitsFile, 'utf8').trim();
            return count ? parseInt(count, 10) : 0;
        }
        return 0;
    } catch (err) {
        logger.error('Error reading visit count', { error: err.message });
        return 0;
    }
}

function incrementVisitCounter() {
    // Use /data directory for persistent storage in StatefulSet
    const dataDir = fs.existsSync('/data') ? '/data' : __dirname;
    const visitsFile = path.join(dataDir, 'visits');
    
    try {
        const count = getVisitCount() + 1;
        fs.writeFileSync(visitsFile, count.toString());
        logger.info('Visit counter incremented', { count, filePath: visitsFile });
        return count;
    } catch (err) {
        logger.error('Error incrementing visit count', { error: err.message, filePath: visitsFile });
        return 0;
    }
}

app.get('/', (req, res) => {
    // Increment visit counter
    incrementVisitCounter();
    
    const moscowTime = moment().tz('Europe/Moscow');
    logger.info('Generating Moscow time', {
        time: moscowTime.format('HH:mm:ss'),
        date: moscowTime.format('MMMM D, YYYY')
    });
    
    const html = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Moscow Time</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f2f5;
                }
                .container {
                    text-align: center;
                    padding: 2rem;
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                .time {
                    font-size: 3rem;
                    color: #1a73e8;
                    margin: 1rem 0;
                }
                .date {
                    font-size: 1.5rem;
                    color: #5f6368;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="time">${moscowTime.format('HH:mm:ss')}</div>
                <div class="date">${moscowTime.format('MMMM D, YYYY')}</div>
            </div>
        </body>
        </html>
    `;
    
    res.send(html);
});

// Health check endpoint
app.get('/health', (req, res) => {
    logger.info('Health check requested');
    res.status(200).json({ status: 'healthy' });
});

// Visits endpoint
app.get('/visits', (req, res) => {
    const visitCount = getVisitCount();
    logger.info('Visits endpoint called', { count: visitCount });
    res.status(200).json({ visits: visitCount });
});

// Metrics endpoint
app.get('/metrics', async (req, res) => {
    try {
        res.set('Content-Type', promClient.register.contentType);
        res.end(await promClient.register.metrics());
    } catch (err) {
        res.status(500).end(err);
    }
});

if (require.main === module) {
    app.listen(port, () => {
        logger.info('Server started', { port });
    });
}

module.exports = app;
