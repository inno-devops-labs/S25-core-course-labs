const express = require('express');
const app = express();
const port = 3000;
const promClient = require('prom-client');
const fs = require('fs');
const path = require('path');

// Define path for visits file
const visitsFilePath = process.env.VISITS_FILE_PATH || path.join(__dirname, 'visits');

// Function to read visit count
const readVisitCount = () => {
  try {
    if (fs.existsSync(visitsFilePath)) {
      const count = parseInt(fs.readFileSync(visitsFilePath, 'utf8').trim(), 10);
      return isNaN(count) ? 0 : count;
    }
    return 0;
  } catch (error) {
    console.error('Error reading visit count:', error);
    return 0;
  }
};

// Function to write visit count
const writeVisitCount = (count) => {
  try {
    fs.writeFileSync(visitsFilePath, count.toString());
  } catch (error) {
    console.error('Error writing visit count:', error);
  }
};

// Create a Registry to register the metrics
const register = new promClient.Registry();
promClient.collectDefaultMetrics({ register });

// Create custom metrics
const httpRequestDurationMicroseconds = new promClient.Histogram({
    name: 'http_request_duration_seconds',
    help: 'Duration of HTTP requests in seconds',
    labelNames: ['method', 'route', 'status_code'],
    buckets: [0.1, 0.3, 0.5, 0.7, 1, 3, 5, 7, 10]
});

const httpRequestCounter = new promClient.Counter({
    name: 'http_requests_total',
    help: 'Total number of HTTP requests',
    labelNames: ['method', 'route', 'status_code']
});

// Register the metrics
register.registerMetric(httpRequestDurationMicroseconds);
register.registerMetric(httpRequestCounter);

// Middleware to track request duration and count
app.use((req, res, next) => {
    const start = Date.now();
    
    res.on('finish', () => {
        const duration = Date.now() - start;
        const route = req.path;
        const method = req.method;
        const statusCode = res.statusCode;
        
        httpRequestDurationMicroseconds
            .labels(method, route, statusCode)
            .observe(duration / 1000);
        
        httpRequestCounter
            .labels(method, route, statusCode)
            .inc();
    });
    
    next();
});

// Array of funny advertisements
const funnyAds = [
    "Need a break? Our pillows are so comfy, you'll forget what year it is!",
    "Our coffee is so strong, it can wake up your neighbor's dreams!",
    "Buy our socks! They're like a party for your feet, minus the loud music.",
    "Our vacuum cleaners are so powerful, they might accidentally suck up your mother-in-law's complaints!",
    "Try our chocolate! It's like a hug for your taste buds.",
    "Our GPS is so accurate, it can even find your lost TV remote!",
    "Our mattresses are so comfortable, counting sheep will file for unemployment.",
    "Our umbrellas are so reliable, even ducks are jealous!",
    "Our toasters don't just make toast, they make breakfast worth waking up for!",
    "Our gym membership comes with free guilt trips for skipping workouts!"
];

// Endpoint to get current year
app.get('/year', (req, res) => {
    const currentYear = new Date().getFullYear();
    res.json({ year: currentYear });
});

// Endpoint to get random funny advertisement
app.get('/ad', (req, res) => {
    const randomIndex = Math.floor(Math.random() * funnyAds.length);
    res.json({ advertisement: funnyAds[randomIndex] });
});

// Combined endpoint to get both year and ad
app.get('/year-and-ad', (req, res) => {
    const currentYear = new Date().getFullYear();
    const randomIndex = Math.floor(Math.random() * funnyAds.length);
    res.json({
        year: currentYear,
        advertisement: funnyAds[randomIndex]
    });
});

// New endpoint to get and increment visit count
app.get('/visits', (req, res) => {
  let count = readVisitCount();
  count++;
  writeVisitCount(count);
  res.json({ visits: count });
});

// Expose metrics endpoint
app.get('/metrics', async (req, res) => {
    res.set('Content-Type', register.contentType);
    res.end(await register.metrics());
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
}); 