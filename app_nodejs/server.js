const http = require('http');

const PORT = 8000;

const getMoscowTime = () => {
    const now = new Date();
    const offset = 3 * 60; // UTC+3 in minutes
    const moscowTime = new Date(now.getTime() + (offset - now.getTimezoneOffset()) * 60000);
    return moscowTime.toISOString().replace('T', ' ').substring(0, 19);
};

const requestHandler = (req, res) => {
    if (req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        const response = { moscow_time: getMoscowTime() };
        res.end(JSON.stringify(response));
    } else {
        res.writeHead(405, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Method Not Allowed' }));
    }
};

const server = http.createServer(requestHandler);

server.listen(PORT, '0.0.0.0', () => {
    console.log(`Serving on port ${PORT}`);
});