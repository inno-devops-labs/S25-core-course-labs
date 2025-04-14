## Differences Between Distroless and Regular Docker Images

### Regular Docker Images
- **Base**: Full OS (e.g., Alpine, Ubuntu).
- **Size**: Larger (includes OS, package manager, shell, and tools).
- **Use Case**: Development and debugging (easy to modify and debug).
- **Security**: Larger attack surface (more tools and packages).

### Distroless Images
- **Base**: Minimal runtime environment (no OS, shell, or package manager).
- **Size**: Smaller (only application and runtime dependencies).
- **Use Case**: Production (optimized for security and minimalism).
- **Security**: Reduced attack surface (no unnecessary tools or packages).

### Key Differences
| Feature          | Regular Image               | Distroless Image              |
|------------------|-----------------------------|-------------------------------|
| **Base**         | Full OS                    | Minimal runtime               |
| **Size**         | Larger                     | Smaller                       |
| **Security**     | Larger attack surface      | Reduced attack surface        |
| **Debugging**    | Easy (includes shell)      | Hard (no shell)               |
| **Use Case**     | Development                | Production                    |

### Why Use Distroless?
- **Smaller Size**: Saves storage and bandwidth.
- **Improved Security**: Fewer components, fewer vulnerabilities.
- **Production-Ready**: Optimized for running apps in production.

### Why Use Regular Images?
- **Ease of Debugging**: Includes tools like `bash` and `curl`.
- **Flexibility**: Easier to modify during development.

### Some problems...
In this case distroless image is bigger than the regular one  
![image](https://github.com/user-attachments/assets/5217f5c9-7a00-4d93-ae40-60689273f7df)

