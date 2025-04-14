const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  const moscowTime = new Date().toLocaleString('en-US', {
    timeZone: 'Europe/Moscow',
    hour12: false,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  });
  
  res.send(`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Moscow Time (Node.js)</title>
        <style>
          body { text-align: center; padding: 50px; }
          h1 { color: #2c3e50; }
          .time { font-size: 24px; color: #e74c3c; }
        </style>
      </head>
      <body>
        <h1>Current Time in Moscow</h1>
        <p class="time">${moscowTime}</p>
      </body>
    </html>
  `);
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});
