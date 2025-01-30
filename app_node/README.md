# 🚀 Moscow Time Web Application (Node.js)

## 📚 Overview

This is a simple **Node.js** web application that displays the current time in Moscow. It is built using **Express.js** and updates dynamically.

## 🚀 Features

- 🌍 Displays real-time **Moscow time (MSK)**
- ⚡ Built with **Express.js** – fast and lightweight
- 🔄 Updates on page refresh
- 🛠️ Ready for **local development & deployment**

---

## 🏰 Installation & Setup

### **🔹 1. Clone the Repository**

```bash
git clone https://github.com/your-username/devops-labs.git
cd devops-labs/app_node
```

### **🔹 2. Install Dependencies**

```bash
npm install
```

---

## ▶️ Running the Application

```bash
node server.js
```

The server will run on **`http://127.0.0.1:3000/`**.

---

## 📝 API Endpoint

| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/`     | Returns the current **Moscow time** |

---

## 🧪 Testing

1. Run `node server.js`
2. Open `http://127.0.0.1:3000/` in a browser
3. Refresh the page – the time should update!

---

## 📌 Deployment

This Node.js app can be deployed using **Docker**:

1. **Create a `Dockerfile`**:

   ```dockerfile
   FROM node:18
   WORKDIR /app
   COPY . .
   RUN npm install
   CMD ["node", "server.js"]
   ```

2. **Build & Run the Container**:

   ```bash
   docker build -t node-moscow-time .
   docker run -p 3000:3000 node-moscow-time
   ```

---

## 🛡️ Best Practices Followed

- ✅ **Follows RESTful principles**
- ✅ **Minimal dependencies**
- ✅ **Structured project files**
- ✅ **Clear documentation**

---

## 📝 Author

**Mohammad Jaafar**\
📧 [m.jaafar@innopolis.university](mailto:m.jaafar@innopolis.university)\
👉 [GitHub Profile](https://github.com/MoeJaafar)
