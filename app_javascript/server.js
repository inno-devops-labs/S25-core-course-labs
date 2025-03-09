const express = require('express');
const client = require('prom-client');
const fs = require('fs').promises;
const path = require('path');
const app = express();
const port = 3000;

const register = new client.Registry();
client.collectDefaultMetrics({ register });

const httpRequestDurationMicroseconds = new client.Histogram({
  name: 'http_request_duration_ms',
  help: 'Duration of HTTP requests in ms',
  labelNames: ['method', 'route', 'code'],
  buckets: [50, 100, 200, 300, 400, 500, 1000]
});
register.registerMetric(httpRequestDurationMicroseconds);

app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    httpRequestDurationMicroseconds.labels(req.method, req.route ? req.route.path : req.path, res.statusCode).observe(duration);
  });
  next();
});

app.use(express.static('public'));

const highScoreFile = path.join('/app/data', 'highscore.txt');

async function getHighScore() {
  try {
    const data = await fs.readFile(highScoreFile, 'utf8');
    return parseInt(data.trim(), 10) || 0;
  } catch (err) {
    return 0;
  }
}

async function incrementHighScore() {
  const currentScore = await getHighScore();
  const newScore = currentScore + 10;
  try {
    await fs.writeFile(highScoreFile, newScore.toString(), 'utf8');
    console.log(`Wrote new high score: ${newScore}`);
    return newScore;
  } catch (err) {
    console.error(`Error writing high score: ${err.message}`);
    return currentScore;
  }
}

app.get('/', async (req, res) => {
  await incrementHighScore();
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/highscore', async (req, res) => {
  await incrementHighScore();
  const score = await getHighScore();
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>Snake Game High Score</title>
      <link rel="stylesheet" href="/styles.css"> <!-- Optional -->
    </head>
    <body>
      <h1>High Score</h1>
      <p>Current High Score: ${score}</p>
      <p><a href="/">Back to Game</a></p>
    </body>
    </html>
  `);
});

app.get('/metrics', async (req, res) => {
  try {
    res.set('Content-Type', register.contentType);
    res.end(await register.metrics());
  } catch (ex) {
    res.status(500).end(ex);
  }
});

app.listen(port, () => {
  console.log(`Snake game running at http://localhost:${port}`);
});
