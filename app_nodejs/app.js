const express = require("express");
const moment = require("moment");
const client = require("prom-client");
const fs = require("fs");
const path = require("path");

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



const visitsFilePath = path.join(__dirname, "data/visits.json");

const readVisits = () => {
  try {
    if (!fs.existsSync(visitsFilePath)) {
      fs.writeFileSync(visitsFilePath, JSON.stringify({ visits: 0 }));
    }

    const data = fs.readFileSync(visitsFilePath, "utf-8");
    return JSON.parse(data);
  } catch (error) {
    console.error("Error reading visits file:", error);
    return { visits: 0 }; 
  }
};

const writeVisits = (visits) => {
  try {
    fs.writeFileSync(visitsFilePath, JSON.stringify({ visits }));
  } catch (error) {
    console.error("Error writing visits file:", error);
  }
};

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

app.use((req, res, next) => {
  const visitsData = readVisits();
  visitsData.visits += 1; 
  writeVisits(visitsData.visits); 
  console.log(`Updated visits count: ${visitsData.visits}`);
  next(); 
});

app.get("/visits", (req, res) => {
  try {
    const visitsData = readVisits();
    res.json({ visits: visitsData.visits });
  } catch (error) {
    console.error("Error reading visits:", error);
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
