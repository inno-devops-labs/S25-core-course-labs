const express = require('express');
const moment = require('moment-timezone');

console.log("Web app")


const app = express();
const PORT = 3001;

app.get('/', (req, res) => {
  const moscowTime = moment().tz('Europe/Moscow').format('YYYY-MM-DD HH:mm:ss');
  res.send(`<h1>Current time in Moscow (MSK): ${moscowTime}</h1>`);
});

if (process.env.NODE_ENV !== 'test') {
    app.listen(PORT, () => {
      console.log(`Server is running on port ${PORT}`);
    });
}
  
module.exports = app;