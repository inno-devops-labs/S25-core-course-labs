const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files (HTML, CSS, JS) from the 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Optional: a route to send a custom message if needed
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server only if this module is run directly
if (require.main === module) {
  app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
  });
}

// Export the app for testing
module.exports = app;
