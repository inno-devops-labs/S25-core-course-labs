const express = require("express");
const moment = require("moment");

const app = express();

app.use(express.static("public"));

app.get("/current-time", (req, res) => {
  try {
    const abuDabiTime = moment().utcOffset("+04:00").format("HH:mm:ss");
    res.json({ time: abuDabiTime });
  } catch (error) {
    console.error(error)
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.use((req, res) => {
  res.status(404).json({ error: "Not Found" });
});

if (require.main === module) {
  const PORT = 3000;
  app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
  });
}

module.exports = app;
