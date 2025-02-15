const express = require('express');
const app = express();

// Helper function to format the date in 'YYYY-MM-DD HH:MM:SS' format
function formatDate(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

// Main route: shows current time in Moscow
app.get('/', (req, res) => {
  // Get current date/time in MSK
  const moscowTime = new Date().toLocaleString('en-US', {
    timeZone: 'Europe/Moscow',
  });

  // Format the date in 'YYYY-MM-DD HH:MM:SS' format
  const formattedTime = formatDate(new Date(moscowTime));

  // Send a HTML response
  res.send(`
    <h1>Welcome to my Node.js Web App!</h1>
    <h1>Current Time in Moscow: ${formattedTime} MSK</h1>
  `);
});

// Start server on port 3000 (or process.env.PORT if defined)
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Node.js app is running at http://localhost:${PORT}`);
});