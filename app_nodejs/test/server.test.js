const request = require('supertest');
let expect;

before(async () => {
  const chaiModule = await import('chai');
  expect = chaiModule.expect;
});

const app = require('../server');

describe('GET /', () => {
  it('should return status code 200 and correct content type', (done) => {
    request(app)
      .get('/')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('should contain the expected welcome message and time format', (done) => {
    request(app)
      .get('/')
      .expect(200)
      .end((err, res) => {
         if (err) return done(err);
         const text = res.text;
         expect(text).to.include('Welcome to my Node.js Web App!');
         expect(text).to.include('Current Time in Moscow:');
         const regex = /Current Time in Moscow:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) MSK/;
         const match = text.match(regex);
         expect(match).to.not.be.null;
         
         const dateStr = match[1];
         const parsedDate = new Date(dateStr);
         expect(parsedDate.toString()).to.not.equal('Invalid Date');
         done();
      });
  });

  it('should display the current time accurately within a 2-second threshold', (done) => {
    request(app)
      .get('/')
      .expect(200)
      .end((err, res) => {
         if (err) return done(err);
         const text = res.text;
         const regex = /Current Time in Moscow:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) MSK/;
         const match = text.match(regex);
         expect(match).to.not.be.null;
         const displayedTimeStr = match[1];
         const displayedTime = new Date(displayedTimeStr);
         // Get current Moscow time using the same method as in server.js
         const moscowTime = new Date().toLocaleString('en-US', { timeZone: 'Europe/Moscow' });
         const nowMoscow = new Date(moscowTime);
         const diffSeconds = Math.abs((nowMoscow - displayedTime) / 1000);
         expect(diffSeconds).to.be.below(2);
         done();
      });
  });
});
