const request = require("supertest");
const app = require("../app");

jest.mock("moment", () => {
  return jest.fn(() => ({
    utcOffset: jest.fn().mockReturnValue({
      format: jest.fn().mockReturnValue("12:34:56"),
    }),
  }));
});

describe("API Tests - /current-time", () => {
  test("Should return a valid time string", async () => {
    const response = await request(app).get("/current-time");

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty("time");
    expect(response.body.time).toMatch(/^\d{2}:\d{2}:\d{2}$/);
  });

  test("Should return correct Abu Dhabi time (UTC+4)", async () => {
    const response = await request(app).get("/current-time");
    expect(response.body.time).toBe("12:34:56");
  });

  test("Should return 404 for an invalid route", async () => {
    const response = await request(app).get("/invalid-route");
    expect(response.status).toBe(404);
  });
});

