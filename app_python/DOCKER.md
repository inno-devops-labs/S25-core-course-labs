# 🐙 Dockerization of Python Web App

## 💪 Best Practices Implemented

- **Rootless User**: Runs as a **non-root user** to enhance security.
- **Slim Base Image**: Uses `python:3.12-alpine` for smaller size and efficiency.
- **Layer Optimization**: Installs dependencies before copying the full application to leverage Docker layer caching.
- **`.dockerignore` File**: Prevents unnecessary files from being copied into the image.

---

## 🏰 How to Build & Run

### **🌟 Build the Docker Image**

```bash
docker build -t em1999jay/moscow-time-app .
```

### **🌟 Run the Container**

```bash
docker run -p 5000:5000 em1999jay/moscow-time-app
```

### **🌟 Pull the Image from Docker Hub**

```bash
docker pull em1999jay/moscow-time-app:v1
```

---

## 🧪 Distroless Findings

- **What is Distroless?** Distroless images contain only the essential application and dependencies, minimizing security risks.
- **Smaller Image Size**: The distroless image is significantly smaller than `python:3.12-alpine`, reducing deployment time.
- **Security Enhancements**: Removes unnecessary OS components, making the container more secure.
- **Performance Optimization**: Faster startup and lower resource consumption.

---

## 💪 Running the Fixed Distroless Container

### **🌟 Build the Distroless Image**

```bash
docker build -t em1999jay/moscow-time-app-distroless -f distroless.Dockerfile .
```

### **🌟 Run the Distroless Container**

```bash
docker run -p 5000:5000 em1999jay/moscow-time-app-distroless:v11
```

### **🌟 Compare Image Sizes**

Run the following command to compare:

```bash
docker images | grep moscow-time-app
```

---

## 📊 Image Size Comparison Screenshot

![Image Size Comparison](Screenshot.jpg)

### 📊 Analysis of Image Size Comparison

- **Standard Image (`moscow-time-app`)**: 199MB
- **Distroless Image (`moscow-time-app-distroless`)**: **93.4MB**  
  🔹 **The distroless image is 53% smaller** than the standard one.

### 🚀 Key Observations

✅ **Reduced Attack Surface**: Since Distroless images do not include a package manager or shell, they minimize security risks.  
✅ **Smaller Size**: The distroless version significantly reduces the container size, making deployments faster and more efficient.  
✅ **Performance Optimization**: The smaller image loads and starts faster, improving efficiency in containerized environments.  
