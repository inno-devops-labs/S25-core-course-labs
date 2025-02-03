const http = require("http");

// Function to get the current time in different time zones
const getTimeForZones = () => {
    const timeZones = {
        "Moscow": "Europe/Moscow",
        "UTC": "UTC",
        "New York": "America/New_York",
        "Tokyo": "Asia/Tokyo"
    };

    let timeString = "Current Time in Different Zones:\n";
    for (const [city, zone] of Object.entries(timeZones)) {
        timeString += `${city}: ${new Date().toLocaleString("en-US", { timeZone: zone })}\n`;
    }
    return timeString;
};

// Server Configuration
const PORT = 3000;
const HOST = "0.0.0.0";

const server = http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end(getTimeForZones());
});

server.listen(PORT, HOST, () => {
    console.log(`Server running at http://${HOST}:${PORT}/`);
});;
