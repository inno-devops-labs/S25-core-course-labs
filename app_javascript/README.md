# Game "Snake" in pure js

## Running the application

1. Install the dependencies
```bash
npm install
```

2. Run the server
```bash
npm start
```

That's it! The website can be accessed at `localhost:3000`.

## How to play

Use arrow, like in the good old days, wasd is for losers!
Other than that, who doesn't know how to play snake?

# Unit Tests

The repository uses `jest` framework for testing purposes of main game logic and functionality.
You can run then like this:

```bash
npm test
```

P.S. The further web-side testing might be added later.

# CI

This project has a `GitHub Actions` setup to automatically lint,test and secure scan the code on pull request
or push before pushing it to dockerhub. Please see `.github/workflows/app_javascript.yml` for
more details.
