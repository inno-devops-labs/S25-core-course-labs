const express = require('express');
const app = express();
const port = 3000;

// Set EJS as templating engine
app.set('view engine', 'ejs');

// Array of motivational quotes
const quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "You are stronger than you think.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future depends on what you do today. – Mahatma Gandhi"
];

// Route for home page
app.get('/', (req, res) => {
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    res.render('index', { quote: randomQuote });
});

// Start the server
app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});
