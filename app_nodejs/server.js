const express = require('express');
const moment = require('moment-timezone');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  const currentTime = moment().tz("Europe/Moscow").format("YYYY-MM-DD HH:mm:ss");
  res.render('index', { currentTime });
});

app.use((req, res) => {
  res.status(404).render('error', { message: 'Page not found' });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});