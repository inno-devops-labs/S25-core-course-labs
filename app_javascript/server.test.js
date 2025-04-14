const request = require('supertest');
const moment = require('moment-timezone');
const app = require('./server');

describe('Server Tests', () => {
  test('GET / should return 200 status code', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
  });

  test('Response should contain "Current time in Moscow"', async () => {
    const response = await request(app).get('/');
    expect(response.text).toContain('Current time in Moscow');
  });

  test('Response should include properly formatted time', async () => {
    const response = await request(app).get('/');
    const timeRegex = /\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/;
    expect(response.text).toMatch(timeRegex);
  });

  test('Time should be in Moscow timezone', async () => {
    const response = await request(app).get('/');
    const moscowTime = moment().tz('Europe/Moscow');
    const responseTime = response.text.match(/\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/)[0];
    const timeDiff = Math.abs(
      moment.tz(responseTime, 'YYYY-MM-DD HH:mm:ss', 'Europe/Moscow').diff(moscowTime, 'seconds')
    );
    expect(timeDiff).toBeLessThan(2);
  });

  test('Response should be HTML', async () => {
    const response = await request(app).get('/');
    expect(response.text).toMatch(/<h1>.*<\/h1>/);
  });
});