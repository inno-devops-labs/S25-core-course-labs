const express = require('express');
const moment = require('moment-timezone');

const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  const mskTime = moment().tz('Europe/Moscow').format('YYYY-MM-DD HH:mm:ss');
  res.send(`<h1>Current time in Moscow (MSK): ${mskTime}</h1>`);
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
