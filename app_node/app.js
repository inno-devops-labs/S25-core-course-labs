const express = require('express');
const client = require('prom-client'); 
const fs = require('fs');
const path = require('path');
const util = require('util');

const app = express();
const PORT = 3001;

const logDir = '/app/logs';
try {
  if (!fs.existsSync(logDir)) {
    fs.mkdirSync(logDir, { recursive: true });
  }
} catch (err) {
  console.error("Error creating log directory:", err);
}

const logFilePath = path.join(logDir, 'app_nodejs.log');
let logStream;
try {
  logStream = fs.createWriteStream(logFilePath, { flags: 'a' });
} catch (err) {
  console.error("Error opening log file:", err);
}

const logStdout = process.stdout;

client.collectDefaultMetrics();
const requestCounter = new client.Counter({
  name: 'node_app_requests_total',
  help: 'Total number of requests'
});

console.log = function () {
  const message = util.format.apply(null, arguments) + "\n";
  try {
    logStream.write(message);
  } catch (err) {
    console.error("Logging failed, writing to stdout instead.");
  }
  logStdout.write(message);
};

const quotes = [
  "Talk is cheap. Show me the code. - Linus Torvalds",
  "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
  "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
  "First, solve the problem. Then, write the code. - John Johnson",
  "Code is like humor. When you have to explain it, it’s bad. - Cory House"
];

function getRandomQuote() {
  return quotes[Math.floor(Math.random() * quotes.length)];
}

app.get('/', (req, res) => {
  const quote = getRandomQuote();
  requestCounter.inc();
  console.log(`Request received at /, sending quote: ${quote}`);
  res.send(`<h1>Programming Quote</h1><p>${quote}</p>`);
});

app.get('/metrics', async (req, res) => {
  try {
    res.set('Content-Type', client.register.contentType);
    res.end(await client.register.metrics());
  } catch (err) {
    console.error("Error fetching metrics:", err);
    res.status(500).send("Error retrieving metrics");
  }
});

app.get('/health', (req, res) => {
  res.status(200).send('OK');
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
}

module.exports = app;
