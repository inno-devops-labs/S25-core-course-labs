# Typescript app report

## Decisions

- Vite as a build tool - webpack is too slow and its configuration is cringe
- Vitest as a testing tool - since it plays nicely with Vite (new thing to me, thanks for making me research the best practice test tools for TS!)
- No UI framework - it's a small app and I don't want it to be bloated

## Best practices

- No ': any', hence no problems with the type inference and type safety
- Extensive usage of exceptions for error handling - could be good for error monitoring such as Sentry
- The code is modular and simple with no unnecessary dependencies

### Testing

- Unit tests check both core modules of the app: formula parser and the CNF checker
- A unit test should direct express the intent of a user story. East step in the story is the "unit".
- Used helper structure to easily assert the results
- One test per one concern
- Watchdog mode for `npm test` by default improves the development experience while changing critical code
- lightweight and modern testing tool that integrates well with the IDEs
