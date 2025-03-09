const express = require("express");
const moment = require("moment-timezone");
const promBundle = require("express-prom-bundle");
const fs = require("fs");  // Добавил импорт fs

const app = express();
const port = 3000;

const metricsMiddleware = promBundle({ includeMethod: true });
app.use(metricsMiddleware);

const VISITS_FILE = "/app/data/visits.txt";

function getVisitsCount() {
    if (fs.existsSync(VISITS_FILE)) {
        const count = fs.readFileSync(VISITS_FILE, "utf8");
        return parseInt(count, 10) || 0;
    }
    return 0;
}

function saveVisitsCount(count) {
    fs.writeFileSync(VISITS_FILE, count.toString());
}

app.get("/", (req, res) => {
    const moscowTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
    res.send(`Current Moscow Time: ${moscowTime}`);
});

app.get("/metrics", (req, res) => {
    res.set("Content-Type", metricsMiddleware.metricsContentType);
    res.end(metricsMiddleware.metrics());
});

app.get("/visits", (req, res) => {
    const visitCount = getVisitsCount();
    res.json({ visitCount });
});

if (require.main === module) {
    app.listen(port, () => {
        console.log(`Server is running on http://localhost:${port}`);
    });
}

module.exports = app;
