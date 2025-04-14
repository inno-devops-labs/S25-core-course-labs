const express = require("express");
const path = require("path");
const app = express();
const PORT = 8080;

app.use(express.json());

const metrics = {
  start_timer: 0,
  reset_timer: 0,
  timer_finished: 0,
};

app.use(express.static(path.join(__dirname, 'public')));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.get("/metrics", (req, res) => {
  const metricText = `# HELP start_timer_total Total count of start timer events\n# TYPE start_timer_total counter\nstart_timer_total ${metrics.start_timer}\n` +
                     `# HELP reset_timer_total Total count of reset timer events\n# TYPE reset_timer_total counter\nreset_timer_total ${metrics.reset_timer}\n` +
                     `# HELP timer_finished_total Total count of finished timer events\n# TYPE timer_finished_total counter\ntimer_finished_total ${metrics.timer_finished}\n`;

  res.set('Content-Type', 'text/plain');
  res.send(metricText);
});

app.post("/metrics", (req, res) => {
  const { event } = req.body;
  if (metrics.hasOwnProperty(event)) {
    metrics[event]++;
    res.json({ success: true, message: `Metric ${event} recorded.` });
  } else {
    res.status(400).json({ success: false, message: "Invalid event type." });
  }
});

app.listen(PORT, () => {
  console.log(`Metrics server running on http://localhost:${PORT}`);
});
