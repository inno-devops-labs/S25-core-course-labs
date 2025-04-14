const request = require('supertest');
const { JSDOM } = require('jsdom');
const moment = require('moment-timezone');
const app = require('../app');

describe('Moscow Time App', () => {
    it('should return 200 status code', async () => {
        const response = await request(app).get('/');
        expect(response.status).toBe(200);
    });

    it('should contain time and date elements', async () => {
        const response = await request(app).get('/');
        const dom = new JSDOM(response.text);
        const document = dom.window.document;

        expect(document.querySelector('.time')).not.toBeNull();
        expect(document.querySelector('.date')).not.toBeNull();
    });

    it('should display correct Moscow time format and current time', async () => {
        const response = await request(app).get('/');
        const dom = new JSDOM(response.text);
        const document = dom.window.document;

        const timeElement = document.querySelector('.time');
        const dateElement = document.querySelector('.date');

        const displayedTime = timeElement.textContent;
        expect(displayedTime).toMatch(/^\d{2}:\d{2}:\d{2}$/);

        const moscowTime = moment().tz('Europe/Moscow');
        
        const [displayedHours, displayedMinutes] = displayedTime.split(':').map(Number);
        expect(displayedHours).toBe(moscowTime.hours());
        expect(displayedMinutes).toBe(moscowTime.minutes());

        const expectedDate = moscowTime.format('MMMM D, YYYY');
        expect(dateElement.textContent).toBe(expectedDate);
    });
});
