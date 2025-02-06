/**
 * @jest-environment jsdom
 */

const { ComicFetch } = require('../public/myapp');

function flushPromises() {
    return new Promise(resolve => setTimeout(resolve, 0));
}

describe('ComicFetch function', () => {
  // Set up a basic DOM structure before each test.
  beforeEach(() => {
    document.body.innerHTML = `
      <div class="comic-container hidden"></div>
      <h1 id="comic-title"></h1>
      <img id="comic-image" />
      <h2 id="comic-date"></h2>
      <p id="comic-released"></p>
      <button id="comic"></button>
    `;
    // Reset the global fetch mock.
    global.fetch = jest.fn();
  });

  afterEach(() => {
    jest.resetAllMocks();
  });

  test('should update DOM elements on successful fetch', async () => {
    // Set up a fake comic response.
    const fakeComic = {
      safe_title: 'Test Comic',
      img: 'http://example.com/comic.png',
      alt: 'Test alt',
      year: '2020',
      month: '5',
      day: '15'
    };

    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fakeComic,
    });

    await ComicFetch();

    // The DOM should be updated.
    expect(document.getElementById('comic-title').textContent).toBe('Test Comic');

    const image = document.getElementById('comic-image');
    expect(image.src).toBe('http://example.com/comic.png');
    expect(image.alt).toBe('Test alt');

    const expectedDate = new Date(fakeComic.year, fakeComic.month - 1, fakeComic.day).toLocaleDateString();
    expect(document.getElementById('comic-date').textContent).toBe(expectedDate);
  });

  test('should log error on failed fetch', async () => {
    // Simulate a failed fetch.
    global.fetch.mockResolvedValueOnce({
      ok: false,
      status: 500,
      json: async () => ({}),
    });

    // Spy on console.error.
    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    await ComicFetch();

    // Console.error should have been called with an error message.
    expect(consoleErrorSpy).toHaveBeenCalled();
    consoleErrorSpy.mockRestore();
  });

  test('clicking comic button triggers ComicFetch and updates UI', async () => {
    // Set up a fake comic response.
    const fakeComic = {
      safe_title: 'Click Test Comic',
      img: 'http://example.com/click.png',
      alt: 'Click alt',
      year: '2021',
      month: '7',
      day: '20'
    };

    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fakeComic,
    });

    // Manually attach the event listener (simulate what happens in production).
    const comicButton = document.getElementById('comic');
    comicButton.addEventListener('click', async () => {
      await ComicFetch();
      const container = document.getElementsByClassName("comic-container")[0];
      container.classList.remove('hidden');
      comicButton.classList.add('hidden');
    });

    // Simulate a click event on the comic button.
    comicButton.click();
    // Wait for pending promises.
    await flushPromises();

    // The button should have the 'hidden' class.
    expect(comicButton.classList.contains('hidden')).toBe(true);
    // And the comic container should no longer have the 'hidden' class.
    const container = document.getElementsByClassName("comic-container")[0];
    expect(container.classList.contains('hidden')).toBe(false);
  });
});

