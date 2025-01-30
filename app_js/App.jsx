import React, { useState } from 'react'
import { createRoot } from 'react-dom/client'

function App() {
  const [tasks, setTasks] = useState([])
  const [newTask, setNewTask] = useState('')

  const addTask = () => {
    if (newTask.trim()) {
      setTasks([...tasks, { id: Date.now(), text: newTask, completed: false }])
      setNewTask('')
    }
  }

  const toggleTask = (taskId) => {
    setTasks(tasks.map(task =>
      task.id === taskId ? { ...task, completed: !task.completed } : task
    ))
  }

  const deleteTask = (taskId) => {
    setTasks(tasks.filter(task => task.id !== taskId))
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      addTask()
    }
  }

  return (
    <div style={{ maxWidth: '600px', margin: '20px auto', padding: '0 20px' }}>
      <h1>React Task Manager</h1>
      
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Enter new task"
          style={{ padding: '5px', width: '70%', marginRight: '10px' }}
        />
        <button onClick={addTask} style={{ padding: '5px 10px' }}>Add Task</button>
      </div>

      <div>
        {tasks.map(task => (
          <div
            key={task.id}
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              padding: '10px',
              margin: '5px 0',
              backgroundColor: task.completed ? '#e0e0e0' : '#f5f5f5',
              borderRadius: '5px'
            }}
          >
            <div>
              <input
                type="checkbox"
                checked={task.completed}
                onChange={() => toggleTask(task.id)}
              />
              <span style={{ 
                marginLeft: '10px',
                textDecoration: task.completed ? 'line-through' : 'none'
              }}>
                {task.text}
              </span>
            </div>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  )
}

createRoot(document.getElementById('root')).render(<App />)