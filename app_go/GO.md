### 1. Choice Justification

When quickly writing a simple webapp with few functionality the [net/http](https://pkg.go.dev/net/http) package is well suited for ~~that i know only this library~~ its leightweight and simple interfaces. Also, it does not add external dependencies ~~making requirements.txt document empty :\( please don't punish for that~~

### 2. Best Practices
1. [Godoc](https://go.dev/blog/godoc) briefly explaining every program component/module involved in the system. Yes, this regards Python conventions rather, but always putting reasonable comments makes developers/readers understand the structure faster... In most of the cases.
2. [GoLint](https://github.com/golangci/golangci-lint) extension helped identify lines to be edited for following conventions.
3. Due to the application having just one functionality, a testing has been done manually, without automatic systems.

