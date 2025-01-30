# React Task Manager Application

## Project Overview
A simple task management application built with React and Vite. The application allows users to create, complete, and delete tasks in a user-friendly interface.

## Technology Stack
- React.js (Frontend library)
- Vite (Build tool and development server)
- JavaScript (ES6+)
- HTML/CSS

## Project Structure
```
app_js/
├── index.html          # Entry HTML file
├── App.jsx            # Main React component
├── package.json       # Project dependencies and scripts
├── vite.config.js     # Vite configuration
└── js.md             # Project documentation
```

## Features
1. Task Management
   - Add new tasks
   - Mark tasks as completed
   - Delete tasks
   - Enter key support for adding tasks

2. User Interface
   - Clean and minimalist design
   - Responsive layout
   - Visual feedback for completed tasks
   - Intuitive controls

## Setup Instructions

### Prerequisites
- Node.js (v14 or higher)
- npm (Node Package Manager)

### Installation
1. Clone or create the project directory:
```bash
mkdir app_js
cd app_js
```

2. Initialize the project and install dependencies:
```bash
npm init -y
npm install react react-dom @vitejs/plugin-react vite
```

3. Start the development server:
```bash
npm run dev
```

4. Build for production:
```bash
npm run build
```

## Usage Guide

### Adding Tasks
1. Type task description in the input field
2. Click "Add Task" button or press Enter

### Managing Tasks
- Use checkboxes to mark tasks as completed
- Click "Delete" to remove tasks
- Completed tasks are visually distinguished with strikethrough and grey background

## Component Structure

### App Component (App.jsx)
Main component that handles:
- Task state management using React hooks
- Task operations (add, toggle, delete)
- User interface rendering

## Implementation Details

### State Management
```javascript
const [tasks, setTasks] = useState([])
const [newTask, setNewTask] = useState('')
```
- Tasks stored in React state
- Each task has: id, text, and completed status

### Core Functions
- `addTask()`: Creates new tasks
- `toggleTask()`: Toggles completion status
- `deleteTask()`: Removes tasks from the list

## Best Practices Implemented
- Functional components with hooks
- Clean code structure
- Event handling for keyboard input
- Conditional rendering
- Proper state management

## Future Enhancements
1. Data Persistence
   - Local storage integration
   - Backend API integration

2. Additional Features
   - Task categories
   - Due dates
   - Priority levels