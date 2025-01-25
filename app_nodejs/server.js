const express = require("express");
const moment = require("moment-timezone");

const app = express();
const port = 3000;

app.get("/", (req, res) => {
    // Get the current time in Moscow
    const moscowTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
    res.send(`Current Moscow Time: ${moscowTime}`);
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});