# React Web Application: Moscow Time

This is a simple React web application that displays the current time in Moscow, Russia. The application is built using **Vite** for fast development and follows best practices for React development. It uses `pnpm` as the package manager for efficient dependency management.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Building the Application](#building-the-application)
6. [Previewing the Production Build](#previewing-the-production-build)
7. [Testing](#testing)
8. [Code Quality Checks](#code-quality-checks)
9. [Author](#author)

---

## Overview

The application displays the current time in the Moscow timezone (`Europe/Moscow`). It is built using **React** and **Vite**, ensuring a fast and modern development experience. The application uses `pnpm` for package management, which is faster and more disk-space efficient compared to `npm` or `yarn`.

---

## Prerequisites

Before proceeding, ensure you have the following installed:

- **Node.js**: React and Vite require Node.js. Download and install it from the official [Node.js website](https://nodejs.org/).
- **pnpm**: A fast and efficient package manager. Install it globally using npm:

  ```bash
  npm install -g pnpm
  ```

---

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone git@github.com:Mohammed-Nour/S25-core-course-labs.git
   cd S25-core-course-labs/app_react
   ```

2. Install dependencies using `pnpm`:

   ```bash
   pnpm install
   ```

---

## Running the Application

1. Start the development server:

   ```bash
   pnpm run dev
   ```

2. Open your browser and navigate to `http://localhost:5173/`.

   > **Note**: The application will start a development server on `http://localhost:5173/`. You can stop the server by pressing `Ctrl+C` in the terminal.

---

## Building the Application

To build the application for production, run the following command:

```bash
pnpm run build
```

This will generate a production-ready build in the `dist/` directory. The build process optimizes the code for performance and ensures the application is ready for deployment.

---

## Previewing the Production Build

After building the application, you can preview the production build locally using Vite's preview server:

```bash
pnpm run preview
```

This will start a local server serving the production build. Open your browser and navigate to `http://localhost:4173/` to view the application.

---

## Testing

To ensure the application works correctly:

1. Run the application and verify that the displayed time matches the current time in Moscow.
2. Refresh the page to confirm that the time updates dynamically.

---

## Code Quality Checks

To ensure the code adheres to best practices and coding standards, the following tools are used:

### 1. **ESLint**

   ESLint is a static code analysis tool for identifying problematic patterns in JavaScript and React code.

   Run ESLint on the project:

   ```bash
   pnpm run lint
   ```

   > **Note**: ESLint will generate a report with suggestions for improving the code. Fix any reported issues to ensure compliance.

### 2. **Prettier**

   Prettier is a code formatter that ensures consistent code style across the project.

   Run Prettier on the project:

   ```bash
   pnpm run format
   ```

   > **Note**: Prettier will check for formatting issues. You can automatically fix them by running:

   ```bash
   pnpm run format:fix
   ```

---

## Author

- **Name**: Mohamad Nour Shahin
- **Email**: <mo.shahin@innopolis.university>
