const express = require('express');
const path = require('path');
const app = express();
const timeRoutes = require('./app/routes/timeRoutes');

app.set('views', path.join(__dirname, 'app/views'));

app.set('view engine', 'html');
app.engine('html', require('ejs').renderFile);

// Routes
app.use('/time', timeRoutes);

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});