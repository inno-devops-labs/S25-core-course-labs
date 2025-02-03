// eslint-disable-next-line no-undef
const express = require('express');
const app = express();
const PORT = 3001;

// Array of programming quotes
const quotes = [
  "Talk is cheap. Show me the code. - Linus Torvalds",
  "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
  "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
  "First, solve the problem. Then, write the code. - John Johnson",
  "Code is like humor. When you have to explain it, it’s bad. - Cory House"
];

// Function to get a random quote
function getRandomQuote() {
  return quotes[Math.floor(Math.random() * quotes.length)];
}

// Define the root route
app.get('/', (req, res) => {
  const quote = getRandomQuote();
  res.send(`<h1>Programming Quote</h1><p>${quote}</p>`);
});

// Start the server (only if not in test mode)
// eslint-disable-next-line no-undef
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server is running on  http://localhost:${PORT}`);
  });
}

// eslint-disable-next-line no-undef
module.exports = app; // Export the app for testing