## Bonus Task (Node.js)

In this bonus task, I explored **Docker multi-stage builds** and **Distroless images** to optimize the containerization
of my **Node.js** application.

---

## **Dockerizing the Node.js App**

- Created a `Dockerfile` for the **Node.js** application.
- Followed best practices:
  ✅ Used a **non-root** base image.  
  ✅ Created a **strict `.dockerignore`** to exclude unnecessary files.  
  ✅ Ensured **layer caching efficiency**.

---

## **Implementing Multi-Stage Builds**

> [!WARNING]
> For this application, multi-stage builds did not provide significant benefits due to its simplicity. However, I
> explored the concept to understand its advantages.

### **Why Multi-Stage Builds?**

- Reduces the final image size by **separating the build process from the runtime environment**.
- Ensures **only necessary files** are included in the final image.
- Improves **security** by excluding unnecessary tools from the runtime stage.

### **Key Improvements**

- **Efficient Caching**: Installs dependencies before copying the source code.
- **Security**: Runs as a non-root user (`node`).
- **Smaller Image**: Only includes production dependencies.

---

## **Exploring Distroless Images**

### **Why Use Distroless?**

- **Smaller image size** (removes unnecessary tools like shells, package managers).
- **Reduced attack surface** (fewer security vulnerabilities).
- **Optimized for production** (no debugging tools, just runtime dependencies).

### **Key Benefits**

- **Minimal Image**: No shell, package manager, or extra utilities.
- **Non-Root by Default**: Runs as `nonroot`.
- **More Secure**: Smaller attack surface.

---

## **Image Comparison**

To evaluate the impact of these optimizations, I compared the **image sizes** of:

1. **Standard Alpine Image**
2. **Multi-Stage Build**
3. **Distroless Image**

| Image Type            |      Size | Security Benefits                                        |
|-----------------------|----------:|----------------------------------------------------------|
| `node:18-alpine`      |     127MB | Lightweight, includes package manager                    |
| **Multi-Stage Build** |     127MB | It is useless for my application actually                |
| **Distroless**        | **115MB** | **Minimal attack surface, no shell, no package manager** |

---

## **7. Running the Optimized Container**

### **1. Build the Multi-Stage Image**

```sh
docker build -t node-moscow-time-webapp .
```

### **2. Run the Multi-Stage Container**

```sh
docker run -d -p 8000:8000 --name node-moscow-time node-moscow-time-webapp
```

### **3. Build the Distroless Image**

```sh
docker build -t node-moscow-time-webapp-distroless -f distroless.Dockerfile .
```

### **4. Run the Distroless Container**

```sh
docker run -d -p 8000:8000 --name node-moscow-time-distroless node-moscow-time-webapp-distroless
```

---

## **Conclusion**

This bonus task helped me explore **advanced Docker optimizations**:
✅ **Multi-Stage Builds** reduced unnecessary dependencies in the final image.  
✅ **Distroless Images** improved security and minimized attack surface.  
✅ **Image size comparison** confirmed significant reductions in size and complexity.

> [!TIP]
> For production deployments, **Distroless images** are the best choice due to their **security** and *
*efficiency**. 🚀