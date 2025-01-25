# React Web Application Documentation

## Framework Choice: React with Vite

I chose **React** for this web application because it is a popular and powerful JavaScript library for building user interfaces. React's component-based architecture makes it easy to build reusable and maintainable code. Additionally, I used **Vite** as the build tool for its fast development experience and modern features.

---

## Best Practices Applied

### 1. **Component-Based Architecture**

- The application follows a component-based structure, separating the main logic (`App.jsx`) from the HTML template (`index.html`). This makes the codebase modular and easy to maintain.

### 2. **Modern Tooling**

- **Vite** is used for its fast development server and optimized build process. It provides a better development experience compared to traditional tools like Webpack.
  - **pnpm** is used as the package manager for its efficiency in disk space usage and faster dependency installation.

### 3. **Code Quality**

- **ESLint** and **Prettier** are used to enforce coding standards and ensure consistent code style.
  - The application follows React best practices, such as using functional components and avoiding unnecessary state.

---

## Testing

To ensure the application works as expected, the following steps were taken:

1. **Manual Testing**:
   - The application was run locally, and the displayed time was verified to match the current time in Moscow.
   - The page was refreshed multiple times to ensure the time updates correctly.

2. **Static Code Analysis**:
   - ESLint and Prettier were used to check for code quality and formatting issues.

---

## Building and Previewing the Application

### Building the Application

To create a production-ready build of the application, run the following command:

```bash
pnpm run build
```

This generates an optimized build in the `dist/` directory, which is ready for deployment.

### Previewing the Production Build

To preview the production build locally, use Vite's preview server:

```bash
pnpm run preview
```

This starts a local server serving the production build. Open your browser and navigate to `http://localhost:4173/` to view the application.

---

## Code Quality Checks

To ensure the code adheres to best practices and coding standards, the following tools are used:

### 1. **ESLint**

   ESLint is a static code analysis tool for identifying problematic patterns in JavaScript and React code.

   Run ESLint on the project:

   ```bash
   pnpm run lint
   ```

### 2. **Prettier**

   Prettier is a code formatter that ensures consistent code style across the project.

   Run Prettier on the project:

   ```bash
   pnpm run format
   ```

   > **Note**: Prettier will check for formatting issues. You can automatically fix them by running:

   ```bash
   pnpm run format:fix
