const express = require('express');
const app = express();
const port = 3000;

// Array of funny advertisements
const funnyAds = [
    "Need a break? Our pillows are so comfy, you'll forget what year it is!",
    "Our coffee is so strong, it can wake up your neighbor's dreams!",
    "Buy our socks! They're like a party for your feet, minus the loud music.",
    "Our vacuum cleaners are so powerful, they might accidentally suck up your mother-in-law's complaints!",
    "Try our chocolate! It's like a hug for your taste buds.",
    "Our GPS is so accurate, it can even find your lost TV remote!",
    "Our mattresses are so comfortable, counting sheep will file for unemployment.",
    "Our umbrellas are so reliable, even ducks are jealous!",
    "Our toasters don't just make toast, they make breakfast worth waking up for!",
    "Our gym membership comes with free guilt trips for skipping workouts!"
];

// Endpoint to get current year
app.get('/year', (req, res) => {
    const currentYear = new Date().getFullYear();
    res.json({ year: currentYear });
});

// Endpoint to get random funny advertisement
app.get('/ad', (req, res) => {
    const randomIndex = Math.floor(Math.random() * funnyAds.length);
    res.json({ advertisement: funnyAds[randomIndex] });
});

// Combined endpoint to get both year and ad
app.get('/year-and-ad', (req, res) => {
    const currentYear = new Date().getFullYear();
    const randomIndex = Math.floor(Math.random() * funnyAds.length);
    res.json({
        year: currentYear,
        advertisement: funnyAds[randomIndex]
    });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
}); 