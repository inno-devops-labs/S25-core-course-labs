const express = require('express');
const moment = require('moment-timezone');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
    const moscowTime = moment().tz('Europe/Moscow');
    
    const html = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Moscow Time</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f2f5;
                }
                .container {
                    text-align: center;
                    padding: 2rem;
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                .time {
                    font-size: 3rem;
                    color: #1a73e8;
                    margin: 1rem 0;
                }
                .date {
                    font-size: 1.5rem;
                    color: #5f6368;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="time">${moscowTime.format('HH:mm:ss')}</div>
                <div class="date">${moscowTime.format('MMMM D, YYYY')}</div>
            </div>
        </body>
        </html>
    `;
    
    res.send(html);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
