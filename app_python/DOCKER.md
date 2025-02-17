# 🐳 Containerization of Moscow Time App
# 📌 Implemented Best Practices
- **KISS Principle:** Simple and efficient Dockerfile structure.
- **Security:** The application runs as a non-root user (`appuser`).
- **Minimal Base Image:** Uses `python:3.12-alpine3.18` to reduce image size.
- **Layer Optimization:** `COPY requirements.txt` first to leverage Docker caching.
- **Docker Ignore:** `.dockerignore` excludes unnecessary files.
# 🚀 How to Run
### **Build the Image**
```bash
docker build -t enot0704/moscow-time-app:latest .
```
### **Run container**
```bash
docker run -d -p 5000:5000 --name moscow-time-app enot0704/moscow-time-app:latest
```
### 📖 **Open Your Browser**
`http://localhost:5000`