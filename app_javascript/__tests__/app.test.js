const request = require("supertest");
const app = require("../server.js");

let server;

beforeAll((done) => {
    server = app.listen(3000, done);
});

afterAll((done) => {
    server.close(done);
});

test("GET / should return Moscow time", async () => {
    const response = await request(app).get("/");
    expect(response.status).toBe(200);
    expect(response.text).toContain("Current Time in Moscow");
});