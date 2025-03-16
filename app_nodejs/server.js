const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8000;
const VISITS_FILE = path.join(__dirname, 'visits');

// Initialize visits counter
const initVisits = () => {
    try {
        if (!fs.existsSync(VISITS_FILE)) {
            fs.writeFileSync(VISITS_FILE, '0');
            return 0;
        }
        return parseInt(fs.readFileSync(VISITS_FILE, 'utf8')) || 0;
    } catch (error) {
        console.error('Error initializing visits counter:', error);
        return 0;
    }
};

// Update visits counter
const updateVisits = (count) => {
    try {
        fs.writeFileSync(VISITS_FILE, count.toString());
    } catch (error) {
        console.error('Error updating visits counter:', error);
    }
};

const getMoscowTime = () => {
    const now = new Date();
    const offset = 3 * 60; // UTC+3 in minutes
    const moscowTime = new Date(now.getTime() + (offset - now.getTimezoneOffset()) * 60000);
    return moscowTime.toISOString().replace('T', ' ').substring(0, 19);
};

const requestHandler = (req, res) => {
    if (req.method === 'GET') {
        // Increment visits counter for all GET requests
        let visits = initVisits();
        visits++;
        updateVisits(visits);

        if (req.url === '/visits') {
            // Handle /visits endpoint
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ visits }));
        } else {
            // Handle default endpoint
            res.writeHead(200, { 'Content-Type': 'application/json' });
            const response = { moscow_time: getMoscowTime() };
            res.end(JSON.stringify(response));
        }
    } else {
        res.writeHead(405, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Method Not Allowed' }));
    }
};

const server = http.createServer(requestHandler);

server.listen(PORT, '0.0.0.0', () => {
    console.log(`Serving on port ${PORT}`);
});
