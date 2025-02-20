const express = require("express");
const moment = require("moment-timezone");
const client = require("prom-client");

const app = express();

const collectDefaultMetrics = client.collectDefaultMetrics;
collectDefaultMetrics({ timeout: 5000 });

const requestCounter = new client.Counter({
    name: "app_requests_total",
    help: "Total number of requests",
});

app.get("/", (req, res) => {
    requestCounter.inc();
    const moscowTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
    res.send(`<h1>Current Time in Moscow</h1><p>${moscowTime}</p>`);
});

app.get("/metrics", async (req, res) => {
    res.set("Content-Type", client.register.contentType);
    res.end(await client.register.metrics());
});

const PORT = 6000;
if (require.main === module) {
    app.listen(PORT, "0.0.0.0", () => {
        console.log(`Server running on http://localhost:${PORT}`);
    });
}

module.exports = app;