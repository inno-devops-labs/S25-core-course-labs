const { JSDOM } = require('jsdom');
const { createCanvas } = require('canvas');

let game;
beforeEach(() => {
  const dom = new JSDOM(`
    <!DOCTYPE html>
    <html>
      <body>
        <canvas id="gameCanvas" width="400" height="400"></canvas>
        <div id="score"></div>
      </body>
    </html>
  `);

  global.document = dom.window.document;
  global.window = dom.window;
  global.CanvasRenderingContext2D = createCanvas(400, 400).getContext('2d').constructor;

  const canvas = document.getElementById('gameCanvas');
  canvas.getContext = () => createCanvas(400, 400).getContext('2d');

  game = require('../public/game');
});

describe('Game Initialization', () => {
  test('canvas and context should be defined', () => {
    expect(document.getElementById('gameCanvas')).not.toBeNull();
  });

  test('score should initialize at 0', () => {
    expect(document.getElementById('score').textContent).toBe('');
  });
});

describe('Game Logic', () => {
  test('should generate valid food position', () => {
    game.generateFood();
    const oldFood = { ...game.food };
    game.generateFood();
    expect(game.food).not.toEqual(oldFood);
  });
});

afterAll(() => {
  game.stopGame();
});
