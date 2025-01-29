# Moscow Time Web App

## Framework

For this web application, I chose `Go` because it is known for its efficiency and strong standard library. We use the `time` package to handle timezone conversions, and `net/http` package to handle HTTP requests and responses.

## Applied Practices

- **Go Coding Conventions**: We followed best practices from [Effective Go](https://go.dev/doc/effective_go), which is a fantastic guide for writing clean and efficient Go code.
- **Testing**: The app was thoroughly tested locally to make sure everything works as expected.
- **Others**: All the packages I used (`net/http`, `time`, and `fmt`) are built into Go's standard library. This means that we do not need any external dependencies, keeping our environment stable and portable.
