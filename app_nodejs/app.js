const express = require('express');
const moment = require('moment-timezone');
const winston = require('winston');

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
    });
    next();
});

app.get('/', (req, res) => {
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

if (require.main === module) {
    app.listen(port, () => {
        logger.info(`Server started`, { port });
    });
}

module.exports = app;
