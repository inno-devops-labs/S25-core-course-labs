class FetchComicError extends Error {
    constructor(message) {
        super(message);
        this.name = 'FetchComicError';
    }
}

async function ComicFetch() {
    const title = document.getElementById("comic-title");
    const image = document.getElementById("comic-image");
    const date = document.getElementById("comic-date");
    const released = document.getElementById("comic-released");

    try {
        const response = await fetch(`https://xkcd.vercel.app/?comic=latest`);
        console.log(response)
       
        if (!response.ok) {
            throw new FetchComicError('Fetching the Comic has failed');
        }

        const comic = await response.json();
        
        title.textContent = comic.safe_title;
        image.src = comic.img;
        image.alt = comic.alt;
        const ComicDate = new Date(comic.year, comic.month - 1, comic.day);
        date.textContent = ComicDate.toLocaleDateString();

    } catch (error) {
        if (error instanceof FetchComicError) {
            console.error(error.message);
        } else {
            console.error('An unexpected error occurred:', error);
        }
    }
}

const comic = document.getElementById('comic');
if (comic) {
    comic.addEventListener('click', () => {
        ComicFetch().then(()=>{
            const container = document.getElementsByClassName("comic-container")[0];
            container.classList.remove('hidden');
        });
        comic.classList.add('hidden');
    });
}

// Export functions for testing
module.exports = { ComicFetch, FetchComicError };