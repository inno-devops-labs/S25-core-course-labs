const request = require("supertest");
const app = require("../app");

describe("GET /", () => {
  it("should return 200 and include the New York time header", async () => {
    const response = await request(app).get("/");
    expect(response.status).toBe(200);
    expect(response.text).toMatch(/Current Time in New York:/);
  });
});
