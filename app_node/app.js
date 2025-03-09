const express = require('express');
const fs = require('fs');
const util = require('util');
const app = express();
const PORT = 3001;

const logStream = fs.createWriteStream('/app/logs/app_nodejs.log', { flags: 'a' });
const logStdout = process.stdout;

console.log = function () {
  logStream.write(util.format.apply(null, arguments) + "\n");
  logStdout.write(util.format.apply(null, arguments) + "\n");
};

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
  console.log(`Request received at /, sending quote: ${quote}`);
  res.send(`<h1>Programming Quote</h1><p>${quote}</p>`);
});

// Start the server (only if not in test mode)
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
}

module.exports = app; // Export the app for testing