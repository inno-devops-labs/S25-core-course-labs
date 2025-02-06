// Database of popular songs by year
const songDatabase = {
    1990: { song: "Nothing Compares 2 U", artist: "Sinéad O'Connor" },
    1991: { song: "Everything I Do (I Do It for You)", artist: "Bryan Adams" },
    1992: { song: "I Will Always Love You", artist: "Whitney Houston" },
    1993: { song: "I'd Do Anything for Love (But I Won't Do That)", artist: "Meat Loaf" },
    1994: { song: "The Sign", artist: "Ace of Base" },
    1995: { song: "Gangsta's Paradise", artist: "Coolio ft. L.V." },
    1996: { song: "Macarena (Bayside Boys Mix)", artist: "Los del Río" },
    1997: { song: "Candle in the Wind 1997", artist: "Elton John" },
    1998: { song: "Too Close", artist: "Next" },
    1999: { song: "Believe", artist: "Cher" },
    2000: { song: "Breathe", artist: "Faith Hill" },
    2001: { song: "Hanging by a Moment", artist: "Lifehouse" },
    2002: { song: "How You Remind Me", artist: "Nickelback" },
    2003: { song: "In Da Club", artist: "50 Cent" },
    2004: { song: "Yeah!", artist: "Usher ft. Lil Jon, Ludacris" },
    2005: { song: "We Belong Together", artist: "Mariah Carey" },
    2006: { song: "Bad Day", artist: "Daniel Powter" },
    2007: { song: "Irreplaceable", artist: "Beyoncé" },
    2008: { song: "Low", artist: "Flo Rida ft. T-Pain" },
    2009: { song: "Boom Boom Pow", artist: "The Black Eyed Peas" },
    2010: { song: "Tik Tok", artist: "Kesha" },
    2011: { song: "Rolling in the Deep", artist: "Adele" },
    2012: { song: "Somebody That I Used to Know", artist: "Gotye ft. Kimbra" },
    2013: { song: "Thrift Shop", artist: "Macklemore & Ryan Lewis ft. Wanz" },
    2014: { song: "Happy", artist: "Pharrell Williams" },
    2015: { song: "Uptown Funk", artist: "Mark Ronson ft. Bruno Mars" },
    2016: { song: "Love Yourself", artist: "Justin Bieber" },
    2017: { song: "Shape of You", artist: "Ed Sheeran" },
    2018: { song: "God's Plan", artist: "Drake" },
    2019: { song: "Old Town Road", artist: "Lil Nas X ft. Billy Ray Cyrus" },
    2020: { song: "Blinding Lights", artist: "The Weeknd" },
    2021: { song: "Levitating", artist: "Dua Lipa" },
    2022: { song: "As It Was", artist: "Harry Styles" },
    2023: { song: "Last Night", artist: "Morgan Wallen" },
    2024: { song: "Cruel Summer", artist: "Taylor Swift" }
};

// DOM elements
const generateBtn = document.getElementById('generateBtn');
const resultDiv = document.getElementById('result');
const yearSpan = document.getElementById('year');
const songP = document.getElementById('song');
const artistP = document.getElementById('artist');

// Generate random year between 1990 and 2024
function getRandomYear() {
    return Math.floor(Math.random() * (2024 - 1990 + 1)) + 1990;
}

// Event listener for button click
generateBtn.addEventListener('click', () => {
    const year = getRandomYear();
    const songData = songDatabase[year];
    
    yearSpan.textContent = year;
    songP.textContent = songData.song;
    artistP.textContent = songData.artist;
    
    resultDiv.classList.remove('hidden');
}); 