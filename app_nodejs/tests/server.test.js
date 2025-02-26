const request = require("supertest");
const app = require("../server"); // Импортируем app, а не server

describe("GET /", () => {
    it("should return the current Moscow time", async () => {
        const response = await request(app).get("/");
        expect(response.statusCode).toBe(200);
        expect(response.text).toMatch(/Current Moscow Time:/);
    });
});
