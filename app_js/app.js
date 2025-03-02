const express = require("express");
const os = require("os");

const app = express();
const port = 3000;

// Function to get the local IPv4 address
function getLocalIP() {
    const interfaces = os.networkInterfaces();
    for (const interfaceName in interfaces) {
        for (const iface of interfaces[interfaceName]) {
            if (!iface.internal && iface.family === "IPv4") {
                return iface.address;
            }
        }
    }
    return "IP not found";
}

app.get("/", (req, res) => {
    const localIP = getLocalIP();
    res.send(`<h1>Your Local IP Address: ${localIP}</h1>`);
});

// Start the server on localhost
app.listen(port, "127.0.0.1", () => {
    console.log(`Server running on http://localhost:${port}`);
});
