const express = require('express');
const app = express();
const port = 3000;

// Middleware to serve static files
app.use(express.static('public'));

// Route to display the current time in Moscow
app.get('/', (req, res) => {
    const moscowTime = new Date().toLocaleString('en-US', { timeZone: 'Europe/Moscow' });
    res.send(`
        <h1>Current Time in Moscow:</h1>
        <p class='time'>${moscowTime}</p>
        <p class='note'>Refresh the page to update the time.</p>
        <style>
            body { background-color: #8bd4ff; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: Arial, sans-serif; overflow: hidden; }
            .time { font-size: 40px; font-weight: bold; }
        </style>
    `);
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});