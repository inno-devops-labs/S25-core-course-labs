# 🌟 Moscow Time Web Application

## 📚 Overview

This is a simple web application that displays the **current time in Moscow**, developed using **Flask**. The application dynamically updates the time whenever the page is refreshed.

## 🚀 Features

- 🌍 Displays real-time **Moscow time (MSK)**
- ⚡ Built with **Flask** – lightweight and efficient
- 📖 Follows best coding practices
- 🔄 Updates on page refresh
- 🛠️ Ready for **local development & deployment**

---

## 📚 Project Structure

```bash
app_python/
│── app.py              # Main Flask application
│── requirements.txt    # Dependencies
│── PYTHON.md           # Justification & Best Practices
│── README.md           # Documentation
│── .gitignore          # Ignore unnecessary files

```

---

## 🏰 Installation & Setup

### **🔹 1. Clone the Repository**

```bash
git clone https://github.com/your-username/devops-labs.git
cd devops-labs/app_python
```

### **🔹 2. Set Up a Virtual Environment (Recommended)**

```bash
python -m venv venv
```

#### **Activate Virtual Environment:**

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### **🔹 3. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Once dependencies are installed, start the Flask application:

```bash
python app.py
```

The server will run on **`http://127.0.0.1:5000/`**. Open your browser and visit this URL to see the Moscow time.

---

## 📝 API Endpoint

| Method | Endpoint | Description                         |
| ------ | -------- | ----------------------------------- |
| `GET`  | `/`      | Returns the current **Moscow time** |

---

## 🧪 Testing

To verify that the application updates time correctly:

1. Run `python app.py`
2. Open `http://127.0.0.1:5000/` in a browser
3. Refresh the page – the time should update!

---

## 📌 Deployment

This Flask app can be deployed on **Heroku, AWS, or Docker**. Example Docker deployment:

1. **Create a** `Dockerfile`:

   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   CMD ["python", "app.py"]
   ```

2. **Build & Run the Container**:

   ```bash
   docker build -t flask-moscow-time .
   docker run -p 5000:5000 flask-moscow-time
   ```

---

## 🛡️ Best Practices Followed

- ✅ **PEP 8 Compliance** (Python Coding Standards)
- ✅ **Virtual Environment for Dependency Management**
- ✅ **Structured Project Files**
- ✅ **Clear Documentation**
- ✅ **Modular Code for Maintainability**

---

## 📝 Author

**Mohammad Jaafar**\
📧 [m.jaafar@innopolis.university](mailto:m.jaafar@innopolis.university)\
👉 [GitHub Profile](https://github.com/MoeJaafar)
