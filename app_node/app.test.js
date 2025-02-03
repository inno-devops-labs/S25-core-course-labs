/* eslint-disable */

const request = require('supertest');
const app = require('./app'); // Import your Express app

describe('Node.js Web Application Tests', () => {
  // Test the root route
  it('should return a random programming quote', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toContain('<h1>Programming Quote</h1>');
  });
});

/* eslint-enable */
