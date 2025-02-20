const express = require('express');
const path = require('path');
const winston = require('winston');

const app = express();
const port = 3000;

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
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server only if this module is run directly
if (require.main === module) {
  logger.info(`Server is running at http://localhost:${port}`);
  app.listen(port);
}

// Export the app for testing
module.exports = app;
