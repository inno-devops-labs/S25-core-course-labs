const express = require('express');
const moment = require('moment');

const app = express();

app.use(express.static('public'));

app.get('/current-time', (req, res) => {
    const abuDabiTime = moment().utcOffset("+04:00").format("HH:mm:ss");
    res.json({ time: abuDabiTime });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

