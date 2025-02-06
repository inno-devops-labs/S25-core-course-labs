const request = require('supertest');
const app = require('../server');

describe('Express Server', () => {
  // Test the root endpoint (GET /) to verify it serves the index.html page.
  test('GET / returns index.html with status 200 and HTML content', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.headers['content-type']).toMatch(/html/);
    expect(res.text).toContain('<title>XKCD comic</title>');
  });

  // Test an endpoint that does not exist to verify it returns a 404.
  test('GET /nonexistent returns 404', async () => {
    const res = await request(app).get('/nonexistent');
    expect(res.statusCode).toEqual(404);
  });

  // Test serving of a static asset.
  test('GET /myapp.js returns JavaScript file with status 200', async () => {
    const res = await request(app).get('/myapp.js');
    expect(res.statusCode).toEqual(200);
    expect(res.headers['content-type']).toMatch(/javascript/);
    expect(res.text).toContain('class FetchComicError extends Error');
  });
});
