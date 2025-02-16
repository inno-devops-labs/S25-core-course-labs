const express = require('express');
const moment = require('moment-timezone');

const app = express();


const PORT = process.env.PORT || 7000;

app.get('/', (req, res) => {
    const moscowTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
    res.send(`<h1>Current Time in Moscow: ${moscowTime}</h1>`);
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
