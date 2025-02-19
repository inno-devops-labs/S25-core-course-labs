const express = require("express");
const moment = require("moment-timezone");
const promBundle = require("express-prom-bundle");

const app = express();
const port = 3000;

const metricsMiddleware = promBundle({ includeMethod: true });
app.use(metricsMiddleware);

app.get("/", (req, res) => {
    const moscowTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
    res.send(`Current Moscow Time: ${moscowTime}`);
});

app.get("/metrics", (req, res) => {
    res.set("Content-Type", metricsMiddleware.metricsContentType);
    res.end(metricsMiddleware.metrics());
});

if (require.main === module) {
    app.listen(port, () => {
        console.log(`Server is running on http://localhost:${port}`);
    });
}

module.exports = app;
