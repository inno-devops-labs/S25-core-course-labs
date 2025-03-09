const express = require("express");
const moment = require("moment-timezone");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
    const newYorkTime = moment().tz("America/New_York").format("YYYY-MM-DD HH:mm:ss");
    res.send(`<h1>Current Time in New York: ${newYorkTime}</h1>`);
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
