# Fork Counter Web Application

![CI](https://github.com/secretanry/S25-core-course-labs/actions/workflows/ci-go.yml/badge.svg)

A GO web application built with **net/http** to display current amount of forks of https://github.com/inno-devops-labs/S25-core-course-labs.

---

## **Features**
- Displays current amount of forks in course repo.
- Automatically updates the amount on page refresh.
- Responsive design for seamless viewing on all devices.
- Do not show raw data, shows loading page if data is still processing

---

## **Technologies Used**
- **net/http**: A basic, built-in WEB framework.
- **goroutines**: To make a really asyncronous app.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/secretanry/S25-core-course-labs.git
   cd app_go
2. Run the application:
   ```bash
   go run .
3. Open your browser and navigate to:
   ```text
   http://localhost:8080

## **Project Structure**
```
app_go/
├── main.go                # net/http application
├── templates/             # HTML templates
│   └── index.html
├── README.md              # Project documentation
├── GO.md                  # Best practices and coding standards
└── .gitignore             # Files to ignore in version control
```


## **Dependencies**
No external dependencies

## Docker

### Overview

Our application is containerized using Docker to ensure consistent environments across development, testing, and production stages. Below are instructions on how to build, pull, and run the containerized application.

### How to Build?

To build the Docker image locally, follow these steps:

1. Navigate to the `app_go` directory.
2. Ensure you have Docker installed and running on your machine.
3. Run the following command to build the Docker image:

   ```sh
   docker build -t app_go .
   ```
### How to Pull?

If the Docker image has been pushed to a registry (e.g., Docker Hub), you can pull it directly without building:

1. Ensure Docker is installed and running.
2. Run the following command to pull the image:
   ```shell
   docker pull secretanry/app_go:latest
   ```

### How to Run?
1. After building or pulling the image, you can run the container using the following command:
   ```shell
   docker run -p 8080:8080 app_go
   ```

## Unit Tests

To run the unit tests for this application, follow these steps:

1. **Run the tests**:
   ```bash
   go test
   ```
2. **Inspect the output**:
   You will see tests report about tests status.

## CI/CD Workflow

This project uses GitHub Actions for continuous integration and continuous deployment. The CI workflow runs on **every branch** and includes the following steps:

- **Dependencies:** Installs project dependencies using go mod.
- **Linter:** Runs `go vet` to check code style and catch potential issues.
- **Tests:** Executes unit tests using `go test` to ensure code quality.
- **Docker:**
   - **Login:** Authenticates to DockerHub.
   - **Build:** Builds a Docker image for the application.
   - **Push:** Pushes the Docker image to DockerHub.

## **License**
This project is licensed under the **MIT License**.