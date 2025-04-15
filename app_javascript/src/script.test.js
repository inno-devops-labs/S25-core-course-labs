/**
 * @jest-environment jsdom
 */

global.TextEncoder = require("util").TextEncoder;
global.TextDecoder = require("util").TextDecoder;

const fs = require("fs");
const path = require("path");
const {JSDOM} = require("jsdom");

const html = fs.readFileSync(path.resolve(__dirname, "index.html"), "utf8");
let document, window, timerDisplay, startButton, minutesInput, secondsInput;

beforeEach(() => {
    const dom = new JSDOM(html, {runScripts: "dangerously"});
    window = dom.window;
    document = dom.window.document;

    window.alert = jest.fn();

    jest.useFakeTimers({doNotFake: ["setTimeout", "clearTimeout"]});

    jest.spyOn(global, "setInterval").mockImplementation((fn, delay) => {
        return setTimeout(fn, delay);
    });

    jest.spyOn(global, "clearInterval").mockImplementation((id) => {
        clearTimeout(id);
    });

    timerDisplay = document.getElementById("timer");
    startButton = document.getElementById("start");
    resetButton = document.getElementById("reset");
    minutesInput = document.getElementById("minutes");
    secondsInput = document.getElementById("seconds");

    const scriptEl = document.createElement("script");
    scriptEl.textContent = fs.readFileSync(path.resolve(__dirname, "script.js"), "utf8");
    document.body.appendChild(scriptEl);
});

describe("Countdown Timer", () => {
    test("Initial timer display should be 00:00", () => {
        expect(timerDisplay.textContent).toBe("00:00");
    });


    test("Should not start timer if no time is set", () => {
        minutesInput.value = "";
        secondsInput.value = "";

        startButton.click();

        expect(window.alert).toHaveBeenCalledWith("Please set a valid time!");
    });

});
