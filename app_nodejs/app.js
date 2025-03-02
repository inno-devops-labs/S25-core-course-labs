const express = require("express");
const moment = require("moment");
const client = require("prom-client");

const app = express();
const collectDefaultMetrics = client.collectDefaultMetrics;
collectDefaultMetrics();

const requestCounter = new client.Counter({
    name: "app_requests_total",
    help: "Total number of requests",
});

const currentTimeGauge = new client.Gauge({
    name: "current_time",
    help: "Current time in Abu Dhabi timezone",
});

app.use(express.static("public"));

app.get("/current-time", (req, res) => {
  try {
    requestCounter.inc();
    const abuDabiTime = moment().utcOffset("+04:00").format("HH:mm:ss");
    currentTimeGauge.set(Date.now());
    res.json({ time: abuDabiTime });
  } catch (error) {
    console.error(error)
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.get("/metrics", async (req, res) => {
    res.set("Content-Type", client.register.contentType);
    res.end(await client.register.metrics());
});

app.use((req, res) => {
  res.status(404).json({ error: "Not Found" });
});

if (require.main === module) {
  const PORT = 3001;
  app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

module.exports = app;
