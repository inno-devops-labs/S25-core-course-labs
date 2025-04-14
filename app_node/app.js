const express = require("express");
const app = express();
const port = 3000;

const quotes = [
  "Talk is cheap. Show me the code. — Linus Torvalds",
  "Programs must be written for people to read, and only incidentally for machines to execute. — Harold Abelson",
  "Simplicity is the soul of efficiency. — Austin Freeman",
  "Code is like humor. When you have to explain it, it’s bad. — Cory House",
];

app.get("/", (req, res) => {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  const randomQuote = quotes[randomIndex];
  res.send(`<h1>${randomQuote}</h1>`);
});

app.listen(port, () => {
  console.log(`Node app listening at http://localhost:${port}`);
});
