# Typescript app report

## Decisions

- Vite as a build tool - webpack is too slow and its configuration is cringe
- Vitest as a testing tool - since it plays nicely with Vite (new thing to me, thanks for making me research the best practice test tools for TS!)
- No UI framework - it's a small app and I don't want it to be bloated

## Best practices

- Tested the hell out of both the parser and the CNF checker
- No ': any' except the catch block, hence no problems with the type inference and type safety
- Extensive usage of exceptions for error handling - could be good for error monitoring such as Sentry
- The code is modular and simple with no unnecessary dependencies
