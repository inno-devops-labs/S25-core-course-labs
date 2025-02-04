check:
	golangci-lint run
	gofumpt -d -e .

format:
	gofumpt -w .

build:
	go build -o build/ cmd/main.go

run:
	go run cmd/main.go

test:
	go test -cover ./... > coverage.out
