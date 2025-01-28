# Fork Counter Web Application

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

### **License**
This project is licensed under the **MIT License**.