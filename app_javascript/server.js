const express = require("express");
const moment = require("moment-timezone");

const app = express();

app.get("/", (req, res) => {
    const moscowTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
    res.send(`<h1>Current Time in Moscow</h1><p>${moscowTime}</p>`);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});